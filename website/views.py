from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import AddComplaintForm
from .models import complaintstructure,NewsPost

# Create your views here.

path = 'http://localhost:8000/static'


def viewcomplaints(request):
    obj =complaintstructure.objects.all()
    return  render(request,"viewallcomplaints.html",{'obj':obj})


def checkLogin(request):
    request.session["loginyes"] = 1
    return redirect('http://localhost:8000/addComplaint') 


def addComplaint(request):


    if request.session["loginyes"] != 0 :
        obj =AddComplaintForm()
        return   render(request,"apythonddComplaint.html",{'form':obj})
    else:
        return   render(request,"login.html",None)


def savecomplaint(request):

            newdoc = complaintstructure( csubmiterphone=request.POST.get("csubmiterphone"),cagainstname=request.POST.get("cagainstname"),cdes=request.POST.get("cdes"),ctitle=request.POST.get("ctitle"),cpname=request.POST.get("cpname"),cimage1=request.FILES['cimage1'],cimage2=request.FILES['cimage2'],cimage3=request.FILES['cimage3'])
            newdoc.save()

            # Redirect to the document list after POST
            return render(request,"successpage.html",None)



def loginpage(request):
    return   render(request,"login.html",None)


def index(request):
  return  render(request,"index.html",None)
 


def  signup(request):
    return   render(request,"signup.html",None)


def  helplinenumbers(request):

    return   render(request,"helpline.html",None)


def  seemycomplaintstatus(request):
    return   render(request,"seemycomplaintstatus.html",None)

def  seeAreawiseSafety(request):
    return render(request, "seeAreaSafety.html", None)



def newsandnotifications(request):
    obj =NewsPost.objects.all()
    return render(request, "newsandnotifications.html", {'obj':obj})

def  mainpage(request):
    request.session["loginyes"] = 0
    return  render(request,"mainpage.html",{'path':path})

def AboutUs(request):
   return render(request,"AboutUs.html",None)

def lawsandacts(request):
  return render(request,"lawsandacts.html",None)

