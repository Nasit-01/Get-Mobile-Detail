from django.shortcuts import render
from django.shortcuts import HttpResponse
from mobileInfo.models import Contact
import phonenumbers  
from phonenumbers import timezone,carrier,geocoder


# Create your views here...

def index(request):
    #return HttpResponse('this is main page')
    return render(request,'index.html')

def info(request):

    if request.method=='POST':
        login_data = request.POST.dict()
        num = login_data.get("number")
        # num=request.POST.get('number')  --> not properly work
        # print(num)

        phone=phonenumbers.parse(num)
        time=timezone.time_zones_for_number(phone)
        car=carrier.name_for_number(phone,"en")
        reg= geocoder.description_for_number(phone,"en")

        context = {
            "phone" : phone,
            "time"  : time,
            "car"  : car,
            "reg"  : reg,
        }
        
        return render(request,"info.html",context)



