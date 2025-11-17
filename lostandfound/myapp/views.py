from django.shortcuts import render
from .models import User, Student, SecurityGuard, AdminProfile, LostItem, FoundItem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User(email=email, password=password)
        user.save()
        return HttpResponse("User registered successfully.")
    return render(request, 'register.html')

def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        results = LostItem.objects.filter(itemName__icontains=query)
        return render(request, 'search_results.html', {'results': results})
    return render(request, 'search.html')

def record(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_description = request.POST.get('item_description')
        item_image = request.FILES.get('item_image')
        lost_date = request.POST.get('lost_date')
        student_id = request.POST.get('student_id')
        
        student = Student.objects.get(studentID=student_id)
        lost_item = LostItem(itemName=item_name, itemDescription=item_description, itemImage=item_image, lostDate=lost_date, student=student)
        lost_item.save()
        
        return HttpResponse("Lost item recorded successfully.")
    return render(request, 'record.html')

def report(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_description = request.POST.get('item_description')
        item_image = request.FILES.get('item_image')
        found_date = request.POST.get('found_date')
        guard_id = request.POST.get('guard_id')
        
        guard = SecurityGuard.objects.get(guardID=guard_id)
        found_item = FoundItem(itemName=item_name, itemDescription=item_description, itemImage=item_image, foundDate=found_date, guardID=guard)
        found_item.save()
        
        return HttpResponse("Found item reported successfully.")
    return render(request, 'report.html')

def security_guard(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        guard = SecurityGuard(email=email, password=password)
        guard.save()
        return HttpResponse("Security guard registered successfully.")
    return render(request, 'security_guard.html')

def student(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        student = Student(email=email, password=password)
        student.save()
        return HttpResponse("Student registered successfully.")
    return render(request, 'student.html')  

def upload(request):    
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_description = request.POST.get('item_description')
        item_image = request.FILES.get('item_image')
        lost_date = request.POST.get('lost_date')
        student_id = request.POST.get('student_id')
        
        student = Student.objects.get(studentID=student_id)
        lost_item = LostItem(itemName=item_name, itemDescription=item_description, itemImage=item_image, lostDate=lost_date, student=student)
        lost_item.save()
        
        return HttpResponse("Lost item uploaded successfully.")
    return render(request, 'upload.html')

def verify(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_description = request.POST.get('item_description')
        item_image = request.FILES.get('item_image')
        found_date = request.POST.get('found_date')
        guard_id = request.POST.get('guard_id')
        
        guard = SecurityGuard.objects.get(guardID=guard_id)
        found_item = FoundItem(itemName=item_name, itemDescription=item_description, itemImage=item_image, foundDate=found_date, guardID=guard)
        found_item.save()
        
        return HttpResponse("Found item verified successfully.")
    return render(request, 'verify.html')

def view_page(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_description = request.POST.get('item_description')
        item_image = request.FILES.get('item_image')
        lost_date = request.POST.get('lost_date')
        student_id = request.POST.get('student_id')
        
        student = Student.objects.get(studentID=student_id)
        lost_item = LostItem(itemName=item_name, itemDescription=item_description, itemImage=item_image, lostDate=lost_date, student=student)
        lost_item.save()
        
        return HttpResponse("Lost item viewed successfully.")
    return render(request, 'view.html')

def sgdashboard(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_description = request.POST.get('item_description')
        item_image = request.FILES.get('item_image')
        found_date = request.POST.get('found_date')
        guard_id = request.POST.get('guard_id')
        
        guard = SecurityGuard.objects.get(guardID=guard_id)
        found_item = FoundItem(itemName=item_name, itemDescription=item_description, itemImage=item_image, foundDate=found_date, guardID=guard)
        found_item.save()
        
        return HttpResponse("Found item viewed successfully.")
    return render(request, 'sgdashboard.html')



@login_required
def register(request):
    if request.user.is_authenticated:
        return render(request, 'register.html', {'user': request.user})
    else:
        return HttpResponse("You are not logged in.")

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

    


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
    return render(request, 'index.html')

from django.http import HttpResponse
from django.template import loader
def navigate_to_home(request):
    template = loader.get_template('lostandfound.myapp/home.html')
    return HttpResponse(template.render({}, request))

def dashboard(request):
    return render(request, 'dashboard.html')
def record(request):
    return render(request, 'record.html')
def report(request):
    return render(request, 'report.html')
def search(request):
    return render(request, 'search.html')
def security_guard(request):
    return render(request, 'Security Guard.html')
def security_guard_login(request):
    return render(request, 'Securityguardlogin.html')
def sg_dashboard(request):
    return render(request, 'sgdashboard.html')
def student(request):
    return render(request, 'student.html')
def upload(request):
    return render(request, 'upload.html')
def verify(request):
    return render(request, 'verify.html')
def view_page(request):
    return render(request, 'view.html')

def api_securityguards(request):
    guards = SecurityGuard.objects.all()
    data = [
        {
            'guardID': guard.guardID,
            'guardemail': guard.guardemail,
            'guardname': guard.guardname
        }
        for guard in guards
    ]
    return JsonResponse(data, safe=False)