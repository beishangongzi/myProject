from django.urls import path

from .views import StudentListView

urlpatterns = [
    path("students/", StudentListView.as_view({"get": "list", "post": "create"})),
    path("students/<int:pk>/", StudentListView.as_view({"get": "retrieve",
                                                        "put": "update",
                                                        "patch":"partial_update",
                                                        "delete": "destroy"})),
]