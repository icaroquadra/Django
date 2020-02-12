from django import forms
from .models import Report, ProblemReported


class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        exclude = ('user', 'production_line',)


class ProblemReportedForm(forms.ModelForm):

    class Meta:
        model = ProblemReported
        # fields = '__all__'
        exclude = ('user', 'report',)
