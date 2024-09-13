from rest_framework import serializers
from django.db.models import Q

from account.models import User


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')


        if not email:
            raise serializers.ValidationError('You must provide an email.')

        user_exists = User.objects.filter(Q(email=email) if email else Q()).exists()

        if user_exists:
            raise serializers.ValidationError("Already registered. Please login.")

        if password != confirm_password:
            raise serializers.ValidationError("Password and confirm password is not match.")

        return data

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        return user

