from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from operations import views
from django.contrib.auth.views import LoginView, LogoutView  # <-- Add this line


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('survey/', views.home, name='home'),
    path('view-towers/', views.view_towers, name='view_towers'),
    path('location/', views.location, name='location'),
    path('add/', views.add_pin, name='add_pin'),
    path('api/towers_by_province/<int:province_id>/', views.towers_by_province, name='towers_by_province'),
    path('login/', LoginView.as_view(template_name='operations/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    path("update-construction/<int:pin_id>/", views.update_construction, name="update_construction"),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
