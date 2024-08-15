from .models import reviews
from django import forms

class YoursReviews(forms.ModelForm):
    class Meta:
        model = reviews
        fields=['title', 'published', 'summary', 'points', 'chapter', 'tags','is_complete', 'image']
    