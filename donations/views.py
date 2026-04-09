from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Donation
from django_esewa import EsewaPayment
import uuid

# Create your views here.
def donate(request):
    if request.method == "POST":
        donor = request.POST.get("donor")
        email = request.POST.get("email")
        amount = request.POST.get("amount")
        uid = uuid.uuid4()
        donation = Donation.objects.create(
            uuid=uid,
            donor=donor,
            email=email,
            amount=amount,
            total_amount=amount
        )
        messages.success(request, "Thank you for your donation! Please confirm it.")
        return redirect('donations:donation_confirm',uuid = donation.uuid)

    return render(request, 'donations/donate.html')

def confirm(request, uuid):
    order = Donation.objects.get(uuid=uuid)
    payment = EsewaPayment(
        product_code=order.product_code,
        success_url=f"http://localhost:8000/donations/success/{order.uuid}/",
        failure_url=f"http://localhost:8000/donations/failure/{order.uuid}/",
        amount=order.amount,
        tax_amount=order.tax_amount,
        total_amount=order.total_amount,
        product_delivery_charge=order.delivery_charge,
        product_service_charge=order.service_charge,
        transaction_uuid=order.uuid,
        secret_key='8gBm/:&EnhH.1/q',
    )
    signature = payment.create_signature() #Saves the signature as well as return it
    context = {
        'form':payment.generate_form()
    }
    
    return render(request, 'donations/confirm.html',context)

def success(request, uuid):
    object = Donation.objects.get(uuid=uuid)
    object.confirmed = True 
    object.save()
    return render(request, 'donations/success.html')

def failure(request, uuid):
    return render(request, 'donations/failure.html')