from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import UserSerializer, SavingsSerializer, EqubGroupSerializer, EqubMembershipSerializer, BlogSerializer, TransactionSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Savings, EqubGroup, EqubMembership, Blog, Transaction
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination

class UserAPIView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class SavingListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the authenticated user
        user = request.user

        # Filter Saving data for the specific user
        savings = Savings.objects.filter(user=user)

        # Serialize the data
        serializer = SavingsSerializer(savings, many=True)

        # Return the response with the serialized data
        return Response(serializer.data)
    

class UserEqubGroupAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the authenticated user
        user = request.user

        # Try to get the EqubMembership for the authenticated user
        try:
            user_membership = EqubMembership.objects.get(user=user)
        except EqubMembership.DoesNotExist:
            raise NotFound("The user is not a member of any Equb group.")

        # Get the EqubGroup associated with the user's membership
        equb_group = user_membership.equb_group

        # Serialize the EqubGroup data
        serializer = EqubGroupSerializer(equb_group)

        # Return the serialized data as a response
        return Response(serializer.data)

class UserEqubMembershipAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the authenticated user
        user = request.user

        # Get the user's EqubMembership
        try:
            user_membership = EqubMembership.objects.get(user=user)
        except EqubMembership.DoesNotExist:
            raise NotFound("The user is not a member of any Equb group.")

        # Get the EqubGroup the user is part of
        equb_group = user_membership.equb_group

        # Get all other members of the same EqubGroup (excluding the current user)
        other_memberships = EqubMembership.objects.filter(equb_group=equb_group)

        # Serialize the other memberships
        serializer = EqubMembershipSerializer(other_memberships, many=True)

        # Return the response with the serialized data
        return Response(serializer.data)


class BlogPostPagination(PageNumberPagination):
    page_size = 10  # Set the number of blog posts per page

class BlogPostListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        blog_posts = Blog.objects.all()
        paginator = BlogPostPagination()
        result_page = paginator.paginate_queryset(blog_posts, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class TransactionListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the authenticated user
        user = request.user

        # Filter Saving data for the specific user
        transaction = Transaction.objects.filter(user=user)

        # Serialize the data
        serializer = TransactionSerializer(transaction, many=True)

        # Return the response with the serialized data
        return Response(serializer.data)
    