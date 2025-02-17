from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Notification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('id','username')



class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [ 'id','recipient', 'message']
