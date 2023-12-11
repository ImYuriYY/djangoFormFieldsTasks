from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

def index(request):
    return render(request, 'deliveryform/index.html')


def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNum = request.POST.get('phoneNum')
        selectServ = request.POST.get('selectServ')
        userComment = request.POST.get('userComment')
        return HttpResponse(f'User Name: {name}<br>Email: {email}<br>Phone number: {phoneNum}<br> Service: {selectServ}<br>Comment: {userComment}')
        
    appointmentFormInputs = AppointmentForm()
    return render(request, 'deliveryform/appointmentForm.html', context={'appointmentFormInputs': appointmentFormInputs})

def orders(request):
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    email = request.POST.get('email')
    address = request.POST.get('address')
    return HttpResponse(f'{name} {surname}, проверьте адрес доставки:<br>{address}')

def delivery(request):
    deliveryFormInputs = DeliveryForm()
    return render(request, 'deliveryform/deliveryForm.html', context={'deliveryFormInputs': deliveryFormInputs})










