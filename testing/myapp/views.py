

# Create your views here.


# Create your views here.




import os
import uuid

from django.conf import settings
from myapp import *

from django.shortcuts import  redirect,render 
from .models import *

from .models import MasterCategory 













# def login_views(request):
#     if request.method == "POST":
#         return redirect('/dashboard_view')
#     return render(request,'login.html')


def login_views(request):
    if request.session.get('email'):
        return redirect('dashboard')
    
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        userinfo=AdminUserMaster.objects.filter(admEmail=email,admPassword=password).first() # type: ignore
        if userinfo:
            request.session["email"]=userinfo.admEmail
            request.session["password"]=userinfo.admPassword
            return redirect('dashboard') # type: ignore
        else:
            errorMessage = "Invalid Credentials."
            return render(request,'login.html',{"message":errorMessage})
    return render(request,'login.html')

def dashboard(request):
    
    if request.session.get('email'):
        
        return render(request,'dashboard/dashboard.html')
    else:
        return redirect('login_views') 
        
def logout(request):
    request.session.flush()
    return redirect('login_views') 





def catList(request):
    category=MasterCategory.objects.all()
    print(category)
    return render(request,"category/category.html",{"categories":category})
 


def catCreate(request):
    if request.method == "POST":

        name=request.POST.get('name')
        seqno=request.POST.get('seqno')
        slug=name.lower().replace(" ","-")
        isExist=MasterCategory.objects(catName=name)
        if isExist:
            errorMsg = "Category is already Exist."
            return render(request,"category/category_adddata.html",{"errorMsg":errorMsg})
        else:
            cat = MasterCategory(
                catName=name,
                catSlug=slug,
                catSeqNo=seqno
            )
            cat.save()

        return redirect('tablelist')
    return render(request,"category/category_adddata.html")

















# def dashboard_view(request):
#     return render(request,'dashboard/dashboard.html')

def category_view(request):
    return render(request,'category/category.html')


def category_viewdata(request):
    if request.method == "POST":

        name=request.POST.get('name')
        seqno=request.POST.get('seqno')
        slug=name.lower().replace(" ","-")
        isExist=MasterCategory.objects.filter(catName=name).exists()
        if isExist:
            errorMsg = "Category is already Exist."
            return render(request,"category/category_adddata.html",{"errorMsg":errorMsg})
        else:
            cat = MasterCategory(
                catName=name,
                catSlug=slug,
                catSeqNo=seqno  
            )
            cat.save()
        return redirect('tablelist')
    return render(request,'category/category_adddata.html')
    












def article_view(request):
    result = article_master.objects.all()
    return render(request,'article/article.html',{'result':result})
    

# def articale_create(request):
#     records=MasterCategory.objects.all()
#     if request.method=='POST':
#         title=request.POST.get('title')
#         image=request.FILES.get('image')
#         status=request.POST.get("status")
#         category=request.POST.get('category')
#         description=request.POST.get("description")

#         article_master.objects.create(
#             title=title,
#             image=image,
#             status=status,
#             category=category,
#             description=description
#         )
#         return redirect("article_view")
#     records =MasterCategory.objects.all()  
#     return render(request,"article/article_form.html",{"records":records})


def articale_create(request):
    records = MasterCategory.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        status=True
        if request.POST.get("status")==None:
            status=False


        try:
            category_obj = MasterCategory.objects.get(id=category_id)
        except MasterCategory.DoesNotExist:
            return render(request, "article/article_form.html", {
                "records": records,
                "errorMsg": "Category does not exist"
            })

        article_master.objects.create(
            title=title,
            image=image,
            status=status,
            # category=category_obj,
            catName=category_obj,  
            description=description
        )
        return redirect("article_view")

    return render(request, "article/article_form.html", {"records": records})



def articale_delete(request,id):
    ArtDelete=article_master.objects.get(id=id)
    ArtDelete.delete()
    return redirect("article_view")





# def articale_Edit(request,id):
#     artData=article_master.objects.get(id=id)
#     categories = MasterCategory.objects.all()

#     if request.method=="POST":
#         title=request.POST.get("title")
#         image = request.FILES.get("image")
#         if image:
#            artData.image = image      
#         category=request.POST.get("category")
#         description=request.POST.get("description")
#         status=True
#         if request.POST.get("status")==None:
#             status=False

#         istitle=article_master.objects.filter(title=title).exclude(id=id).first()
#         isimage=article_master.objects.filter(image=image).exclude(id=id).first()
#         iscategory=article_master.objects.filter(category=category).exclude(id=id).first()
#         isdescription=article_master.objects.filter(description=description).exclude(id=id).first()



#         if istitle:
#             errorMsg="Title is already exist."
#             return render(request,"article/article_adit.html",{"errorMsg":errorMsg,"ArtDelete":artData})

#         if isimage:
#             errorMsg="Image is already exist."
#             return render(request,"article/article_adit.html",{"errorMsg":errorMsg,"ArtDelete":artData})
        
#         if iscategory:
#             errorMsg="Category is already exist."
#             return render(request,"article/article_adit.html",{"errorMsg":errorMsg,"ArtDelete":artData})
        
#         if isdescription:
#             errorMsg="Description is already exist."
#             return render(request,"article/article_adit.html",{"errorMsg":errorMsg,"ArtDelete":artData})




#         else:
#             print(artData.id)
#             artData.title=title
#             artData.image=image
#             artData.category_id=category
#             artData.description=description
#             artData.status=status
#             artData.save()
#             return redirect('article_view')
        
#     return render(request,"article/article_adit.html",{"ArtDelete":artData,'categories':categories})


def articale_Edit(request, id):
    
    artData = article_master.objects.get(id=id)
    categories = MasterCategory.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")
        category_id = request.POST.get("category")
        description = request.POST.get("description")
        status=True
        if request.POST.get("status")==None:
            status=False

        try:
            category_obj = MasterCategory.objects.get(catName=category_id)
        except MasterCategory.DoesNotExist:
            return render(request, "article/article_adit.html", {
                "errorMsg": "Invalid category",
                "ArtDelete": artData,
                "categories": categories
            })

        artData.title = title
        if image:
            artData.image = image
        artData.category_id = category_id
        artData.description = description
        artData.status = status

        artData.save()
        return redirect('article_view')

    return render(request, "article/article_adit.html", {"ArtDelete": artData, 'categories': categories})

















def catDelete(request,id):
    data=MasterCategory.objects.get(id=id)
    if data:
        data.delete()
        return redirect('tablelist')


def catEdit(request,id):
    catData=MasterCategory.objects.get(id=id)

    if request.method=="POST":
        name=request.POST.get("name")
        cId=request.POST.get("id")
        seqno=request.POST.get("seqno")
        slug=name.lower().replace(" ","-")
        status=True
        if request.POST.get("status")==None:
            status=False
            
        isSeqNo=MasterCategory.objects.filter(catSeqNo=seqno).exclude(id=id).first()
        namename=MasterCategory.objects.filter(catName=name).exclude(id=id).first()
        if namename:
            errorMsg="Name is already exist."
            return render(request,"category/category_add.html",{"errorMsg":errorMsg,"data":catData})


        if isSeqNo:
            print("record exist")
            id1= str(isSeqNo.id)
            id2= str(cId)
            if id1==id2:
                catData.catName=name
                catData.catSlug=slug
                catData.catSeqNo=seqno
                catData.catStatus=status
                catData.save()
                return redirect('tablelist')
            else:
                errorMsg="Seq No is already exist."
                return render(request,"category/category_add.html",{"errorMsg":errorMsg,"data":catData})
        else:
            print(catData.id)
            catData.catName=name
            catData.catSlug=slug
            catData.catSeqNo=seqno
            catData.catStatus=status
            catData.save()
            return redirect('tablelist')
    return render(request,"category/category_add.html",{"data":catData})




def catImage(request):
    if request.method == "POST":
        fle=request.FILES.get('catImage')
        
        ext = os.path.splitext(fle.name)[1]
        fileName=f"{uuid.uuid4().hex}{ext}"
        path=os.path.join(settings.MEDIA_ROOT,fileName)

        with open(path,'wb+') as destination:
            for chunk in fle.chunks():
                destination.write(chunk)
    return render(request,"category/image.html")








