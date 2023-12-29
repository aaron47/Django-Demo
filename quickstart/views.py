from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from .models import User


class CreateUserView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserMixinView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Can also be rewritten as:
class CreateUserCreateMixinView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    """
        Can also perform the password hashing over here by writing this method

        def perform_create(self, serializer):
            password = make_password(serializer.validated_data.get('password'))
            serializer.save(password=password)
    """

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GetAllUsersView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        response_data = {"users": serializer.data}

        return Response(response_data, status=status.HTTP_200_OK)


class GetAllUsersGenericView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# Can rewrite it like this as well
class GetAllUsersListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
