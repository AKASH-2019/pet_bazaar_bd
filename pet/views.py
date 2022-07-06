from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import BadHeaderError, send_mail
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage


from pet import database

import json



# Create your views here.

@api_view(['GET'])
def hello_world(request):

    storeProcedure = 'pet.product__pagination_by_pet'
    payload = json.dumps({"slug":"dog","limit":10,"offset_id":1})
    data = database.db(storeProcedure,payload)
    

    context = {
        'data':data[0]
    }

    return render(request, 'hello_world/hello_world.html', context)

@api_view(['GET'])
def home(request):

    storeProcedure = 'pet.product__pagination_for_home'
    payload = json.dumps({"limit":10,"offset_id":0})
    data = database.db(storeProcedure,payload)
    
    context = {
        'top_sell':data[0]['ret_data'][0]['top_sell'],
        'latest_product':data[0]['ret_data'][0]['latest_product']
    }

    return render(request, 'pet/homeView.html', context)

@api_view(['GET'])
def productPaginateByPetView(request,slug,secondary_slug):
    
    storeProcedure = 'pet.product__pagination_by_pet'
    payload = json.dumps({"slug":slug,"secondary_slug":secondary_slug,"limit":25,"offset_id":1})
    data = database.db(storeProcedure,payload)
    
    section_title = slug.capitalize()+' '+secondary_slug.capitalize()
    context = {
        'data':data[0],
        'section_title': section_title
    }
    return render(request, 'pet/productPetView.html', context)

def productSelect(request, slug):
    print(slug)
    return render(request, 'pet/productSelectView.html')

@api_view(['POST'])
def productPaginateByPet(request):
    storeProcedure = 'pet.product__pagination_by_pet'
    payload = json.dumps({"slug":"dog","limit":10,"offset_id":1})
    data = database.db(storeProcedure,payload)
    
    return Response(data)


def cart(request):
    return render(request, 'pet/cartView.html')


def checkout(request):
    if(request.session.get('user_record', False) == False):
        return redirect('/petbazaar/login?next=/checkout') 
    else:
        cookieData = json.loads(request.session.get('user_record', False))
        print(cookieData)
        return render(request, 'pet/checkoutView.html')

    
    
    

def order(request,id):

    if(request.session.get('user_record', False) == False):
        return redirect('/petbazaar/login?next=/order') 
    else:
        storeProcedure = 'pet.order__select_by_order_id'
        cookieData = json.loads(request.session.get('user_record', False))
        payload = json.dumps({"order_id":id,"user_id":cookieData[0]['user_id']})
        res = database.db(storeProcedure,payload)

        context = {
            'data':res[0]['ret_data'][0]
        }

        return render(request, 'pet/orderView.html', context)

def orderList(request):
    
    if(request.session.get('user_record', False) == False):
        return redirect('/petbazaar/login?next=/order-list') 
    else:
        storeProcedure = 'pet.order__pagination_by_id'
        cookieData = json.loads(request.session.get('user_record', False))

        payload = json.dumps({"user_id":cookieData[0]['user_id']})

        res = database.db(storeProcedure,payload)

        context = {
            'data':res[0]['ret_data'][0]
        }

        return render(request, 'pet/orderListView.html', context)





@api_view(['POST'])
@csrf_protect
def orderUpsert(request):
    cookieData = json.loads(request.session.get('user_record', False))

    if request.method == "POST":
        storeProcedure = 'pet.order__upsert'
        order_id = 0
        user_id = cookieData[0]['user_id']
        email = request.POST['email']
        phone = request.POST['phone']
        district = request.POST['district']
        city = request.POST['city']
        street = request.POST['street']
        total_price = request.POST['total_price']
        # shipping = request.POST['shipping']
        status = 1
        order_item = request.POST['order_item']
       
        payload = json.dumps({"order_id":order_id,"user_id":user_id, "email":email,"phone":phone,"district":district,"total_price":total_price,
                    "city":city,"street":street,"status":status,"order_item":order_item })
        # print(payload)
        res = database.db(storeProcedure,payload)
        # print(res)
        # send_mail("order_id", "product_details", email, ['akashdemo1234@gmail.com'], fail_silently=False)
        # context = {
        #     'email' : email,
        #     'success_msg' : "successfully send your email",
        # }


        # message = get_template("email/adminOrderEmail.html").render(context = {
        #     'order': res
        # })
        # mail = EmailMessage(
        #     subject="Order confirmation",
        #     body=message,
        #     from_email='akashmunazer@gmail.com',
        #     to=["akashdemo1234@gmail.com"],
        #     reply_to=["akashmunazer@gmail.com"],
        # )
        # mail.content_subtype = "html"
        # return mail.send()
        # # mail.send()


        return JsonResponse(res, safe=False)


@api_view(['POST'])
# @csrf_protect
def orderEmail(request):
    """
    Send email to customer with order details.
    """
    message = get_template("email/adminOrderEmail.html").render(context={
        'order': 'order details'
    })
    mail = EmailMessage(
        subject="Order confirmation",
        body=message,
        from_email='akashmunazer@gmail.com',
        to=['akasdemo1234@gmail.com'],
        reply_to=['akashmunazer@gmail.com'],
    )
    mail.content_subtype = "html"
    return mail.send()









