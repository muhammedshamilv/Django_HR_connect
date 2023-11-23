from django.urls import path

from staff import views
urlpatterns = [
    path("project/", views.ProjectAPI.as_view(), name="project"),
    path("project/<uuid:id>/", views.GetProject.as_view(), name="get-project"),

    path("task-log/",
         views.TaskLogAPI.as_view(), name="task-log"),
    path("task-log/all/", views.GetAllTaskLog.as_view(), name="get-all-task-log"),
    path("task-log/<uuid:id>/", views.TaskLogDetailAPI.as_view(),
         name="task-details-log"),

    path("grievance/",
         views.GrievanceAPI.as_view(), name="grievance"),
    path("grievance/<uuid:id>/",
         views.GrievanceDetailAPI.as_view(), name="grievance-detail"),
    path("grievance/all/", views.GetAllGrievance.as_view(),
         name="get-all-grievance"),

    path("user-project/",
         views.UserProjectAPI.as_view(), name="user-project"),
    path("user-project/all/", views.GetAllUserProject.as_view(),
         name="all-user-project"),
    path("user-project/<uuid:id>/", views.DeleteUserProjectAPI.as_view(),
         name="delete-user-project"),

    path("achievement-history/all/", views.GetAllAchievement.as_view(),
         name="get-all-achievement"),
    path("achievement-history/", views.AchievementHistoryAPI.as_view(),
         name="achievement-history"),
    path("achievement-history/<uuid:id>/", views.AchievementHistoryDetailAPI.as_view(),
         name="get-achievement"),

    path("promotion-history/", views.PromotionHistoryAPI.as_view(),
         name="promotion-history"),
    path("promotion-history/<uuid:id>/", views.PromotionHistoryDetailAPI.as_view(),
         name="get-promotion-history"),
    path("promotion-history/all/", views.PromotionAllHistory.as_view(),
         name="all-promotion-history"),

    path("designation/all/", views.DesignationAPI.as_view(),
         name="designation"),
    path("designation/", views.DesignationPost.as_view(),
         name="add-designation"),
    path("designation/<uuid:id>/", views.DesignationDetailAPI.as_view(),
         name="designation-detail"),

    path("service-record/", views.ServiceRecordAPI.as_view(),
         name="service-record"),
    path("service-record/<uuid:id>/", views.ServiceRecordDetailAPI.as_view(),
         name="service-record-detail"),
]
