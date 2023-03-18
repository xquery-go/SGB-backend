

class Status:
    HAS_ACCOUNT = 1
    NO_ACCOUNT = 2
    def choices(self):
        return (
            (self.HAS_ACCOUNT, 'Has Account'),
            (self.NO_ACCOUNT, 'No Account'),
        )


class Duration:

    def choices(self):
        return (
            (),
        )


class CreditHistory:

    def choices(self):
        return (
            (),
        )


class Purpose:

    def choices(self):
        return (
            (),
        )


class Amount:

    def choices(self):
        return (
            (),
        )


class Savings:

    def choices(self):
        return (
            (),
        )


class EmploymentDuration:

    def choices(self):
        return (
            (),
        )


class InstallmentRate:

    def choices(self):
        return (
            (),
        )


class PersonalStatusSex:

    def choices(self):
        return (
            (),
        )


class OtherDebtors:

    def choices(self):
        return (
            (),
        )


class PresentResidence:

    def choices(self):
        return (
            (),
        )


class MostValuableProperty:

    def choices(self):
        return (
            (),
        )


class Age:

    def choices(self):
        return (
            (),
        )


class OtherInstallmentPlans:

    def choices(self):
        return (
            (),
        )


class Housing:

    def choices(self):
        return (
            (),
        )


class NumberCredits:

    def choices(self):
        return (
            (),
        )


class Job:

    def choices(self):
        return (
            (),
        )


class PeopleLiable:

    def choices(self):
        return (
            (),
        )


class HasTelephone:

    def choices(self):
        return (
            (),
        )


class IsForeignWorkerclass:

    def choices(self):
        return (
            (),
        )


class UserGroup:
    VISITOR = 1
    BANK_STAFF = 2
    BANK_STAFF_MANAGER = 3
    ADMIN = 4
    DEBTOR = 5
    ACCOUNT_HOLDER = 6

    def choices(self):
        return (
            (self.VISITOR, 'Visitor'),
            (self.BANK_STAFF, 'Bank Staff'),
            (self.BANK_STAFF_MANAGER, 'Bank Manager'),
            (self.ADMIN, 'Administrator'),
            (self.DEBTOR, 'Debtor'),
            (self.ACCOUNT_HOLDER, 'Account Holder'),
        )
