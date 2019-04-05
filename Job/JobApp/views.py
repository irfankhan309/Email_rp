from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from JobApp.models import Test_Form
from . import forms
# Create your views here.
# def index_view(request):
#     subject = 'Thanks for visitng'
#     message = 'this is all about you buying the vehicle'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['irfanqehs@gmail.com',]
#     send_mail(subject, message, email_from, recipient_list)
#     return render(request,'JobApp/index.html')

# def email_view(request):
#     if request.method =='GET':
#         Form = forms.ContactForm()
#     else:
#         Form =forms.ContactForm(request.POST)
#         if Form.is_valid():
#             subject = Form.cleaned_data['subject']
#             your_email = Form.cleaned_data['your_email']
#             message = Form.cleaned_data['message']
#             send_mail(subject,message, your_email,[your_email])
#             # except BadHeaderError:
#             #     return HttpResponse('Invalid header found.')
#             # return redirect('{% url "success"%}')
#     return render(request,'JobApp/mail.html',{'Form':Form})

def home_view(request):
    return render(request,'JobApp/index.html')

def test_email_view(request):
    form =forms.form_test()
    if request.method == 'POST':
        form = forms.form_test(request.POST or None)

        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            # send_mai(subject,message,from_email,to_email_list,fail_silently=True)
            subject = 'Thank you for subscribing please visit for more stuff'
            message = ' welcome to our tap to get business and browse more to buy with exciting offers...'
            from_mail = settings.EMAIL_HOST_USER
            to_list = [save_it.Email,settings.EMAIL_HOST_USER]

            send_mail(subject,message,from_mail,to_list,fail_silently=True)
            return redirect('home')
        else:
            form= forms.form_test()
    args={'form':form}
    return render(request,'JobApp/mail.html',args)
