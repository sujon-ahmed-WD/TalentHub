from rest_framework import permissions

class IsAdminOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method=="GET":
            return True
        return bool(request.user and request.user.is_staff)
    

# class IsReadApplication(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method==

class IsEmployerOrApplicant(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Employer  
        if obj.job.employer == request.user:
            return True
        # Applicant  
        if obj.applicant == request.user:
            return True
        return False