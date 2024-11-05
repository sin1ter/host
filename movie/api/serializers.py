from rest_framework import serializers

from movie.models import Movie, Rating, Report
from accounts.api.serializers import UserSerializer


class MovieSerializer(serializers.ModelSerializer):
    
    average_rating = serializers.SerializerMethodField()
    total_ratings = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
             'title', 'description', 'released_at', 
            'duration_hours', 'duration_minutes', 'duration_seconds', 
            'genre', 'created_by', 'language', 'average_rating', 'total_ratings'
        ]

    def get_average_rating(self, obj):
        return obj.average_rating()

    def get_total_ratings(self, obj):
        return obj.total_ratings()

    

class RatingSerializer(serializers.ModelSerializer):

    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ['user', 'movie', 'rating', 'created_at']


class ReportSerializer(serializers.ModelSerializer):

    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Report
        fields = ['user', 'movie', 'reason']
