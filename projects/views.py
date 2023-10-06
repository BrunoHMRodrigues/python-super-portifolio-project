from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly)
from django.shortcuts import render, get_object_or_404
# from django.shortcuts import render, get_object_or_404
from .models import Profile, Project, Certificate, CertifyingInstitution
from .serializers import (ProfileSerializer,
                          ProjectSerializer,
                          CertificateSerializer,
                          CertifyingInstitutionSerializer)
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
            certificates = Certificate.objects.filter(profiles=profile)
            certifying_institutions = CertifyingInstitution.objects.filter(
                certificates__in=certificates
            )

            context = {
                'profile': profile,
                'projects': projects,
                'certificates': certificates,
                'certifying_institutions': certifying_institutions,
            }

            return render(request, 'profile_detail.html', context)

        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
