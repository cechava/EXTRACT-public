from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'agents'

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profile_list'),
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('update/', views.ProfileUpdateView.as_view(), name='profile_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
