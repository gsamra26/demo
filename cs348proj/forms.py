from django import forms

from .models import Student, Test, MetaTest


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'firstname',
            'lastname',
            'age',
            'grade',
            'teacher',
            'gender'
        ]


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = [
            'sID',
            'score',
            'subject'
        ]


class MetaTestForm(forms.ModelForm):
    class Meta:
        model = MetaTest
        fields = [
            # 'tID',
            'subject'
        ]


class GetDataForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['subject']


class GetStudForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['sID']
