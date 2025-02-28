from django.shortcuts import render

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
# Create your views here.

def main_view(request):
    return render(request, 'main.html')

def form_view(request):
    return render(request, 'form.html')

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # メール送信処理
        send_mail(
            subject=f"お問い合わせ: {name}",
            message=f"電話番号: {phone}\nメールアドレス: {email}\nメッセージ:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        return redirect('contact_sent')
    return HttpResponse("無効なリクエストです。")

def contact_sent(request):
    return render(request, 'sent.html')