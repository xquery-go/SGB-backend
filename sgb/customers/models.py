from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import UserBusinessModel, BaseModel


class Customer(UserBusinessModel):
    name = models.CharField(
        _("Name"),
        max_length=225,
        null=True,
        blank=True,
        default='',
    )
    telephone = models.CharField(
        _("Phone number"),
        max_length=20,
        null=True,
        blank=True,
        default='',
    )
    email = models.EmailField(
        _("Email address"),
        max_length=250,
    )
    social_media_link = models.CharField(
        _("Social media link"),
        max_length=155,
        null=True,
        blank=True,
        default='',
    )
    highest_education = models.CharField(
        _("Highest education"),
        null=True,
        blank=True,
        max_length=150,
        default='',
    )

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = _("customer")
        verbose_name_plural = _("customers")
        db_table = "customer"


class CustomerCreditRiskParameter(BaseModel):
    """
    This model contains the values of customer credit risk parameters for existing customers and
     later on will contain the value for new customers
    """
    customer = models.ForeignKey(
        'customers.Customer',
        on_delete=models.CASCADE,
        related_name='customer_credit_risk_parameters',
    )
    is_good_credit_risk = models.BooleanField(
        _("Is Good Credit Risk"),
        null=True,
        blank=True,
    )
    status = models.PositiveIntegerField(
        _("Status of the debtor's checking account with the bank (categorical)"),
        null=True,
        blank=True,
    )
    duration = models.PositiveIntegerField(
        _("Credit duration in months (quantitative)"),
        null=True,
        blank=True,
    )
    credit_history = models.PositiveIntegerField(
        _("History of compliance with previous or concurrent credit contracts (categorical)"),
        null=True,
        blank=True,
    )
    purpose = models.PositiveIntegerField(
        _("Purpose for which the credit is needed (categorical)"),
        null=True,
        blank=True,
    )
    amount = models.PositiveIntegerField(
        _("Credit amount in DM (quantitative)"),
        null=True,
        blank=True,
    )
    savings = models.PositiveIntegerField(
        _("Debtor's savings (categorical)"),
        null=True,
        blank=True,
    )
    employment_duration = models.PositiveIntegerField(
        _("Duration of debtor's employment with current employer (ordinal; discrete quantitative)"),
        null=True,
        blank=True,
    )
    installment_rate = models.PositiveIntegerField(
        _("Credit installments as a percentage of debtor's disposable income (ordinal; discrete quantitative)"),
        null=True,
        blank=True,
    )
    personal_status_sex = models.PositiveIntegerField(
        _("Combined information on sex and marital status; categorical"),
        null=True,
        blank=True,
    )
    other_debtors = models.PositiveIntegerField(
        _("Is there another debtor or a guarantor for the credit? (categorical)"),
        null=True,
        blank=True,
    )
    present_residence = models.PositiveIntegerField(
        _("Length of time (in years) the debtor lives in the present residence (ordinal)"),
        null=True,
        blank=True,
    )
    most_valuable_property = models.PositiveIntegerField(
        _("The debtor's most valuable property (choices)"),
        null=True,
        blank=True,
    )
    age = models.PositiveIntegerField(
        _("Age in years (quantitative)"),
        null=True,
        blank=True,
    )
    other_installment_plans = models.PositiveIntegerField(
        _("Installment plans from providers other than the credit-giving bank (categorical)"),
        null=True,
        blank=True,
    )
    housing = models.PositiveIntegerField(
        _("Type of housing the debtor lives in (categorical)"),
        null=True,
        blank=True,
    )
    number_credits = models.PositiveIntegerField(
        _("Number of credits including the current one the debtor has (or had) at this bank (ordinal, discrete"
          "quantitative)"),
        null=True,
        blank=True,
    )
    job = models.PositiveIntegerField(
        _("Quality of debtor's job (ordinal)"),
        null=True,
        blank=True,
    )
    people_liable = models.PositiveIntegerField(
        _("Number of persons who financially depend on the debtor (i.e., are entitled to maintenance) "
          "(binary,discrete quantitative)"),
        null=True,
        blank=True,
    )
    has_telephone = models.BooleanField(
        _("Is there a telephone landline registered on the debtor's name?"),
        null=True,
        blank=True,
    )
    is_foreign_worker = models.PositiveIntegerField(
        _("Is the debtor a foreign worker?"),
        null=True,
        blank=True,
    )

    @property
    def credit_risk_status(self):
        if self.is_good_credit_risk:
            return "High Credit Risk"
        elif self.is_good_credit_risk is False:
            return "Low Credit Risk"
        else:
            return "Not Calculated"

    def __str__(self):
        return f"{self.customer} - {self.credit_risk_status}"

    class Meta:
        verbose_name = _("Customer Parameter")
        verbose_name_plural = _("Customer Parameters")
        db_table = "customer_parameters"


