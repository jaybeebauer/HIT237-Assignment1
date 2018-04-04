"""
Definition of urls for HIT237_Assignment1.
"""

from django.conf.urls import include, url
from books_repo import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', HIT237_Assignment1.views.home, name='home'),
    # url(r'^HIT237_Assignment1/', include('HIT237_Assignment1.HIT237_Assignment1.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.home, name='home'),
    url(r'^books/?$', views.books, name='books'),
    url(r'^book/(\d{1,4})/?$', views.single_book, name='book'),
    url(r'^datamodel/?$', views.datamodel, name='datamodel'),
]