from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from user.models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = ("password", "phone_number", "username", "email")

    def validate_phone_number(self, phone_number):
        is_exists = User.objects.filter(phone_number=phone_number.__str__()).exists()
        if is_exists:
            raise serializers.ValidationError(("A user is already registered with this phone number."))
        return phone_number

    # overirde create method to set hashed password
    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'], phone_number=validated_data['phone_number'])
        user.set_password(validated_data['password'])
        user.save()
        return user
