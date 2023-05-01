from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Teacher, Group, Subject
from .forms import TeacherForm, GroupForm


def index(request):
    return render(request, "department/index.html")


def teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            Teacher.objects.create(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                patronymic=form.cleaned_data["patronymic"],
                birthday=form.cleaned_data["birthday"],
                subject=form.cleaned_data["subject"],
            )
            return HttpResponseRedirect("/teachers/")
    else:
        form = TeacherForm()
    return render(request, "department/teacher.html", {"form": form})


def teachers(request):
    teachers_list = []
    for person in Teacher.objects.all().order_by("id"):
        result = {
            "id": person.id,
            "first_name": person.first_name,
            "last_name": person.last_name,
            "birthday": person.birthday,
            "subject": person.subject.name,
        }
        teachers_list.append(result)
    return render(request, "department/teachers.html", {"teachers_list": teachers_list})


def group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            Group.objects.create(name=form.cleaned_data["name"])
            return HttpResponseRedirect("/groups/")
    else:
        form = GroupForm()
    return render(request, "department/group.html", {"form": form})


def groups(request):
    groups_list = list(Group.objects.all().order_by("id").values())
    return render(request, "department/groups.html", {"groups_list": groups_list})
