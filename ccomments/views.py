from ccomments.models import CComment
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
def ccomment(request):

    
    if request.method == 'POST':
        user_id=request.POST['user_id']
        user_name=request.POST['user_name']
        course_id=request.POST['course_id']
        course_name=request.POST['course_name']
        try:
            stars=request.POST['rating']
        except:
            messages.error(request,'评价星级范围为1-5')
            return redirect('/courses/'+course_id)

        message=request.POST['message']
        if int(stars)<1 or int(stars)>5:
            messages.error(request,'评价星级范围为1-5')
            return redirect('/courses/'+course_id)
      
        has_commented = CComment.objects.all().filter(course_id=course_id,user_id=user_id)
        if has_commented: #如果评价过，可以修改
            for i in has_commented:
                i.stars=stars
                i.message=message
                i.save()
            messages.success(request,'评价修改成功')
            return redirect('/courses/'+course_id)
       

        comment = CComment(user_id=user_id,user_name=user_name,course_id=course_id,
        stars=stars,message=message,course_name=course_name)

        comment.save()
        messages.success(request,'评价成功')

     
        return redirect('/courses/'+course_id)
    return redirect('index')