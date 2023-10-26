from django.urls import include, path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('chat/', views.chat, name='chat'),
    path('addbook/', views.addbook, name='addbook'),
    path('manage_file/', views.manage_file, name='manage_file'),
    path('openbook/<int:book_id>/', views.openbook, name='openbook'),
    path('exam_list/', views.exam_list, name='exam_list'),
    path('exam_detail<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('submit_exam/<int:exam_id>/submit/', views.submit_exam, name='submit_exam'),
    path('add_exam', views.add_exam, name='add_exam'),
    path('update_exam<int:exam_id>/update/', views.update_exam, name='update_exam'),
    path('delete_exam<int:exam_id>/delete/', views.delete_exam, name='delete_exam'),
    path('manage_teacher/', views.list_teacher, name='manage_teacher'),
    path('indexadmin/', views.list_teacher, name='indexadmin'),
    path('delete_teacher_user<int:user_id>/', views.delete_teacher_user, name='delete_teacher_user'),
    path('manage_student/', views.list_student, name='manage_student'),
    path('delete_student_user<int:user_id>/', views.delete_student_user, name='delete_student_user'),
    path('manage_admin/', views.list_admin, name='manage_admin'),
    path('indexadmin/', views.indexadmin, name='indexadmin'),
    path('indexteacher/', views.indexteacher, name='indexteacher'),
    path('manage_video/', views.manage_video, name='manage_video'),
    path('add_video/', views.add_video, name='add_video'),
]
    

