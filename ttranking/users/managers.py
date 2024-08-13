from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def email_validator(self, email: str):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Please enter a valid email address."))

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        Creates and saves a new staff user with the given email and password.
        :param email:
        :param first_name:
        :param last_name:
        :param password:
        :param extra_fields:
        :return:
        """
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("An email address is required."))

        if not first_name:
            raise ValueError(_("First name is required."))

        if not last_name:
            raise ValueError(_("Last name is required."))

        user = self.model(email=email, first_name=first_name, last_name=last_name, is_staff=True)
        user.set_password(password)
        user.save(using=self._db)
        return user
