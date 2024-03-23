from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
from .models import Jobs
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_login(request):
    error=''
    if request.method=="POST":
        una = request.POST['uname']
        pas = request.POST['pass']
        user =authenticate(username=una,password=pas)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}

    return render(request, 'admin.html',d)

def user_login(request):
    error=" "
    if request.method == 'POST':
      un = request.POST['uname']
      p= request.POST['pass']
      user =authenticate(username=un,password=p)
      if user:
          try:
                users =Commonuser.objects.get(user=user)
                if users.type == "jobseeker":
                    login(request,user)
                    error='no'
                else: 
                    error='yes'
          except:
              error="yes"
      else:
          error="yes"
    d={'error':error}
    return render(request, 'userlogin.html',d)

def recruiter_login(request):
    error=" "
    if request.method == 'POST':
      un = request.POST['uname']
      p= request.POST['pass']
      user =authenticate(username=un,password=p)
      if user:
          try:
                users =Recruiter.objects.get(user=user)
                if users.type == "recruiter":
                    login(request,user)
                    error='no'
                else: 
                    error='yes'
          except:
              error="yes"
      else:
          error="yes"
    d={'error':error}
    return render(request,'recruiterlogin.html',d)

def recruiter_signup(request):
    error=" "
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        img=request.FILES['img']
        pas=request.POST['pass']
        em=request.POST['email']
        ph= request.POST['contact']
        gen=request.POST['gender']
        com=request.POST['cname']
        try:
            user=User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pas)
            h=Recruiter.objects.create(user=user,mobile=ph,image=img,gender=gen,company=com,type="recruiter")
            h.save()
            error="no"

        except:
            error="yes"
    d = {'error':error}

    return render(request,'recruitersignup.html',d)

def user_home(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return redirect('user_login')
    
    # Retrieve the Commonuser object associated with the logged-in user
    try:
        common = Commonuser.objects.get(user=request.user)
    except Commonuser.DoesNotExist:
        # Handle the case where no Commonuser object is found for the user
        # You might want to handle this differently based on your application's requirements
        return redirect('user_login')  # or redirect to a different page or show an error message

    error = ""  # Initialize the error message

    if request.method == "POST":
        # Process the form data if the request method is POST
        fn = request.POST.get('fname', '')
        ln = request.POST.get('lname', '')
        ph = request.POST.get('contact', '')
        gen = request.POST.get('gender', '')

        # Update the common and user objects with the new data
        common.user.first_name = fn
        common.user.last_name = ln
        common.mobile = ph
        common.gender = gen

        try:
            # Save the changes to the database
            common.user.save()
            common.save()
            error = "no"  # Set error message to indicate success
        except Exception as e:
            # Handle exceptions
            print(e)  # Print the exception for debugging
            error = "yes"  # Set error message to indicate failure

    # Construct the context dictionary
    context = {'common': common, 'error': error}

    # Render the template with the context
    return render(request, 'userhome.html', context)

def recruiter_home(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    
    # Retrieve the recruiter object associated with the logged-in user
    try:
        recruiter = Recruiter.objects.get(user=request.user)
    except Recruiter.DoesNotExist:
        # Handle the case where no Recruiter object is found for the user
        # You might want to handle this differently based on your application's requirements
        return redirect('recruiter_login')  # or redirect to a different page or show an error message

    error = ""  # Initialize the error message

    if request.method == "POST":
        # Process the form data if the request method is POST
        fn = request.POST.get('fname', '')
        ln = request.POST.get('lname', '')
        ph = request.POST.get('contact', '')
        gen = request.POST.get('gender', '')

        # Update the recruiter and user objects with the new data
        recruiter.user.first_name = fn
        recruiter.user.last_name = ln
        recruiter.mobile = ph
        recruiter.gender = gen

        try:
            # Save the changes to the database
            recruiter.user.save()
            recruiter.save()
            error = "no"  # Set error message to indicate success
        except Exception as e:
            # Handle exceptions
            print(e)  # Print the exception for debugging
            error = "yes"  # Set error message to indicate failure

    # Construct the context dictionary
    context = {'recruiter': recruiter, 'error': error}

    # Render the template with the context
    return render(request, 'recruiterhome.html', context)

def admin_home(request):
    if not  request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'adminhome.html')

def Logout(request):
    logout(request)
    return redirect('index')



def user_signup(request):
    error=" "
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        re=request.FILES['resume']
        pas=request.POST['pass']
        em=request.POST['email']
        ph= request.POST['contact']
        gen=request.POST['gender']
        try:
            user=User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pas)
            h=Commonuser.objects.create(user=user,mobile=ph,resume=re,gender=gen,type="jobseeker")
            h.save()
            error="no"

        except:
            error="yes"
    d = {'error':error}
    
    return render(request, 'usersignup.html',d)

def view_users(request):
    if not  request.user.is_authenticated:
        return redirect('admin_login')
    data = Commonuser.objects.all()
    d = {'data': data}
    return render(request,'viewusers.html',d)

def delete_user(request,pid):
    if not  request.user.is_authenticated:
        return redirect('admin_login')
    user = Commonuser.objects.get(id=pid)
    user.delete()
    return redirect('view_users')

def view_recruiters(request):
    if not  request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.all()
    d = {'data': data}
    return render(request,'viewrecruiter.html',d)

def delete_recruiter(request,pid):
    if not  request.user.is_authenticated:
        return redirect('admin_login')
    user = Recruiter.objects.get(id=pid)
    user.delete()
    return redirect('view_recruiters')

def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    if request.method=="POST":
        o= request.POST['currentpassword']
        n=request.POST['newpass']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(o):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="no"
        except:
            error="yes"

    d = {'error':error}
    return render(request,'changepassworduser.html',d)

def change_passwordrecruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    if request.method=="POST":
        o= request.POST['currentpassword']
        n=request.POST['newpass']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(o):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="no"
        except:
            error="yes"

    d = {'error':error}
    return render(request,'changepasswordrecruiter.html',d)


def job(request):#add job
    if not  request.user.is_authenticated:
        return redirect('recruiter_login')
    error=" "
    if request.method=="POST":
        jn=request.POST['jname']
        sd=request.POST['sdate']
        re=request.POST['edate']
        sal=request.POST['salary']
        em=request.POST['exp']
        lo= request.POST['location']
        sk=request.POST['skills']
        des=request.POST['description']
        user = request.user
        recruiter=Recruiter.objects.get(user=user)
        try:
           j= Jobs.objects.create(recruiter=recruiter,start_date=sd,end_date=re,title=jn,salary=sal,exp=em,location=lo,skills=sk,description=des,creationdate=date.today())
           j.save()
           error="no"

        except:
            error="yes"
    d = {'error':error}
    
    return render(request,'addjob.html',d)

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    
    user = request.user
    try:
        recruiter = Recruiter.objects.get(user=user)
        job_list = Jobs.objects.filter(recruiter=recruiter)
    except Recruiter.DoesNotExist:
        job_list = []

    context = {'job_list': job_list}
    return render(request, 'job_list.html', context)



from django.shortcuts import render, redirect
from .models import Jobs
from datetime import datetime

def edit_job(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    
    error = ""
    job2 = Jobs.objects.get(id=pid)

    if request.method == "POST":
        jn = request.POST.get('jname')
        sd = request.POST.get('sdate')
        re = request.POST.get('edate')
        sal = request.POST.get('salary')
        em = request.POST.get('exp')
        lo = request.POST.get('location')
        sk = request.POST.get('skills')
        des = request.POST.get('description')
        
        job2.title = jn
        job2.salary = sal
        job2.exp = em
        job2.location = lo
        job2.skills = sk
        job2.description = des

        try:
            if sd:
                job2.start_date = datetime.strptime(sd, "%Y-%m-%d")
            if re:
                job2.end_date = datetime.strptime(re, "%Y-%m-%d")
            job2.save()
            error = "no"
        except Exception as e:
            error = str(e)

    context = {'error': error, 'job2': job2}
    return render(request, 'editjob.html', context)


def latest_jobs(request):

    data = Jobs.objects.all().order_by('start_date')
    d = {'data': data}
    return render(request,'latestjob.html',d)

def user_joblist(request):

    data = Jobs.objects.all().order_by('start_date')
    user = request.user
    commonuser = Commonuser.objects.get(user=user)
    data1=Apply.objects.filter(commonuser=commonuser)
    li=[]
    for i in data1:
        li.append(i.job.id)

    d = {'data': data,'li':li}
    return render(request,'userjoblist.html',d)

def job_detail(request,pid):

    data = Jobs.objects.get(id=pid)
    d = {'data': data}
    return render(request,'job_detail.html',d)

def applyforjob(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    user=request.user
    commonuser = Commonuser.objects.get(user=user)
    job = Jobs.objects.get(id=pid)
    date1=date.today()
    if job.end_date< date1:
        error="close"
    elif job.start_date > date1:
        error="notopen"
    else:
        if request.method == 'POST':
            r=request.FILES['resume']
            Apply.objects.create(job=job,commonuser=commonuser ,resume=r,applydate=date.today())
            error="done"
    d= {'error':error}
    return render(request,'applyforjob.html',d)

def appliedlist(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    data = Apply.objects.all()
    d={'data':data}
    return render(request,'appliedlist.html',d)



def delete_job(request,pid):
    if not  request.user.is_authenticated:
        return redirect('recruiter_login')
    job = Jobs.objects.get(id=pid)
    job.delete()
    return redirect('job_list')