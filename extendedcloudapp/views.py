from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect

# Create your views here.


from extendedcloudapp.forms import LoginRegister, ReceiverRegister, OwnerRegister, UploadForm, RequestForm

from extendedcloudapp.models import Upload, Owner, Receiver, Request


def index(request):
    return render(request, 'index.html')


def cenrtal_authority(request):
    return render(request, 'admin/central_authority.html')


def data_owner_register(request):
    login_form = LoginRegister()
    owner_form = OwnerRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        owner_form = OwnerRegister(request.POST)
        if login_form.is_valid() and owner_form.is_valid():
            l = login_form.save(commit=False)
            l.is_dataowner = True
            l.save()
            owner = owner_form.save(commit=False)
            owner.User = l
            owner.save()
            messages.info(request, 'data owner registered successfully')
            return redirect('login_view')
    return render(request, 'owner/data_owner_register.html', {'login_form': login_form, 'owner_form': owner_form})


def data_receiver_register(request):
    login_form = LoginRegister()
    receiver_form = ReceiverRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        receiver_form = ReceiverRegister(request.POST)
        if login_form.is_valid() and receiver_form.is_valid():
            l = login_form.save(commit=False)
            l.is_datareceiver = True
            l.save()
            receiver = receiver_form.save(commit=False)
            receiver.User = l
            receiver.save()
            messages.info(request, 'datareceiver registered successfully')
            return redirect('login_view')
    return render(request, 'receiver/data_receiver_register.html',
                  {'login_form': login_form, 'receiver_form': receiver_form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('central_authority')
            elif user.is_dataowner:
                return redirect('data_owner_panel')
            elif user.is_datareceiver:
                return redirect('data_receiver_panel')


    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')


def data_owner_panel(request):
    return render(request, 'owner/data_owner_panel.html')


def data_receiver_panel(request):
    return render(request, 'receiver/data_receiver_panel.html')


# FILE_TYPES = ['png', 'jpg', 'jpeg','pdf']

def upload_files_owner(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.User = request.user
            file.Files = request.FILES['Files']
            file_type = file.Files.url.split('.')[-1]
            file_type.lower()
            file.save()
            return render(request, 'owner/confirm_upload.html', {'file': file})
    context = {"form": form, }
    return render(request, 'owner/upload_owner.html', context)



def view_file(request):
    f = request.user
    u = Upload.objects.filter(User=f)
    return render(request, 'owner/owner_view_uploads.html', {'view_file': u})


def receiver_view_file(request):
    user = Upload.objects.all()
    return render(request, 'receiver/receiver_view_uploads.html', {'receiver_view_file': user})


def file_delete(request, id):
    u = Upload.objects.get(id=id)
    u.delete()
    return redirect('view_file')


def profile_view(request):
    u = request.user
    user = Owner.objects.filter(User=u)
    return render(request, 'owner/profile_view.html', {'user': user})

def owner_view(request):
    o=Owner.objects.all()
    return render(request,'admin/owner_view.html',{'Owner':o})

def owner_delete(request,id):
    n =Owner.objects.get(id=id)
    n.delete()
    return redirect('owner_view')

def view_profile(request):
    u = request.user
    user = Receiver.objects.filter(User=u)
    return render(request, 'receiver/view_profile.html', {'user': user})

def receiver_view(request):
    r=Receiver.objects.all()
    return render(request,'admin/receiver_view.html',{'Receiver':r})

def receiver_delete(request,id):
    n =Receiver.objects.get(id=id)
    n.delete()
    return redirect('receiver_view')


def send_request(request):
    form = RequestForm()
    u = request.user
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.User = u
            form.save()
            return redirect('send_request')
    else:
        return render(request, 'receiver/send_request.html', {'form': form})

def view_request(request):
    a = Request.objects.all()
    return render(request, 'admin/view_request.html', {'Request': a})

def confirm_request(request,id):
    req= Request.objects.get(id=id)
    req.Status = 1
    req.save()
    return redirect('view_request')

def reject_request(request,id):
    req= Request.objects.get(id=id)
    req.Status = 2
    req.save()
    return redirect('view_request')

def admin_view_file(request):
    us = Upload.objects.all()
    return render(request, 'admin/admin_view_uploads.html', {'admin_view_file': us})

def view_status(request):
    u= request.user
    req=Request.objects.filter(User=u)
    return render(request,'receiver/view_status.html', {'Request': req})

def view_user_download(request):
    req=Request.objects.filter(Status=1)
    return render(request,'owner/view_user_download.html', {'Request': req})
