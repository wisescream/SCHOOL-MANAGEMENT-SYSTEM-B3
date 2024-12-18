from django import forms
from .models import Student, Teacher, Class, Subject, Grade, Attendance

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'