from django.shortcuts import  get_object_or_404
from django.http import HttpResponse
from .models import Invoice, ProductInInvoice
from django.template.loader import get_template
from decimal import Decimal
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def download_invoice_pdf(request):
    invoice_id = request.GET.get('invoice_id')
    if not invoice_id:
        return HttpResponse("Invoice not found or invalid request.")
        
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    products = ProductInInvoice.objects.select_related('product').filter(invoice=invoice).all()
    
    total_amount = sum(item.amount * item.product.unit_price * (1 + item.VAT / 100) for item in products)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Invoice_{invoice.number}.pdf"'

    buffer = canvas.Canvas(response, pagesize=letter)
    buffer.drawString(100, 750, f"Invoice Number: {invoice.number}")
    buffer.drawString(100, 730, f"Date: {invoice.date.strftime('%Y-%m-%d')}")
    buffer.drawString(100, 710, f"Client: {invoice.client.first_name} {invoice.client.last_name}")
    buffer.drawString(100, 690, "Products:")

    y = 670
    for item in products:
        buffer.drawString(120, y, f"{item.product.name} - Amount: {item.amount} - Price: {item.product.unit_price} - VAT: {item.VAT}%")
        y -= 20

    buffer.drawString(100, 50, f"Total Amount: {total_amount}")
    buffer.save()

    return response

