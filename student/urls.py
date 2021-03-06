from django.conf.urls import url
from . import views

app_name = 'student'
# URL: student/
urlpatterns = [
    url(r'^$', views.dashboard.as_view(), name='dashboard'),
    url(r'^set_session_link/$', views.set_session_link.as_view(), name='set_session_link'),
    url(r'^attendance/$', views.attendance.as_view(), name='attendance'),
    url(r'^get_attendance/$', views.get_attendance.as_view(), name='get_attendance'),
    url(r'^view_attendance/$', views.view_attendance.as_view(), name='view_attendance'),
    url(r'^student/$', views.student_info_form_view.as_view(), name='student_info_form_view'),
    url(r'^edit_student/$', views.edit_student.as_view(), name='edit_student'),
    url(r'^update_cell/$', views.update_cell.as_view(), name='update_cell'),
    url(r'^edit_full_student/(?P<pk>\d+)/$', views.edit_full_student.as_view(), name='edit_full_student'),
    url(r'^delete_student/$', views.delete_student.as_view(), name='delete_student'),
    url(r'^batch/$', views.batch_form_view.as_view(), name='batch_form_view'),
    url(r'^delete_batch/$', views.delete_batch.as_view(), name='delete_batch'),
    url(r'^standard/$', views.standard_form_view.as_view(), name='standard_form_view'),
    url(r'^delete_standard/$', views.delete_standard.as_view(), name='delete_standard'),
    url(r'^board/$', views.board_form_view.as_view(), name='board_form_view'),
    url(r'^delete_board/$', views.delete_board.as_view(), name='delete_board'),
    url(r'^get_attendance/$',  views.get_attendance, name='get_attendance'),
    url(r'^fee/$', views.fee_form_view.as_view(), name='fee'),
    url(r'^test_model/$', views.test_model_form_view.as_view(), name='test'),
    url(r'^get_test_students/$',  views.get_test_students, name='get_test_students'),
    url(r'^login/$',  views.login_view.as_view(), name='login_view'),
    url(r'^logout/$',  views.logout_user, name='logout_user'),
    url(r'^view_fees/$',  views.fee_installment_form_view.as_view(), name='fee_installment_form_view')
]
