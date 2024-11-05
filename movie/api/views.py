from django.shortcuts import redirect, get_object_or_404

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from movie.models import Movie, Rating, Report
from .serializers import MovieSerializer, RatingSerializer, ReportSerializer
from .permissions import IsOwnerOrReadOnly

# Movie Views
class MovieListView(generics.ListAPIView):
    """
    API endpoint that allows users to view all movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = []

    @extend_schema(  
        summary='Retrieve a list of movies',  
        description='This endpoint allows users to retrieve a list of all available movies in the system. The response includes details such as title, description, release date, and average rating.',
        responses={
            200: MovieSerializer(many=True),  
        },
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class MovieCreateView(generics.CreateAPIView):
    """
    API endpoint that allows users to create movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='Create a Movie',  
        description='This endpoint allows users to create a movie. In order to create a movie, the user must login to the Movie Management System',
        responses={
            200: MovieSerializer(many=True),  
        },
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        summary='Create a Movie',
        description='This endpoint allows users to create a movie. In order to create a movie, the user must login to the Movie Management System',
        responses={
            200: MovieSerializer(many=True),  
        },
    )
    
    def post(self, requset, *args, **kwargs):
        return super().post(requset, *args, **kwargs)

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to view, update, or delete a specific movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    @extend_schema(
        summary="Retrieve a specific movie",
        description="Retrieve details of a specific movie by providing the movie's ID.",
        responses={200: MovieSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Update a specific movie",
        description="Update the details of a specific movie. Only authenticated users can update movie information.",
        request=MovieSerializer,
        responses={200: MovieSerializer, 400: "Bad Request", 403: "Forbidden"}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Partial update of a specific movie",
        description="Partially update the details of a specific movie. Only authenticated users can perform this action.",
        request=MovieSerializer,
        responses={200: MovieSerializer, 400: "Bad Request", 403: "Forbidden"}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        summary="Delete a specific movie",
        description="Delete a specific movie by providing the movie's ID. Only authenticated users can delete movies.",
        responses={204: "No Content", 403: "Forbidden", 404: "Not Found"}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

# Rating Views
class MovieRatingListView(generics.ListAPIView):
    """
    API endpoint that allows users to view all ratings for a specific movie.
    """
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Rating.objects.filter(movie_id=pk)

    @extend_schema(
        summary="Retrive a list of specific movie rating",
        description="Retrieve a specific movie rating by providing the movie's ID. Only authenticated users can see the movie rating.",
        responses={204: "No Content", 403: "Forbidden", 404: "Not Found"}
    )
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
class MovieRatingCreateView(generics.CreateAPIView):
    """
    API endpoint that allows users to create a new rating for a specific movie.
    """
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        user = self.request.user
        movie_id = self.kwargs['pk']
        movie = Movie.objects.get(pk=movie_id)

        rating_user = Rating.objects.filter(user=user, movie=movie)
        if rating_user.exists():
            raise ValidationError('You have already rated this movie')
    
        serializer.save(user=user, movie=movie)
    
    @extend_schema(
            summary="Create a new rating for a specific movie",
            description="Create a new rating for a specific movie by providing the movie's ID. Only authenticated users can create a new rating for a movie.",
            responses={204:"No Content", 400:"Bad Request"}
    )
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

    
class MovieRatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to view a specific movie rating.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    @extend_schema(
        summary="Retrieve a specific movie rating",
        description="Retrieve a specific movie rating by providing the movie's ID and rating's ID. Only authenticated users can see the movie rating.",
        responses={204: "No Content", 403: "Forbidden", 404: "Not Found"}
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Update a specific movie rating",
        description="Update the details of a specific movie. Only authenticated users can update movie information.",
        request=MovieSerializer,
        responses={200: MovieSerializer, 400: "Bad Request", 403: "Forbidden"}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Partial update of a specific movie rating",
        description="Partially update the details of a specific movie. Only authenticated users can perform this action.",
        request=MovieSerializer,
        responses={200: MovieSerializer, 400: "Bad Request", 403: "Forbidden"}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
        summary="Delete a specific movie rating",
        description="Delete a specific movie rating by providing the movie's ID and rating's ID. Only authenticated users can delete a movie rating.",
        responses={204: "No Content", 403: "Forbidden", 404: "Not Found"}
    )

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Report Views
class MovieReportListView(generics.ListAPIView):
    """
    API endpoint that allows users to view all reports for a specific movie.
    """
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        user = self.request.user
        return Report.objects.filter(user=user, movie_id=pk)
    
    @extend_schema(
        summary="Retrive a list of specific movie report",
        description="Retrieve a specific movie report by providing the movie's ID and logged in user. Only authenticated users with admin privileges can see the movie report.",
        responses={204: "No Content", 403: "Forbidden", 404: "Not Found"}
    )
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class MovieReportCreateView(generics.CreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
        
    def perform_create(self, serializer):
        movie_id = self.kwargs['pk']
        user = self.request.user

        movie = Movie.objects.get(id=movie_id)
        report = Report.objects.filter(user=user, movie=movie)

        if report.exists():
            raise ValidationError('You have already reported this movie')

        serializer.save(user=user, movie=movie)
    
    @extend_schema(
        summary="Create a new report for a particular movie.",
        description="Create a new report for a specific movie and the reason for reporting this movie. Only authenticated users with admin privileges can create a new report for a movie.",
        responses={204:"No Content", 400:"Bad Request"}
    )
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    
class MovieReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to view a specific movie report.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    @extend_schema(
        summary="Retrieve a specific movie report",
        description="Retrieve a specific movie report by providing the movie's ID and report's ID. Only authenticated users with admin privileges can see the movie report.",
        responses={204: "No Content", 403: "Forbidden", 404: "Not Found"}
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        summary="Update a specific movie report",
        description="Update the details of a specific movie report. Only authenticated users with admin privileges can perform this action.",
        request=ReportSerializer,
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(
        summary="Partial update of a specific movie report",
        description="Partially update the details of a specific movie report. Only authenticated users with admin privileges can perform this action.",
        request=ReportSerializer,
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
        summary="Delete a specific movie report",
        description="Delete a specific movie report by providing the movie's ID and report's ID. Only authenticated users with admin privileges can delete a movie report.",
        responses={204: "No Content", 403: "Forbidden", 404: "Not Found"}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Admin reports views

class AdminReportListView(generics.ListAPIView):
    """
    API endpoint that allows administrators to view all reports.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser] 

    @extend_schema(
        summary="Retrieve a list of all reports",
        description="Retrieve a list of all reports. Only administrators can see the list of reports.",
        responses={204: "No Content", 403: "Forbidden"}
    )
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AdminReportApprove(generics.UpdateAPIView):
    """
    API endpoint that allows administrators to approve a specific report.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser]
    def update(self, *args, **kwargs):
        report = self.get_object()

        if report.approved:
            raise ValidationError('Report is already approved')
        
        report.approved = True
        report.rejected = False
        report.save()

        serializer = self.get_serializer(report)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        summary="Approve a specific report for a specific user and movie.",
        description="Approve a specific report by providing the report's ID. Only administrators can approve a report.",
        responses={200: "No Content", 400: "Bad Request", 404: "Not Found"}
    )

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(
        summary="Approve a specific report for a specific user and movie.",
        description="Approve a specific report by providing the report's ID. Only administrators can approve a report.",
        responses={200: "No Content", 400: "Bad Request", 404: "Not Found"}
    )

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    

class AdminReportReject(generics.UpdateAPIView):
    """
    API endpoint that allows administrators to reject a specific report.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser]

    def update(self, *args, **kwargs):
        report = self.get_object()

        if report.rejected:
            raise ValidationError('Report is already rejected')
        
        report.rejected = True
        report.approved = False
        report.save()

        serializer = self.get_serializer(report)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        summary="Reject a specific report for a specific user and movie.",
        description="Reject a specific report by providing the report's ID. Only administrators can reject a report.",
        responses={200: "No Content", 400: "Bad Request", 404: "Not Found"}
    )
    
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(
        summary="Reject a specific report for a specific user and movie.",
        description="Reject a specific report by providing the report's ID. Only administrators can reject a report.",
        responses={200: "No Content", 400: "Bad Request", 404: "Not Found"}
    )
    
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class AdminReportStatusView(APIView):
    """
    API endpoint that allows users to view their own report status.
    """
    permission_classes = [IsAdminUser]

    def get(self, request):
        report_approved_count = Report.objects.filter(approved=True).count()
        report_rejected_count = Report.objects.filter(rejected=True).count()

        return Response({
            'approved_count': report_approved_count,
            'rejected_count': report_rejected_count
            }, status=status.HTTP_200_OK
        )
    
    @extend_schema(
        summary="Retrieve a report status",
        description="Retrieve the number of approved and rejected reports for the authenticated user. Only administrators can see this information.",
        responses={200: "No Content", 403: "Forbidden"}
    )
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)