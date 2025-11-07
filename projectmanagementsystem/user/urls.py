from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,login,home,register,forgot

router = DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = [
    path('',home,name="home"),
    path('',include(router.urls)),
    path('login/',login,name="login"),
    path('register/',register,name="register"),
    path('forgot/',register,name="forgot")
]

# All the urls available

# GET /user/users/ → List all users
# POST /user/users/ → Create a user
# GET /user/users/<username>/ → Retrieve one user
# PUT /user/users/<username>/ → Update a user (full update)
# PATCH /user/users/<username>/ → Update a user (partial update)
# DELETE /user/users/<username>/ → Delete a user