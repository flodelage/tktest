from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from apptkt.models import Company


def index(request):
    companies = Company.objects.order_by("name")
    """ Pagination - Show 120 companies per page """
    paginator = Paginator(companies, 120)
    page = request.GET.get('page')
    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        companies = paginator.page(1)
    except EmptyPage:
        companies = paginator.page(paginator.num_pages)

    context = {'companies': companies, }
    return render(request, 'index.html', context)


def detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    results = company.result_set.order_by("year")

    context = {'company': company, 'results': results, }
    return render(request, 'detail.html', context)
