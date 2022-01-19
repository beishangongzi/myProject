from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .authentication import CustomAuthentication
from students.models import Student
from students.serializers import StudentModelSerializer
from .permissions import IsAdminOrReadOnly

# class Students(APIView):
#     # authentication_classes = [CustomAuthentication, ]
#
#     def get(self, request):
#         if request.user.id is None:
#             return Response("未认证", status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(f"the user: {request.user}")


class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    authentication_classes = [CustomAuthentication, SessionAuthentication]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAdminOrReadOnly]
