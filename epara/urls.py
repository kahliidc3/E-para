from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),  # Add users URLs with explicit namespace
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),  # Our custom accounts URLs with explicit namespace
    path('accounts/', include('allauth.urls')),  # allauth URLs
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('core.urls', namespace='core')),
    path('products/', include('products.urls', namespace='products')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
