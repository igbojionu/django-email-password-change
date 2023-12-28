# your_app/forms.py
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

class CustomPasswordChangeForm(PasswordChangeForm):
    def save(self, user):
        new_password = get_random_string()
        user.set_password(new_password)
        user.save()

        # Shoot that new password via email
        send_mail(
            'Password Reset',
            f'Your new password is: {new_password}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )
