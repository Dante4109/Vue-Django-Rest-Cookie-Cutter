from django.urls import path, include
from backend.profile import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"UserProfile", views.ProfileView, basename="UserProfile")

# The API URLs are now determined automatically by the router.
urlpatterns = [path("", include(router.urls))]

# Example URL
# http://127.0.0.1:8000/api/UserProfile/