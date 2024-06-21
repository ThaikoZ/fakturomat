from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Client(models.Model):
    class Meta:
        db_table = 'client'
        
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    company_details = models.CharField(max_length=255, null=True, blank=True)
    nip = models.CharField(max_length=15, null=True, blank=True)
    address_details = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    class Meta:
        db_table = 'product'
    
    name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    PAYMENT_METHODS = [
        ("CASH", 'In Cash'),
        ("DEBIT", 'Debit Card'),
        ("CREDIT", 'Credit Card'),
        ("PAYPAL", 'PayPal'),
    ]
    PAYMENT_STATUSES = [
        ("UNPAID", 'Unpaid'),
        ("PAID", 'Paid'),
    ]
    
    class Meta:
        db_table = 'invoice'
    
    number = models.CharField(max_length=55, unique=True)
    date = models.DateField(default=timezone.now())
    payment_period = models.DateField(default=timezone.now() + timezone.timedelta(days=7) )
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHODS, default="CREDIT")
    payment_status = models.CharField(max_length=255, choices=PAYMENT_STATUSES, default="UNPAID")
    client = models.ForeignKey(Client, on_delete=models.PROTECT)

    def __str__(self):
        return self.number


class ProductInInvoice(models.Model):
    class Meta:
        db_table = 'products_in_invoice'
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    VAT = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0)]) 

    def __str__(self):
        return f"Product {self.product.name} in Invoice {self.invoice.number}"


class Template(models.Model):
    PAYMENT_METHODS = [
        ("CASH", 'In Cash'),
        ("DEBIT", 'Debit Card'),
        ("CREDIT", 'Credit Card'),
        ("PAYPAL", 'PayPal'),
    ]
    
    class Meta:
        db_table = 'template'
    
    number = models.CharField(max_length=55, unique=True)
    frequency = models.IntegerField(validators=[MinValueValidator(0)], default=30)
    date = models.DateField(default=timezone.now())
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHODS, default="CREDIT")
    client = models.ForeignKey(Client, on_delete=models.PROTECT)

    def __str__(self):
        return self.number


class ProductInTemplate(models.Model):
    class Meta:
        db_table = 'products_in_template'
        
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    amount = models.IntegerField()
    VAT = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Product {self.product.name} in Template {self.template.number}"


class User(models.Model):
    class Meta:
        db_table = 'User'
        
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    roles = models.IntegerField()

    def __str__(self):
        return self.name
