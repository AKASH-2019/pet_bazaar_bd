from django.urls import path
from authentication import views
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'authentication'


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('privacy', views.privacy, name='privacy'),

    path('social-login/<slug>', views.social_login, name='social_login'),

    path('google-login', views.google_login, name='google_login'),
    path('facebook-login', views.facebook_login, name='facebook_login'),



    
    # request
    path('signupUpsert', views.signupUpsert, name='signupUpsert'),
    path('loginUpsert', views.loginUpsert, name='loginUpsert'),
]
