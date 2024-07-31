from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email=None, full_name=None, phone=None, password=None, **extra_fields):
        if not email and not phone:
            raise ValueError("User must have either email or phone!")
        if email:
            extra_fields['email'] = email
        if phone:
            extra_fields['phone'] = phone
        if not full_name:
            raise ValueError("User must have a full name!")
        
        extra_fields["full_name"] = full_name
        
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,  phone, password, full_name):
        if not password:
            raise ValueError("User must have password")
        user = self.create_user( phone=phone, password=password, full_name=full_name)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

