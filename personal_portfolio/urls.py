"""personal_portfolio URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# code to add the portfolio views
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # The below code is showing the portfolio app
    # Thats why we imported portfolio views above
    path('', views.home, name='home'),
    # see the reason above for this import
    # The below code will separate the different apps of the site
    # Use the same style to create different paths.
    path('blog/', include('blog.urls')),
]

# This code will add the link to images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# The below code helps to show the static images
# code told by the author was not working and was showing 404 error
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)