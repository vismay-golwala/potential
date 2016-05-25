from django.conf.urls import url
from . import views

app_name = 'student'
# URL: /create/student
urlpatterns = [
    url(r'^$', views.dashboard.as_view(), name='dashboard'),
    url(r'^attendance/$', views.attendance.as_view(), name='attendance'),
    url(r'^view_attendance/$', views.view_attendance.as_view(), name='view_attendance'),
    url(r'^student/$', views.student_info_form_view.as_view(), name='student_info_form_view'),
    url(r'^edit_student/$', views.edit_student.as_view(), name='edit_student'),
    url(r'^batch/$', views.batch_form_view.as_view(), name='batch_form_view'),
    url(r'^standard/$', views.standard_form_view.as_view(), name='standard_form_view'),
    url(r'^board/$', views.board_form_view.as_view(), name='board_form_view'),
    url(r'^update_cell/$', views.update_cell.as_view(), name='update_cell'),
    url(r'^get_attendance/$', views.get_attendance.as_view(), name='get_attendance'),
    url(r'^edit_full_student/(?P<pk>\d+)/$', views.edit_full_student.as_view(), name='edit_full_student'),
    url(r'^delete_student/$', views.delete_student.as_view(), name='delete_student'),
]
