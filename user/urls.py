from django.urls import path

from user.views import HealthCheck, Account, UserLogin, EmployeeAcccount

urlpatterns = [
    path("", HealthCheck.as_view(), name="health"),
    path("sign-up/", Account.as_view(), name="sign-up"),
    path("sign-in/", UserLogin.as_view(), name="sign-ip"),
    path("create-user/", EmployeeAcccount.as_view(), name="create-user")
    # path("update-profile/<uuid:uuid>/", AccountUpdate.as_view(), name="update"),

]
