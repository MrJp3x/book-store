from django.db.models import Q
from rest_framework import serializers
from account.models import User, UserProfile, PublisherProfile, AdminProfile


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password')

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

        validated_data.pop('confirm_password')
        user = User.objects.create(**validated_data)
        return user


# region Profile
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class PublisherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherProfile
        fields = '__all__'


class AdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = '__all__'

# endregion
