from django.shortcuts import render
from .forms import ReportForm, ProblemReportedForm
from .models import Report

# Create your views here.


def report_view(request, production_line):
    form = ReportForm(request.POST or None)
    problem_reported_form = ProblemReportedForm(request.POST or None)
    queryset = Report.objects.filter(production_line__name=production_line)

    r_id = request.POST.get('report_id')
    print(r_id)

    if problem_reported_form.is_valid():
        report = Report.objects.get(id=r_id)
        print('data here')
        obj = problem_reported_form.save(commit=False)
        obj.user = request.user
        obj.report = report
        obj.save()

    context = {
        'form': form,
        'problem_reported_form': problem_reported_form,
        'object_list': queryset,
    }

    return render(request, 'reports/report.html', context)
