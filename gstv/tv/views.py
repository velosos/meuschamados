# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests

from django.shortcuts import render

# Create your views here.



def home(request,template_name="index.html"):


	# Set the request parameters
    url = 'https://your_instance.service-now.com/api/now/table/sys_user_group?sysparm_query=active%3Dtrue%5EtypeISEMPTY'

# Eg. User name="admin", Password="admin" for this code sample.
    user = 'login'
    pwd = 'Password'

# Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

# Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)

    return render(request,template_name,{'obj':data['result']}) 



def chamados(request,value):

    value = request.POST.get('valor')


    url = 'https://your_instance-now.com/api/now/table/task?sysparm_query=active%3Dtrue%5Eassignment_group%3D' + value

# Eg. User name="admin", Password="admin" for this code sample.
    user = 'login'
    pwd = 'password'

# Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

# Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)     

    return render(request,'chamados.html',{'obj':data['result']})  