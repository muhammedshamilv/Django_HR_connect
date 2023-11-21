from django.urls import path

from staff.views import ProjectAPI, TaskLogAPI, GrievanceAPI, DesignationAPI, ServiceRecordAPI, PromotionHistoryAPI, UserProjectAPI, AchievementHistoryAPI

urlpatterns = [
    path("project/", ProjectAPI.as_view(), name="project"),
    path("task-log/", TaskLogAPI.as_view(), name="task-log"),
    path("grievance/", GrievanceAPI.as_view(), name="grievance"),
    path("user-project/", UserProjectAPI.as_view(), name="user-project"),
    path("achievement-history/", AchievementHistoryAPI.as_view(),
         name="achievement-history"),
    path("promotion-history/", PromotionHistoryAPI.as_view(),
         name="promotion-history"),
    path("service-record/", ServiceRecordAPI.as_view(),
         name="service-record"),
    path("designation/", DesignationAPI.as_view(),
         name="designation"),

]
