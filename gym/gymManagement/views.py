from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

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