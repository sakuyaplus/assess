from tcomments.models import TComment
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.db.models import Q,Avg
from .models import Course
from .choices import academy_choices
# Create your views here.
def index(request):
    
    listings = Course.objects.all().filter(show=True)

    if 'q' in request.GET:
        keywords=request.GET['q']
     
        if keywords:
            listings = listings.filter(
                Q(name__icontains=keywords)|Q(description__icontains=keywords)
            )

    if 'academy' in request.GET: #选择开课学院
        academy=request.GET['academy']
      
        if academy !='全部':
            listings = listings.filter(
                courseacademy__iexact=academy
            )

    if 'credits' in request.GET: #选择学分
        credits=request.GET['credits']

        if credits !='':
            listings = listings.filter(
                credits__icontains=credits
            )   
    
    if 'type' in request.GET: #选择类型
        type=request.GET['type']

        if type !='全部':
            listings = listings.filter(
                typeofcourse__icontains=type
            )   
    
    if 'campus' in request.GET: #选择校区
        campus=request.GET['campus']

        if type !='全部':
            listings = listings.filter(
                campus__icontains=campus
            )   

    paginator=Paginator(listings,12)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
        
    context={
        'listings': paged_listings,
        'academy_choices':  academy_choices,
        'values': request.GET
    }
   
    return render(request, 'courses/courses.html',context)


def listing(request, listing_id):
    '''
    listing = get_object_or_404(Teacher, pk=listing_id)
    comments = TComment.objects.order_by('-comment_date').filter(
        teacher_id=listing_id
    )
    avgscore=TComment.objects.filter(teacher_id=listing_id).aggregate(Avg("stars"))['stars__avg']
    if avgscore==None:
        avgscore=0
    commentcounts = len(comments)
    context = {
        'listing': listing,
        'comments': comments,
        'commentcounts': commentcounts,
        'avgscore': avgscore,
    }
'''
    context={

    }
    return render(request, 'teachers/listing.html', context)

def search(request):

    context= {
        
    }
    return render(request, 'teachers/search.html', context)

