from django.urls import path
from myapp.views import NewIssueView

urlpatterns = [
    # Other URL patterns...
    path('new_issue/', NewIssueView.as_view(), name='new_issue'),
]
