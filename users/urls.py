from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views.create_user import CreateUser


urlpatterns = [
    # Views Api
    path('create/', CreateUser.as_view(), name='create_user_view'),

    # Login & Refresh Api
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/token/', TokenRefreshView.as_view(), name='token_refresh'),

]

