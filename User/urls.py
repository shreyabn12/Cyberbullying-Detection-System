from django.urls import path
from .import views 

urlpatterns=[ 
    path('',views.index,name='homepage'),
    path('register',views.register,name='reg'),
    path('login',views.login,name="login"),
    path('data',views.data,name='data'),
    path('cyberbullying',views.cyberbullying,name='cyber'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about')
]