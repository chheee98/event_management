from django.contrib.auth import get_user_model
from django.db import models


user_model = get_user_model()


class AbstractBaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(
        user_model,
        on_delete=models.CASCADE,
        related_name="%(class)s_created_by",
        editable=False,
    )

    write_date = models.DateTimeField(auto_now=True)
    write_by = models.ForeignKey(
        user_model,
        on_delete=models.CASCADE,
        editable=False,
        related_name="%(class)s_update_by",
    )

    class Meta:
        abstract = True
