from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime
#from home.models import Scholarform

# Create your views here.
def index(request):
    context = {
        
        "variable":"Rohit is Great"
    }
    return render(request,'index.html',context)
    #return HttpResponse("this is the homepage")

def about(request):
    return render(request,'about.html')

def Education(request):
    #return HttpResponse("This is the services page")
    return render(request,'Education.html')

def contact(request):
    return render(request,'contact.html')

def form(request):
    #return HttpResponse("This is the contact page")
    return render(request,'form.html')

def Mission(request):
    #return HttpResponse("This is the contact page")
    return render(request,'Mission.html')

def aboutscho(request):
    #return HttpResponse("This is the contact page")
    return render(request,'aboutscho.html')

def child(request):
    #return HttpResponse("This is the contact page")
    return render(request,'child.html')

def goal(request):
    #return HttpResponse("This is the contact page")
    return render(request,'goal.html')

    raise Http404

def health(request):
    #return HttpResponse("This is the contact page")
    return render(request,'health.html')

#def scholarform(request):
    #if request.method == "POST":
            #fname = request.POST.get('fname')
            #MName = request.POST.get('MName')
            #name = request.POST.get('lname')
            #Gender = request.POST.get('Gender')
            #dob = request.POST.get('dob')
            #Category = request.POST.get('Category')
            #Aadhar = request.POST.get('Aadhar')
            #Mobile = request.POST.get('Mobile')
            #email = request.POST.get('email')
            #father = request.POST.get('father')
            #ffather = request.POST.get('ffather')
            #fffather = request.POST.get('fffather')
            #mother = request.POST.get('mother')
            #mmother = request.POST.get('mmother')
            #mmmother = request.POST.get('mmmother')
            #Pincode = request.POST.get('Pincode')
            #Village = request.POST.get('Village')
            #Distric = request.POST.get('Distric')
            #State = request.POST.get('State')
            #Address = request.POST.get('Address')
            #Board = request.POST.get('Board')
            #School= request.POST.get('School')
            #cls = request.POST.get('cls')
            #astPercentage = request.POST.get('lastPercentage')
            #scholarform = Scholarform(fname=fname, MName=MName, lname=lname, Gender=Gender,dob=dob,Category=Category,Aadhar=Aadhar,Mobile=Mobile,email=email,father=father,ffather=ffather,fffather=fffather,mother=mother,mmother=mmother,mmmother=mmmother,Pincode=Pincode,Village=Village,Distric=Distric,State=State,Address=Address,Board=Board,School=School,cls=cls,lastPercentage=lastPercentage,date=datetime.today())
            #scholarform.save()
    #return HttpResponse("This is the contact page")
    #return render(request,'scholarform.html')

def team(request):
    #return HttpResponse("This is the contact page")
    return render(request,'team.html')

def vision(request):
    #return HttpResponse("This is the contact page")
    return render(request,'vision.html')

def Womens(request):
    #return HttpResponse("This is the contact page")
    return render(request,'Womens.html')

def nav(request):
    #return HttpResponse("This is the contact page")
    return render(request,'nav.html')

def uploadfile(request):
    return render(request,'uploadfile.html')

def more(request):
    return render(request,'more.html')

def schobase(request):
    return render(request,'schobase.html')

def eligibi(request):
    return render(request,'eligibi.html')

def syllbus(request):
    return render(request,'syllbus.html')

def goal(request):
    return render(request,'goal.html')

def hindi(request):
    return render(request,'hindi.html')


def hindig(request):
    return render(request,'hindig.html')

def formhindi(request):
    return render(request,'formhindi.html')

def Exam(request):
    return render(request,'Exam.html')
