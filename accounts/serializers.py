from django.contrib.auth.models import User
from rest_framework import serializers
from teachme.models import Profile


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"Error": "Password Does not match"})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({"Error": "Email already exist"})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account

class Profile_Serializer(serializers.ModelSerializer):
    saved_courses = serializers.CharField(source='saved_courses.name')
    created_by = serializers.CharField(source='created_by.username')
    # It was used to make string name the pk of course
    # story_post_name = serializers.CharField(source='story_post.story_name')

    class Meta:
        model = Profile
        fields = [
            'created_by', 'first_name', 'last_name', 'saved_courses'
        ]