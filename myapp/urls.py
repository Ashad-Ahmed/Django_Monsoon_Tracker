from django.urls import path
from .views import SignUpView
from myapp import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('djangodb', views.djangodb, name="djangodb"),
    path('otherdb', views.otherdb, name="otherdb"),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
