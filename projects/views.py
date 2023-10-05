from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly)
from django.shortcuts import render, get_object_or_404
# from django.shortcuts import render, get_object_or_404
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer
# from .permissions import ProfileDetailPermission


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [IsAuthenticatedOrReadOnly()]
    #     return [IsAuthenticated()]
    
    def retrieve(self, request, *args, **kwargs):
        if request.method == 'GET':
            profile = get_object_or_404(Profile, pk=kwargs['pk'])
            projects = Project.objects.filter(profile=profile)

            context = {
                'profile': profile,
                'projects': projects,
            }

            return render(request, 'profile_detail.html', context)

        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
