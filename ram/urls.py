
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('', include('webpage.urls')),
    path('blog/', include('blog.urls')),
   # path('', include('webpage.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('members.urls')),

]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 