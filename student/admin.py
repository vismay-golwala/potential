from django.contrib import admin
from .models import student_info, board, standard, batch, attends, fee_installment, test_model
# Register your models here.
admin.site.register(student_info)
#admin.site.register(attendance)
admin.site.register(board)
admin.site.register(standard)
admin.site.register(batch)
admin.site.register(attends)
admin.site.register(fee_installment)
admin.site.register(test_model)
