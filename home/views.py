from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import requests,json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Contact
from django.contrib import messages
from datetime import datetime



def home(request):
   
    return render(request,'home/login.html')

def contact(request):
    if request.method=="POST":
        fname = request.POST['fname']
        lname =request.POST['lname']
        email = request.POST['email']
        message =request.POST['message']
        contact = Contact(first_name=fname,last_name=lname,email=email,message=message)


        # recaptcha code
        clientkey= request.POST['g-recaptcha-response']
        secretKey = '6LcPN_oZAAAAACQU8kPi5epu7dRtHNC0_ACacbq-'
        captchaData = {
            'secret':secretKey,
            'response':clientkey
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchaData)
        response = json.loads(r.text)
        verify = response['success']
        

        if verify:
            contact.save()
            messages.success(request,"Your message has been sent")
        else:
            messages.error(request,"Please select the Recaptcha")
    return render(request,'home/contact.html')
    
def analytics(request,):
    if request.method=='POST':
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        if enddate<startdate:
            messages.error(request,"Please select the date properly")
            return redirect('analytics')
        
        item = Contact.objects.filter(time_stamp__range=[startdate,enddate])
        d={}
        for i in item:
            a = str((i.time_stamp))
            d[a]=d.get(a,0)+1
        dat=[]
        count=[]
        for j in d:
            dat.append(j)
            count.append(d[j])
        messages.success(request,f'Number of queries in between {startdate} and {enddate}')
     
      
        return render(request,'home/analytics.html',{'dat':dat,'count':count})
    return render(request,'home/analytics.html')
    

def handleLogout(request):
    logout(request)
    messages.success(request,'You are logged out successfully')
    return redirect('/')