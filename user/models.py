from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, user_id, username, password=None):
        if not user_id:
            raise ValueError("Users must have an id")
        if not username:
            raise ValueError("User must have an username")
        user = self.model(user_id=user_id, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, user_id, username, password=None):
        user = self.create_user(user_id=user_id, password=password, username=username)
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    user_id = models.CharField("아이디", max_length=50, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    username = models.CharField("이름", max_length=20)
    created_date = models.DateTimeField("생성일", auto_now_add=True)
    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "user_id"

    REQUIRED_FIELDS = ["password", "username"]

    objects = UserManager()

    def __str__(self):
        return f"{self.user_id} / {self.username}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
