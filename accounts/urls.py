
from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('addAddress',views.addAddress,name='addAddress'),
    path('removeAddress/<int:id>',views.removeAddress,name='removeAddress'),
    path('showDetails',views.showDetails,name='showDetails'),
    path('login_signup',views.login_signup,name='login_signup'),
    path('addUser',views.addUser,name='addUser')
]
