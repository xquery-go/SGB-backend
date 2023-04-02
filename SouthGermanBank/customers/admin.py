from django.contrib import admin
from customers import models
# Register your models here.


class CustomerCreditRiskParameterInline(admin.StackedInline):
    model = models.CustomerCreditRiskParameter


@admin.register(models.Customer)
class CustomerCreditRiskParametersAdmin(admin.ModelAdmin):
    inlines = [CustomerCreditRiskParameterInline,
               ]
