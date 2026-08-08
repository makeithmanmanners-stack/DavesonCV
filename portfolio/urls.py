from django.urls import path
from .views import HomeView, WebResumeView, DownloadResumeView, ContactFormApiView, SystemStatusApiView

app_name = 'portfolio'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('resume/', WebResumeView.as_view(), name='web_resume'),
    path('resume/download/', DownloadResumeView.as_view(), name='download_resume'),
    path('api/contact/', ContactFormApiView.as_view(), name='api_contact'),
    path('api/status/', SystemStatusApiView.as_view(), name='api_status'),
]
