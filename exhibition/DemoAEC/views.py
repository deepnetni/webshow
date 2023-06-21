from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import os
import json5

# Create your views here.


def show_demo_aec(request):
    """return results"""
    content = {"success": 0, "error": ""}
    if request.method == "GET":
        x = request.GET.get("xx", "")
        pass
    elif request.method == "POST":
        x = request.POST.get("xx", "")
        pass
    return JsonResponse(content, safe=False)


def show_demo_arch(request):
    """get model arch image or svg"""
    content = {"success": 0, "error": ""}
    if request.method == "GET":
        image_path = ""
        content["image_path"] = image_path

    return JsonResponse(content, safe=False)


def show_demo_content(request):
    """get title, authors, abstracts"""
    pass
