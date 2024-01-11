from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mainPage'),
]


    # path('product/', views.product, name='product'),
    # path('news/', views.news, name='news'),
    # path('contacts/', views.contacts, name='contacts'),
    # path('about/', views.about, name='about'),
    #
    # path('product/<slug:product-name>', views.productName, name='productName'),
    # path('news/<int:news-title>', views.newsTitle, name='newsTitle'),
    # path('contacts/<slug:contacts-title>', views.newsTitle, name='newsTitle'),