# from django.shortcuts import render
# from django.http import HttpResponse
# from myapp.models import Student

# Create your views here.


# def home(request):
#     return HttpResponse("hello abhi")

# def Student(request):
#     if request.method=="POST":
#         form_data=request.POST
#         first_name=form_data.get("first_name")
#         last_name=form_data.get("last_name")
#         age=form_data.get("age")
#         discription=form_data.get("discription")
#         s1=Student(
#             first_name=first_name,
#             last_name=last_name,
#             age=age,
#             discription=discription

#         )
#         s1.save()

#     return render(request,'student.html' )

from django.shortcuts import render, redirect , get_object_or_404 
from .models import Student  # Import the Student model
from .models import Login
from .models import Profile

def student_view(request):  # Rename the view function
    data=Student.objects.all()
    if request.method == "POST":
        form_data = request.POST
        first_name = form_data.get("first_name")
        last_name = form_data.get("last_name")
        age = form_data.get("age")
        discription = form_data.get("discription")  # Note: Ensure the spelling matches the model

        # Create an instance of Student and save it to the database
        s1 = Student(
            first_name=first_name,
            last_name=last_name,
            age=age,
            discription=discription  # Make sure this matches the model field name
        )
        s1.save()

        data=Student.objects.all()
        return redirect('student')


    return render(request,'student.html',{'data':data})

def delete_student(request,id):
    s1=Student.objects.filter(id=id)
    s1.delete()
    

    return redirect('student')


def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == 'POST':
        
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.age = request.POST.get('age')
        student.discription = request.POST.get('discription') 

        student.save()  
        return redirect('student')  
    
  
    return render(request, 'update_student.html', {'student': student})

def profile_view(request):
    raw = Profile.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        
        name = data.get("name")
        profile_picture = files.get("profile_picture")
        bio = data.get("bio")
        
        p1 = Profile(
            name = name,
            profile_picture = profile_picture,
            bio = bio
        )
        p1.save()
        
        print(name)
        print(profile_picture)
        print(bio)
        
        return redirect('profile')
    
    return render(request, 'profile.html', {'raw': raw})

def login_view(request):  # Renamed the function to avoid conflict with the model
    if request.method == "POST":
        form_data = request.POST
        user_name = form_data.get("user_name")
        password = form_data.get("password")
        email = form_data.get("email")
        
        # Basic validation to ensure no field is left empty
        if user_name and password and email:
            # Create a new Login instance and save it to the database
            l1 = Login(
                user_name=user_name,
                password=password,
                email=email,
            )
            l1.save()

            # Debug prints
            print(user_name)
            print(password)
            print(email)
        else:
            print("All fields are required.")

    return render(request, 'login.html')


def home(request):
    return render(request,'index.html')


