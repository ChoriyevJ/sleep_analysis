from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


from django.db import models
from utils.models import BaseModel


class User(AbstractUser):
    """
    Default custom user model for My Awesome Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class DOBChoice(models.TextChoices):
    EXAMPLE1 = 'Example1'
    EXAMPLE2 = 'Example2'


class GenderChoice(models.TextChoices):
    MALE = 'Male'
    FEMALE = 'Female'


class Language(BaseModel):
    title = models.CharField(max_length=31)

    def __str__(self):
        return self.title


class Country(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class State(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Currency(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    image = models.ImageField(upload_to='images/profile/', blank=True, null=True)
    phone = models.CharField(max_length=15)
    dob = models.CharField(max_length=15, choices=DOBChoice.choices,
                           blank=True, null=True)

    height = models.PositiveSmallIntegerField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    # doctor_personal_info = models.OneToOneField('DoctorPersonalInfo', on_delete=models.CASCADE,
    #                                             related_name="profile", blank=True, null=True)
    # doctor_detail = models.OneToOneField('DoctorAwardDetail', on_delete=models.CASCADE,
    #                                      related_name='profile', blank=True, null=True)
    # doctor_experience = models.OneToOneField('DoctorExperience', on_delete=models.CASCADE,
    #                                          related_name='profile', blank=True, null=True)

    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.user


# Doctor profile models
class DoctorPersonalInfo(BaseModel):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,
                                   related_name="personal")

    gender = models.CharField(max_length=8, choices=GenderChoice.choices)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True, null=True)


class DoctorDetail(BaseModel):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,
                                   related_name="detail")

    degree = models.CharField(max_length=255)
    college_institute = models.CharField(max_length=255)
    year_of_completion = models.CharField(max_length=4)


class Certificate(BaseModel):
    award_detail = models.ForeignKey(DoctorDetail,
                                     on_delete=models.CASCADE,
                                     related_name="certificates")
    file = models.FileField(upload_to='files/certificate/',validators=[
        FileExtensionValidator(['jpg', 'doc', 'pdf'])
    ])


class OtherDetail(BaseModel):
    award_detail = models.ForeignKey(DoctorDetail,
                                     on_delete=models.CASCADE,
                                     related_name="others")
    detail = models.CharField(max_length=255)


class DoctorExperience(BaseModel):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,
                                   related_name="experience")

    has_experience = models.BooleanField(default=False)
    experience = models.CharField(max_length=2, blank=True, null=True)

    has_clinic = models.BooleanField(default=False)
    clinic = models.CharField(max_length=255, blank=True, null=True)


class ExperienceLetter(BaseModel):
    doctor_experience = models.ForeignKey(DoctorExperience, on_delete=models.CASCADE,
                                          related_name="letters")
    file = models.FileField(upload_to='files/letters/', validators=[
        FileExtensionValidator(['jpg', 'doc', 'pdf'])
    ])


# Seller profile models
class SellerBusiness(BaseModel):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,
                                   related_name="business")
    street_address = models.CharField(max_length=255)
    pin_code = models.CharField(max_length=31)
    info = models.CharField(max_length=255, blank=True, null=True)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)


class BankAttachment(BaseModel):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,
                                   related_name="attachment")


class AttachmentBusinessDoc(BaseModel):

    class DocTypeChoice(models.TextChoices):
        BUSINESS = 'Business'
        PERMISSION = 'Permission'

    doc_type = models.CharField(max_length=15, choices=DocTypeChoice.choices)

    attachment = models.ForeignKey(BankAttachment, on_delete=models.CASCADE,
                                   related_name='business_docs')
    document = models.FileField(upload_to='files/docs', validators=[
        FileExtensionValidator(['pdf', 'doc'])
    ])


class BankDetail(BaseModel):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,
                                   related_name="bank_detail")
    name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    account_phone = models.CharField(max_length=15)
    gst_number = models.CharField(max_length=31)







