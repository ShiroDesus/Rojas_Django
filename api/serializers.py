from rest_framework import serializers
from blog.models import Post  # Assuming your Post model is in blog.models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # Or specify the fields you want: ['title', 'content']
