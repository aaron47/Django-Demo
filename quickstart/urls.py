from django.urls import path

from quickstart.views import CreateUserView, GetAllUsersView, GetAllUsersGenericView

urlpatterns = [
    path("create", CreateUserView.as_view(), name="Create a user"),
    path("", GetAllUsersView.as_view(), name="Returns all users"),
    path(
        "mixin",
        GetAllUsersGenericView.as_view(),
        name="Returns all users but using generic api view and mixins",
    ),
]
