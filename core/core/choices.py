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
    NO_CREDIT = 0
    ALL_AT_THIS_BANK_PAID = 1
    HAS_CREDIT_DULY_PAID = 2
    DELAY_IN_PAST = 3
    CRITICAL_ACCOUNT = 4

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
    @ComputedProperty
    def choices(self):
        return

class Savings:
    @ComputedProperty
    def choices(self):
        return

class EmploymentDuration:
    @ComputedProperty
    def choices(self):
        return

class PersonalStatusSex:
    @ComputedProperty
    def choices(self):
        return

class OtherDebtors:
    @ComputedProperty
    def choices(self):
        return

class PropertyType:
    @ComputedProperty
    def choices(self):
        return

class OtherInstallmentPlans:
    @ComputedProperty
    def choices(self):
        return

class Housing:
    @ComputedProperty
    def choices(self):
        return

class Job:
    @ComputedProperty
    def choices(self):
        return

class Telephone:
    @ComputedProperty
    def choices(self):
        return

class ForeignWorker:
    @ComputedProperty
    def choices(self):
        return


# class Duration:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class CreditHistory:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class Purpose:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class Amount:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class Savings:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class EmploymentDuration:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class InstallmentRate:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class PersonalStatusSex:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class OtherDebtors:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class PresentResidence:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class MostValuableProperty:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class Age:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class OtherInstallmentPlans:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class Housing:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class NumberCredits:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class Job:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class PeopleLiable:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class HasTelephone:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )
#
#
# class IsForeignWorkerclass:
#     @ComputedProperty
#     def choices(self):
#         return (
#             (),
#         )

