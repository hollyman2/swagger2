from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .models import Post
from .serializers import PostSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class NewsListswagerView(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination 
    
class UserNewsViewSet(viewsets.ViewSet):
    """
    API endpoint that allows posts by a specific user to be viewed.
    """
    pagination_class = PageNumberPagination # Или LimitOffsetPagination, если нужно

    def list(self, request, username=None):
        user = User.objects.filter(username=username).first()
        if user is None:
            return Response({'detail': 'User not found'}, status=404)

        queryset = Post.objects.filter(author=user).order_by('-date_posted')

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
