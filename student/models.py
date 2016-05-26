from __future__ import unicode_literals
from django.db import models
import datetime
# Create your models here.

class standard(models.Model):
    standard = models.CharField(max_length = 10)

    def __str__(self):
        return self.standard

class board(models.Model):
    board = models.CharField(max_length = 10)

    def __str__(self):
        return self.board

class batch (models.Model):
    batch_std = models.ForeignKey(standard, on_delete=models.CASCADE)
    batch_board = models.ForeignKey(board, on_delete=models.CASCADE)

    # UI should not get this field as an input. It's auto-generated.
    batch_id = models.CharField (max_length = 30, blank=True)

    def save(self, *args, **kwargs):

        #TODO: Write code here to handle multiple batches of same standard and board.

        self.batch_id = str(self.batch_std) + '-' + str(self.batch_board)
        return super(batch, self).save(*args, **kwargs)
        
        
    def __str__(self):
        return str (self.batch_id)
    
class student_info (models.Model):
    
    name = models.CharField (max_length = 100)
    batch = models.ForeignKey (batch, on_delete = models.SET_DEFAULT, default = "NA")
    father_name = models.CharField (max_length = 100)  
    father_mob = models.CharField (max_length = 15)
    mother_name = models.CharField (max_length = 100)
    mother_mob = models.CharField (max_length = 15)
    sms_mob = models.CharField (max_length = 12, default = None)
    school = models.CharField (max_length = 100)
    total_fees = models.CharField (max_length = 100)

    def __str__(self):
        return str (self.name) + " (" + str (self.batch) + ")"


class attends (models.Model):

    student = models.ForeignKey (student_info, on_delete = models.CASCADE)
    batch = models.ForeignKey (batch, on_delete = models.CASCADE, null=True)

    #attends - choice ?
    attends = models.CharField (max_length = 100, default = "NA")
    attendance_date = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        if self.attends == '1':
            attendance = "Present"
        else:
            attendance = "Absent"

        return str (self.student) + " - " + str (attendance)

