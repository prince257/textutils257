"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from . import views

# dekh...ab jo bhi urlpatterns m path h...aur usme jo h...vo cheeze baari baari hmmari website m dikh jaayegi
# urlpatterns = [
#     path('admin/', admin.site.urls),
    # path('',views.index1,name='index1'),# view hmaara ek programm file h..jisme index1 ek func h
    #path ka pahla attribute h..blank string=''...mtlb aapke url ke baad kya append krna chaiye
    #path ka doosa attribute h...vo function run karega..jab aapka koi uspe jaaye
    #3rd attribute path ka...path ka naam h
    # path('',views.notes,name='notes'),
#     path('',views.sitesname,name='sitesname'),
#
#     path('about/',views.about,name='about')
# ]

# tutes-7 se

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
path('admin/',admin.site.urls),
path('', views.index , name='index'),
# path('removepunc', views.removepunc , name='rempun'),
# path('capitalizefirst', views.capfirst , name='capfirst'),
# path('newlineremove', views.newlineremove , name='newlineremove'),
# path('spaceremove', views.spaceremove , name='spaceremove'),
# path('charcount', views.charcount , name='charcount'),
path('analyze',views.analyze,name='analyze')]