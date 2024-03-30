from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.serializers import PostSerializer


# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False)
    return render(request, 'post_list_with_bootstrap.html', {'posts': posts})


class PostViewSet(ModelViewSet):
    queryset = Post.objects.filter(published_date__isnull=False)
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]  # allows anonymous user to access the endpoints
