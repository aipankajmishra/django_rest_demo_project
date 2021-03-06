

# from django.contrib.auth.models import User,Group
from rest_framework import serializers

from .models import Posts, User


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#
# 	class Meta:
# 		model = User
# 		fields = ['url','username','email','groups']
#
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#
# 	class Meta:
#
# 		model  = Group
# 		fields = ['url','name']


class PostSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		fields = ('id', 'title', 'content')
		model = Posts




class MyUserSerializer(serializers.HyperlinkedModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many = True, read_only = True)

	class Meta:
		model = User
		fields = ('name','email','creation_date','posts')