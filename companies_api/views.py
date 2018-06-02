from companies_api.models import *
from companies_api.serializers import *
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import generics
# from rest_framework.renderers import JSONRenderer


class PostalAddressList(generics.ListCreateAPIView):
    queryset = PostalAddress.objects.all()
    serializer_class = PostalAddressSerializer


class PostalAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostalAddress.objects.all()
    serializer_class = PostalAddressSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyFilterView(View):
    '''
    Filtered view for company model
    '''

    def get(self, request):
        city = request.GET.get('city')
        name = request.GET.get('name')
        count = request.GET.get('count')

        response = {}

        # To retrieve all the Postal Codes which has more than X number of companies
        if count:
            queryset = Company.objects.values('postal_code').annotate(
                c=Count('postal_code')).filter(c__gte=int(count)+1).distinct()

            response.update({
                'status': 200,
                'total': len(queryset),
                'postal_codes': []
            })
            for item in queryset:
                response['postal_codes'].append(item.get('postal_code'))

        # To get list of all companies in a certain city
        elif city:
            queryset = Company.objects.filter(postal_code__city=city)
            response.update(
                {'status': 200, 'total': len(queryset), 'companies': []})
            for company in queryset:
                response['companies'].append({
                    'name': company.name,
                    'building_number': company.building_number,
                    'postal_code': company.postal_code.postal_code,
                    'locality': company.postal_code.locality,
                    'city': company.postal_code.city,
                    'state': company.postal_code.state
                })

        # To get address based on given company name
        elif name:
            queryset = Company.objects.filter(name=name)
            response.update(
                {'status': 200, 'total': len(queryset), 'companies': []})
            for company in queryset:
                response['companies'].append({
                    'name': company.name,
                    'building_number': company.building_number,
                    'postal_code': company.postal_code.postal_code,
                    'locality': company.postal_code.locality,
                    'city': company.postal_code.city,
                    'state': company.postal_code.state
                })

        return JsonResponse(response)
