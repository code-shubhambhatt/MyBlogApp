from django.http import HttpResponse # type: ignore
from django.shortcuts import redirect # type: ignore
from django.http import HttpResponseRedirect # type: ignore
from django.urls import reverse # type: ignore



def index(request) : 
    # return HttpResponseRedirect(reverse('App_Blog:blog_list'))
    return HttpResponseRedirect(reverse('App_Blog:blog_list')   )