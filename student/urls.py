from django.contrib import admin
from django.urls import path
from student import views   

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("courses",views.courses,name='courses'),
    path("admission",views.admission,name='admission'),
    path("contact",views.contact,name='contact'),
    path("login1",views.login1,name='login1'),
    path("addstudents",views.addstudents,name='addstudents'),
    path("editstudents",views.editstudents,name='editstudents'),
    path("viewstudents",views.viewstudents,name='viewstudents'),
    path("logout1",views.logout1,name='logout1'),
    path('editstudents/<int:student_id>',views.deletestudents),
    path('editstudents/<int:student_id>',views.updatestudents),
]
