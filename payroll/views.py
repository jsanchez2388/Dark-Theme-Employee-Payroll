from django.shortcuts import render

# Create your views here.

"""
To render HTML web pages
"""
from django import template
from django.http import HttpResponse
from django.template.loader import render_to_string
from models import employee, paystub, admin

def admin_dashboard(request):

    admin_obj = admin.objects.get(id=1)

    context = {
        "user": admin_obj.name
    }
    
    HTML_STRING = render_to_string("admin-view.html", context=context)

    return HttpResponse(HTML_STRING)

def add_employee_view(request):
    context = {}

    if request.method == "POST":
        emp_id = request.POST.get("id") #needs to be updated to auto generate
        emp_fname = request.POST.get("fname")
        emp_minitial = request.POST.get("minitial")
        emp_lname = request.POST.get("lname")
        emp_phone_number = request.POST.get("phone_number")
        emp_dob = request.POST.get("dob")
        emp_ssn = request.POST.get("ssn")
        emp_position = request.POST.get("position")
        emp_wage = request.POST.get("wage")
        emp_st_address = request.POST.get("st_address")
        emp_unit_num = request.POST.get("unit_num")
        emp_city = request.POST.get("city")
        emp_state = request.POST.get("state")
        emp_zipcode = request.POST.get("zipcode")
        emp_username = emp_fname[0] + emp_lname + emp_id
        emp_pw = "default"

        employee.objects.create(ID = emp_id, First_Name = emp_fname, middle_initial = emp_minitial, last_name = emp_lname,
                                phone_number = emp_phone_number, dob = emp_dob, ssn = emp_ssn, position = emp_position, wage = emp_wage,
                                street_address = emp_st_address, unit_number = emp_unit_num, city = emp_city, state = emp_state, 
                                zipcode = emp_zipcode, username = emp_username, password = emp_pw)

        context['created'] = True

    HTML_STRING = render_to_string("add-employee.html", context=context)

    return HttpResponse(HTML_STRING)

def edit_employee_view(request):

    return HttpResponse("add-employee.html")

def paystub_view(request): 

    employee_obj = employee.objects.get(id=1) 
    paystub_obj = paystub.object.get(employee_obj.id)

    context = {
        "name": employee_obj.name,
        "id": employee_obj.id,
        "Date": paystub_obj.date,
        "Pay Period" : paystub_obj.pay_period,
        "Pay Rate" : paystub_obj.pay_rate,
        "Hours Worked" : paystub_obj.hours,
        "Gross Pay" : paystub_obj.gross_pay,
        "Deductions" : paystub_obj.deductions,
        "Net Pay" : paystub_obj.net_pay,
    }
    
    #Django Templates
    HTML_STRING = render_to_string("paystub-view.html", context=context)

    return HttpResponse(HTML_STRING)