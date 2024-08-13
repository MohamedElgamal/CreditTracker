from django.db import models

# Create your models here.


class Countries(models.Model):
    country = models.CharField(max_length=45, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.id}) {self.country}"

    class Meta:
        db_table = "countries"


class Persons(models.Model):
    name = models.CharField(max_length=256)
    identifier = models.CharField(max_length=256)
    notes = models.TextField()
    amount = models.PositiveSmallIntegerField()  # This value should be smalle pos int
    nationality = models.ForeignKey(Countries, on_delete=models.CASCADE)
    suspended = models.BooleanField(default=False)
    suspend_reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.id}) {self.name} {self.amount}"

    class Meta:
        db_table = "persons"


class FiscalYears(models.Model):
    year = models.CharField(max_length=45)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(default=None)


ROLES = (
    ("accountant", "accountant"),
    ("manager", "manager"),
)


class Users(models.Model):
    name = models.CharField(max_length=256)
    role = models.CharField(max_length=45, choices=ROLES)

    def __str__(self):
        return f"({self.id}) {self.name}"

    class Meta:
        db_table = "users"


TYPE = (
    ("debtor", "debtor"),
    ("creditors", "creditors"),
)


class Transcations(models.Model):
    # Convert models.CASCADE TO Restrict
    owner_person = models.ForeignKey(Persons, on_delete=models.RESTRICT)
    fiscal_year = models.ForeignKey(FiscalYears, on_delete=models.RESTRICT)
    commited_by = models.ForeignKey(Users, on_delete=models.RESTRICT)
    reviewed_by = models.ForeignKey(
        Users, null=True, related_name="reviewer", on_delete=models.RESTRICT
    )
    type = models.CharField(max_length=45, choices=TYPE)
    transcation_date = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveSmallIntegerField()
    notres = models.TextField()

    class Meta:
        db_table = "transcations"


class Accounts(models.Model):
    accoutant = models.ForeignKey(Users, on_delete=models.RESTRICT)
    balance = models.DecimalField()
    updated_at = models.DateTimeField(
        auto_now_add=True
    )  # should it be auto_now_add for updates?
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "accounts"
