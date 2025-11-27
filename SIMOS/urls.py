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
    path("update-electrical/<int:pin_id>/", views.update_electrician, name="update_electrical"),

    path("update-instrumentation/<int:pin_id>/", views.update_instrumentation, name="update_instrumentation"),
    path('tower-details/<int:tower_id>/', views.tower_details_view, name='tower_details'),
    
    path("api/cities_by_province/<int:province_id>/", views.cities_by_province, name="cities_by_province"),
    path("api/towers_by_city/<int:city_id>/", views.towers_by_city, name="towers_by_city"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
