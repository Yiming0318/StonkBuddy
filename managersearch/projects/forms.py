from django.forms import ModelForm
from django import forms
from .models import  Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link']
        widgets ={
            'tags':forms.CheckboxSelectMultiple(),
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']


    labels = {
        'value': 'Place Your Vote',
        'body': 'Add Your Comments'
    }