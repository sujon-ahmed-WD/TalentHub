from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Job,jobApplication,Review
from.serializers import Jobs_Serializers,jobApplicationSerializers,ReviewSerializers
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter,OrderingFilter
from .permissions import IsAdminOrReadonly,IsEmployerOrApplicant
from rest_framework.decorators import action
from rest_framework.response import Response
from django.conf import settings 
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class JobsViewset(ModelViewSet):
    queryset= Job.objects.all()
    serializer_class= Jobs_Serializers
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=['title','company_name','category__name']
    permission_classes=[IsAdminOrReadonly]
    
    def perform_create(self, serializer):
         serializer.save(employer=self.request.user)
    
    @action(detail=False, methods=['get'])
    def my_jobs(self, request):
            jobs = Job.objects.filter(employer=request.user)
            serializer = self.get_serializer(jobs, many=True)
            return Response(serializer.data)

class  JobApplicationViewset(ModelViewSet):
    # queryset=jobApplication.objects.all()
    serializer_class=jobApplicationSerializers
    permission_classes=[IsEmployerOrApplicant]

    
    def get_queryset(self):
        job_id = self.kwargs.get('job_pk')
        return jobApplication.objects.filter(job_id=job_id)

    @action(detail=False, methods=['get'])
    def my_applications(self, request, *args, **kwargs):
        applications = jobApplication.objects.filter(applicant=request.user)
        serializer = self.get_serializer(applications, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        application = serializer.save(applicant=self.request.user, job_id=self.kwargs.get('job_pk'))

        job = application.job
        job_seeker_email = application.applicant.email
        employer_email = job.employer.email  
        # job saker
        send_mail(
            subject=f"Application Successful for {job.title}",
            message= f"{application.applicant.first_name} {application.applicant.last_name},\n\nYou have successfully applied for the job: {job.title}.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[job_seeker_email],
            fail_silently=False
        )
        # Employee
        send_mail(
            subject=f"New Application Received for {job.title}",
            message=f"Hi {job.employer.first_name} {job.employer.last_name},\n\n{application.applicant.first_name} {application.applicant.last_name} has applied for your job: {job.title}.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[employer_email],
            fail_silently=False
        )
        
        
    
    def perform_update(self,serializer):
        application=self.get_object()
        
        if self.request.user==application.job.employer:
            
            serializer.save()
        
        else:
            if 'status' in serializer.validated_data:
                serializer.validated_data.pop("status")
                serializer.save()
    
    
class ReviewSet(ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializers
    permission_classes=[IsAuthenticated]
    
    # def get_queryset(self):
    #     # শুধু সেই employer এর review দেখাবে যেটার pk URL এ দেওয়া
    #     job_id =self.kwargs.get('job_pk')
    #     if job_id:
    #         return Review.objects.filter(job_id=job_id)
    #     return Review.objects.all()

def perform_create(self, serializer):
    job_id = self.kwargs.get('job_pk')   # URL থেকে job_pk আনো
    job = Job.objects.get(pk=job_id)     # ওই Job object বের করো

    serializer.save(
        job=job,                         # ✅ এখন job assign হলো
        job_seeker=self.request.user,
        employer=job.employer
    )
         
