from django.urls import path
from . import views, ajax


urlpatterns = [
    path('',views.index, name='index'),
    path('product/detail/<slug:slug>', views.product_detail,name='product_detail'),
    path('product/all-products',views.product_list,name='product_list'),
    path('category/<slug:category_slug>',views.product_list,name='category_detail'),
    path('all-categories/',views.all_Categories,name='all_categories'),
    path('contact-us/',views.contact_us,name='contact_us'),
    path('search/',views.search_Result,name='search'),
    path('product/detail/review/<slug:slug>',views.Comment_Review,name='review'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('subscribe/confirm/<uuid:token>/', views.subscription_confirm, name='subscription_confirm'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/feedback', views.feedback, name='feedback'),
    path('user/', views.user, name='user'),
    path('admin/', views.admin, name='admin'),
]