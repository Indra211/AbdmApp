from django.urls import path,include
from .views import *


urlpatterns =[
    path("P/",PatientList.as_view(),name="students"),
    path('P/<int:pk>/',PatientDetails.as_view(),name='student_details'),
]