from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self,request,view,obj,):
        #allow read-only permission for all users
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #Allow Write permissions for authors of posts
        return obj.author == request.user
        
