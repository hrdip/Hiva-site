
from django.contrib import admin
from django.urls import path
from website.views import *



app_name = 'website'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('newsletter', newsletter_view, name='newsletter'),

]
 