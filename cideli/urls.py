"""
URL configuration for cideli project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



#login state (using cookie, check if session is existent)
#Cart: save as a state (state is saved as a session and session is saved as a cookie) 
    #cookie disappears when the browser is closed (goes away when you re-login) --> saved to browser
    #session saves the information connected to the login


#Home: default (if (login == false) --> register/login, if(login == true) --> menu/order)
#Register: /register
#Login: /login 
#Profile: /myprofile


#Menu: /menu
    #Item i(as dialog): /menu
#Order: /order (includes order summary, barcode)


#database 1: Our Home (Customer, Menu, Product, Payment....)
#database 2: Chadwick Users Database (Login Info, CupID, Contact Info, Student ID)

#get database 2 information --> database 1: customer
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("login", admin.site.urls),
    path("menu/", include("menu.urls"))
]
