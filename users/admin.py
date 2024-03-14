from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import decorators, get_user_model
from django.utils.translation import gettext_lazy as _

from users.forms import UserAdminChangeForm, UserAdminCreationForm
from users import models

User = get_user_model()

if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    # Force the `admin` sign in process to go through the `django-allauth` workflow:
    # https://django-allauth.readthedocs.io/en/stable/advanced.html#admin
    admin.site.login = decorators.login_required(admin.site.login)  # type: ignore[method-assign]


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


class CertificateInline(admin.TabularInline):
    model = models.Certificate
    extra = 0


class OtherDetailInline(admin.TabularInline):
    model = models.OtherDetail
    extra = 0


class ExperienceLetterInline(admin.TabularInline):
    model = models.ExperienceLetter
    extra = 0


class AttachmentBusinessDocInline(admin.TabularInline):
    model = models.AttachmentBusinessDoc
    extra = 0


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DoctorPersonalInfo)
class DoctorPersonalInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DoctorDetail)
class DoctorDetailAdmin(admin.ModelAdmin):
    inlines = [CertificateInline, OtherDetailInline]


@admin.register(models.DoctorExperience)
class DoctorExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceLetterInline]


@admin.register(models.SellerBusiness)
class SellerBusinessAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BankAttachment)
class BankAttachmentAdmin(admin.ModelAdmin):
    inlines = [AttachmentBusinessDocInline]


@admin.register(models.BankDetail)
class BankDetailAdmin(admin.ModelAdmin):
    pass


