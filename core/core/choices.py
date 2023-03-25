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


# class Status:
#     HAS_ACCOUNT = 1
#     NO_ACCOUNT = 2
#
#     @ComputedProperty
#     def choices(self):
#         return (
#             (self.HAS_ACCOUNT, 'Has Account'),
#             (self.NO_ACCOUNT, 'No Account'),
#         )


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

