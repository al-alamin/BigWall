from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Wall.views.home', name='home'),
    url(r'^', include('wall_post.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
