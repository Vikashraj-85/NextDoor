from django.urls import path
from . import views


urlpatterns=[
    path('',views.homePage ,name="home"),
    path('services',views.servicePage ,name="services"),
    path('contact',views.contactPage ,name="contact"),
    # ------------------------
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('host-room/', views.host_room, name='host_room'),
    path('add-review/', views.add_review, name='add_review'),
    path('card-detail/<int:id>', views.card_detail, name='detail'),
    path('payment/<int:id>', views.view_payment, name='payment'),
    path('resetPassword', views.forget_password, name='resetpass'),
    path('test/', views.test, name='test'),
    
]