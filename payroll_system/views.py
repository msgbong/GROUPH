from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from payroll_system.models import Payroll, User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Save user data to the database
            user = User.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                marital_status=form.cleaned_data['marital_status'],
                gender=form.cleaned_data['gender'],
                address=form.cleaned_data['address'],
                nationality=form.cleaned_data['nationality'],
                staff_type=form.cleaned_data['staff_type'],
                bank_account_number=form.cleaned_data['bank_account_number']
            )
            user.save()

            # Redirect the user to the login page
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Get the user inputs from the form
            first_name = form.cleaned_data['first_name']
            marital_status = form.cleaned_data['marital_status']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            nationality = form.cleaned_data['nationality']
            staff_type = form.cleaned_data['staff_type']
            bank_account_number = form.cleaned_data['bank_account_number']
            last_name = form.cleaned_data['last_name']

            # Check if the user exists in the database
            user = authenticate(request, username=first_name,
                                password=bank_account_number)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('welcome')
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'login.html', context)


# @login_required
def welcome(request):
    if request.method == 'POST':
        if 'display_payroll' in request.POST:
            # redirect to display payroll page
            return redirect('display_payroll')
        elif 'compute_payroll' in request.POST:
            # redirect to compute payroll page
            return redirect('compute')
    return render(request, 'welcome.html')


# @login_required
# @user_passes_test(lambda u: u.is_superuser)
def compute(request):
    if request.method == 'POST':
        staff_type = request.POST.get('staff-type')
        basic_salary_ts = request.POST.get('basic-salary-ts')
        housing_allowance_ts = request.POST.get('housing-allowance-ts')
        basic_salary_nts = request.POST.get('basic-salary-nts')
        medical_allowance_nts = request.POST.get('medical-allowance-nts')

        # Compute payroll
        if staff_type == "teaching":
            basic_salary_ts = float(basic_salary_ts)
            housing_allowance_ts = float(housing_allowance_ts)
            gross_pay = basic_salary_ts + housing_allowance_ts
            payee = compute_payee(gross_pay)
            net_pay = gross_pay - payee
            return render(request, 'payroll.html', {
                'staff_type': staff_type,
                'basic_salary_ts': basic_salary_ts,
                'housing_allowance_ts': housing_allowance_ts,
                'gross_pay': gross_pay,
                'payee': payee,
                'net_pay': net_pay
            })
        elif staff_type == "non-teaching":
            basic_salary_nts = float(basic_salary_nts)
            medical_allowance_nts = float(medical_allowance_nts)
            net_pay = basic_salary_nts + medical_allowance_nts
            return render(request, 'payroll.html', {
                'staff_type': staff_type,
                'basic_salary_nts': basic_salary_nts,
                'medical_allowance_nts': medical_allowance_nts,
                'net_pay': net_pay
            })
        else:
            return HttpResponse("Please select a staff type.")
    else:
        return render(request, 'compute.html')


# @login_required
# @user_passes_test(lambda u: u.is_superuser)
def compute_payee(gross_pay):
    if gross_pay <= 30000:
        payee = gross_pay * 0.1
    elif gross_pay <= 100000:
        payee = 3000 + (gross_pay - 30000) * 0.15
    else:
        payee = 13000 + (gross_pay - 100000) * 0.2
    return payee


# @login_required
def display_payroll(request):
    payroll_data = Payroll.objects.all()
    return render(request, 'display_payroll.html', {'payroll_data': payroll_data})
