from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import IFSC
from .serializers import ApiSerializer
from django.shortcuts import redirect, render
from .forms import BankForm
from django.views.generic.edit import FormView


class Index(FormView):
    template_name = 'api/index.html'
    form_class = BankForm

    def form_valid(self, form):
        code = form.cleaned_data.get('ifs_code')
        bank = form.cleaned_data.get('bank_name')
        city = form.cleaned_data.get('city_name')

        code = code.upper()
        bank = bank.replace(' ', '-').lower()
        city = city.replace(' ', '-').lower()

        if code != '':
            if 'html' in self.request.POST:
                return redirect('ifsc', code)
            elif 'api' in self.request.POST:
                return redirect('bank', code)
        if 'html' in self.request.POST:
            return redirect('branch', bank, city)
        return redirect('branches', bank, city)


# Overriding Django's default 404 with custom JSON response
@api_view(['GET'])
def error_404(request):
    return Response(status=status.HTTP_404_NOT_FOUND)


# Get details of the branch with the matching IFSC
@api_view(['GET'])
def bank_details(request, ifs_code):
    ifs_code = ifs_code.upper()
    try:
        ifs_code = IFSC.objects.get(IFSC=ifs_code)
    except IFSC.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApiSerializer(ifs_code)
        return Response(serializer.data)


# Get details of all the branches of a bank in a city
@api_view(['GET'])
def details_of_branches(request, bank, city):
    bank = bank.replace('-', ' ').upper()
    city = city.replace('-', ' ').upper()
    branches = IFSC.objects.filter(BANK=bank, CITY=city).all()
    if not bool(branches):
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApiSerializer(branches, many=True)
        return Response(serializer.data)


def branch(request, bank, city):
    bank = bank.replace('-', ' ').upper()
    city = city.replace('-', ' ').upper()
    state = IFSC.objects.filter(CITY=city, BANK=bank).values_list('STATE', flat=True)[0]
    branches = IFSC.objects.filter(BANK=bank, CITY=city).all()
    return render(request, 'api/branch.html', {'branches': branches, 'bank': bank, 'city': city, 'state': state})

def bank(request, ifs_code):
    ifs_code = ifs_code.upper()
    ifs_code = IFSC.objects.get(IFSC=ifs_code)
    return render(request, 'api/bank.html', {'ifsc': ifs_code})