import datetime
from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    newGymMembers=models.GymMember.objects.filter(joinedAt=datetime.date.today())
    gymMembers=models.GymMember.objects.filter(joinedAt__year=datetime.date.today().year)
    thisMonthGymMembers=models.GymMember.objects.filter(joinedAt__month=datetime.date.today().month)
    print(thisMonthGymMembers)
    thisMonthRevenue=0
    for thisMonthGymMember in thisMonthGymMembers:
        if thisMonthGymMember.plan.price:
            thisMonthRevenue+=thisMonthGymMember.plan.price

    
   
    context={
        'newGymMembers':newGymMembers.__len__(),
        'gymMembers':gymMembers.__len__(),
        'thisMonthGymMembers':thisMonthGymMembers,
        'thisMonthRevenue':thisMonthRevenue

    }

    {

    }

    return render(request,'index.html',context)

def manageMembers(request):
    return render(request,'manageMembers.html')
def addNewMembers(request):
    return render(request,'registration.html')
def getIn(request):
    return render(request,'get_in.html')
def plan(request):
    return render(request,'plan.html')
def payment(request):
    return render(request,'payment.html')
def attendance(request):
    return render(request,'attendance.html')
def generateIdCard(request):
    return render(request,'generate_ID.html')
def reports(request):
    return render(request,'report.html')