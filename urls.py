from django.urls import  path
from django.urls.conf import include
from course import views
urlpatterns = [
    path('cou',views.cou),
    path('show',views.show),
    path('edit/<int:code>, views.edit),
    path('upadte/<int:code>, views.update),
    path('delete/<int:code>, views.destory),

]