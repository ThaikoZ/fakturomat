from typing import Any
from django.contrib import admin
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import F
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils import timezone
from django.urls import path, reverse
from . import models

# class Summary(admin.AdminSite):
#     autocomplete_fields = ['product']
#     model = models.ProductInInvoice
#     extra = 1

class InvoiceItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    model = models.ProductInInvoice
    extra = 1
    

@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    autocomplete_fields = ['client']
    list_display = ['number', 'date', 'client', 'payment_status', 'payment_period', 'payment_method', 'download']
    fields = ['date', 'payment_period', 'payment_method', 'payment_status', 'client']
    readonly_fields = ['number']
    ordering = ['number']
    inlines = [InvoiceItemInline]

    def save_model(self, request, invoice, form, change):
        if not invoice.number: 
            invoice.number = self.generate_invoice_number()
        super().save_model(request, invoice, form, change)

    def generate_invoice_number(self):
        month = timezone.now().month
        year = timezone.now().year
        try:
            last_invoice = models.Invoice.objects.latest('id')
            invoice_number = last_invoice.number.split(' ')[2] 
            invoice_id = int(invoice_number.split('/')[0])
            return f'FV - {invoice_id + 1}/{month}/{year}'
        except models.Invoice.DoesNotExist:
            return f'FV - 1/{month}/{year}'
    
    def download(self, invoice):
        url = reverse('download_invoice_pdf')
        params = urlencode({'invoice_id': invoice.pk})
        return format_html('<a href="{}?{}">Download</a>', url, params)
        

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',  'company_details', 'address_details', 'phone_number',)
    search_fields = ('first_name', 'last_name')
    ordering = ['first_name', 'last_name']
    
    

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_price', 'description')
    search_fields = ('name',)
    ordering = ['name']
    
    
    
    
class TemplateItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    model = models.ProductInTemplate
    extra = 1
    
    
@admin.register(models.Template)
class TemplateAdmin(admin.ModelAdmin):
    autocomplete_fields = ['client']
    list_display = ['number', 'date', 'client', 'frequency','issue_an_invoice']
    fields = ['date', 'frequency', 'payment_method', 'client']
    readonly_fields = ['number']
    ordering = ['number']
    inlines = [TemplateItemInline]

    def save_model(self, request, template, form, change):
        if not template.number: 
            template.number = self.generate_template_number()
        super().save_model(request, template, form, change)

    def generate_template_number(self):
        month = timezone.now().month
        year = timezone.now().year
        try:
            last_template = models.Template.objects.latest('id')
            template_number = last_template.number.split(' ')[2] 
            template_id = int(template_number.split('/')[0])
            return f'T - {template_id + 1}/{month}/{year}'
        except models.Template.DoesNotExist:
            return f'T - 1/{month}/{year}'
    
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('issue_invoice/<int:template_id>/', self.admin_site.admin_view(self.issue_invoice), name='issue-invoice'),
        ]
        return custom_urls + urls
    
    def issue_invoice(self, request, template_id, *args, **kwargs):
        template = get_object_or_404(models.Template, id=template_id)
        # Logic to issue the invoice
        # For example, create an Invoice object from the template
        invoice = models.Invoice.objects.create(
            number=self.generate_invoice_number(),
            date=timezone.now(),
            payment_period=timezone.now() + timezone.timedelta(days=7),
            payment_method=template.payment_method,
            payment_status='UNPAID',
            client=template.client
        )
        # Copy other fields or related objects if needed
        products_in_template = models.ProductInTemplate.objects.filter(template=template)
        for item in products_in_template:
            models.ProductInInvoice.objects.create(
                product=item.product,
                invoice=invoice,
                amount=item.amount,
                VAT=item.VAT
            )
            
        self.message_user(request, "Invoice issued successfully.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    def issue_an_invoice(self, obj):
        return format_html(
            '<a href="{}">Issue Invoice</a>',
            reverse('admin:issue-invoice', args=[obj.pk])
        )

    issue_an_invoice.short_description = 'Issue Invoice'
    issue_an_invoice.allow_tags = True

    def generate_invoice_number(self):
        month = timezone.now().month
        year = timezone.now().year
        try:
            last_invoice = models.Invoice.objects.latest('id')
            invoice_number = last_invoice.number.split(' ')[2]
            invoice_id = int(invoice_number.split('/')[0])
            return f'FV - {invoice_id + 1}/{month}/{year}'
        except models.Invoice.DoesNotExist:
            return f'FV - 1/{month}/{year}'