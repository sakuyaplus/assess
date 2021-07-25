from django.shortcuts import render
from tcomments.models import TComment
from ccomments.models import CComment
from teachers.models import Teacher
from courses.models import Course
from django.db.models import Q,Avg

# Create your views here.
def index(request):
    
    tavgscore=TComment.objects.values('teacher_name','teacher_id').annotate(avgstars=Avg('stars')).order_by('-avgstars')[:4]
    teacherlen=len(tavgscore)
    ids=[]
    tstars=[]
    for i in range(teacherlen):
        ids.append(tavgscore[i]['teacher_id'])
        tstars.append(tavgscore[i]['avgstars'])
   
    Tres=[]
    for i in range(teacherlen):
        res_one = Teacher.objects.get(id=ids[i])
        Tres.append(res_one)
  
 
    cavgscore=CComment.objects.values('course_name','course_id').annotate(avgstars=Avg('stars')).order_by('-avgstars')[:4]
    courselen=len(cavgscore)
    ids=[]
    cstars=[]
   
    for i in range(courselen):
        ids.append(cavgscore[i]['course_id'])
        cstars.append(cavgscore[i]['avgstars'])

    Cres=[]
    for i in range(courselen):
        res_one = Course.objects.get(id=ids[i])
        Cres.append(res_one)
    print(Cres)
    

    latesttcomments=TComment.objects.order_by('-comment_date')[:3]
    latestccomments=CComment.objects.order_by('-comment_date')[:3]

    context={
        'bestteachers': zip(Tres,tstars),
        'bestcourses': zip(Cres,cstars),
        'latesttcomments': latesttcomments,
        'latestccomments': latestccomments,
    }
    return render(request, 'index.html' ,context)
    

def about(request):
    context={

    }
    return render(request, 'about.html' ,context)