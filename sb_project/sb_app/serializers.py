from django.contrib.auth.models import User
from rest_framework import serializers

from sb_app.models import UserProfile, Transaction


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['password', 'first_name', 'last_name', 'email']
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active',)

    def create(self, validated_data):
        validated_data["username"] = validated_data["email"]
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        # create user profile by default when user got created.
        UserProfile.objects.create(user=user)
        return user

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"
