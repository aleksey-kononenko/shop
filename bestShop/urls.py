from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('', include('main.urls')),
    path('', include('registration.urls')),
    path('', include('products.urls')),
    path('', include('orders.urls')),
    path('', include('shop.urls')),
    path('', include('about.urls')),
    path('', include('emails.urls')),
    path('', include('constructor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)