from django.conf.urls import url,include
from .views import index, UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^visitor$',UserViewSet.as_view(), name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]