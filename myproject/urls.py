"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from myapp.views import home
# from myapp.views import Student

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('home/',home),
#     path('student/',Student, name="student")
# ]

from django.contrib import admin
from django.urls import path
from myapp.views import student_view
from myapp.views import delete_student
from myapp.views import login_view
from myapp.views import update_student
from myapp.views import profile_view
from myapp.views import home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),   
    path('student_view/',student_view,name="student"),
    path('delete_student/<int:id>/', delete_student, name="delete_student"),
    path('login_view/', login_view , name='login_view'),
    path('update_student/<int:id>/', update_student , name='update_student'),
    path('profile_view/', profile_view ,name="profile_view"),
    path('home/',home,name='home')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

