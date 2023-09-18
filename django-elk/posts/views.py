from rest_framework import generics, permissions, views

from .models import Post
from .serializers import PostSerializer

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()

class ErrorView(views.APIView):

    def get(self, request):
        raise ConnectionError    