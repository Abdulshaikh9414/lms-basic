"""
Created on 05-Jun-2022
@author: Abdulkadir
"""
from rest_framework import viewsets, permissions, views, filters, status

from .models import Book, CustomUserManager, User
from .serializers import BookSerializer, UserSerializer
from .utils import response


class UserSignupAPIView(views.APIView):
    """
    Handles user Signup API flow.
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer

    def post(self, request):
        request_data = request.data
        try:
            if request_data['user_type'] == "admin-user":
                user = CustomUserManager().create_superuser(
                    email=request_data.get('email'), password=request_data.get('password')
                )
            else:
                user = CustomUserManager().create_user(
                    email=request_data.get('email'), password=request_data.get('password')
                )
            return response(self.serializer_class(user).data, status.HTTP_201_CREATED)
        except Exception as IntegrityError:
            return response("Unable to create user", status.HTTP_400_BAD_REQUEST)


class LoginAPIView(views.APIView):
    """
    Handles Login requests
    """
    serializer_class = UserSerializer

    def post(self, request):
        '''
        Validate login data
        '''
        request_data = request.data
        if request_data.get('email') and request_data.get('password'):
            user = User.check_user_exist(email=request_data.get('email'), password=request_data.get('password'))
            if user:
                data = self.serializer_class(user).data
                data['password'] = request_data.get('password')
                return response(data, status.HTTP_200_OK)
            else:
                return response("Data not found", status.HTTP_404_NOT_FOUND)
        else:
            return response("Given email and password is not valid", status.HTTP_400_BAD_REQUEST)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]
    search_fields = ['title', 'isbn', 'author']
    filter_backends = (filters.SearchFilter,)
