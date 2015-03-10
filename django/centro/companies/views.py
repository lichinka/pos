from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from companies.models import Company
from utils.views import render


def index (request):
    """
    The default view.
    """
    all_companies = Company.objects.all ( ).order_by ('name')
    
    return render ('companies/company_list.html', 
                   {'all_companies': all_companies},
                   RequestContext (request))


def detail (request, company_id):
    """
    Shows all fields of the company received.
    """
    return HttpResponse ("You're looking at company %s." % company_id)


