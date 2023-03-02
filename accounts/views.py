from django.shortcuts import render,redirect,HttpResponse
from .models import Address
from .models import Signup
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    address  = Address.objects.all()
    context = {
        'address':address
    }
    return render(request,'accounts/register.html',context)



def addAddress(request):
    if request.method == "POST":
        name = request.POST.get('name')
        city = request.POST.get('city')
        age=request.POST.get('age')

        x = Address.objects.create(
            name=name,
            city=city,
            age=age
        )
        x.save()
        return redirect('/user/register')
    else:
        return HttpResponse("UNAVAILABLE")
    





def removeAddress(request,id):
      Address.objects.get(id=id).delete()
      address  = Address.objects.all()
      context = {
        'address':address
    }
      return redirect('/user/showDetails')
    #   return render(request,'accounts/register.html',context)


def showDetails(request):
    address=Address.objects.all()
    context={
        'address':address
    }
    return render(request,'accounts/userDetail.html',context)


def login_signup(request):
    context={

    }
    return render(request,'accounts/login.html',context)

# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword') 
# user.last_name = 'Lennon'
# user.save()


def addUser(request):
    if request.method=='POST':
        name=request.POST.get('txt')
        email=request.POST.get('email')
        password=request.POST.get('pswd')
        
        y=Signup.objects.create(
            name=name,
            email=email,
            password=password
        )
        y.save()
        return render(request,'accounts/login.html')
    




    

       


    

