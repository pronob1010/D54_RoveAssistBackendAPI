from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('note/', include('note.urls')),
    path('agent/', include('travel_agent.urls')),
    path('features/', include('features.urls')),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)