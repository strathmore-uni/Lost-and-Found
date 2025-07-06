from rest_framework import serializers
from .models import User, Student, SecurityGuard, AdminProfile, LostItem, FoundItem
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SecurityGuardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityGuard
        fields = '__all__'

class AdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = '__all__'

class LostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItem
        fields = '__all__'

class FoundItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundItem
        fields = '__all__'