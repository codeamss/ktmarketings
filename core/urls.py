from django.urls import path
from .views import home, pricing, services_page, contact,portfolio_list,portfolio_detail,blog_list,blog_detail

urlpatterns = [
    path('', home, name='home'),
    path('pricing/', pricing, name='pricing'),
    path('services/', services_page, name='services'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio_list, name='portfolio'),
    path('portfolio/<slug:slug>/', portfolio_detail, name='portfolio_detail'),
    path('blog/', blog_list, name='blog'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),



]
