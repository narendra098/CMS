from django.db import models

# Create your models here.
class Report(models.Model):
    location = models.CharField(max_length=100)
    Incident_Dept = models.CharField(max_length=100)
    dateandtime = models.DateTimeField(blank=True, null=True, default='')
    incident_location = models.TextField(max_length=500)
    suspected_cause = models.TextField(max_length=500)
    immediate_action_taken = models.TextField(max_length=500)
    reported_by =  models.CharField(max_length=20, default='username')

    def __str__(self):
        return self.reported_by
