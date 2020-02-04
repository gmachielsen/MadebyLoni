from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm
# Create your views here.
def contact(request):
    if request.method == 'POST':
        post = ContactForm(request.POST)
        if post.is_valid():
            post.save()
            messages.success(request, 'We have received your message correctly, we try to answer your email within two working days.')

            # return HttpResponse("Contact details created")
            return redirect('contact:contact')
        else:
            return HttpResponse("form is not validated")
    # if post.is_valid():
    #     post.save()
    #     name = post.cleaned_data.get('name')
    #     email = post.cleaned_data.get('email')
    #     phone = post.cleaned_data.get('phone')
    #     message = post.cleaned_data.get('message')
    #
    #
    # # messages.success(request, ("animalcaresheet successfully added"))
    # # return redirect('post_list')
    #
    # else:
    # # messages.error(request, ("animalcaresheet is NOT been added, please try again"))
    # # return redirect('post_form')
    #     return render(request, 'contact/contact.html', {'post': post})
    else:
        post = ContactForm()

    return render(request, 'contact/contact.html', {'post': post})
