from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('note/', include('note.urls')),
    path('agent/', include('travel_agent.urls')),
]
