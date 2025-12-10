
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf import settings # type: ignore
from django.contrib.staticfiles.urls import static , staticfiles_urlpatterns # type: ignore
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/' , include('App_Login.urls')),
    path('blog/' , include('App_Blog.urls')),
    path('' , views.index , name='index'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
