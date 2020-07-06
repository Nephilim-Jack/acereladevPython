from rest_framework.permissions import BasePermission


class OnlyAdminCanCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_staff

        else:
            return True
