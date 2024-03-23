from django.urls import path
from job.views import*
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name="index"),
    path('admin_login',admin_login,name='admin_login'),
    path('user_login',user_login,name='user_login'),
    path('recruiter_login',recruiter_login,name='recruiter_login'),
     path('user_signup',user_signup,name='user_signup'),
    path('user_home',user_home,name='user_home'),
    path('Logout',Logout,name='Logout'),
    path('recruiter_signup',recruiter_signup,name='recruiter_signup'),
    path('recruiter_home',recruiter_home,name='recruiter_home'),
    path('admin_home',admin_home,name='admin_home'),
    path('view_users',view_users,name='view_users'),
    path('delete_user/<int:pid>',delete_user,name='delete_user'),
    path('view_recruiters',view_recruiters,name='view_recruiters'),
    path('delete_recruiter/<int:pid>',delete_recruiter,name='delete_recruiter'),
    path('change_passworduser',change_passworduser,name='change_passworduser'),
    path('change_passwordrecruiter',change_passwordrecruiter,name='change_passwordrecruiter'),
    path('job',job,name='job'),
    path('job_list',job_list,name='job_list'),
    path('edit_job/<int:pid>',edit_job,name='edit_job'),
    path('delete_job/<int:pid>',delete_job,name='delete_job'),
    path('latest_jobs',latest_jobs,name='latest_jobs'),
    path('user_joblist',user_joblist,name='user_joblist'),
    path('job_detail/<int:pid>', job_detail,name='job_detail'),
    path('applyforjob/<int:pid>/', applyforjob, name='applyforjob'),
    path('appliedlist', appliedlist, name='appliedlist'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)