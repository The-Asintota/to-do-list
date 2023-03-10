from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


UserModel = get_user_model()

class EmailBackend(ModelBackend):

    def user_can_authenticate(self, user):
        """
        Verifica si el usuario puede autenticarse.
        """
        is_active = getattr(user, 'is_active', None)
        if is_active is None:
            return True
        return is_active
    
    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None or password is None:
            return None
        try:
            user = UserModel.objects.get(Q(email=email))
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            return None
        
        
