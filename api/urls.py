from django.urls import path,include
from Jobs.views import JobsViewset,JobApplicationViewset,ReviewSet
from rest_framework_nested import routers

router=routers.DefaultRouter()
router.register('jobs',JobsViewset,basename='jobs')
# router.register('application',JobApplicationViewset,basename='JobApplication')

job_router=routers.NestedDefaultRouter(router,'jobs',lookup='job')
job_router.register('apply',JobApplicationViewset,basename='applications')
job_router.register('review',ReviewSet,basename='review')

urlpatterns = [
     path('',include(router.urls)),
     path('',include(job_router.urls)),
     path('auth/', include('djoser.urls')),
     path('auth/', include('djoser.urls.jwt'))
]
