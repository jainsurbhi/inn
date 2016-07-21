from django.shortcuts import render
from django.http import HttpResponse
from .models import Visitor
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.
def index(request):
	return HttpResponse("People visting to a co-working space")

# ViewSets define the view behavior.
class UserViewSet(APIView):
    def get(self, request, format=None):
        snippets = Visitor.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)