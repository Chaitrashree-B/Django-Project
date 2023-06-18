from django.shortcuts import render
from django.views import View
from .models import Issue

class NewIssueView(View):
    def get(self, request):
        return render(request, 'myapp/new_issue.html')

    def post(self, request):
        user_id = request.POST.get('user_id')
        location = request.POST.get('location')
        problem = request.POST.get('problem')

        issue = Issue.objects.create(userID=user_id, location=location, problem=problem)
        issue.save()

        return render(request, 'myapp/issue_submitted.html', {'issue': issue})
