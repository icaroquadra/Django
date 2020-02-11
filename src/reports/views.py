from django.shortcuts import render
from .forms import ReportForm, ProblemReportedForm
from .models import Report

# Create your views here.


def report_view(request, production_line):
    form = ReportForm()
    problem_reported_form = ProblemReportedForm()
    queryset = Report.objects.filter(production_line__name=production_line)

    context = {
        'form': form,
        'problem_reported_form': problem_reported_form,
        'object_list': queryset,
    }

    return render(request, 'reports/report.html', context)
