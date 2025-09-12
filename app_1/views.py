from django.shortcuts import *
from .models import *
from django.http import HttpResponse
# Create your views here.

def first_program(request):
    return HttpResponse("<h1>  Hello Gourav, welcome to the battle field where you will start to build the things! </h1>")

def stu_reg(request):
    if request.method == "POST":
        name = request.POST.get("name")
        std = request.POST.get("std")
        roll_no = request.POST.get("roll_no")
        father_name = request.POST.get("father_name")
        mother_name = request.POST.get("mother_name")
        address = request.POST.get("address")
        blood_group = request.POST.get("blood_group")

        # save into the db.
        stu = Student.objects.create(
            name = name,
            std = std,
            roll_no = roll_no,
            father_name = father_name,
            mother_name = mother_name,
            address = address,
            blood_group = blood_group
        )
        return redirect("student_registers_detail")
    return render(request, "student.html")

def view_details(request):
    stu = Student.objects.all()
    return render(request, 'view_student_details.html', {'students' : stu})


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.std = request.POST.get("std")
        student.roll_no = request.POST.get("roll_no")
        student.father_name = request.POST.get("father_name")
        student.mother_name = request.POST.get("mother_name")
        student.address = request.POST.get("address")
        student.blood_group = request.POST.get("blood_group")
        student.save()

        return redirect("student_registers_detail")

    return render(request, "edit_student.html", {"student": student})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect("student_registers_detail")