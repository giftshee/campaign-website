from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),
    path(
    'delete-home-image/',
    views.delete_home_image,
    name='delete_home_image'
),
    path(
    "dashboard/volunteers/delete/<int:id>/",
    views.delete_volunteer,
    name="delete_volunteer"
),
    path(
    'dashboard/volunteers/',
    views.volunteer_dashboard,
    name='volunteer_dashboard'
),


    path('volunteer/', views.volunteer, name='volunteer'),

    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/', views.gallery, name='gallery'),
path('gallery/', views.gallery, name='gallery'),
path('gallery/delete/<int:pk>/', views.delete_gallery, name='delete_gallery'),

    # NEWS
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('news/add/', views.add_news, name='add_news'),
    path('news/edit/<int:id>/', views.edit_news, name='edit_news'),
    path('news/delete/<int:id>/', views.delete_news, name='delete_news'),

    # MANIFESTO (FIXED)
    path('manifesto/', views.manifesto_page, name='manifesto'),
    path('manifesto/add/', views.add_manifesto_item, name='add_manifesto_item'),
    path('manifesto/delete/<int:pk>/', views.delete_manifesto_item, name='delete_manifesto_item'),

    # DASHBOARD
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/volunteers/', views.dashboard_volunteers, name='dashboard_volunteers'),
    path('dashboard/news/', views.dashboard_news, name='dashboard_news'),
    path('dashboard/messages/', views.dashboard_messages, name='dashboard_messages'),
    path('dashboard/manifesto/', views.dashboard_manifesto, name='dashboard_manifesto'),

    # AUTH
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # PAGES
    path('edit/<str:page_name>/', views.edit_page, name='edit_page'),
    path('delete/<str:page_name>/image/', views.delete_page_image, name='delete_page_image'),
]