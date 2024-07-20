import requests
from django.shortcuts import render
from django.http import JsonResponse

def consulta_dni(request):
    if request.method == 'POST':
        dni = request.POST.get('dni')
        url = f"https://api.sunat.gob.pe/v1/dni/{dni}"
        headers = {
            'Authorization': 'Bearer 04e62642-a3f2-4af2-821c-f1e0b3fb3f45'
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        return JsonResponse(data)
    return render(request, 'consulta_dni.html')