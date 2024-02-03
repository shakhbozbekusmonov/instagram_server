import re
from rest_framework.exceptions import ValidationError


email_regex = re.compile(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+")
phone_regex = re.compile(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")


def check_email_or_phone(email_or_phone):
    if re.fullmatch(email_regex, email_or_phone):
        email_or_phone = 'email'
    elif re.fullmatch(phone_regex, email_or_phone):
        email_or_phone = 'phone'
    else:
        data = {
            "success": False,
            "message": "Email yoki telefon raqamingiz noto'g'ri."
        }
        raise ValidationError(data)

    return email_or_phone


