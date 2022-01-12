from django.shortcuts import redirect, render
from .models import SignupMaster
from .forms import CareerForm, InquiryForm, SignupForm
from django.contrib.auth import logout
from django.core.mail import send_mail
from Ehousing import settings
import requests
import json
import random

# Create your views here.

def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            signupfrm=SignupForm(request.POST)
            if signupfrm.is_valid():
                signupfrm.save()
                print("Signup Successfully!")
                
                # Email sending
                sub="SignUp Successful! "
                msg="Hello user,\nYour account has been created with Shilpan builders! \nEnjoy our services.\nThanks & regards! \nShilpan Builders \n Rajkot\n+91 96246 44441 \ninfo@shilpan.in "
                from_id=settings.EMAIL_HOST_USER
                #to_id=['Nitinjethava143@yahoo.com']
                to_id=[request.POST['email']]

                send_mail(sub,msg,from_id,to_id)
                print("Email send successfully!")
                return redirect('/')
            else:
                print(signupfrm.errors)
        elif request.POST.get('Signin')=='Signin':
                unm=request.POST['email']
                pas=request.POST['password']

                userid=SignupMaster.objects.get(email=unm)

                user=SignupMaster.objects.filter(email=unm,password=pas)
                if user:
                    print("Signin successfully!")
                    request.session['user']=unm
                    request.session['email']=unm

                    request.session['userid']=userid.id

                    # # mention url
                    # url = "https://www.fast2sms.com/dev/bulk"


                    # # create a dictionary
                    # my_data = {
                    #     # Your default Sender ID
                    #     'sender_id': 'FSTSMS',
                        
                    #     # Put your message here!
                    #     'message': 'This is a test message',
                        
                    #     'language': 'english',
                    #     'route': 'p',
                        
                    #     # You can send sms to multiple numbers
                    #     # separated by comma.
                    #     'numbers': '8469640498'	
                    # }

                    # # create a dictionary
                    # headers = {
                    #     'authorization': 'KLyAgC3SzuUN0b4IoTchWJQ9vRHldktiMemOnDpj5ZwsfB8Y21JC3btipYBfgq8WoKXHnZ0Lm7ysSIGD',
                    #     'Content-Type': "application/x-www-form-urlencoded",
                    #     'Cache-Control': "no-cache"
                    # }

                    # # make a post request
                    # response = requests.request("POST",
                    #                             url,
                    #                             data = my_data,
                    #                             headers = headers)
                    # #load json data from source
                    # returned_msg = json.loads(response.text)

                    # # print the send message
                    # print(returned_msg['message'])
                    return redirect('/home')
                else:
                    print("Signin failed...Try again!")
        else:
            print("Something went wrong...")
           

    return render(request,'index.html')
    
def about(request):
    user=request.session.get('user')
    return render(request,'about.html',{'user':user})

def shilpannova(request):
    user=request.session.get('user')
    return render(request,'shilpannova.html',{'user':user})

def shilpanreva(request):
    user=request.session.get('user')
    return render(request,'shilpanreva.html',{'user':user})

# def about(request):
#     return render(request,'about.html')

def nri(request):
    user=request.session.get('user')
    return render(request,'nri.html',{'user':user})

def career(request):
    user=request.session.get('user')
    if request.method=="POST":
        careerfrm=CareerForm(request.POST,request.FILES)
        if careerfrm.is_valid():
            careerfrm.save()
            print("Your application has been submitted!")

            sub="Career Shilpan Builders! "
            msg="Hello user,\nYour application has been submitted successfully with Shilpan builders! \nOur team will contact you shortly! \nEnjoy our services.\nThanks & regards! \nShilpan Builders \n Rajkot\n+91 96246 44441 \ninfo@shilpan.in "
            from_id=settings.EMAIL_HOST_USER
            #to_id=['Nitinjethava143@yahoo.com']
            to_id=[request.POST['email']]

            send_mail(sub,msg,from_id,to_id)
            print("Email send successfully!")

            return redirect('/career')
        else:
            print(careerfrm.errors)
    else:
        careerfrm=CareerForm()
    return render(request,'career.html',{'user':user})

def inquiry(request):
    user=request.session.get('user')
    # userid=request.session.get('userid')
    # id=SignupMaster.objects.get(id=userid)

    if request.method=="POST":
        inquiryfrm=InquiryForm(request.POST)
        if inquiryfrm.is_valid():
            #inquiryfrm=InquiryForm(request.POST,instance=id)
            inquiryfrm.save()
            print("Inquiry submitted successfully!")

            sub="Inquiry Submitted "
            msg="Hello user,\nYour inquiry has been submitted successfully with Shilpan builders! \n Our team will contact you shortly! \nEnjoy our services.\nThanks & regards! \nShilpan Builders \n Rajkot\n+91 96246 44441 \ninfo@shilpan.in "
            from_id=settings.EMAIL_HOST_USER
            #to_id=['Nitinjethava143@yahoo.com']
            to_id=[request.POST['email']]

            send_mail(sub,msg,from_id,to_id)
            print("Email send successfully!")

            return redirect('/inquiry')
        else:
            print(inquiryfrm.errors)
    else:
        inquiryfrm=InquiryForm()
    # return render(request,'inquiry.html',{'user':user,'userid':SignupMaster.objects.get(id=userid)})
    return render(request,'inquiry.html',{'user':user})

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

def updateprofile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    id=SignupMaster.objects.get(id=userid)

    if request.method=="POST":
        signupfrm=SignupForm(request.POST)
        if signupfrm.is_valid():
            signupfrm=SignupForm(request.POST,instance=id)
            signupfrm.save()
            print("Your profile data has been Updated!")
            return redirect('/home')
        else:
            print(signupfrm.errors)
            signupfrm=SignupForm()
    else:
        print("Error...Something went wrong!")

    return render(request,'updateprofile.html',{'user':user,'userid':SignupMaster.objects.get(id=userid)})

def forgotpassword(request):
    if request.method=="POST":
        email=request.POST['email']
        try:
            user=SignupMaster.objects.get(email=email)
            otp=random.randint(1111,9999)
            sub="OTP for forgot Password "
            msg="Hello user,\nYour OTP for forgot password is "+str(otp)
            from_id=settings.EMAIL_HOST_USER
            #to_id=['Nitinjethava143@yahoo.com']
            to_id=[user.email,]

            send_mail(sub,msg,from_id,to_id)
            return render(request,'otp.html',{'otp':otp,'email':email})
        except:
            msg="Email is not registered"
            return render(request,'forgotpassword.html',{'msg':msg})
    else:
        return render(request,'forgotpassword.html')

def otp(request):
    otp=request.POST['otp']
    uotp=request.POST['uotp']
    email=request.POST['email']

    if otp==uotp:
        return render(request,'newpassword.html',{'email':email})
    else:
        msg="otp is invalid"
        return render(request,'otp.html',{'otp':otp,'email':email,'msg':msg})
    
def newpassword(request):
    email=request.POST['email']
    password=request.POST['password']
    cpassword=request.POST['cpassword']

    if password==cpassword:
        user=SignupMaster.objects.get(email=email)
        user.password=password
        user.cpassword=password
        user.save()
        #msg="Password updated successfully"
        return render(request,'index.html') 
    else:
        msg="Password and conform does not match"
        return render(request,'newpassword.html',{'msg':msg,'email':email})
    
def changepassword(request):
    if request.method=="POST":
        user=SignupMaster.objects.get(email=request.session['email'])
        if user.password==request.POST['oldpassword']:
            if request.POST['newpassword']==request.POST['cnewpassword']:
                user.password=request.POST['newpassword']
                user.cpassword=request.POST['cnewpassword']
                user.save()
                return redirect('/userlogout')
            else:
                msg="New password and Confirm new password does not match"
                return render(request,'changepassword.html',{'msg':msg})
        else:
            msg="old password incorrect"
            return render(request,'changepassword.html',{'msg':msg})
    else:
        return render(request,'changepassword.html')