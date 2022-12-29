from django.shortcuts import render,HttpResponse,redirect
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime,timedelta,date
from .models import UserExtend, Member, Author, Category, Publisher, Book, Order, Return
from django.contrib.auth import authenticate ,logout
from django.contrib.auth import login as dj_login

def index(request):
    return render(request,'index.html')

def staff(request):
    return render(request,'staff.html')

def stafflogin(request):
    if request.session.has_key('is_logged'):
        return redirect('dashboard')
    return render(request,'stafflogin.html')

def staffsignup(request):
    return render(request,'staffsignup.html')

def dashboard(request):
    if request.session.has_key('is_logged'):
        book = Book.objects.all()
        return render(request,'dashboard.html',{'Book':book})
    return redirect('stafflogin')

def addauthor(request):
    author = Author.objects.all()
    return render(request,'addauthor.html',{'Author':author})

def AddAuthorSubmission(request):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            author_id = request.POST["author_id"]
            name = request.POST["name"]
            add = Author(author_id=author_id, name=name)
            add.save()
            author = Author.objects.all()
            return render(request,'dashboard.html',{'Author':author})
    return redirect('/')

def addcategory(request):
    category = Category.objects.all()
    return render(request,'addcategory.html',{'Category':category})

def AddCategorySubmission(request):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            type = request.POST["type"]
            add = Category(type=type)
            add.save()
            category = Category.objects.all()
            return render(request,'dashboard.html',{'Category':category})
    return redirect('/')

def addpublisher(request):
    publisher = Publisher.objects.all()
    return render(request,'addpublisher.html',{'Publisher':publisher})

def AddPublisherSubmission(request):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            name = request.POST["name"]
            add = Publisher(name=name)
            add.save()
            publisher = Publisher.objects.all()
            return render(request,'dashboard.html',{'Publisher':publisher})
    return redirect('/')


def addbook(request):
    book = Book.objects.all()
    return render(request,'addbook.html',{'Book':book})

def SignupBackend(request):
    if request.method =='POST':
            uname = request.POST["uname"]
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            email = request.POST["email"]
            phone=request.POST['phone']
            password=request.POST['password']
            userprofile = UserExtend(name=fname+lname, email=email, phone=phone)
            if request.method == 'POST':
                try:
                    UserExists = User.objects.get(username=request.POST['uname'])
                    messages.error(request,"Username already existed. Please try again!")
                    return redirect("staffsignup")    
                except User.DoesNotExist:
                    if len(uname)>10:
                        messages.error(request," Username must be max 15 characters. Please try again!")
                        return redirect("staffsignup")
            
                    if not uname.isalnum():
                        messages.error(request," Username should only contain letters and numbers, Please try again!")
                        return redirect("staffsignup")
            
            # create the user
            user = User.objects.create_user(uname, email, password)
            user.first_name=fname
            user.last_name=lname
            user.email = email
            user.save()
            userprofile.user = user
            userprofile.save()
            messages.success(request," Your account has been successfully created")
            return redirect("stafflogin")
    else:
        return HttpResponse('404 - NOT FOUND ')

def LoginBackend(request):
    if request.method =='POST':
        loginuname = request.POST["loginuname"]
        loginpassword=request.POST["loginpassword"]
        RegisteredUser = authenticate(username=loginuname, password=loginpassword)
        if RegisteredUser is not None:
            dj_login(request, RegisteredUser)
            request.session['is_logged'] = True
            RegisteredUser = request.user.id
            request.session["user_id"] = RegisteredUser
            messages.success(request, " Successfully logged in")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Credentials. Please try again!")  
            return redirect("/")  
    return HttpResponse('404-not found')

def AddBookSubmission(request):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            user = User.objects.get(id=request.session["user_id"])
            isbn = request.POST["isbn"]
            title = request.POST["title"]
            status = request.POST["status"]
            author = Author.objects.get(name = request.POST["author"])
            category = Category.objects.get(type = request.POST["category"])
            publisher = Publisher.objects.get(name = request.POST["publisher"])
            add = Book(user = user, isbn=isbn,title=title, status=status,author=author,category=category, publisher=publisher)
            add.save()
            book = Book.objects.all()
            return render(request,'dashboard.html',{'Book':book})
    return redirect('/')

def deletebook(request,id):
    if request.session.has_key('is_logged'):
        AddBook_info = Book.objects.get(id=id)
        AddBook_info.delete()
        return redirect("dashboard")
    return redirect("login") 

def bookissue(request):
    return render(request,'bookissue.html')

def returnbook(request):
    return render(request,'returnbook.html')

def HandleLogout(request):
        del request.session['is_logged']
        del request.session["user_id"] 
        logout(request)
        messages.success(request, " Successfully logged out")
        return redirect('dashboard')

def issuebooksubmission(request):
       if request.method=='POST':
            user = User.objects.get(id=request.session["user_id"])
            member = Member.objects.get(member_id = request.POST["member_id"])
            book = Book.objects.get(isbn = request.POST["isbn"])
            store=Book.objects.filter(isbn = book)
            def get_status(addbook):
                if addbook.status=="Not-Issued":
                    addbook.status="Issued"
                    obj= Order(user=user, member=member,book=book)
                    obj.save()
                    addbook.save()
                else:
                    messages.error(request," Book already issued !!!")
            category_list=list(set(map(get_status, store)))         
            issue=Order.objects.all()
            return render(request,'bookissue.html',{'Order':issue})
       return redirect('/')

def returnbooksubmission(request):
    if request.method=='POST':
            user = User.objects.get(id=request.session["user_id"])
            member = Member.objects.get(member_id = request.POST["member_id"])
            book = Book.objects.get(isbn = request.POST["isbn"])
            store=Book.objects.filter(isbn = book)
            def return_book(returnbook):
                if returnbook.status=="Issued":
                    returnbook.status="Not-Issued"
                    obj1=Return(user=user, member=member, book=book)
                    obj=Order.objects.filter(book=book)
                    obj.delete()
                    obj1.save()
                    returnbook.save()
                else:
                    messages.error(request," Book not issued !!!")
            returncategorylist=list(set(map(return_book, store)))
            ReturnBook= Return.objects.all()
            return render(request,'returnbook.html',{'Return':ReturnBook})
    return redirect('/')

def Search(request):
    if request.session.has_key('is_logged'):
        query2=request.GET["query2"]
        book=Book.objects.filter(title__icontains=query2)
        params={'Book':book}
        return render(request,'dashboard.html',params)
    return redirect("login") 

def editbookdetails(request,id):
    if request.session.has_key('is_logged'):
        book = Book.objects.get(id=id)
        return render(request,'editdetails.html',{'Book':book})
    return redirect('login')

def updatedetails(request,id):
    if request.session.has_key('is_logged'):
        if request.method=="POST":
                add=Book.objects.get(id=id)
                add.isbn=request.POST["isbn"]
                add.title=request.POST["title"]
                add.category=Category.objects.get(type=request.POST["category"])
                add.author=Author.objects.get(name=request.POST["author"])
                add.publisher=Publisher.objects.get(name=request.POST["publisher"])
                add.status=request.POST['status']
                add.save()
                return redirect("dashboard")
    return redirect('login')

def addstudent(request):
    if request.session.has_key('is_logged'):
       return render(request,'addstudent.html')
    return redirect ('login')

def viewstudents(request):
    if request.session.has_key('is_logged'):
        student=Member.objects.all()
        return render(request,'viewstudents.html',{'Student':student})
    return redirect('stafflogin')

def Searchstudent(request):
    if request.session.has_key('is_logged'):
        query3=request.GET["query3"]
        member=Member.objects.filter(name__icontains=query3)
        params={'Student':member}
        return render(request,'viewstudents.html',params)
    return redirect("stafflogin")

def addstudentsubmission(request):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            user = User.objects.get(id=request.session["user_id"])
            name = request.POST["name"]
            member_id = request.POST["member_id"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            add = Member(user = user,name=name,member_id=member_id, email=email, phone = phone)
            add.save()
            student = Member.objects.all()
            return render(request,'addstudent.html',{'Student':student})
    return redirect('/')

def viewissuedbook(request):
    if request.session.has_key('is_logged'):
        issuedbooks=Order.objects.all()
        lis=[]
        li=[]
        for books in issuedbooks:
            issdate=str(books.startTime.day)+'-'+str(books.startTime.month)+'-'+str(books.startTime.year)
            expdate=str(books.returnTime.day)+'-'+str(books.returnTime.month)+'-'+str(books.returnTime.year)
            #fine calculation
            days=(date.today()-books.startTime)
            d=days.days
            fine=0
            if d>15:
                day=d-15
                fine=day*10
            print(d)

            book=list(Book.objects.filter(isbn=books.book))
            member=list(Member.objects.filter(member_id=books.member))
            print(book)
            print(member)
            i=0
            for k in book:
                print(li)
                t=(member[i].name,member[i].member_id,book[i].isbn,book[i].title,issdate,expdate, fine)
                print(t)
                i=i+1
                lis.append(t)
                print(lis)

        return render(request,'viewissuedbook.html',{'lis':lis})
    return redirect('/')

