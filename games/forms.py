from django import forms
from games import views
from django.shortcuts import redirect

from games.models import GameReview, Game

class GiveReviewForm(forms.ModelForm):

    class Meta:
        model=GameReview
        fields = [ 'title','body', 'rating']

class UpdateReviewForm(forms.ModelForm):

    class Meta:
        model = GameReview
        fields = [ 'title','body', 'rating']

    def save(self, commit=True):
        review = self.instance
        review.title= self.cleaned_data['title']
        review.body = self.cleaned_data['body']
        review.rating = self.cleaned_data['rating']

        if commit:
            review.save()
            

        return review
