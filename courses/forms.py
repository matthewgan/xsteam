from django import forms
from .models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = [
            'cid',
            'timestamp',
            'updated',
        ]