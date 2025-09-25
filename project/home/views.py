from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
# Create your views here.
def index(request):
   
   context = {
       "variable":"Nice"
   }
   return render(request, 'index.html',context)
   
    #return render(request,'index.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # Check if all required fields are filled
        if name and email and phone and desc:
            contact = Contact(
                name=name,
                email=email,
                phone=phone,
                desc=desc,
                date=datetime.today()
            )
            contact.save()
            context['success'] = True
        else:
            context['error'] = "All fields are required."

    return render(request, 'contact.html', context)


def service(request):
    return render(request, 'service.html')