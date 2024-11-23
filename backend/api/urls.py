from django.urls import path
from api.views import BlogPostListAPIView, SavingListAPIView, UserEqubGroupAPIView, UserEqubMembershipAPIView, UserAPIView, TransactionListCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('user-login/', UserAPIView.as_view(), name= 'get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='get_refresh'),
    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path('equb-list/', UserEqubMembershipAPIView.as_view(), name='equb-member'),
    path('saving/', SavingListAPIView.as_view(), name='saving-account'),
    path('blog-posts/', BlogPostListAPIView.as_view(), name='blog-list'),
    path('equb-gruop/', UserEqubGroupAPIView.as_view(), name='equb-group'),
    path('transaction-list/', TransactionListCreate.as_view(), name='transaction-list'),
]
