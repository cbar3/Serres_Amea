from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('announcements/', views.announcement, name='announcements'),
    path('deltia_typou/', views.deltia, name='deltia_typou'),
    path('istoria', views.history, name='istoria'),
    path('ergastirio', views.image_list, name='ergastirio'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)