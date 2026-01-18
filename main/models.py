from django.db import models
from django.conf import settings
from parler.models import TranslatableModel, TranslatedFields

User = settings.AUTH_USER_MODEL

class BaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.user.username} - {self.amount}"


class Income(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        source=models.CharField(max_length=255, null=True, blank=True),
    )

class Expense(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        source=models.CharField(max_length=255, null=True, blank=True),
    )





