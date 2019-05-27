from django.shortcuts import render,get_object_or_404,redirect
from accounts.models import User
from .models import Resume
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.core.paginator import Paginator
import json

from io import BytesIO
from django.template.loader import get_template
# from xhtml2pdf import pisa

@login_required
def resume_list(request):
    user = get_object_or_404(User,id=request.user.id)
    resume_list = Resume.objects.filter(user=user).order_by('-created')
    if resume_list:
        paginator = Paginator(resume_list,5)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        return render(request,'cv/resume_list.html',{'page_obj':page_obj,'paginator':paginator,'is_paginated':True,})
    else:
        return render(request,'cv/resume_list.html')

def handle(a,b):
    return json.dumps(list(zip(a,b)))

@login_required
@csrf_exempt
def create_resume(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        post_data = request.POST.dict()
        post_data_key = list(post_data.keys())[0]
        data = json.loads(post_data_key)[0]
        judge = False
        if 'number' in data.keys():
            judge = Resume.objects.filter(pk=int(data['number']))
        if judge:
            resume = Resume.objects.get(pk=int(data['number']))
            resume.name=data['name']
            resume.position=data['position']
            resume.profile=handle(data['profile'][0],data['profile'][1])
            resume.contact=handle(data['contact'][0],data['contact'][1])
            resume.stack=handle(data['stack'][0],data['stack'][1])
            resume.education=handle(data['education'][0],data['education'][1])
            resume.work=handle(data['work'][0],data['work'][1])
            resume.project=handle(data['project'][0],data['project'][1])
            resume.trophy=handle(data['trophy'][0],data['trophy'][1])
            resume.aboutme=data['aboutme']
            resume.save()
            return JsonResponse({'msg': 'success'})
        else:
            resume = Resume(name=data['name'],
                            position=data['position'],
                            profile=handle(data['profile'][0],data['profile'][1]),
                            contact=handle(data['contact'][0],data['contact'][1]),
                            stack=handle(data['stack'][0],data['stack'][1]),
                            education=handle(data['education'][0],data['education'][1]),
                            work=handle(data['work'][0],data['work'][1]),
                            project=handle(data['project'][0],data['project'][1]),
                            trophy=handle(data['trophy'][0],data['trophy'][1]),
                            aboutme=data['aboutme'],
                            user=user)
            resume.save()
            return JsonResponse({'msg': 'success'})
    else:
        return render(request,'accounts/resume.html')

@login_required
def edit_resume(request,pk):
    pass

'''
    预览并打印PDF，依赖于 xhtml2pdf 包，但是不支持中文打印以及一些 css 样式
    可以在模板中 style 中添加
    @font-face {
    font-family: simsun;    
    src: url(C:/Windows/Fonts/simsun.ttc);
    }

'''
# def render_to_pdf(template_src, context={}):
#     template = get_template(template_src)
#     html  = template.render(context)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None 

@login_required
def preview_resume(request,pk):
    # pdf = render_to_pdf('cv/pdf.html', {})
    # return HttpResponse(pdf, content_type='application/pdf')
    resume = get_object_or_404(Resume,pk=pk)
    context = {
        "number":resume.id,
    	"name":resume.name,
    	"position":resume.position,
    	"profile":json.loads(resume.profile),
    	"contact":json.loads(resume.contact),
    	"stack":json.loads(resume.stack),
    	"education":json.loads(resume.education),
    	"work":json.loads(resume.work),
    	"project":json.loads(resume.project),
    	"trophy":json.loads(resume.trophy),
    	"aboutme":resume.aboutme,
        "print":True if request.path == '/print/{}/'.format(resume.id) else False,
        "edit":True if request.path == '/edit/{}/'.format(resume.id) else False,
        "preview":True if request.path == '/preview/{}/'.format(resume.id) else False,
    }
    return render(request,'cv/preview_resume.html',context=context)

@login_required
def delete_resume(request,pk):
    resume = Resume.objects.get(pk=pk)
    resume.delete()
    return HttpResponseRedirect(reverse('cv:list'))