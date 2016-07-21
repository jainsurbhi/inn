#from . import views
from .models import Visitor
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ('name', 'age', 'mobile_no', 'company','visiting')