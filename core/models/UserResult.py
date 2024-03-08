from django.db import models

from sport_connect_api.models import BaseModel


class UserResult(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="user_results",
                             verbose_name="Користувач")

