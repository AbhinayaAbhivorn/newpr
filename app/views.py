     
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("iam sharing my project")

from .models import Student


#read
def read(request):
    data = Student.objects.all()  
    return render(request, 'read.html', {'students': data})
#create
def create_student(request):
    if request.method == "POST":
        name = request.POST["name"]
        no = request.POST["no"]
        image = request.FILES.get("image")
 
        Student.objects.create(name=name, no=no, image=image)
        return redirect("read")
 
    return render(request, "create.html")
# UPDATE
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
 
    if request.method == "POST":
        student.name = request.POST["name"]
        student.no = request.POST["no"]
 
        if request.FILES.get("image"):
            student.image = request.FILES.get("image")
 
        student.save()
        return redirect("read")
 
    return render(request, "update.html", {"student": student})# DELETE
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("read")