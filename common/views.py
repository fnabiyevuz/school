from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from common.models import Grade


def home(request):

    grade_count = Grade.objects.all().count()

    context = {
        'grade_count':grade_count
    }

    return render(request, 'home.html', context)


def grade(request):
    grades = Grade.objects.all().order_by('base', 'name')

    context = {
        'grades': grades,
    }

    return render(request, 'grade.html', context)


def add_grade(request):
    base = request.POST['base']
    name = request.POST['name']

    Grade.objects.create(
        base=base,
        name=name,
    )

    return redirect('common:grade')


def delete_grade(request, id):
    grade = Grade.objects.get(id=id)
    grade.delete()

    return redirect('common:grade')


def update_grade(request, id):
    if request.method == 'POST':

        grade = Grade.objects.get(id=id)
        grade.base = request.POST['base']
        grade.name = request.POST['name']
        grade.save()

        return redirect('common:grade')

    else:
        grade = Grade.objects.get(id=id)
        grades = Grade.objects.all().order_by('base', 'name')
        context = {
            "grade": grade,
            "grades": grades,
        }

        return render(request, 'grade.html', context)

def teacher(request):
    return render(request, 'teacher.html')


def student(request):
    return render(request, 'student.html')
