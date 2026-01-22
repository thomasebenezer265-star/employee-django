from django import forms
 
class EmployeeForm(forms.Form):

    employeename=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    department=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    address=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    