
from core.base.miscellaneous import ComputedProperty


class UserGroup:
    VISITOR = 1
    BANK_STAFF = 2
    BANK_STAFF_MANAGER = 3
    ADMIN = 4
    DEBTOR = 5
    ACCOUNT_HOLDER = 6

    @ComputedProperty
    def choices(self):
        return (
            (self.VISITOR, 'Visitor'),
            (self.BANK_STAFF, 'Bank Staff'),
            (self.BANK_STAFF_MANAGER, 'Bank Manager'),
            (self.ADMIN, 'Administrator'),
            (self.DEBTOR, 'Debtor'),
            (self.ACCOUNT_HOLDER, 'Account Holder'),
        )


class UserActiveStatus:
    ACTIVE = 1
    DEACTIVATED = 2
    BLOCKED = 3
    INACTIVE = 4

    @ComputedProperty
    def choices(self):
        return (
            (self.ACTIVE, 'Active'),
            (self.DEACTIVATED, 'Deactivated'),
            (self.BLOCKED, 'Blocked'),
            (self.INACTIVE, 'Inactive'),
        )


class Status:
    HAS_ACCOUNT = 1
    NO_ACCOUNT = 2

    @ComputedProperty
    def choices(self):
        return (
            (self.HAS_ACCOUNT, 'Has Account'),
            (self.NO_ACCOUNT, 'No Account'),
        )


class CreditStatus:
    LESS_THAN_ZERO = 1
    ZERO_TO_200 = 2
    MORE_THAN_200 = 3
    NO_CHECKIN_ACCOUNT = 4

    @ComputedProperty
    def choices(self):
        return (
            (self.LESS_THAN_ZERO, '... <    0 DM'),
            (self.ZERO_TO_200, '0 <= ... <  200 DM'),
            (self.MORE_THAN_200, '... >= 200/salary assignments for at least 1 year'),
            (self.NO_CHECKIN_ACCOUNT, 'no checking account')
        )


class CreditHistory:
    NO_CREDIT = 1
    ALL_AT_THIS_BANK_PAID = 2
    HAS_CREDIT_DULY_PAID = 3
    DELAY_IN_PAST = 4
    CRITICAL_ACCOUNT = 5

    @ComputedProperty
    def choices(self):
        return (
            (self.NO_CREDIT, 'No Credits Taken/All Debts Duly Paid'),
            (self.ALL_AT_THIS_BANK_PAID, 'All Credits At This Bank Paid Back Duly'),
            (self.HAS_CREDIT_DULY_PAID, 'Existing credits paid back duly till now'),
            (self.DELAY_IN_PAST, 'Delay in paying off in the past'),
            (self.CRITICAL_ACCOUNT, 'Critical account/other credits existing(not at this bank)'),
        )


class Purpose:
    CAR_NEW = 1
    CAR_USED = 2
    FURNITURE_OR_EQUIPMENT = 3
    RADIO_OR_TELEVISION = 4
    DOMESTIC = 5
    APPLIANCES = 6
    REPAIRS = 7
    EDUCATION = 8
    VACATION = 9
    RETRAINING = 10
    BUSINESS = 11
    OTHERS = 12

    @ComputedProperty
    def choices(self):
        return (
         (self.CAR_NEW, 'Car (new)'),
         (self.CAR_USED, 'Car (used)'),
         (self.FURNITURE_OR_EQUIPMENT, 'Furniture/equipment'),
         (self.RADIO_OR_TELEVISION, 'Radio/television'),
         (self.DOMESTIC, 'Domestic appliances'),
         (self.APPLIANCES, 'Repairs'),
         (self.REPAIRS, 'Education'),
         (self.EDUCATION, '(Vacation - does not exist?)'),
         (self.VACATION, 'Retraining'),
         (self.RETRAINING, 'Business'),
         (self.BUSINESS, 'Others'),
        )


class Savings:
    LESS_THAN_100 = 1
    HUNDRED_TO_500 = 2
    FIVE_HUNDRED_TO_1000 = 3
    MORE_THAN_1000 = 4
    UNKNOWN_OR_NO_ACCOUNT = 5

    @ComputedProperty
    def choices(self):
        return (
         (self.LESS_THAN_100, 'Less than 100 DM'),
         (self.HUNDRED_TO_500, '100 to 500 DM'),
         (self.FIVE_HUNDRED_TO_1000, '500 to 1000 DM'),
         (self.MORE_THAN_1000, 'More than 1000 DM'),
         (self.UNKNOWN_OR_NO_ACCOUNT, 'Unknown / no savings account')
        )


class EmploymentDuration:
    UNEMPLOYED = 1
    LESS_THAN_1_YEAR = 2
    ONE_TO_4_YEARS = 3
    FOUR_TO_7_YEARS = 4
    MORE_THAN_7_YEARS = 5

    @ComputedProperty
    def choices(self):
        return (
             (self.UNEMPLOYED, 'Unemployed'),
             (self.LESS_THAN_1_YEAR, 'Less than 1 year'),
             (self.ONE_TO_4_YEARS, '1 to 4 years'),
             (self.FOUR_TO_7_YEARS, '4 to 7 years'),
             (self.MORE_THAN_7_YEARS, 'More than 7 years'),

        )


class PersonalStatusSex:
    MALE_DIVORCED = 1
    FEMALE_DIVORCED = 2
    MALE_SINGLE = 3
    MALE_MARRIED = 4
    FEMALE_SINGLE = 5

    @ComputedProperty
    def choices(self):
        return (
             (self.MALE_DIVORCED, 'Male: divorced/separated'),
             (self.FEMALE_DIVORCED, 'Female: divorced/separated/married'),
             (self.MALE_SINGLE, 'Male: single'),
             (self.MALE_MARRIED, 'Male: married/widowed'),
             (self.FEMALE_SINGLE, 'Female: single'),
        )


class OtherDebtors:
    NONE = 1
    CO_APPLICANT = 2
    GUARANTOR = 3

    @ComputedProperty
    def choices(self):
        return (
             (self.NONE, 'None'),
             (self.CO_APPLICANT, 'Co-applicant'),
             (self.GUARANTOR, 'Guarantor'),
        )


class PropertyType:
    REAL_ESTATE = 1
    BUILDING_SOCIETY = 2
    CAR_OR_OTHER = 3
    UNKNOWN = 4

    @ComputedProperty
    def choices(self):
        return (
            (self.REAL_ESTATE, 'Real estate'),
            (self.BUILDING_SOCIETY, 'If not A121: building society savings agreement /life insurance'),
            (self.CAR_OR_OTHER, 'If not A121/A122: car or other, not in attribute 6'),
            (self.UNKNOWN, 'Unknown / no property'),

        )


class OtherInstallmentPlans:
    BANK = 1
    STORES = 2
    NONE = 3

    @ComputedProperty
    def choices(self):
        return (
             (self.BANK, 'Bank'),
             (self.STORES, 'Stores'),
             (self.NONE, 'None'),
        )


class Housing:
    RENT = 1
    OWN = 2
    FOR_FREE = 3

    @ComputedProperty
    def choices(self):
        return (
             (self.RENT, 'Rent'),
             (self.OWN, 'Own'),
             (self.FOR_FREE, 'For free'),
        )


class Job:
    UNEMPLOYED = 1
    UNSKILLED_RESIDENT = 2
    SKILLED_EMPLOYEE = 3
    MANAGEMENT_LEVEL = 4

    @ComputedProperty
    def choices(self):
        return (
             (self.UNEMPLOYED, 'Unemployed / unskilled - non-resident'),
             (self.UNSKILLED_RESIDENT, 'Unskilled - resident'),
             (self.SKILLED_EMPLOYEE, 'Skilled employee / official'),
             (self.MANAGEMENT_LEVEL, 'Management / Self-employed /HQE / Officer'),
        )


class ApplicationSelector:
    ANALYSER_APPLICATION = 1
    CRUD_APPLICATION = 2

    def choices(self):
        return (
            (self.ANALYSER_APPLICATION, 'None'),
            (self.CRUD_APPLICATION, 'Yes, registered under the customers name'),
        )
