from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from . import views

app_name = 'agents'

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profile_list'),
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
