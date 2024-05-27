from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import Subscriber
from bookstore.settings import EMAIL_HOST_USER
import uuid


def subscriber(request):
    if request.is_ajax:
        email_address = request.GET.get('subscribe')
        print(email_address)
        save_data = Subscriber(
           email_address = email_address,
        )
        save_data.save()
    # save_data = Subscriber(
    #     email_address = str(subscribe),
    # )
    # save_data.save()
    # token = Subscriber.object.get(email = subscribe)

    # subject = 'BookShelf: Confirmation email for subscriber'
    # message = 'Welcome to our website, please click on the link bellow to confirm subscription to our shop \
    #                localhost:8000/subscribe/confirm/'
    # send_mail(subject, message + token.token, EMAIL_HOST_USER, [subscribe], fail_silently = False)
        data = {

        }
        return JsonResponse(data)