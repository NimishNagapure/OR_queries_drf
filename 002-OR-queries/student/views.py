from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q

# To print all items from table 

def student_list_(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list(request):
    posts = Student.objects.filter(surname__startswith='austin').values('firstname', 'surname') 

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})


# Filter the data and extract it from table 

def student_list_(request):
    posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

# Using the Q keyword to processing the data and 

def student_list_(request):
    posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q (surname__startswith='baldwin') | Q (surname__startswith='avery-parker'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

# Performing AND(&) Operations

def student_list_(request):
    posts = Student.objects.filter(classroom=1) & Student.objects.filter(age=20)

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

# Performing AND(&) Operations with Q

def student_list_(request):
    posts = Student.objects.filter(Q(surname__startswith='baldwin')& Q(firstname__startswith='lakisha'))

    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})

# Performing Union with two database to get fileds

def student_list_(request):

    posts = Student.objects.all().values_list("id","firstname").union(Teacher.objects.all().values_list("id","firstname"))
    
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})

# Performing Exclude() , gt,gte,lt,lte.

def student_list_(request):

    posts = Student.objects.exclude(age__lt=20)
    
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})

def student_list_(request):

    posts = Student.objects.filter(age__gt=20)
    
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})


def student_list_(request):

    posts = Student.objects.filter(classroom=2).only('firstname','age')
    
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})


def student_list_(request):

    posts = Student.objects.all().values_list("teacher").intersection(Teacher.objects.all().values_list("firstname"))

    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})



