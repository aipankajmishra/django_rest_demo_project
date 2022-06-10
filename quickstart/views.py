from django.shortcuts import render

from rest_framework import status 
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions 
from .serializers import PostSerializer, MyUserSerializer
from .models import Posts, User

from rest_framework.views import APIView

# class UserViewSet(viewsets.ModelViewSet):
#
# 	queryset = User.objects.all().order_by('-date_joined')
# 	serializer_class = UserSerializer
# 	permission_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#
# 	queryset = Group.objects.all()
# 	serializer_class =  GroupSerializer
# 	permission_classes = [permissions.IsAuthenticated]



class MyUserView(APIView):

	def get(self,request):
		queryset = User.objects.all().order_by('-creation_date')
		serializer_class = MyUserSerializer(queryset,many = True)
		#permission_classes  = [permissions.IsAuthenticated]
		return Response(serializer_class.data)

	def post(self,request):
		serializer = MyUserSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PostViewSet(APIView):

	def get(self,request):
		queryset = Posts.objects.all().order_by('-created_at')
		serializer_class = PostSerializer(queryset,many = True)
		permission_classes = [permissions.IsAuthenticated]
		return Response(serializer_class.data)


	def post(self,request):
		serializer = PostSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUES)