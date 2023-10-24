from django import forms
from core import choices


class CreditRatingInput(forms.Form):
    Status = forms.IntegerField()
    Duration = forms.IntegerField()
    CreditHistory = forms.IntegerField()
    Purpose = forms.IntegerField()
    Amount = forms.IntegerField()
    Savings = forms.IntegerField()
    EmploymentDuration = forms.IntegerField()
    InstallmentRate = forms.IntegerField()
    PersonalStatusSex = forms.IntegerField()
    OtherDebtors = forms.IntegerField()
    PresentResidence = forms.IntegerField()
    PropertyType = forms.IntegerField()
    Age = forms.IntegerField()
    OtherInstallmentPlans = forms.IntegerField()
    Housing = forms.IntegerField()
    NumberCredits = forms.IntegerField()
    Job = forms.IntegerField()
    PeopleLiable = forms.IntegerField()
    ForeignWorker = forms.IntegerField()


class CustomerEnquiry(forms.Form):
    Name = forms.CharField(
        required=True,
        initial='Abhilash',
        label="Name"
    )
    Telephone = forms.CharField(
        required=True,
        widget=forms.NumberInput(),
        initial='0123456789',
        label="Telephone No. "
    )
    Email = forms.CharField(
        required=True,
        widget=forms.EmailInput,
        initial="Abhilash@xact.com",
        label="Email Address "
    )
    SocialMedia = forms.CharField(
        widget=forms.URLInput,
        initial="https://www.linkedin.com/in/abhilash23/",
        label="Social Media Profile Link "
    )
    FormalEducation = forms.CharField(
        required=False,
        label="Highest Education "
    )


class AnalyserDropdown(forms.Form):
    Status = forms.ChoiceField(
        required=True,
        choices=choices.CreditStatus.choices
    )
    Duration = forms.IntegerField(
        required=True,
    )
    CreditHistory = forms.ChoiceField(
        required=True,
        choices=choices.CreditHistory.choices
    )
    Purpose = forms.ChoiceField(
        required=True,
        choices=choices.Purpose.choices
    )
    Amount = forms.IntegerField(
        required=True,
    )
    Savings = forms.ChoiceField(
        required=True,
        choices=choices.Savings.choices
    )
    EmploymentDuration = forms.ChoiceField(
        required=True,
        choices=choices.EmploymentDuration.choices
    )
    InstallmentRate = forms.IntegerField(
        required=True,
    )
    PersonalStatusSex = forms.ChoiceField(
        required=True,
        choices=choices.PersonalStatusSex.choices
    )
    OtherDebtors = forms.ChoiceField(
        required=True,
        choices=choices.OtherDebtors.choices
    )
    PresentResidence = forms.IntegerField(
        required=True,
        label='Number of years at current residence'
    )
    PropertyType = forms.ChoiceField(
        required=True,
        choices=choices.PropertyType.choices
    )
    Age = forms.IntegerField(
        required=True,
    )
    OtherInstallmentPlans = forms.ChoiceField(
        required=True,
        choices=choices.OtherInstallmentPlans.choices
    )
    Housing = forms.ChoiceField(
        required=True,
        choices=choices.Housing.choices
    )
    NumberCredits = forms.IntegerField(
        required=True,
        label='Number of credits at this bank'
    )
    Job = forms.ChoiceField(
        required=True,
        choices=choices.Job.choices
    )  #
    PeopleLiable = forms.IntegerField(
        required=True,
    )
    HasTelephone = forms.BooleanField(
        required=True,
        label='Has telephone'
    )
    IsForeignWorker = forms.BooleanField(
        required=True,
        label='Is a foreign worker'
    )


class ApplicationSelector(forms.Form):
    HiddenKey = forms.UUIDField(
        required=True,
        widget=forms.HiddenInput()
    )
    App = forms.ChoiceField(
        required=True,
        choices=choices.ApplicationSelector.choices,
    )


class AddCustomerCreditRiskParameterForm(AnalyserDropdown):
    def __init__(self):
        super().__init__()


class EditCustomerCreditRiskParameterForm(AnalyserDropdown):
    def __init__(self):
        super().__init__()

    CustomerCreditRiskParameterId = forms.IntegerField(
        required=True,
        label='Customer Credit Risk Parameter Id'
    )


class DeleteCustomerCreditRiskParameterForm(forms.Form):

    CustomerCreditRiskParameterId = forms.IntegerField(
        required=True,
        label='Customer Credit Risk Parameter Id'
    )
