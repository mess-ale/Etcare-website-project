from django.urls import path
from api.views import  BlogPostListAPIView, SavingListAPIView, TransactionListCreate, UserEqubMembershipAPIView, UserFormSubmissionView, UserProfileView, UserAPIView, LogoutView, CookieTokenObtainPairView, UserEqubGroupAPIView, CustomTokenRefreshView, UpdateUserProfileView

urlpatterns = [
    path('token/', CookieTokenObtainPairView.as_view(), name= 'get_token'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='get_refresh'),
    path('logout/', LogoutView.as_view()),
    path('userlogin/', UserAPIView.as_view(), name= 'get_user'),
    path('profileget/', UserProfileView.as_view(), name= 'get_profile'),
    path('profileupdate/', UpdateUserProfileView.as_view(), name= 'update'),
    path('service/saving/', SavingListAPIView.as_view(), name='saving-account'),
    path('service/equbgroup/', UserEqubGroupAPIView.as_view(), name='saving-account'),
    path('service/equbmembership/', UserEqubMembershipAPIView.as_view(), name='equb-member'),
    path('service/saving/transactionlist/', TransactionListCreate.as_view(), name='transaction-list'),
    path('blogposts/', BlogPostListAPIView.as_view(), name='blog-list'),
    path("form-submissions/", UserFormSubmissionView.as_view(), name="form-submissions"),
    path('equb-gruop/', UserEqubGroupAPIView.as_view(), name='equb-group'),
]
