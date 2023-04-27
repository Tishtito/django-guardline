from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello,name='hello'),
    path('hi/', views.hi),
    path('sup/', views.sup),
    path('getsession/', views.getsession),
    path('evenodd', views.evenodd),
    path('error/', views.error),
    path('index/', views.index,name='index'),
    path('variables/', views.variables,name='variables'),
    path('employee/', views.employee,name='employee'),
    path('image/', views.image),
    path('session', views.setsession,name='session'),
    path('members/', views.members,name='Members'),
    path('form/', views.student,name='studentform'),
    path('employee2/', views.employee2,name='emp'),
    path('form/', views.form),
    path('', views.form2),
]
