from django.shortcuts import render, get_object_or_404
from .forms import student_info_form, batch_form, standard_form, board_form
from .models import student_info, batch, attends
from django.views.generic import View
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect

#Migrated from FBVs to CBVs as CBVs handle get and post logic cleanly
class get_attendance(View):

	def get(self, request):
		return HttpResponse(str(request.method))

	def post(self, request):
		batch = request.POST['batch']
		all_student = student_info.objects.all().filter(batch__batch_id=batch)
		return render(request, "student/student_attendance.html", {"all_student":all_student, "batch_id": batch, "index":1})		

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

class dashboard(View):
	template_name = 'student/dashboard.html'	
	
	def get(self, request):
                return render(request, self.template_name)
	
	def post(self,request):
            pass
        
class attendance(View):
	template_name = 'student/attendance.html'	
	
	def get(self, request):
                batches = batch.objects.all()
                return render(request, self.template_name, {"batch_all":batches })
	
	def post(self,request):
			post = request.POST
			batch_id = post.get('batch_id')
			post._mutable = True
			del post['batch_id']
			del post['csrfmiddlewaretoken']

			for student_id in post:
				attendance = post[student_id]
				obj = student_info.objects.filter(pk=int(student_id))
				query = attends.objects.create(student=obj[0], attends=attendance)
				query.save()

			return HttpResponseRedirect('/dashboard/')
            #form = NameForm(request.POST)
            #if form.is_valid():
                    #return HttpResponse('Getting form data')
                    # student_form = form.save(commit=False)
                    # name = form.cleaned_data['name'] ... ...
                    #form.save()
                    # return HttpResponseRedirect('/success/')

class view_attendance(View):
	pass

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

class batch_form_view(View):
	form_class = batch_form
	template_name = 'student/base_form.html'	
	
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
	template_name = 'student/base_form.html'	
	
	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {"form":form})

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/dashboard/')

class board_form_view(View):
	form_class = board_form
	template_name = 'student/base_form.html'	
	
	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {"form":form})

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/dashboard/')