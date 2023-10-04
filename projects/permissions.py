# from rest_framework import permissions

# class ProfileDetailPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if view.action in ['update', 'destroy']:
#             return request.user and request.user.is_authenticated
#         return True
