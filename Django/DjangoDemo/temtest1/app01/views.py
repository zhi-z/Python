from django.shortcuts import render
from django.http import HttpResponse
from app01.models import Customer,Apps,DeviceAppUpdate
from rest_framework.response import Response
						
# Create your views here.



def index(request):
	return HttpResponse('index...')


class CustomerView():
	pass