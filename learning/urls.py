# TODO: Cleanup the project in a better way

from django.contrib import admin

from django.urls import include, path
from rest_framework import routers
from quickstart import views as quickstartviews
admin.autodiscover()

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin',admin.site.urls),
    path('posts',quickstartviews.PostViewSet.as_view()),
    path('api/',include('quickstart.urls')) # All the urls with api/ will end up to our app quickstart
]
