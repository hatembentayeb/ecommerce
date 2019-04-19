from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={

                "class": "form-control",
                "placeholder": "your fullname"

            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={

                "class": "form-control",
                "placeholder": "your email"

            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={

                "class": "form-control",
                "placeholder": "your message"

            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not "gmail.com" in email:
            raise forms.ValidationError("the Email mmust be GMAIL")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="comfirm password", widget=forms.PasswordInput)
