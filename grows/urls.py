from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve 

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('res/',ResultView.as_view(),name='res'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)