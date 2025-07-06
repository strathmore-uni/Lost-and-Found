from django.db import models

# Create your models here.
class User(models.Model):
    userID = models.IntegerField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Student(User):
    studentID = models.IntegerField(unique=True)
    studentemail = models.EmailField(unique=True)
    studentname = models.CharField(max_length=100)

    def __str__(self):
        return self.studentname
    
class SecurityGuard(User):
    guardID = models.IntegerField(unique=True)
    guardemail = models.EmailField(unique=True)
    guardname = models.CharField(max_length=100)

    def __str__(self):
        return self.guardname
    
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_level = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} - {self.access_level}"
    
class LostItem(models.Model):
    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=100)
    itemDescription = models.TextField()
    itemImage = models.ImageField(upload_to='lost_items/')
    lostDate = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName
    
class FoundItem(models.Model):
    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=100)
    itemDescription = models.TextField()
    itemImage = models.ImageField(upload_to='found_items/')
    foundDate = models.DateField()
    guardID = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName