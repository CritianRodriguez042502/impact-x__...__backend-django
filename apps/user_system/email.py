# from django.core.mail import send_mail


from djoser import email

class Activation (email.ActivationEmail):
    template_name = "activation.html"

class Confirmation (email.ConfirmationEmail):
    template_name = "confirmation.html"

class PasswordReset (email.PasswordResetEmail):
    template_name = "password_reset.html"

class PasswordChangedConfirmation (email.PasswordChangedConfirmationEmail):
    template_name = "password_changed_confirmation.html"