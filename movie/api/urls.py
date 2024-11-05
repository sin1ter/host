from django.urls import path
from .views import ( MovieListView, MovieCreateView, MovieDetailView, 
                    MovieRatingListView, MovieRatingCreateView, MovieRatingDetailView,
                    MovieReportListView, MovieReportCreateView, MovieReportDetailView, 
                    AdminReportListView, AdminReportApprove, AdminReportReject, AdminReportStatusView) 

urlpatterns = [
    # Movie URLs / Endpoints
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movie-create/', MovieCreateView.as_view(), name='movie-create'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),

    # Movie Rating URLs / Endpoints
    path('<int:pk>/rating/', MovieRatingListView.as_view(), name='movie-rating'),
    path('<int:pk>/rating-create/', MovieRatingCreateView.as_view(), name='rating-create'),
    path('rating/<int:pk>/', MovieRatingDetailView.as_view(), name='movie-rating'),

    # Movie Report URLs/ Endpoints 
    path('<int:pk>/report/', MovieReportListView.as_view(), name='movie-report'),
    path('<int:pk>/report-create/', MovieReportCreateView.as_view(), name='movie-report-create'),
    path('report/<int:pk>/', MovieReportDetailView.as_view(), name='movie-report-detail'),

    # Admin Report View URL/ Endpoints
    path('admin-report/', AdminReportListView.as_view(), name='admin-report'),
    path('report-approve/<int:pk>/', AdminReportApprove.as_view(), name='admin-report-approve'),
    path('report-reject/<int:pk>/', AdminReportReject.as_view(), name='admin-report-reject'),
    path('report-status/', AdminReportStatusView.as_view(), name='admin-report-status'),
]
