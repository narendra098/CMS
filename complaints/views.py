from django.shortcuts import render
from django.contrib import messages

from .models import Report

def report(request):
    return render(request,'report.html')

def post(request):
    if request.method=='POST':
        location = request.POST.get('location')
        incident_department=request.POST.get('incident_dept')
        dateandtime=request.POST.get('dateandtime')
        incident_location = request.POST.get('incident_location')
        suspected_cause = request.POST.get('suspected_cause')
        immediate_action_taken = request.POST.get('immediate_action_taken')
        reported_by = request.POST.get('reported_by')
        save_report = Report(reported_by=reported_by,location=location,Incident_Dept=incident_department,dateandtime=dateandtime,incident_location=incident_location,suspected_cause=suspected_cause,immediate_action_taken=immediate_action_taken)
        save_report.save()
        messages.info(request,'successfully submitted')
    return  render(request,'index.html')





