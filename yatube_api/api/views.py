from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsOwnerOrReadOnly, ReadOnly
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer, \
    FollowSerializer
from posts.models import Group, Post, Follow, User


class PostViewSet(viewsets.ModelViewSet):
    """Преопределены методы создания, изменения и удаления поста."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        # подставляет юзера как автора для создания поста
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (ReadOnly,)
    pagination_class = None


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    pagination_class = None

    def get_queryset(self):
        # user = get_object_or_404(User, username=self.request.user)
        # new_queryset = Follow.objects.filter(user=self.request.user)
        # return self.request.user.following.all()
        # return new_queryset
        # return Follow.objects.filter(user=user)
        return self.request.user.followers.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Преопределены методы создания, изменения и удаления комментария.
    А также получение кверисета."""
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = None

    def get_queryset(self):
        # возвращает кверисет только комментариев поста из запроса
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        # Подставляет юзера как автора коммента
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
