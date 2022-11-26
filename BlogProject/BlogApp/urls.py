from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home_view , name='home'),
    path('addblog/' , views.addblog_view , name='addblog'),
    path('deleteblog/<int:id>' , views.deleteblog_view , name='deleteblog'),
    path('updateblog/<int:id>' , views.updateblog_view , name='updateblog'),
]