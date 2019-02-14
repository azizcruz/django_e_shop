from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from .forms import CustomUserCreationForm, RequestActivationLinkForm
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth import login, authenticate
from django.core.mail import EmailMessage
from .models import CustomUser

# Needed Functions.
def send_activation_link(request, user, to_email):
    # Begin Activation Link Logic Proccess.
    current_site = get_current_site(request)
    mail_subject = 'Shppy Activation'
    message = render_to_string('shop_auth/acc_active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        'token':account_activation_token.make_token(user)
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()

# Create your views here.

def register(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            to_email = form.cleaned_data.get('email')
            send_activation_link(request, user,to_email)
            return redirect('shop_auth:confirm_message')
        else:
            return render(request, 'shop_auth/register.html', {'form':form, 'title':'register'})


    form = CustomUserCreationForm()
    context = {
        'title': 'Register',
        'form': form,
    }

    return render(request, 'shop_auth/register.html', context)

def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.active = True
        user.save()
        return redirect('shop_auth:activation_success')
    else:
        return HttpResponse('Activation link is invalid!')

def confirm_message(request):
    return render(request, 'shop_auth/confirmation_message_page.html', context=None)

def activation_success(request):
    return render(request, 'shop_auth/confirmation_success.html', context=None)

def request_activation(request):
    if request.method == 'POST':
        form = RequestActivationLinkForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(CustomUser, username=request.user.username)
            print(user)
            return HttpResponse('0')
    user = get_object_or_404(CustomUser, username=request.user.username)
    send_activation_link(request, user, user.email)
    return redirect('shop_auth:confirm_message')