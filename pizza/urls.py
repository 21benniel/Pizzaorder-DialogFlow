from . import views
from django.urls import path

urlpatterns=[
    path('',views.order,name='order'),
    path('bill',views.bill,name='bill'),
    path('about/',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('login',views.login ,name='login'),
    path('signup',views.signup ,name='signup'),
    path('logout',views.logout,name='logout')
    
]