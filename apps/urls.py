from django.urls import path

from apps import views

urlpatterns = [
    path('index/', views.index),
    path('add/', views.add_index),
    path('get/', views.get_people),
    path('heh/', views.heh, name="jump"),
    path('hehe/', views.hehe, name="jp2"),
    path('json/', views.get_json, name="json_con"),
    path('setCookies/', views.set_Cookies, name="setcookie"),
    path('getCookies/', views.get_Cookies, name="getcookie"),

]
