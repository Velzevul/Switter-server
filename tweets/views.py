# from json import loads
from .models import Tweet, Author
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TweetSerializer, TweetNestedSerializer


@api_view(['GET', 'POST'])
def tweets(request):
    if request.method == 'GET':
        tweets = Tweet.objects.all()
        serializer = TweetNestedSerializer(tweets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
