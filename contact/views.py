from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# Create your views here.
def contact(request):
    return render(request, 'contact/contact.html')



def email(request):  
    # request.encoding='utf-8'
    # if 'q' in request.GET and request.GET['q']:
    #     message = '你搜索的内容为: ' + request.GET['q']
    # else:
    #     message = '你提交了空表单'
    # return HttpResponse(message)
    if request.POST:
        return HttpResponse(request.POST['q'])