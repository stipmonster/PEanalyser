from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.template import Template, RequestContext
from scans.models import App,AppForm,File

import dllscanner.pluginLoader
import os
import zipfile
import pefile

# Create your views here.
def index(request):
    scan_list = App.objects.all()
    output = ', '.join([p.name for p in scan_list])
    context = {'latest_poll_list': scan_list}
    return render(request, 'scans/index.html', context)

def add(request):
    AppFormSet = modelformset_factory(App)
    if request.method == 'POST':
        formset = AppFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/scans/")
            
    else:
        formset = AppFormSet(queryset=App.objects.none())
        
    return render_to_response("scans/add.html", {
        "formset": formset,
    },context_instance=RequestContext(request))

def detail(request,scan_id):
    try:
        a = App.objects.get(pk=scan_id)
    except App.DoesNotExist:
        raise Http404
    return render_to_response('scans/details.html', {'app': a})

def extract_to_files(request,scan_id):
    a = App.objects.get(pk=scan_id)
    if zipfile.is_zipfile(a.filezip):
        toExtract = zipfile.ZipFile(a.filezip)
        toExtract.extractall("/tmp/obb/"+ str(scan_id))
        createfiles("/tmp/obb/"+ str(scan_id),a)
    return HttpResponseRedirect("/scans/"+ scan_id)

def files(request,scan_id):
    try:
        a = App.objects.get(pk=scan_id)
    except App.DoesNotExist:
        raise Http404
    file_set= a.file_set.all()
        
    return render(request, 'scans/result.html', {'files': file_set})

def file_result(request,scan_id,file_id):
    try:
        a = App.objects.get(pk=scan_id)
        file = a.file_set.get(pk=file_id)
    except App.DoesNotExist,File.DoesNotExist:
        raise Http404
    file_set= a.file_set.all()
    
    print dllscanner.pluginLoader.loadPlugin(dllscanner.pluginLoader.getPlugins()[0]).info()
    pe =  pefile.PE(file.path)
    totalstring= ""
    for plugin in dllscanner.pluginLoader.getPlugins():
        totalstring= totalstring+ dllscanner.pluginLoader.loadPlugin(plugin).start(file.path,pe)
    print file.path
    print totalstring
    return render(request, 'scans/file_result.html', {'files': file_set,'file':file})

# functions
def createfiles(path,app):
    for root, subFolders, files in os.walk(path):
        for filename in files:
            filePath = os.path.join(root, filename)
            app.file_set.create(path=filePath)
            
    