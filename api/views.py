from json import loads
from .models import Tweet, Author
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TweetSerializer, TweetNestedSerializer, AuthorSerializer


@api_view(['GET', 'POST'])
def tweets(request):
    def ensure_author(author_data):
        try:
            author = Author.objects.get(pk=author_data['screen_name'])
        except Author.DoesNotExist:
            author = Author.objects.create(**author_data)
        return author

    if request.method == 'GET':
        tweets = Tweet.objects.all()
        serializer = TweetNestedSerializer(tweets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # request.data is assumed to be passed as a string,
        # e.g. {'tweet': JSON.stringify(tweet))}
        data = loads(request.data['tweet'])

        # make sure author exists & substitute
        author_data = data.pop('author')
        author = ensure_author(author_data)
        data['author'] = author.screen_name

        # make sure retweet authors exist & substitute
        if 'retweeted_by' in data.keys():
            retweet_authors_data = data.pop('retweeted_by')
            data['retweeted_by'] = [ensure_author(a).screen_name for a in retweet_authors_data]

        # replace retweeted_status with its id
        if 'retweeted_status' in data.keys():
            data['retweeted_status'] = data['retweeted_status']['id']

        serializer = TweetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def tweet(request, id):
    try:
        tweet = Tweet.objects.get(pk=id)
        serializer = TweetNestedSerializer(tweet)
        return Response(serializer.data)
    except Tweet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users = Author.objects.all()
        serializer = AuthorSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # request.data is assumed to be passed as a string,
        # e.g. {'user': JSON.stringify(user))}
        user_data = loads(request.data['user'])

        serializer = AuthorSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user(request, screen_name):
    try:
        user = Author.objects.get(pk=screen_name)
        serializer = AuthorSerializer(user)
        return Response(serializer.data)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
