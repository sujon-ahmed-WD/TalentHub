from djoser.serializers import UserCreateSerializer as BaseCreateSerializer,UserSerializer as BaseUserSerializer

class UserCreateSerializer(BaseCreateSerializer):
    class Meta(BaseCreateSerializer.Meta):
         fields=['id', 'first_name','last_name','email','password','role','phone_number']
         

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
       ref_name='CustomUser'
       fields=['id','email','first_name','last_name','role','phone_number']