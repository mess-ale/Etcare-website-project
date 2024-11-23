from rest_framework import serializers
from .models import Savings, EqubGroup, EqubMembership, Blog, Transaction
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'bio', 'last_name', 'gender', 'phone_number')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data['bio'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            phone_number=validated_data['phone_number'],
        )
        return user

class SavingsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested User data

    class Meta:
        model = Savings
        fields = ['savings_id', 'user', 'account_balance', 'account_type', 'interest_rate', 'created_at']


class EqubGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EqubGroup
        fields = ['equb_id', 'name', 'description', 'group_size', 'cycle_period', 'amount_per_cycle', 'start_date', 'created_at']


class EqubMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested User data
    equb_group = EqubGroupSerializer(read_only=True)  # Nested EqubGroup data

    class Meta:
        model = EqubMembership
        fields = ['membership_id', 'equb_group', 'user', 'join_date', 'role']


class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # Nested User data

    class Meta:
        model = Blog
        fields = ['blog_id', 'author', 'title', 'blog_image', 'content', 'created_at', 'updated_at']


class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested User data

    class Meta:
        model = Transaction
        fields = ['transaction_id', 'user', 'transaction_type', 'amount', 'transaction_date']
