from django.shortcuts import render
from django.views.generic import View



    
# Create your views here.
class FrontendRenderView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'website/website.html')


