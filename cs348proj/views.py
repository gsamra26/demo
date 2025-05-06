from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Avg, Count, Sum
from .forms import StudentForm, TestForm, MetaTestForm, GetDataForm, GetStudForm
from .models import Student, Test, MetaTest

# Create your views here.


def home(request):
    return render(request, "home.html", {})


def students(request):
    students = Student.objects.all()
    return render(request, "student.html", {"students": students})


def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST or None)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('Student')
        context = {
            'form': form
        }

        return render(request, "add_student_test.html", context=context)
    else:
        return render(request, 'add_student_test.html', {})


def tests(request):
    tests = Test.objects.all()
    return render(request, "test.html", {"tests": tests})


def add_test(request):
    if request.method == "POST":
        form = TestForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('Test')
        context = {
            'form': form
        }

        return render(request, "add_test.html", context=context)
    else:
        return render(request, 'add_test.html', {})


def add_metatest(request):
    if request.method == "POST":
        form = MetaTestForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('Test')
        context = {
            'form': form
        }

        return render(request, "add_metatest.html", context=context)
    else:
        return render(request, 'add_metatest.html', {})


def update_student(request, sID):
    student = Student.objects.get(pk=sID)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('Student')
    context = {
        "student": student,
        "form": form
    }
    return render(request, 'update_student.html', context)


def update_test(request, tID):
    test = Test.objects.get(pk=tID)
    form = TestForm(request.POST or None, instance=test)
    if form.is_valid():
        form.save()
        return redirect('Test')
    context = {
        "test": test,
        "form": form
    }
    return render(request, 'update_test.html', context)


def delete_student(request, sID):
    student = Student.objects.get(pk=sID)
    student.delete()
    return redirect("Student")


def delete_test(request, tID):
    test = Test.objects.get(pk=tID)
    test.delete()
    return redirect("Test")


def display_test_data(request):
    scores = Test.objects.aggregate(
        total_tests=Count('tID'),
        avg_score=Avg('score')
    )
    tests = scores['total_tests']
    avg = scores['avg_score']
    return render(request, "data.html", {"tests": tests, "avg": avg})


def data_by_subject(request):
    if request.method == "POST":
        form = GetDataForm(request.POST or None)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            subj_scores = Test.objects.filter(subject__startswith=subject).aggregate(
                score_avg=Avg("score"),
                tot_test=Count("tID")
            )
            tests = subj_scores['tot_test']
            avg = subj_scores['score_avg']
            return render(request, "subj_data.html", {"tests": tests, "avg": avg, "subject": subject})
        context = {
            'form': form
        }

        return render(request, "subject_data_form.html", context=context)
    else:
        return render(request, 'subject_data_form.html', {})


def display_subj_data(request, subject):
    if request.method == "POST":
        subj_scores = Test.objects.filter(subject__startswith=subject).aggregate(
            score_avg=Avg("score"),
            tot_test=Count("tID")
        )
        tests = subj_scores['tot_test']
        avg = subj_scores['avg_score']
        return render(request, "data.html", {"tests": tests, "avg": avg, subject: subject})
    else:
        return render(request, "subject_data_form.html", {})


def data_by_student(request):
    if request.method == "POST":
        form = GetStudForm(request.POST or None)
        if form.is_valid():
            student = form.cleaned_data['sID']
            stud_scores = Student.objects.filter(sID__startswith=student.sID).aggregate(
                score_avg=Avg("test__score"),
                tot_test=Count("test__tID")
            )
            tests = stud_scores['tot_test']
            avg = stud_scores['score_avg']
            return render(request, "stud_data.html", {"tests": tests, "avg": avg, "subject": student})
        context = {
            'form': form
        }

        return render(request, "subject_data_form.html", context=context)
    else:
        return render(request, 'subject_data_form.html', {})
