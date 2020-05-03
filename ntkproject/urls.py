from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from candidate.views import career_view, student_create_view, professional_create_view 

urlpatterns = [
	path('', career_view),
	path('student/', student_create_view),
    path('professional/', professional_create_view),
    # path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)