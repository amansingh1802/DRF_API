import hashlib
from django.conf import settings
from django.http import response
from django.db.models import query
from rest_framework import generics
from rest_framework.views import APIView
from .models import Manager, Plan, SuscribedPlan
from .serializers import PlanSerilizer, SubscribedPlanSerializer, UserSerilizer
from rest_framework.response import Response
from django.shortcuts import render
# from .models import Transaction
from .paytm import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt


class UserView(generics.CreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = UserSerilizer


class PlanView(generics.ListAPIView):

    def get_queryset(self):
        s_plan = SuscribedPlan.objects.get(suscribeduser_id=2)
        print(s_plan.plan.id)
        print(f'subscribed plan {s_plan}')
        result = []
        for plan in Plan.objects.all():
            if plan.id == s_plan.plan.id:
                result.append(s_plan)
            else:
                result.append(plan)
        print(result)
        return Plan.objects.all()
    serializer_class = PlanSerilizer


class SubView(APIView):
    queryset = SuscribedPlan.objects.all()
    serializer_class = SubscribedPlanSerializer

    def post(self, request):
        print(request)
        return Response({"MESSAGE": "SUCCESS"})
        # transaction = Transaction.objects.create(made_by='user', amount=100)
        # transaction.save()
#         merchant_key = settings.PAYTM_SECRET_KEY
#         params = (
#             ('MID', settings.PAYTM_MERCHANT_ID),
#             ('ORDER_ID', str(transaction.order_id)),
#             ('CUST_ID', str(transaction.made_by.email)),
#             ('TXN_AMOUNT', str(transaction.amount)),
#             ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
#             ('WEBSITE', settings.PAYTM_WEBSITE),
#             # ('EMAIL', request.user.email),
#             # ('MOBILE_N0', '9911223388'),
#             ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
#             ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
#             # ('PAYMENT_MODE_ONLY', 'NO'),
#         )

#         paytm_params = dict(params)
#         checksum = generate_checksum(paytm_params, merchant_key)

#         transaction.checksum = checksum
#         transaction.save()

#         paytm_params['CHECKSUMHASH'] = checksum
#         print('SENT: ', checksum)
#         return render(request, 'payments/redirect.html', context=paytm_params)


# @csrf_exempt
# def callback(request):
#     if request.method == 'POST':
#         paytm_checksum = ''
#         print(request.body)
#         print(request.POST)
#         received_data = dict(request.POST)
#         print(received_data)
#         paytm_params = {}
#         paytm_checksum = received_data['CHECKSUMHASH'][0]
#         for key, value in received_data.items():
#             if key == 'CHECKSUMHASH':
#                 paytm_checksum = value[0]
#             else:
#                 paytm_params[key] = str(value[0])
#         # Verify checksum
#         is_valid_checksum = verify_checksum(
#             paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
#         if is_valid_checksum:
#             print("Checksum Matched")
#             received_data['message'] = "Checksum Matched"
#         else:
#             print("Checksum Mismatched")
#             received_data['message'] = "Checksum Mismatched"

#         return render(request, 'payments/callback.html', context=received_data)
