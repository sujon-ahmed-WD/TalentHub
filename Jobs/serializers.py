from rest_framework import serializers
from Jobs.models import Job,jobApplication,Category,Review

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name']
        
class Jobs_Serializers(serializers.ModelSerializer):
    applications_count=serializers.SerializerMethodField()
    # count=serializers.IntegerField(read_only=True,help_text="`Return the number`")
    category=CategorySerializers(read_only=True)
    class Meta:
     model=Job
     fields=['id','title','requirements','description','location','published_date','applications_count','category']
        
    def  get_applications_count(self,obj):
        return jobApplication.objects.filter(job=obj).count()

        

class jobApplicationSerializers(serializers.ModelSerializer):
    Designation=serializers.CharField(source='job.title',read_only=True)
    class Meta:
        model = jobApplication
        fields = '__all__'
        read_only_fields = ['Designation', 'applied_at','resume']  # শুধু applied_at read-only
        
        def create(self, validated_data):
            validated_data['status'] = 'pending'   
            return super().create(validated_data)
        
class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields = ['id','job_seeker', 'rating', 'comment', 'created_at']
        read_only_fields = ['job_seeker', 'created_at']
        