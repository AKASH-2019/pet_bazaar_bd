from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from pet import database

import json



# Create your views here.


def orderList(request):
    cookieData = json.loads(request.session.get('user_record', False))
    # print(cookieData[0]['slug'])
    if(request.session.get('user_record', False) == False):
        return redirect('/petbazaar/login?next=/pet/admin/order-list') 
    else:
        storeProcedure = 'pet.order__pagination_for_admin'
        # payload = json.dumps({"user_id":cookieData[0]['user_id']})
        payload = json.dumps({})
        res = database.db(storeProcedure,payload)

        context = {
            'data':res[0]
        }
        # print(res[0])

        return render(request, 'pet_admin/adminOrderListView.html', context)



@api_view(['POST'])
@csrf_protect
def orderStatusUpsert(request):
    cookieData = json.loads(request.session.get('user_record', False))
    # print("cookieData")
    # print(cookieData[0]['user_id'])
    if request.method == "POST":
        storeProcedure = 'pet.order_status_update'
        order_id = request.POST['order_id']
        user_id = cookieData[0]['user_id']
        status = request.POST['status']
       
        payload = json.dumps({"order_id":order_id,"user_id":user_id, "status":status })
        print(payload)
        res = database.db(storeProcedure,payload)
        # print(res)

        return JsonResponse(res, safe=False)










