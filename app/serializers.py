from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['number', 'date', 'payment_period', 'payment_method', 'payment_status', 'client']
