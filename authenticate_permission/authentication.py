from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user = request.query_params.get("user")
        password = request.query_params.get("password")
        if user == "root" and password == "123456":
            root = get_user_model().objects.first()
            return root, None
        return None
