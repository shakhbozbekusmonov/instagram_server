from rest_framework.exceptions import ValidationError

from common.utility import check_email_or_phone
from .models import User, UserConfirmation, VIA_PHONE, VIA_EMAIL, NEW, CODE_VERIFIED, DONE, PHOTO_STEP
from rest_framework import serializers


class SignUpSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    def __init__(self, *args, **kwargs):
        super(SignUpSerializer, self).__init__(*args, **kwargs)
        self.fields['email_phone_number'] = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'auth_type',
            'auth_status'
        )
        extra_kwargs = {
            'auth_type': {'read_only': True, 'required': False},
            'auth_status': {'read_only': True, 'required': False},
        }

    def validate(self, data):
        super(SignUpSerializer, self).validate(data)
        data = self.auth_validate(data)
        return data

    @staticmethod
    def auth_validate(data):
        user_input = str(data.get('email_phone_number')).lower()
        input_type = check_email_or_phone(user_input)

        if input_type == 'email':
            data = {
                "email": user_input,
                "auth_type": VIA_EMAIL
            }
        elif input_type == 'phone':
            data = {
                "phone_number": user_input,
                "auth_type": VIA_PHONE
            }
        else:
            data = {
                "success": False,
                "message": "You must send email or phone number."
            }
            raise ValidationError(data)

        return data
