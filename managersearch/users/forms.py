from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill, Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name':'Name',
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 
                  'bio', 'short_intro', 'profile_image',
                  'social_youtube','social_twitter','social_telegram',
                  'social_reddit','social_website']



class Skillform(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']

    

