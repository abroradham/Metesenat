from django import views
from django.urls import path


from apps.sponsor.api.List.views import SponsorListView
from apps.sponsor.api.Dashboard.views import DashboardApiView
from apps.sponsor.api.Register.views import SponsorRegisterView
from apps.sponsor.api.RetrieveUpdate.views import SponsorDetailUpdateview


app_name = 'sponsor'

urlpatterns = [
    path('', DashboardApiView.as_view(), name='dashboard'),
    path('list/', SponsorListView.as_view(), name='list'),
    path('register/', SponsorRegisterView.as_view(), name='register'),
    path('<int:pk>/', SponsorDetailUpdateview.as_view(), name='update')
]