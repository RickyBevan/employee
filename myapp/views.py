'''import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import student  # Ensure your model name is exactly as defined
from django.forms.models import model_to_dict
from templates import html1_templates, html_templates
#from .templates import student

@method_decorator(csrf_exempt, name='dispatch')
class StudentListView(View):
    def get(self, request):
        # List all students from the database
        students = list(student.objects.values())
        return JsonResponse({'students': students}, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class StudentCreateView(View):
    def get(self, request):
        # Return the HTML form for creating a student
        return HttpResponse(STUDENT_CREATE_HTML)
    
    def post(self, request):
        # Handle JSON or form data for student creation
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
            name = data.get('name', '')
            email = data.get('email', '')
            age = data.get('age', 0)
        else:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            age = request.POST.get('age', 0)
            try:
                age = int(age)
            except ValueError:
                age = 0

        student_obj = student.objects.create(name=name, email=email, age=age)
        return JsonResponse({
            'message': 'Student created',
            'student': model_to_dict(student_obj)
        })



@method_decorator(csrf_exempt, name='dispatch')
class StudentUpdateView(View):
    def get(self, request, pk):
        return HttpResponse(STUDENT_UPDATE_HTML)

    def post(self, request, pk):
        student_obj = get_object_or_404(Student, pk=pk)
        
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON payload'}, status=400)
        else:
            data = request.POST.dict()  # Convert QueryDict to a dictionary

        # Update fields if provided
        student_obj.name = data.get('name', student_obj.name)
        student_obj.email = data.get('email', student_obj.email)
        
        if 'age' in data:
            try:
                student_obj.age = int(data['age'])
            except (ValueError, TypeError):
                return JsonResponse({'error': 'Invalid age value'}, status=400)

        student_obj.save()
        return JsonResponse({
            'message': 'Student updated successfully',
            'student': model_to_dict(student_obj)})
         

@method_decorator(csrf_exempt, name='dispatch')
class StudentDeleteView(View):
    def post(self, request, pk):
        # Delete a student based on primary key
        try:
            student_obj = student.objects.get(pk=pk)
        except student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        
        student_obj.delete()
        return JsonResponse({'message': 'Student deleted'})
    '''


import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import student  # Ensure your model name is exactly as defined
from django.forms.models import model_to_dict

@method_decorator(csrf_exempt, name='dispatch')
class StudentListView(View):
    def get(self, request):
        # List all students from the database
        students = list(student.objects.values())
        # Return JSON for simplicity
        return JsonResponse({'students': students}, safe=False)



@method_decorator(csrf_exempt, name='dispatch')
class StudentCreateView(View):
    def get(self, request):
        # Render the HTML form for creating a student using create.html
        return render(request, 'create.html')
    
    def post(self, request):
        # Handle form data (or JSON) for student creation
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
            name = data.get('Name', '')
            email = data.get('Email', '')
            age = data.get('Age', 0)
        else:
            name = request.POST.get('Name', '')
            email = request.POST.get('Email', '')
            age = request.POST.get('Age', 0)
        
        try:
            age = int(age)
        except ValueError:
            age = 0

        # Create a new student record without an "address" field
        student_obj = student.objects.create(name=name, email=email, age=age)
        
        # After creation, redirect to the list view (ensure your urls.py defines the 'list' URL name)
        return redirect('list')
    
    



@method_decorator(csrf_exempt, name='dispatch')
class StudentUpdateView(View):
    def get(self, request, pk):
        # Fetch the existing student record and render the update form.
        # The update.html template expects a context variable "mem" with the student data.
        student_obj = get_object_or_404(student, pk=pk)
        return render(request, 'update.html', {'mem': student_obj})
    
    def post(self, request, pk):
        student_obj = get_object_or_404(student, pk=pk)
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON payload'}, status=400)
        else:
            data = request.POST
        
        # Update fields if provided; use form field names from your template (e.g., "Name", "Email", etc.)
        student_obj.name = data.get('Name', student_obj.name)
        student_obj.email = data.get('Email', student_obj.email)
        if 'Age' in data:
            try:
                student_obj.age = int(data['Age'])
            except (ValueError, TypeError):
                return JsonResponse({'error': 'Invalid age value'}, status=400)
        # Remove address update since the model doesn't have an 'address' field.
        student_obj.save()
        return redirect('list')




@method_decorator(csrf_exempt, name='dispatch')
class StudentDeleteView(View):
    def get(self, request, pk):
        student_obj = get_object_or_404(student, pk=pk)
        student_obj.delete()
        return redirect('list')