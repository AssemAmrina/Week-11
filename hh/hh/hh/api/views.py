from django.shortcuts import render
from .models import Company, Vacancy
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
# Create your views here.
def getAllCompanies(request):

    c = Company.objects.all()
    c_json = [cm.to_json() for cm in c]
    return JsonResponse(c_json, safe=False)

def getOneCompany(request, id):
    try:

        c = Company.objects.get(id = id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(c.full())
def getListOfVacancyByCompany(request, id):
    v = Vacancy.objects.all()
    out = []
    for vac in v:
        if vac.company.id == id:
            out.append(vac.to_json())
    return JsonResponse(out,safe=False)
def getAllVacancies(request):
    v = Vacancy.objects.all()
    vacs = [vc.to_json for vc in v]
    return JsonResponse(vacs, safe=False)
def getOneVacancy(request, id):
    v = Vacancy.objects.all()
    for i in v:
        if i.id == id:
            out = i.to_json()
            return JsonResponse(out)
    return HttpResponse("<h1>No such file .(</h1>")
def sortSalary(vac):
    return vac.salary
def getTopTenSortedVacancies(request):
    v = Vacancy.objects.all()
    out = sorted(v, key=sortSalary)[-10:]
    out = [cm.to_json() for cm in out]
    return JsonResponse(out,safe=False)
