
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.db import connection
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Post
from .models import employee, client
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def posts(request, pk):
    #posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts':posts})

def contact(request):
    contact = {'user': request.user}
    return render(request, 'contact.html', contact)

def posts(request):
    posts={'user' : request.user}
    return render(request, 'posts.html')

def about(request):
    about = {'user': request.user}
    return render(request, 'about.html', about)

def insertrec(request):
    if request.method=="POST":
        if request.POST.get('empname') and request.POST.get('empjoindate'):
            saveobj = employee()
            saveobj.empname=request.POST.get('empname')
            saveobj.empjoindate=request.POST.get('empjoindate')
            cursor=connection.cursor()
            cursor.execute("insert into empjoin (empname, empjoindate) values(' "+saveobj.empname+ "', '" + saveobj.empjoindate+ "')")
            messages.success(request, "Employee name  "+saveobj.empname+ " Is save scucessfully")
            return render(request, 'insertrec.html')
    else:
        return render(request, 'insertrec.html')
'''
def calendar(request):
    if request.method=="POST":
        if request.POST.get('first_name') and request.POST.get('appointment_date'):
            saveobj = client()
            saveobj.first_name=request.POST.get('first_name')
            saveobj.appointment_date=request.POST.get('appointment_date')
            cursor=connection.cursor()
            cursor.execute("insert into client(first_name, appointment_date) values(' "+saveobj.first_name+ "', '" + saveobj.appointment_date+ "')")
            messages.success(request, "Client name  "+saveobj.first_name+ " has successfully scheduled appointment on "+ saveobj.appointment_date)
            return render(request, 'calendar.html')
    else:
        return render(request, 'calendar.html')
'''
def calendar(request):
    if request.method=="POST":
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email') and request.POST.get('service') and request.POST.get('appointment_date'):
            saveobj = client()
            saveobj.first_name=request.POST.get('first_name')
            saveobj.last_name=request.POST.get('last_name')
            saveobj.email=request.POST.get('email')
            saveobj.service=request.POST.get('service')
            saveobj.telephone=request.POST.get('telephone')
            saveobj.appointment_date=request.POST.get('appointment_date')
            #subjectforclient="Appointment with MadeleineSalonDeCoiffure on  '" + saveobj.appointment_date+ "'  for  '" + saveobj.service+ "'"
            #subjectforhairdresser="Client Appointment with ' "+saveobj.first_name+ "' ' "+saveobj.last_name+ "' on  '" + saveobj.appointment_date+ "'  for  '" + saveobj.service+ "'"
            #messageforclient="Thank you for scheduling an appointment with Madeleine for this date  '" + saveobj.appointment_date+ "' "
            #messageforhairdresser="You are scheduled with' "+saveobj.first_name+ "' ' "+saveobj.last_name+ "'  for  '" + saveobj.appointment_date+ "' please make sure to follow up with your client at either' "+saveobj.email+ "' or  ' "+saveobj.telephone+ "',"
            cursor=connection.cursor()
            cursor.execute("INSERT INTO client(first_name, last_name, email, service, telephone, appointment_date) values(' "+saveobj.first_name+ "', ' "+saveobj.last_name+ "',  ' "+saveobj.email+ "', '" + saveobj.service+ "'" +", '"+saveobj.telephone+"', '"+saveobj.appointment_date+"')")
            messages.success(request, "Thank you! "+saveobj.first_name+ " "+saveobj.last_name+ " has successfully scheduled appointment on "+ saveobj.appointment_date+" for "+ saveobj.service+" ")
            #try:
                #send_mail(subjectforclient, messageforclient, saveobj.email, [saveobj.email])
                #send_mail(subjectforhairdresser, messageforhairdresser, saveobj.email, ['madeleinesalondecoiffure@gmail.com'])
            #except BadHeaderError:
                #return HttpResponse('Invalid header found.')
            return render(request, 'calendar.html')
    else:
        return render(request, 'calendar.html')
#define a schedule function that gets data from the database from the client modal
#and sends it to a javascript script in calendar.html
#get data jsonresponse
#send the data to the javascript
#return the data to the calendar.html



def getdata(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM client")
    data = cursor.fetchall()
    return JsonResponse(data, safe=False)




def home(request, year, month):
    firstname = 'John'
    month = month.capitalize()

    #Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)

    #Get current year 
    now = datetime.now()
    current_year = now.year()

    #Get current time
    current_time = now.time()





    return render(request, 
        'home.html', {
        'first_name':firstname,
        'year':year,
        'month':month,
        'month_number':month_number,
        'cal':cal,
        'current_year':current_year,
        #'time':time,
        'current_time':current_time,
    })






