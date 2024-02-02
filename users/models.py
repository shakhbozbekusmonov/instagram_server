from django.contrib.auth.models import AbstractUser
from django.db import models

from common.models import BaseModel

ORDINARY_USER, MANAGER, ADMIN, SUPER_ADMIN = ('ordinary_user', 'manager', 'admin', 'super_admin')
VIA_PHONE, VIA_EMAIL = ('via_phone', 'via_email')
NEW, CODE_VERIFIED, DONE, PHOTO_STEP = ('new', 'code_verified', 'done', 'photo_step')
# MALE, FEMALE = ('male', 'female')


class User(AbstractUser, BaseModel):
    USER_ROLES_CHOICES = (
        (ORDINARY_USER, ORDINARY_USER),
        (MANAGER, MANAGER),
        (ADMIN, ADMIN),
        (SUPER_ADMIN, SUPER_ADMIN),
    )
    AUTH_TYPE_CHOICES = (
        (VIA_PHONE, VIA_PHONE),
        (VIA_EMAIL, VIA_EMAIL),
    )
    AUTH_STATUS_CHOICES = (
        (NEW, NEW),
        (CODE_VERIFIED, CODE_VERIFIED),
        (DONE, DONE),
        (PHOTO_STEP, PHOTO_STEP)
    )
    # GENDER_CHOICES = (
    #     (MALE, MALE),
    #     (FEMALE, FEMALE)
    # )
    user_roles = models.CharField(max_length=31, choices=USER_ROLES_CHOICES, default=ORDINARY_USER)
    auth_type = models.CharField(max_length=31, choices=AUTH_TYPE_CHOICES)
    auth_status = models.CharField(max_length=31, choices=AUTH_STATUS_CHOICES, default=NEW)
    # gender = models.CharField(max_length=31, choices=GENDER_CHOICES)
    email = models.EmailField(null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True, unique=True)
    photo = models.ImageField(upload_to='user/photos', null=True, blank=True)

    def __str__(self):
        return self.username