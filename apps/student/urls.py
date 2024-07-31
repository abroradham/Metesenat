from django.urls import path

from apps.student.api.Create.views import StudentCreateView
from apps.student.api.Detail.views import StudentDetailView
from apps.student.api.List.views import StudentListView
from apps.student.api.SponsorShipUpdate.views import StudentSponsorshipUpdateView
from apps.student.api.Update.views import StudentUpdateView



app_name = 'student'
urlpatterns = [
    path('list/', StudentListView.as_view(), name='student-list'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('sponsorship/<int:pk>/', StudentSponsorshipUpdateView.as_view(), name='sponsorship-update'),
]