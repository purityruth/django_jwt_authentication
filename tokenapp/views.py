from django.shortcuts import render

import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import TokenSerializer, OrganizationSerializer
from .models import Token, Organization
from rest_framework_jwt.utils import jwt_encode_handler

@api_view(['GET'])
def generate_license(request):
    # Get data for generating license (e.g., product ID, expiration date, etc.)
    # product_id = request.POST.get('product_id')
    # expiration_date = request.POST.get('expiration_date')

    expiration_date = request.data['expiration_date']
    number_of_users = request.data['number_of_users']


    # Create payload for JWT token
    payload = {
        'product_id': number_of_users,
        'expiration_date': expiration_date,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(days=7)
    }

    # Sign JWT token with secret key from Django settings
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    # Return JWT token as response
    return HttpResponse(token)



