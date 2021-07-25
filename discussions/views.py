from django.shortcuts import render,redirect
from .models import Discussion
from django.contrib import messages
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

#Create your views here.
def index(request):
    
    listings = Discussion.objects.all().order_by('-comment_date')
    paginator=Paginator(listings,12)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
        
    context={
        'listings': paged_listings
    }
    
    return render(request, 'discussions/discussions.html',context)

def dcomment(request):

    
    if request.method == 'POST':
        user_id=request.POST['user_id']
        user_name=request.POST['user_name']
        message=request.POST['message']
        if len(message)>300:
            messages.error(request,'留言长度最大为300字')
            return redirect('discussions')
        discussion = Discussion(user_id=user_id,user_name=user_name,message=message)

        discussion.save()
        messages.success(request,'评价成功')
        print(discussion)
     
        return redirect('discussions')

    return redirect('discussions')

def delcomment(request):
    if request.method == 'POST':
        discussid=request.POST['discuss_id']
        todelete = Discussion.objects.filter(id=discussid)
        if todelete:
            todelete.delete()
            messages.success(request,'删除成功')
        else:
            messages.error(request,'删除失败')
    return redirect('discussions')