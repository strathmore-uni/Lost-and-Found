from django.test import TestCase
from .models import User, Student, SecurityGuard, AdminProfile, LostItem, FoundItem
# Create your tests here.
class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(userID=1, email = 'jane.doe@gmail.com', password = 'password123')
    def test_user_creation(self):
        self.assertEqual(self.user.userID, 1)
        self.assertEqual(self.user.email, 'jane.doe@gmail.com')
        self.assertEqual(self.user.password, 'password123')

class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(userID=2, studentID=1001, studentemail = 'john.doe@gmail.com', studentname = 'John Doe', password = 'password123')
    def test_student_creation(self):
        self.assertEqual(self.student.userID, 2)
        self.assertEqual(self.student.studentID, 1001)
        self.assertEqual(self.student.studentemail, 'john.doe@gmail.com')
        self.assertEqual(self.student.studentname, 'John Doe')

class SecurityGuardModelTest(TestCase):
    def setUp(self):
        self.guard = SecurityGuard.objects.create(userID=3, guardID=2001, guardemail = 'jdoe@gmail.com', guardname = 'Jane Doe', password = 'password123')
    def test_security_guard_creation(self):
        self.assertEqual(self.guard.userID, 3)
        self.assertEqual(self.guard.guardID, 2001)
        self.assertEqual(self.guard.guardemail, 'jdoe@gmail.com')
        self.assertEqual(self.guard.guardname, 'Jane Doe')

class AdminProfileModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(userID=4, email = 'jd123@gmail.com', password = 'password123')
        self.admin_profile = AdminProfile.objects.create(user=user, access_level='superadmin')
    def test_admin_profile_creation(self):
        self.assertEqual(self.admin_profile.user.userID, 4)
        self.assertEqual(self.admin_profile.access_level, 'superadmin')

class LostItemModelTest(TestCase):
    def setUp(self):
        student = Student.objects.create(userID=5, studentID=3001, studentemail = 'jdoe@gmail.com', studentname = 'John Doe', password = 'password123')
        self.lost_item = LostItem.objects.create(itemID=1, itemName='Lost Wallet', itemDescription='Black leather wallet', itemImage='wallet.jpg', lostDate='2023-10-01', student=student)
    def test_lost_item_creation(self):
        self.assertEqual(self.lost_item.itemID, 1)
        self.assertEqual(self.lost_item.itemName, 'Lost Wallet')
        self.assertEqual(self.lost_item.itemDescription, 'Black leather wallet')
        self.assertEqual(self.lost_item.itemImage, 'wallet.jpg')
        self.assertEqual(self.lost_item.lostDate, '2023-10-01')
        self.assertEqual(self.lost_item.student.studentID, 3001)

class FoundItemModelTest(TestCase):
    def setUp(self):
        SecurityGuard.objects.create(userID=6, guardID=4001, guardemail = 'jdow@gmail.com', guardname = 'Jane Dow', password = 'password123')
        self.found_item = FoundItem.objects.create(itemID=1, itemName='Found Phone', itemDescription='Black smartphone', itemImage='phone.jpg', foundDate='2023-10-02', guardID=SecurityGuard.objects.get(guardID=4001))
    def test_found_item_creation(self):
        self.assertEqual(self.found_item.itemID, 1)
        self.assertEqual(self.found_item.itemName, 'Found Phone')
        self.assertEqual(self.found_item.itemDescription, 'Black smartphone')
        self.assertEqual(self.found_item.itemImage, 'phone.jpg')
        self.assertEqual(self.found_item.foundDate, '2023-10-02')
        self.assertEqual(self.found_item.guardID.guardID, 4001)

