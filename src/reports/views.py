from django.shortcuts import render, get_object_or_404
from .forms import ReportForm, ProblemReportedForm
from .models import Report
from production_line.models import ProductionLine

# Create your views here.


def report_view(request, production_line):
    production_report_form = ReportForm(request.POST or None)
    problem_reported_form = ProblemReportedForm(request.POST or None)
    queryset = Report.objects.filter(production_line__name=production_line)

    if 'submit-report-problem-btn' in request.POST:
        r_id = request.POST.get('report_id')
        print(r_id)

        if problem_reported_form.is_valid():
            report = Report.objects.get(id=r_id)
            print('data here')
            obj = problem_reported_form.save(commit=False)
            obj.user = request.user
            obj.report = report
            obj.save()
            production_report_form = ReportForm()
            problem_reported_form = ProblemReportedForm()

    if 'submit-production-report-btn' in request.POST:
        if production_report_form.is_valid():
            line = get_object_or_404(ProductionLine, name=production_line)
            obj = production_report_form.save(commit=False)
            obj.user = request.user
            obj.production_line = line
            obj.save()
            production_report_form = ReportForm()
            problem_reported_form = ProblemReportedForm()

    context = {
        'production_report_form': production_report_form,
        'problem_reported_form': problem_reported_form,
        'object_list': queryset,
    }

    return render(request, 'reports/report.html', context)
