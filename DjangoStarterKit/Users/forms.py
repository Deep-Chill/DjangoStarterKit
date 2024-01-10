from django import forms


class CustomSignupForm(forms.Form):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

    def signup(self, request, user):
        user.save()
        profile = user.profile
        profile.bio = self.cleaned_data.get('bio', '')

        if 'profile_picture' in request.FILES:
            profile.picture = self.cleaned_data['profile_picture']

        profile.save()
