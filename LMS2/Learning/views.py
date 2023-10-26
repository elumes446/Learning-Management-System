from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Message
from .models import *
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from Learning.models import User

def index(request):
    return render(request,'login2.html')

def login_page(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('indexadmin')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('student')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('indexteacher')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login2.html', {'form': form, 'msg': msg})


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_page')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def adminpage(request):
    return render(request,'adminpage.html')

def indexteacher(request):
    return render(request, 'indexteacher.html')

def student(request):
    return render(request,'student.html')

def indexadmin(request):
    return render(request,'indexadmin.html')

def teacher(request):
    return render(request,'teacher.html')


@login_required
def chat(request):
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        sender = request.user
        receiver_id = request.POST['receiver']
        text = request.POST['text']
        reply_to_id = request.POST.get('reply_to')
        reply_to = Message.objects.filter(id=reply_to_id).first() if reply_to_id else None
        receiver = User.objects.get(id=receiver_id)
        Message.objects.create(sender=sender, receiver=receiver, text=text, reply_to=reply_to)
        return redirect('chat')
    else:
        messages = Message.objects.filter(sender=request.user) | Message.objects.filter(receiver=request.user)
        return render(request, 'chat.html', {'users': users, 'messages': messages})


@login_required
def addbook(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        pdf = request.FILES['pdf']
        if pdf.size <= 100 * 1024 * 1024:  # Check if the file size is below 100MB
            Book.objects.create(title=title, author=author, pdf=pdf)
            return redirect('manage_file')
        else:
            return render(request, 'addbook.html', {'error_message': 'File size exceeds the limit (100MB).'})
    else:
        return render(request, 'addbook.html')

@login_required
def manage_file(request):
    books = Book.objects.all()
    return render(request, 'manage_file.html', {'books': books})

@login_required
def openbook(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'openbook.html', {'book': book})


@login_required
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam_list.html', {'exams': exams})

@login_required
def add_exam(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        duration = request.POST.get('duration')
        total_marks = request.POST.get('total_marks')

        exam = Exam.objects.create(title=title, duration=duration, total_marks=total_marks)

        return redirect('exam_list')

    return render(request, 'add_exam.html')

@login_required
def update_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        duration = request.POST.get('duration')
        total_marks = request.POST.get('total_marks')

        exam.title = title
        exam.duration = duration
        exam.total_marks = total_marks
        exam.save()

        return redirect('exam_list')

    return render(request, 'update_exam.html', {'exam': exam})

@login_required
def delete_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)

    if request.method == 'POST':
        exam.delete()
        return redirect('exam_list')

    return render(request, 'delete_exam.html', {'exam': exam})

@login_required
def exam_detail(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    questions = Question.objects.filter(exam=exam)
    current_time = timezone.now()
    end_time = current_time + datetime.timedelta(minutes=exam.duration)
    return render(request, 'exam_detail.html', {'exam': exam, 'questions': questions, 'end_time': end_time})

@login_required
def submit_exam(request, exam_id):
    if request.method == 'POST':
        exam = Exam.objects.get(pk=exam_id)
        questions = Question.objects.filter(exam=exam)
        total_marks = 0
        obtained_marks = 0

        for question in questions:
            submitted_answer = request.POST.get(f'question_{question.id}')
            answer = Answer.objects.get(question=question, is_correct=True)

            total_marks += 1
            if submitted_answer == str(answer.id):
                obtained_marks += 1

        percentage = (obtained_marks / total_marks) * 100
        return render(request, 'exam_result.html', {'exam': exam, 'obtained_marks': obtained_marks, 'total_marks': total_marks, 'percentage': percentage})

    return redirect('exam_list')



def list_teacher(request):
    teachers = User.objects.filter(is_teacher='True')
    return render(request, 'indexadmin.html', {'teachers': teachers})

def add_video(request):
    all_video = Video.objects.all()
    form= VideoUploadForm(data=request.POST, files=request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    context= {
        'form' : form,
        'all' : all_video
            }
    return render(request, 'add_video.html', context)

def manage_video(request):
    video = Video.objects.all()
    return render(request, 'manage_video.html', {'video': video})

def delete_teacher_user(request, user_id):
    user = User.objects.get(id=user_id, is_teacher=True)
    if user:
        user.delete()
    return redirect('manage_teacher')

def list_student(request):
    students = User.objects.filter(is_student='True')
    return render(request, 'manage_student.html', {'students': students})

def delete_student_user(request, user_id):
    user = User.objects.get(id=user_id, is_student=True)
    if user:
        user.delete()
    return redirect('manage_student')

def list_admin(request):
    admins = User.objects.filter(is_admin='True')
    return render(request, 'manage_admin.html', {'admins': admins})

