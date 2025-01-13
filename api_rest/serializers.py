from rest_framework import serializers

from .models import User, UserTasks

class UserSerializer(serializers.ModelSerializer):
  class Meta: 
    model = User
    fields = '__all__'
    
class UserTaskSerializer(serializers.ModelSerializer):
  class Meta: 
    model = UserTasks
    fields = ['user_nickname', 'user_task']
    
  def validate_user_nickname(self, value): 
    if User.objects.filter(user_nickname=value).exists():
      raise serializers.ValidationError('Nickname already in use.')
    return value