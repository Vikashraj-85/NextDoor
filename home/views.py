from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, LoginForm,ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Inquiry,Review,Property ,PropertyImage
from .forms import PropertyForm 


def homePage(request):
    
    if request.method == "GET" :
        listing = Property.objects.all()
        reviews = Review.objects.all()
        
        data ={
            'data':listing,
            'reviews':reviews
        }
       
        return render(request,'index.html',data)
    
    

def servicePage(request):
     if request.method == "GET" :
        listing = Property.objects.all()
               
        data ={
            'data':listing,
           
        }
        return render(request,'service.html',data)
  
   

    
     


def contactPage(request):
    
    if request.method == "POST":
       
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Inquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        messages.success(request, "Message sent successfully!")

        return redirect('contact')

    return render(request, 'contact.html')
   

def test(request):
    return render(request,'test.html')



    # --------from django.shortcuts import render, redirect


    




def signup_view(request):
    

    if request.method == 'POST':

        

        form = SignupForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(request, 'Account Created Successfully')

            return redirect('/')

        else:
            print(form.errors)

    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })

# ==========user profile =================


def login_view(request):

 
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            print("form1")

            if user is not None:
                login(request, user)
                return redirect('/',)

    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render, redirect
from .forms import ProfileForm


from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile


def profile_view(request):

    # Get existing profile or create empty one
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            profile = form.save(commit=False)

            profile.user = request.user

            profile.save()

            return redirect('/')

    else:

        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {
        'form': form
    })
    
    # =====================================HOST ROOM ========================================
    # =====================================HOST ROOM ========================================
    
    
    # ============================
def host_room(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user
            property.save()
            
            # Handle multiple extra images
            extra_images = request.FILES.getlist('images')
            for image in extra_images:
                PropertyImage.objects.create(
                    property=property,
                    image=image
                )
            
            return redirect('/')
    else:
        form = PropertyForm()
    return render(request, 'host_room.html', {'form': form})








# =====================================  review  =============================
# =====================================  review  =============================





@login_required
def add_review(request):

    if request.method == "POST":

        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        Review.objects.create(
            user=request.user,
            rating=rating,
            comment=comment
        )

    return redirect('home')

def card_detail(request,id):
    if request.method == "GET" :
        card_details = get_object_or_404(Property, id=id)
        
        
        if card_details :
            data ={
                'property':card_details,
                
            }
            return render(request,'detail.html',data)
    
    return redirect('/') 
            

def view_payment(request,id):
    user = request.user 
    if request.method == "GET" :
        room_detail = Property.objects.get(id =id)
        
        data = {
            'data':room_detail,
            'user':user
            
        }
        return render(request,'payment.html',data)
    return redirect('/')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def forget_password(request):

    if request.method == "POST":

        email = request.POST.get('email')
        new_password = request.POST.get('password')

        try:

            user = User.objects.get(email=email)
            # reset password
            user.set_password(new_password)
            # save user
            user.save()
            messages.success(
                request,
                "Password Reset Successfully"
            )

            return redirect('login')

        except User.DoesNotExist:

            messages.error(
                request,
                "User Not Found"
            )

            return redirect('resetpass')

    return render(request, 'forget_password.html')