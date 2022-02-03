from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CompanyClass, IndividualClass
from .forms import CompanyForm, IndividualForm , CompanyIT14Form
from django.views import View

# PDF PRINTING
from django.http import HttpResponse
import tempfile
from weasyprint import HTML
from django.template.loader import render_to_string




def home(request):
    return render(request, 'main/home.html')

def newCustomer(request):
    return render(request, 'main/newCustomer.html')

def newCompany(request):
    form = CompanyForm()

    if request.method == 'POST':
        form = CompanyForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')
        else:
            print(form.errors)

    content = {'form':form}
    return render(request, 'main/newCompany.html', content)

def newIndividual(request):
    form = IndividualForm()

    if request.method == 'POST':
        form = IndividualForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')
        else:
            print(form.errors)

    content = {'form':form}
    return render(request, 'main/newIndividual.html', content)

def checklistHome(request):

    return render(request , 'main/checklistHome.html')

class companyIT14(View):

    def get(self,request):
        it14s = CompanyClass.objects.filter(IT14 = True).order_by('CompanyName')
        form = CompanyIT14Form()
        content = {'it14s':it14s , 'form':form}
        return render(request, 'main/Checklists/companyIT14.html', content)

    def post(self,request):
        it14s = CompanyClass.objects.filter(IT14=True).order_by('CompanyName')
        form = CompanyIT14Form(request.POST)
        content = {'it14s': it14s, 'form': form}
        if form.is_valid():
            form.save()
            return redirect('companyIT14')
        else:
            print(form.errors)
            return render(request, 'main/checklistHome.html', content)

def companyFIN(request):

    return render(request, 'main/Checklists/companyFIN.html')

def companyPROV(request):

    return render(request, 'main/Checklists/companyPROV.html')

def companyANNR(request):

    return render(request, 'main/Checklists/companyANNR.html')

def individualIT12(request):

    return render(request, 'main/Checklists/individualIT12.html')

def individualPROV(request):

    return render(request, 'main/Checklists/individualPROV.html')

def reportsHome(request):
    return render(request , 'main/reportsHome.html')

def printAllpdf(request):

    modelCompany = CompanyClass.objects.all().order_by('CompanyName')
    modelIndividual = IndividualClass.objects.all().order_by('Surname')

    content = {'modelCompany':modelCompany, 'modelIndividual':modelIndividual}

    ### Printing PDF FOR ALL CUSTOMERS
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=AllCustomers.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    html_string = render_to_string('main/reports/printAllpdf.html', content)
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()

        output.seek(0)
        response.write(output.read())

    return response