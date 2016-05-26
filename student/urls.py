from django.conf.urls import url
from . import views

app_name = 'student'
# URL: student/
urlpatterns = [
    url(r'^$', views.dashboard.as_view(), name='dashboard'),
    url(r'^attendance/$', views.attendance.as_view(), name='attendance'),
    url(r'^student/$', views.student_info_form_view.as_view(), name='student_info_form_view'),
    url(r'^edit_student/$', views.edit_student.as_view(), name='edit_student'),
    url(r'^batch/$', views.batch_form_view.as_view(), name='batch_form_view'),
    url(r'^standard/$', views.standard_form_view.as_view(), name='standard_form_view'),
    url(r'^board/$', views.board_form_view.as_view(), name='board_form_view'),
    url(r'^get_attendance/$',  views.get_attendance, name='get_attendance'),
    url(r'^fee/$', views.fee_form_view.as_view(), name='fee'),
    url(r'^test_model/$', views.test_model_form_view.as_view(), name='test'),
    url(r'^get_test_students/$',  views.get_test_students, name='get_test_students'),
]
