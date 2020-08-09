import threading

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .forms import ContactForm

letters = []
number_of_letters = 10


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            text = request.POST.get('text')
            timer = int(request.POST.get('timer'))
            letters.append({"text": text, "timer": timer})
            t = threading.Timer(timer, worker, args=(text,))
            t.start()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'mail/index.html', {'title': 'Обратная связь', 'form': form})


def worker(text):
    send_mail(
        'Тестовое сообщение для задания E2',
        text,
        'TestSFE2@rambler.ru',          #Адрес почты отправителя
        ['***@mail.ru'],                #Адрес получателя
        fail_silently=True)


def mails_list(request):
    emails = show_last_tasks()
    mail = '<h1>Список писем</h1>'
    for email in emails:
        mail += '<div><p>'
        for value in email:
            mail += f'{value}:     {email[value]}    '
        mail += '</p></div><hr>'
    return HttpResponse(mail)


def show_last_tasks():
    return letters[-number_of_letters:]
