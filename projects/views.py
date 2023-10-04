from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly)
# from django.shortcuts import render, get_object_or_404
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer
# from .permissions import ProfileDetailPermission


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticatedOrReadOnly()]
        return [IsAuthenticated()]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
