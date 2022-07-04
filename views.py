from django.shortcuts import HttpResponse, get_object_or_404, HttpResponseRedirect
from django.template.response import TemplateResponse

# TemplateResponse is recommended over render
### REFERENCES ###
# https://spookylukey.github.io/django-views-the-right-way/the-pattern.html
### ###
def index(request):
    return TemplateResponse(request, template="t2/base.html", context=None)