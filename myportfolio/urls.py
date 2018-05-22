from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('job/<int:id>/', jobs.views.job, name='job_detail'),
    path('contact/', include('sendemail.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
