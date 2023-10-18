from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

import datetime
# Create your views here.
def index(req):
    today = datetime.datetime.now()
    return HttpResponse(f'(FBV) Current date: {today.date()} and time: {today.time().strftime("%H:%M:%S")}')

class cbv(View):
    def get(self, req):
        today = datetime.datetime.now()
        return HttpResponse(f'(CBV) Current date: {today.date()} and time: {today.time().strftime("%H:%M:%S")}')