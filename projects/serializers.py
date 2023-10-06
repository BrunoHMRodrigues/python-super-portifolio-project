from rest_framework import serializers
from .models import Profile, Project, Certificate, CertifyingInstitution


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class NestedCertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["id", "name", "timestamp"]


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    # certificates = CertificateSerializer(many=True, read_only=True)
    certificates = NestedCertificatesSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ["id", "name", "url", "certificates"]
        # fields = '__all__'

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates")
        new_certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        new_certificate = {}
        for certificate in certificates_data:
            new_certificate = {
                "name": certificate["name"],
                "certifying_institution": new_certifying_institution,
                "profiles": [],
            }
            CertificateSerializer().create(new_certificate)
        return new_certifying_institution


class ProfileSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True, read_only=True)
    certifying_institutions = CertifyingInstitutionSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Profile
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


# class InlineCertificateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Certificate
#         fields = ['name', 'timestamp']
