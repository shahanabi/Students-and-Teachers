from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.utils.timezone import now 

from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def studentregistration(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        pname=request.POST.get('pname')
        address=request.POST.get('address')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        dob=request.POST.get('dob')
        password=request.POST.get('password')

        registration=Student(firstname=firstname,lastname=lastname,email=email,pname=pname,address=address,image=image,dob=dob,password=password)
        registration.save()
    return render(request,'studentregistration.html')


def teacherregistration(request):
    if request.method=='POST':
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')

        registration=teacher(name=name,subject=subject,email=email,phonenumber=phonenumber,image=image,password=password)
        registration.save()
    return render(request,'teacherregistration.html')



def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if Student.objects.filter(email=email,password=password).exists():
        Studentdetails=Student.objects.get(email=request.POST['email'],password=password)
        if Studentdetails.password==request.POST['password']:
            request.session['sid'] = Studentdetails.id

            request.session['sname'] = Studentdetails.firstname

            request.session['email'] = email

            request.session['suser'] = 'suser'

            return render(request,'index.html')
        
    elif teacher.objects.filter(email=email,password=password).exists():
        teacherdetails=teacher.objects.get(email=request.POST['email'],password=password)
        if teacherdetails.password==request.POST['password']:
            request.session['tid'] = teacherdetails.id

            request.session['tname'] = teacherdetails.name

            request.session['email'] = email

            request.session['tuser'] = 'tuser'

            return render(request,'index.html')
        

    else:
        return render(request, 'login.html', {'status':'invalid email or password'})
    
def logout(request):
    session_key = list(request.session.keys())
    for key in session_key:
        del request.session[key]
    return redirect(index)



def studentstable(request):
    dict_pc={
        'pc' : Student.objects.all()
    }
    return render(request,'studentstable.html',dict_pc)


def teachertable(request):
    dict_pc={
        'pc' : teacher.objects.all()
    }
    return render(request,'teachertable.html',dict_pc)

def work(request,id):
    tem = request.session['tid']
    tc = teacher.objects.get(id=tem)
    st = Student.objects.get(id=id)
    return render(request,'work.html',{'res':st, 'result':tc})

def givehomework(request,id): 
    tem = request.session['tid']
    if request.method == "POST":
        teachername_instance = teacher.objects.get(id=tem)
        studentname_instance = Student.objects.get(id=id)
        description = request.POST.get('description')
        submissiondate = request.POST.get('submissiondate')

        HM=Homework(teachername=teachername_instance,studentname=studentname_instance,description=description,submissiondate=submissiondate)
        HM.save()
        return redirect('work', id=id)
    
    # Handle GET requests (optional)
    return render(request, 'work.html')

def profile(request):
    tem = request.session['sid']
    st = Student.objects.get(id=tem)

    return render(request, 'profile.html', {'result': st})

def teacherprofile(request):
    tem = request.session['tid']
    te = teacher.objects.get(id=tem)

    return render(request, 'teacherprofile.html', {'result': te})

def studentprofileedit(request,id):
    st = Student.objects.get(id=id)

    return render(request, 'studentprofileedit.html',{'result': st})

def teacherprofileedit(request,id):
    te = teacher.objects.get(id=id)
    return render(request, 'teacherprofileedit.html', {'result': te})

def teacheredit(request,id):
    if request.method=='POST':
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')

        registration=teacher(name=name,subject=subject,email=email,phonenumber=phonenumber,image=image,password=password,id=id)
        registration.save()
    return redirect(teacherprofile)


def studentedit(request,id):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        pname=request.POST.get('pname')
        address=request.POST.get('address')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        dob=request.POST.get('dob')
        password=request.POST.get('password')

        registration=Student(firstname=firstname,lastname=lastname,email=email,pname=pname,address=address,image=image,dob=dob,password=password,id=id)
        registration.save()

    return redirect(profile)

def homeworkview(request):
    tem = request.session['sid']
    st = Homework.objects.filter(studentname=tem)

    return render(request, 'homeworkview.html', {'result': st})

def answer(request,id):
    tem = request.session['sid']
    st = Student.objects.get(id=tem)
    hw = Homework.objects.get(id=id)
    return render(request,'answer.html',{'result':st, 'res':hw})

def giveanswer(request,id): 
    tem = request.session['sid']
    if request.method == "POST":
        studentname_instance = Student.objects.get(id=tem)
        homework_inst = Homework.objects.get(id=id)
        answer_text = request.POST.get('answer_text')
        submitted_date = now().date()

        A=Answers(studentname=studentname_instance,answer_text=answer_text,submitted_date= submitted_date,homework=homework_inst)
        A.save()
        return redirect('answer', id=id)
    
    # Handle GET requests (optional)
    return render(request, 'answer.html')

def answerview(request,id):
    tem = request.session['tid']
    an = Answers.objects.filter(id=id)

    return render(request, 'answerview.html', {'res': an})

