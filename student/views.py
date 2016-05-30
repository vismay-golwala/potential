from django.shortcuts import render, get_object_or_404, redirect
from .forms import student_info_form, batch_form, standard_form, board_form
from .models import student_info, batch, attends, board, standard
from django.forms import modelformset_factory
from .forms import student_info_form, batch_form, standard_form, board_form, fee_form, user_form
from .models import student_info, batch, attends, test_model
from django.views.generic import View
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


#Migrated from FBVs to CBVs as CBVs handle get and post logic cleanly
#----DASHBOARD----
class dashboard(View):
	template_name = 'student/dashboard.html'	
	
	def get(self, request):
		if request.user.is_authenticated():
			return render(request, self.template_name)
		else:
			return HttpResponse("You need to login first")
	
	def post(self,request):
		pass

#----ATTENDANCE----
class attendance(View):
	template_name = 'student/attendance.html'	
	
	def get(self, request):
                batches = batch.objects.all()
                return render(request, self.template_name, {"batch_all":batches })
	
	def post(self,request):
			post = request.POST
			batch_id = post.get('batch_id')
			attendance_date = post.get('attendance_date')
			date = datetime.datetime.strptime(attendance_date, "%Y-%m-%d").date()
			post._mutable = True
			del post['batch_id']
			del post['attendance_date']
			del post['csrfmiddlewaretoken']

			for student_id in post:
				attendance = post[student_id]
				obj = student_info.objects.filter(pk=int(student_id))
				batch_obj = batch.objects.filter(batch_id=batch_id)
				check_obj = attends.objects.filter(student=obj[0], batch=batch_obj[0], attendance_date=date)
				if check_obj.exists():
					check_obj.update(attends=attendance)
				else:
					query = attends.objects.create(student=obj[0], batch=batch_obj[0], attends=attendance, attendance_date = date)
					query.save()

			return HttpResponseRedirect('/dashboard/')
            #form = NameForm(request.POST)
            #if form.is_valid():
                    #return HttpResponse('Getting form data')
                    # student_form = form.save(commit=False)
                    # name = form.cleaned_data['name'] ... ...
                    #form.save()
                    # return HttpResponseRedirect('/success/')

class get_attendance(View):

	def get(self, request):
		return HttpResponse(str(request.method))

	def post(self, request):
		batch = request.POST.get('batch')
		attendance_date = request.POST.get('attendance_date')
		date = datetime.datetime.strptime(attendance_date, "%Y-%m-%d").date()

		attendance = attends.objects.filter(attendance_date = date, batch__batch_id=batch)

		# column__field is used when using foreign key, we want to access column of another table
		# In this example, we are accessing batch_id of batch object which is a foreign key
		if attendance.exists():
			return render(request, "student/student_attendance_edit.html", {"attendance_all": attendance, "batch_id": batch, "attendance_date": attendance_date})
		else:
			student_all = student_info.objects.all().filter(batch__batch_id=batch)
			return render(request, "student/student_attendance_insert.html", {"student_all": student_all, "batch_id": batch, "attendance_date": attendance_date})		

class view_attendance(View):
	template_name = 'student/view_attendance.html'	
	
	def get(self, request):
		batches = batch.objects.all()
		return render(request, self.template_name, {"batch_all":batches })
	
	def post(self,request):
		batch_id = request.POST.get('batch')
		attendance_month = request.POST.get('attendance_month')
		
		all_students = student_info.objects.all().filter(batch=batch.objects.filter(batch_id=batch_id)).order_by('-name')
		days = attends.objects.all().filter(attendance_date__contains=attendance_month, batch__batch_id=batch_id).order_by('attendance_date').values_list('attendance_date', flat=True).distinct()
		
		attendance = {}
		for student in all_students:
			name = student.name
			attendance[name] = {}
			attendance[name]['data'] = []
			present = 0
			absent = 0
			none = 0
			for day in days:
				attend_obj = attends.objects.filter(student= student, batch__batch_id = batch_id, attendance_date=day)
				if attend_obj.exists():
					temp_obj = attends.objects.get(student= student, batch__batch_id = batch_id, attendance_date=day)
					attendance[name]['data'].append(temp_obj)
					if temp_obj.attends == "1":
						present += 1
					else:
						absent += 1
				else:
					attendance[name]['data'].append("-")
					none += 1

			attendance[name]['present'] = present
			attendance[name]['absent'] = absent
			attendance[name]['none'] = none
			attendance[name]['total'] = present+absent+none
		
		return render(request, 'student/view_attendance_result.html', {"attendance": attendance, "days": days})

#----STUDENT----
class student_info_form_view(View):
	form_class = student_info_form
	template_name = 'student/base_form.html'	
	
	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {"form":form})
	
	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			# student_form = form.save(commit=False)
			# name = form.cleaned_data['name'] ... ...
			# No need to get form elements (like above), django automatically handles them.
			# In case you need to alter form elements you can explicitly retrieve them using
			# above. Cases like: login validation.
			form.save()
            		# return HttpResponseRedirect('/success/')
			return HttpResponseRedirect('/dashboard/')
		return render(request, self.template_name, {"form":form})

class edit_student(View):
	template_name = 'student/edit_student.html'

	def get(self,request):
		students = student_info.objects.all()
		batches = batch.objects.all()
		return render(request, self.template_name, {'students': students, 'batches': batches})

	def post(self,request):
		pass

class update_cell(View):
	
	def get(self, request):
		pass

	def post(self, request):
		record = request.POST['cell']
		data = request.POST['data']
		myArray = record.split('@')
		col = myArray[0]
		row = myArray[1]
		# Using **args, we can pass dynamic column name which is not normally passed
		args = { col: data }
		student_info.objects.filter(pk=row).update(**args)
		return HttpResponse()

class edit_full_student(UpdateView):
	model = student_info
	fields = ['name','batch','father_name','father_mob','mother_name','mother_mob','sms_mob','school','total_fees']
	template_name = 'student/edit_full_student.html'

	def get_success_url(self):
		return '/dashboard/'

class delete_student(View):

	def get(self, request):
		pass

	def post(self, request):
		key = request.POST['key']
		d = student_info.objects.filter(pk=key)
		d.delete()
		return HttpResponse()

#----BATCH----
class batch_form_view(View):
	form_class = batch_form
	template_name = 'student/batch.html'	
	
	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {"form":form})

	def post(self,request):
		form = self.form_class(request.POST)		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/dashboard/')

class standard_form_view(View):
	form_class = standard_form
	template_name = 'student/standard.html'	
	
	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {"form":form})

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/dashboard/')
		else:
			return render(request, self.template_name, {"form":form})

class board_form_view(View):
	form_class = board_form
	template_name = 'student/board.html'	
	
	def get(self, request):
		form = self.form_class
		board_all = board.objects.all().order_by('board')
		return render(request, self.template_name, {"form":form, "board_all": board_all})

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/dashboard/')


class fee_form_view(View):
	form_class = fee_form
	template_name = 'student/base_form.html'

	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {"form":form})

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/dashboard/')
		else:
			return HttpResponse("Failure")

#test module approach as same as attendance module
class test_model_form_view(View):
	template_name = 'student/test_model.html'

	def get(self, request):
		all_batch = batch.objects.all()
		return render(request, self.template_name, {"batch_all":all_batch})

	def post(self,request):
			post = request.POST
			test_date = post.get('test_date')
			date = datetime.datetime.strptime(test_date, "%Y-%m-%d").date()
			test_out_of = post.get('test_out_of')
			test_topic = post.get('test_topic')
			batch_obj = batch.objects.filter(batch_id=str(post.get('test_batch')))
			post._mutable = True
			del post['test_date']
			del post['test_out_of']
			del post['test_topic']
			del post['test_batch']
			del post['csrfmiddlewaretoken']

			for student_id in post:
				mark = post[student_id]
				student_obj = student_info.objects.filter(pk=int(student_id))
				query = test_model.objects.create(student=student_obj[0],
												batch=batch_obj[0],
												date=date,
												topic=test_topic,
												out_of=test_out_of,
												obtained=mark)
				query.save()

			return HttpResponseRedirect('/dashboard/')

def get_test_students(request):
	if (request.method == "POST"):
		batch = request.POST['batch']
		all_student = student_info.objects.all().filter(batch__batch_id=batch)
		return render(request, "student/student_test.html", {"all_student":all_student, "batch_id": batch, "index":0})
	else:
		return HttpResponse(str(request.method))


class login_view(View):
	form_class = user_form
	template_name = 'student/base_form.html'

	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {"form":form})

	def post(self,request):
		form = self.form_class(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/dashboard/')
		else:
			return HttpResponse("Invalid authorization")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('https://www.google.com')