from rest_framework.permissions import BasePermission

#SAFE_METHODS son get, options y head

class LoginOrReadOnly(BasePermission):
    def has_object_permissions(sefl, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        elif request.user.is_authenticated:
            return True

        return False
