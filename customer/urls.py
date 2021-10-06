from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Index, About, Order, Search

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('order/', Order.as_view(), name='order'),
    path('search', Search.as_view(), name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)