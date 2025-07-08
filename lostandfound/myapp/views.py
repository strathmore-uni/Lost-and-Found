from django.shortcuts import render
from .models import User, Student, SecurityGuard, AdminProfile, LostItem, FoundItem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
def user_list(request):
    users = User.objects.all()
    return render(request, 'myapp/user_list.html', {'users': users})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'myapp/student_list.html', {'students': students})

def security_guard_list(request):
    guards = SecurityGuard.objects.all()
    return render(request, 'myapp/security_guard_list.html', {'guards': guards})

def admin_profile_list(request):        
    admin_profiles = AdminProfile.objects.all()
    return render(request, 'myapp/admin_profile_list.html', {'admin_profiles': admin_profiles})

def lost_item_list(request):
    lost_items = LostItem.objects.all()
    return render(request, 'myapp/lost_item_list.html', {'lost_items': lost_items})

def found_item_list(request):
    found_items = FoundItem.objects.all()
    return render(request, 'myapp/found_item_list.html', {'found_items': found_items})

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/dashboard.html', {'user': request.user})
    else:
        return HttpResponse("You are not logged in.")


from rest_framework.response import Response
from rest_framework.decorators import api_view  
from .serializers import UserSerializer  # Add this import
from .serializers import LostItemSerializer  # Add this import
from .serializers import FoundItemSerializer  # Add this import
@api_view(['GET'])
def api_user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)    

@api_view(['GET'])
def api_student_list(request):
    students = Student.objects.all()
    serializer = UserSerializer(students, many=True)
    return Response(serializer.data)    

@api_view(['GET'])
def api_security_guard_list(request):   
    guards = SecurityGuard.objects.all()
    serializer = UserSerializer(guards, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_admin_profile_list(request):    
    admin_profiles = AdminProfile.objects.all()
    serializer = UserSerializer(admin_profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_lost_item_list(request):    
    lost_items = LostItem.objects.all()
    serializer = UserSerializer(lost_items, many=True)
    return Response(serializer.data)    

@api_view(['GET'])
def api_found_item_list(request):    
    found_items = FoundItem.objects.all()
    serializer = UserSerializer(found_items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lost_items_api(request):
    items = LostItem.objects.all()
    serializer = LostItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def found_items_api(request):
    items = FoundItem.objects.all()
    serializer = FoundItemSerializer(items, many=True)
    return Response(serializer.data)

def home(request):
    return HttpResponse("Hello from Lost & Found!")

from django.http import HttpResponse
from django.template import loader
def navigate_to_home(request):
    template = loader.get_template('lostandfound.myapp/home.html')
    return HttpResponse(template.render({}, request))