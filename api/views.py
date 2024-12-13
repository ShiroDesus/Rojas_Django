
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Post
from .serializers import PostSerializer

@api_view(['GET'])  # Allow only GET requests for this view
def viewsPosts(request):
    posts = Post.objects.all()  # Get all Post objects
    serializer = PostSerializer(posts, many=True) # Serialize the posts, 'many=True' for multiple objects
    return Response(serializer.data)  # Return serialized data in a Response object


@api_view(['GET'])
def viewsPostDetail(request, pk):
    post = Post.objects.get(id=pk)  # Get a specific Post object using its ID
    serializer = PostSerializer(post, many=False)  # Serialize the single post
    return Response(serializer.data)  # Return serialized data in a Response object


@api_view(['POST'])
def addPosts(request):
    serializer = PostSerializer(data=request.data)  # Create a serializer instance with the request data
    if serializer.is_valid():  # Check if the data is valid
        serializer.save()  # Save the new Post object
        return Response(serializer.data)  # Return the serialized data of the newly created post
    return Response(serializer.errors)  # Return errors if data is invalid


@api_view(['POST'])  # You might want to consider using PUT for updates
def updatePosts(request, pk):
    post = Post.objects.get(id=pk)  # Get the existing Post object
    serializer = PostSerializer(instance=post, data=request.data)  # Update the serializer with new data
    if serializer.is_valid():  # Check if the data is valid
        serializer.save()  # Save the updated Post object
        return Response(serializer.data)  # Return the serialized data of the updated post
    return Response(serializer.errors)  # Return errors if data is invalid



@api_view(['DELETE'])
def deletePosts(request, pk):
    post = Post.objects.get(id=pk)  # Get the Post object
    post.delete()  # Delete the Post object
    return Response('Item successfully deleted!')  # Return a success message
