from django.shortcuts import render
from myapp.models import *
# Create your views here.
def Homeview(request):
    items = Items.objects.all()
    list = Item_list.objects.all()
    return render (request,'home.html',{'items':items,'list':list})


def Aboutview(request):
   return render (request,'about.html')


def Menuview(request):
    items = Items.objects.all()
    list = Item_list.objects.all()
    return render (request,'menu.html',{'items':items,'list':list})

def BookTableview(request):
    if request.method=='POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_date = request.POST.get('booking_date')
        
        if name != '' and len(phone_number) == 10 and email != '' and total_person != 0 and booking_date != '':
             data = Book_Table(Name=name,
                               Phone_number=phone_number,
                               Email=email,
                               Total_person=total_person, 
                               Booking_date=booking_date)
             data.save()
    return render (request,'book_table.html')
