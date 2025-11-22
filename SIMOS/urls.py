from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from operations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('view-towers/', views.view_towers, name='view_towers'),
    path('location/', views.location, name='location'),
    path('add/', views.add_pin, name='add_pin'),
    path('api/towers_by_province/<int:province_id>/', views.towers_by_province, name='towers_by_province'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
