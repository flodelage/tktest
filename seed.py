import json
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tkttest.settings")
django.setup()
from apptkt.models import Company, Result


with open('apptkt/fixtures/fixtures.json') as json_file:
    data = json.load(json_file)
    for company in data:
        company_instance = Company(name=company["name"], sector=company["sector"], siren=company["siren"])
        company_instance.save()
        results = company["results"]
        for result in results:
            result_instance = Result(company=company_instance, ca=result["ca"], margin=result["margin"],
                                     ebitda=result["ebitda"], loss=result["loss"], year=result["year"])
            result_instance.save()

