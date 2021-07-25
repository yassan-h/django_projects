from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from app_test.models.CharacterKihon import CharacterKihon

class SignUpForm(UserCreationForm):

  class Meta:
    model = User
    fields = ('username', 'password1', 'password2')

class CharacterForm(ModelForm):

  class Meta:
    model = CharacterKihon
    fields = ('CHARACTER_CD', 'CHARACTER_NAME', 'CHARACTER_KIND', 'CHARACTER_BIRTH')
