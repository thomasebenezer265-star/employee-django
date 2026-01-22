from django.shortcuts import render,redirect

from django.views.generic import View

from members.forms import EmployeeForm

from members.models import Employee

class EmployeeCreateView(View):

    def get(self,request,*args, **kwargs):

        form_instance=EmployeeForm()

        return render(request,"empl_create.html",{"form":form_instance})

    def post(self,request,*args, **kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Employee.objects.create(**data)

            return redirect("empl-list")
        
        else:

            return render(request,"empl_create.html",{"form":form_instance})
class EmployeeListView(View):
    def get(self,request,*args, **kwargs):
        
        qs=Employee.objects.all()
        
        return render(request,'empl_list.html',{"data":qs})     
class EmployeeDetailView(View):

    def get(self,request,*args, **kwargs):

        form_instance=EmployeeForm()

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id)

        return render (request,"empl_details.html",{"data":qs})

class EmployeeDeleteView(View):

    def get(self,request,*args, **kwargs):

        id=kwargs.get("pk")

        Employee.objects.get(id=id).delete()

        return redirect("empl-list") 
class EmployeeUpdateView(View):

    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")

        employee_object=Employee.objects.get(id=id)

        dictionary={

            "employeename":employee_object.employeename,

            "department":employee_object.department,

            "age":employee_object.age,

            "address":employee_object.address,

          

            # "producer":student_object.producer
        }

        form_instance=EmployeeForm(initial=dictionary)
        return render(request,"empl_edit.html",{"form":form_instance})
    

    def post(self,request,*args, **kwargs):

        form_instance=EmployeeForm(request.POST)

        id=kwargs.get("pk")

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Employee.objects.filter(id=id).update(**data)

            return redirect("empl-list")

        else:

            return render(request,"empl_edit.html",{"form":form_instance})   
