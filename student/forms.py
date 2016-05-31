from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

from .models import student_info, batch, board, standard, fee_installment, test_model
# Demo Links for using cripsy forms : http://goo.gl/TmPCJb https://godjango.com/29-crispy-forms/

class student_info_form(forms.ModelForm):

        class Meta:
                model = student_info
                fields = ['name', 'batch', 'father_name', 'father_mob', 'mother_name', 'mother_mob',
				'sms_mob', 'school', 'total_fees']
        helper = FormHelper()
        helper.form_method = 'POST'
        helper.form_action = 'student/student/'
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-sm-2'
        helper.field_class = 'col-sm-4'
        helper.disable_csrf = False
        helper.layout = Layout(
		Field('name', css_class='form-input', placeholder='Enter name'),
		Field('batch', css_class='form-input'),
		Field('school', css_class='form-input', placeholder='Enter school'),		
		Field('father_name', css_class='form-input', placeholder='Enter father\'s name'),
		Field('father_mob', css_class='form-input', placeholder='Enter father\'s mobile'),
		Field('mother_name', css_class='form-input', placeholder='Enter mother\'s name'),
		Field('mother_mob', css_class='form-input', placeholder='Enter mother\'s mobile'),
		Field('sms_mob', css_class='form-input', placeholder='Enter mobile for sms registration'),
		Field('total_fees', css_class='form-input', placeholder='Enter total fees'),
		FormActions(Submit('Save', 'Save', css_class='btn-primary'))
    )

class edit_full_student(forms.ModelForm):

    class Meta:
        model = student_info
        fields = ['name', 'batch', 'father_name', 'father_mob', 'mother_name', 'mother_mob',
                'sms_mob', 'school', 'total_fees']
        helper = FormHelper()
        helper.form_method = 'POST'
        helper.form_action = 'student/student/'
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-sm-2'
        helper.field_class = 'col-sm-4'
        helper.disable_csrf = False
        helper.layout = Layout(
        Field('name', css_class='form-input', placeholder='Enter name'),
        Field('batch', css_class='form-input'),
        Field('school', css_class='form-input', placeholder='Enter school'),      
        Field('father_name', css_class='form-input', placeholder='Enter father\'s name'),
        Field('father_mob', css_class='form-input', placeholder='Enter father\'s mobile'),
        Field('mother_name', css_class='form-input', placeholder='Enter mother\'s name'),
        Field('mother_mob', css_class='form-input', placeholder='Enter mother\'s mobile'),
        Field('sms_mob', css_class='form-input', placeholder='Enter mobile for sms registration'),
        Field('total_fees', css_class='form-input', placeholder='Enter total fees'),
        FormActions(Submit('Save', 'Save', css_class='btn-primary'))
    )

class batch_form(forms.ModelForm):

        class Meta:
                model = batch
                fields = ['batch_std', 'batch_board']
        helper = FormHelper()
        helper.form_method = 'POST'
        helper.form_action = 'student/batch/'
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-sm-2'
        helper.field_class = 'col-sm-4'
        helper.disable_csrf = False
        helper.layout = Layout(
		Field('batch_std', css_class='form-input'),
		Field('batch_board', css_class='form-input'),
		FormActions(Submit('Save', 'Save', css_class='btn-primary'))
    )

class standard_form(forms.ModelForm):

        class Meta:
                model = standard
                fields = ['standard']
        helper = FormHelper()
        helper.form_method = 'POST'
        helper.form_action = 'student/standard/'
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-sm-2'
        helper.field_class = 'col-sm-4'
        helper.disable_csrf = False
        helper.layout = Layout(
		Field('standard', css_class='form-input', placeholder='Enter Standard'),
		FormActions(Submit('Save', 'Save', css_class='btn-primary'))
    )

class board_form(forms.ModelForm):

        class Meta:
                model = board
                fields = ['board']
        helper = FormHelper()
        helper.form_method = 'POST'
        helper.form_action = 'student/board/'
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-sm-2'
        helper.field_class = 'col-sm-4'
        helper.disable_csrf = False
        helper.layout = Layout(
		Field('board', css_class='form-input', placeholder='Enter Board'),
		FormActions(Submit('Save', 'Save', css_class='btn-primary'))
    )


class fee_form(forms.ModelForm):

        class Meta:
                model = fee_installment
                fields = ['batch','student', 'date', 'amount']

        helper = FormHelper()
        helper.form_method = 'POST'
        helper.form_action = 'student/fee/'
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-sm-2'
        helper.field_class = 'col-sm-4'
        helper.disable_csrf = False
        helper.layout = Layout(
		Field('batch', css_class='input-sm'),
                Field('student', css_class='input-sm'),
                Field('date', css_class='input-sm', type='date'),
                Field('amount', css_class='input-sm'),
		FormActions(Submit('Save', 'Save', css_class='btn-primary'))
    )

class fee_installment_form(forms.ModelForm):

        class Meta:
                model = fee_installment
                fields = ['batch','student']

        helper = FormHelper()
        helper.form_method = 'POST'
        helper.form_action = 'student/view_fees/'
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-sm-2'
        helper.field_class = 'col-sm-4'
        helper.disable_csrf = False
        helper.layout = Layout(
        Field('batch', css_class='input-sm'),
                Field('student', css_class='input-sm'),
        FormActions(Submit('View', 'View', css_class='btn-primary'))
    )

class user_form (forms.ModelForm):
	password = forms.CharField (widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'password']

        helper = FormHelper()
        helper.form_method = 'POST'
        #helper.form_action = 'student/login/'
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-sm-2'
        helper.field_class = 'col-sm-4'
        helper.disable_csrf = False
        helper.layout = Layout(
        Field('username', css_class='input-sm'),
        Field('password', css_class='input-sm'),
        FormActions(Submit('Login', 'Login', css_class='btn-primary'))
    )