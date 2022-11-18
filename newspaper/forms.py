from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from newspaper.models import Newspaper, Redactor


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    def clean_experience(self):
        return validate_experience(self.cleaned_data["years_of_experience"])


class RedactorExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ["years_of_experience"]

    def clean_experience(self):
        return validate_experience(self.cleaned_data["years_of_experience"])


def validate_experience(
    years_of_experience,
):
    if years_of_experience > 80:
        raise ValidationError("Years of experience should be less than 80")

    return years_of_experience


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"})
    )


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"})
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by topic name"}
        )
    )
