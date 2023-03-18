
class UserGroup:
    VISITOR = 1
    BANK_STAFF = 2
    BANK_STAFF_MANAGER = 3
    ADMIN = 4
    DEBTOR = 5
    ACCOUNT_HOLDER = 6

    @classmethod
    def choices(cls):
        return (
            (cls.VISITOR, 'Visitor'),
            (cls.BANK_STAFF, 'Bank Staff'),
            (cls.BANK_STAFF_MANAGER, 'Bank Manager'),
            (cls.ADMIN, 'Administrator'),
            (cls.DEBTOR, 'Debtor'),
            (cls.ACCOUNT_HOLDER, 'Account Holder'),
        )


class UserActiveStatus:
    ACTIVE = 1
    DEACTIVATED = 2
    BLOCKED = 3
    INACTIVE = 4

    @classmethod
    def choices(cls):
        return (
            (cls.ACTIVE, 'Active'),
            (cls.DEACTIVATED, 'Deactivated'),
            (cls.BLOCKED, 'Blocked'),
            (cls.INACTIVE, 'Inactive'),
        )


class Status:
    HAS_ACCOUNT = 1
    NO_ACCOUNT = 2

    @classmethod
    def choices(cls):
        return (
            (cls.HAS_ACCOUNT, 'Has Account'),
            (cls.NO_ACCOUNT, 'No Account'),
        )


class Duration:

    def choices(cls):
        return (
            (),
        )


class CreditHistory:

    def choices(cls):
        return (
            (),
        )


class Purpose:

    def choices(cls):
        return (
            (),
        )


class Amount:

    def choices(cls):
        return (
            (),
        )


class Savings:

    def choices(cls):
        return (
            (),
        )


class EmploymentDuration:

    def choices(cls):
        return (
            (),
        )


class InstallmentRate:

    def choices(cls):
        return (
            (),
        )


class PersonalStatusSex:

    def choices(cls):
        return (
            (),
        )


class OtherDebtors:

    def choices(cls):
        return (
            (),
        )


class PresentResidence:

    def choices(cls):
        return (
            (),
        )


class MostValuableProperty:

    def choices(cls):
        return (
            (),
        )


class Age:

    def choices(cls):
        return (
            (),
        )


class OtherInstallmentPlans:

    def choices(cls):
        return (
            (),
        )


class Housing:

    def choices(cls):
        return (
            (),
        )


class NumberCredits:

    def choices(cls):
        return (
            (),
        )


class Job:

    def choices(cls):
        return (
            (),
        )


class PeopleLiable:

    def choices(cls):
        return (
            (),
        )


class HasTelephone:

    def choices(cls):
        return (
            (),
        )


class IsForeignWorkerclass:

    def choices(cls):
        return (
            (),
        )

