from django.shortcuts import render,redirect
from django.http import HttpResponse



from .models import *

from django.contrib.auth.models import User

from django.contrib.auth  import authenticate,  login, logout

from django.contrib import messages 


# Create your views here.

def home(request):
    return render(request,'home.html')




def student_save(request):
    student_items = student(student_name = request.POST['st_name'],
                            student_contact = request.POST['st_cont']
    )
    student_items.save()
    return redirect('home')


def process_patient_entry(request):
    if request.method == 'POST':
        patient_name = request.POST.get('pname')
        patient_email = request.POST.get('email')
        patient_phone = request.POST.get('phone')
        patient_message = request.POST.get('message')
        booked_date = request.POST.get('date')
        
        
        # Create a new patient entry in the database using the Patient model
        Patients = record(patient_name=patient_name, patient_email=patient_email, patient_phone = patient_phone , patient_message = patient_message,  booked_date=booked_date)
        Patients.save()



        return HttpResponse("Data successfully inserted!")
    else:
        return HttpResponse("Invalid request method.")


def index(request):
    return render(request,'index.html')


def booking(request):
    return render(request,'booking.html')


def registation(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_phone = request.POST.get('phone')
        
        reg_user = reguser(user_name = user_name, user_email= user_email, user_phone= user_phone)
        reg_user.save()
        return render(request,'index.html')



def modal(request):
    return render(request,'modal.html')


def handlesignup(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        username = request.POST['username']
        phone = request.POST['phone']
        uemail = request.POST['uemail']
        upass1 = request.POST['upass1']
        upass2 = request.POST['upass2']


        #check for errorneous input

        if len(username)<8:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('index')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('index')
        if (upass1!= upass2):
             messages.error(request, " Passwords does not match")
             return redirect('index')
        

        myuser = User.objects.create_user(username, uemail, upass1)
        myuser.first_name= fullname
        
        myuser.save()
        messages.success(request, " Your has been successfully created")
        return redirect('index')

    else:
        return HttpResponse("404 - Not Found")



def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("index")

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('index')


def appointment(request):
    if request.method == "POST":
        patient_name = request.POST['patient_name']
        patient_email = request.POST['patient_email']
        patient_phone = request.POST['patient_phone']
        patient_message = request.POST['patient_message']

        appoint_user = appointment(patient_name = patient_name, patient_email= patient_email, patient_phone= patient_phone, patient_message = patient_message)
        appoint_user.save()

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            myuser = User.objects.create_user(username, patient_email,)
            myuser.first_name= patient_name
        
            myuser.save()
            messages.success(request, " Your has been successfully created")


        return render(request,'index.html')
