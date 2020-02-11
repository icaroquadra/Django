from django.shortcuts import render
from .forms import ReportForm, ProblemReportedForm

# Create your views here.

def report_view(request):
    form = ReportForm()
    problem_reported_form = ProblemReportedForm()

    context = {
        'form': form,
        'problem_reported_form': problem_reported_form,
    }

    return render(request, 'reports/report.html', context)