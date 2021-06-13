from django import forms


class ProfileForm(forms.Form):
    #user_image = forms.FileField()
    # add MEDIA_ROOT in settings.ppy for this field
    user_image = forms.ImageField()
