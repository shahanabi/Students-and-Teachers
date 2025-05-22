
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('studentstable/', views.studentstable, name='studentstable'),
    
    path('studentregistration/', views.studentregistration, name='studentregistration'),

    path('teacherregistration/', views.teacherregistration, name='teacherregistration'),

    path('login/', views.login, name='login'),

    path('logout/', views.logout, name='logout'),

    path('teachertable/', views.teachertable, name='teachertable'),

    path('work/<int:id>', views.work, name='work'),
    
    path('work/givehomework/<int:id>', views.givehomework, name='givehomework'),

    path('profile/', views.profile, name='profile'),

    path('teacherprofile/', views.teacherprofile, name='teacherprofile'),
    
    path('studentprofileedit/<int:id>', views.studentprofileedit, name='studentprofileedit'),

    path('teacherprofileedit/<int:id>', views.teacherprofileedit, name='teacherprofileedit'),

    path('teacherprofileedit/teacheredit/<int:id>', views.teacheredit, name='teacheredit'),

    path('studentprofileedit/studentedit/<int:id>', views.studentedit, name='studentedit'),

    path('homeworkview', views.homeworkview, name='homeworkview'),

    path('answer/<int:id>', views.answer, name='answer'),

    path('answer/giveanswer/<int:id>', views.giveanswer, name='giveanswer'),

    path('answerview/<int:id>', views.answerview, name='answerview'),


]


