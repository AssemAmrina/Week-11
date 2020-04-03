from django.contrib import admin
from django.urls import path
import api.views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies', v.getAllCompanies),
    path('api/companies/<int:id>', v.getOneCompany),
    path('api/companies/<int:id>/vacancies', v.getListOfVacancyByCompany),
    path('api/vacancies/', v.getAllVacancies),
    path('api/vacancies/<int:id>', v.getOneVacancy),
    path('api/vacancies/top_ten/', v.getTopTenSortedVacancies),
    ]

