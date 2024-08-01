from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import User
from apps.users.api.LogIn.serializers import UserLoginSerializer


class UserLoginApiView(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            tokens = user.tokens
            return Response(
                {
                    'full_name': user.full_name,
                    'phone' : user.phone,
                    'access_token' : tokens['access'],
                    'refresh_token' : tokens['refresh']
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)