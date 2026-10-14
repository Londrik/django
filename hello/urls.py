from django.urls import path
from hello import views

urlpatterns = [
    path("", views.HomeListView.as_view(), name="home"),
    path("log/", views.log_message, name="log"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
