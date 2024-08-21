from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Task, Comment
from .serializers import TaskSerializer, CommentSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created_at', 'is_completed']
    search_fields = ['name', 'description', 'done']

    def get_queryset(self):
            queryset = Task.objects.all()
            is_done= self.request.query_params.get('done', None)
            
            if is_done is not None:
                is_done = is_done.lower() in ['true', '1']
                queryset = queryset.filter(done=is_done)
            
            return queryset

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer