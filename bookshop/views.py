from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from .models import Category, Feedback, Product, Review, Subscriber
from django.views.generic import  DetailView
from cart.forms import CartAddProductForm
from django.contrib import messages
from blog.models import Blog
from bookstore.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import HttpResponse
import uuid
# Create your views here.

def index(request):
    top_five_products = Product.objects.all()[:4]
    # showing only 6 categoires in menu bar 
    categories = Category.objects.all()[:6]
    products = Product.objects.all()
    blogs = Blog.objects.all()

    context = {
        'categories':categories,
        'products':products,
        'top_five_products':top_five_products,
        'blogs': blogs,
    }

    return render(request,'bookshop/index.html', context)
    


    #total products display function
def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    return render(request,'bookshop/products_list.html',{'category':category,
                                                     'categories':categories,
                                                     'products':products})

    #single product vi

def product_detail(request, slug):
    product = get_object_or_404(Product,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    
    #getting product id for showing all review realted to one product
    reviewproduct = Product.objects.filter(slug=slug)
    prid = None
    for product_id in reviewproduct:
        prid = product_id.id

    all_reviews = Review.objects.filter(product=prid)
    
    return render(request,'bookshop/product_detail.html',{'product': product,'cart_product_form': cart_product_form,'all_reviews':all_reviews})

def all_Categories(request):
    categories = Category.objects.all()
    return render(request,'bookshop/all_category_list.html',{'categories':categories})



def contact_us(request):
    return render(request,'bookshop/contact_us.html')


def search_Result(request):
    if request.method== 'POST':
        searh_query = request.POST['search']
        query_result = Product.objects.filter(name__startswith=searh_query)
        return render(request,'bookshop/search.html',{'query_result':query_result,'searh_query':searh_query})


#review 
def Comment_Review(request,slug):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        rating = request.POST['rating']
        review_comment = request.POST['review']
        product = get_object_or_404(Product,slug=slug,available=True)
        comment_review = Review(product=product,name=name,email=email,rating=rating,review_comment=review_comment)
        comment_review.save()
        message = messages.success(request,"Your reviews is submitted")
        
        cart_product_form = CartAddProductForm()
        
        #getting product id for showing all review realted to one product
        reviewproduct = Product.objects.filter(slug=slug)
        prid = None
        for product_id in reviewproduct:
            prid = product_id.id

        all_reviews = Review.objects.filter(product=prid)
        
        context = {
            'product': product,
            'cart_product_form': cart_product_form,
            'all_reviews': all_reviews,
            'message': message,
        }

        return render(request,'bookshop/product_detail.html', context)

def about_us(request):
    return render(request,'bookshop/about-us.html')

def feedback(request):
    if request.method == 'POST':
        name = request.POST["contact_name"]
        email = request.POST["contact_email"]
        text = request.POST["contact_text"]
        feedback = Feedback(name=name,email=email,feedback=text)
        feedback.save()
        return render(request,'bookshop/feedback_created.html')

def subscribe(request):
    if request.method == "POST":
        subscriber = request.POST['subscribe']
        print(subscriber)
        email = Subscriber.objects.all().filter(email_address=subscriber)
        flag = True
        page_message = ""
        if email:
            check_email = Subscriber.objects.get(email_address=subscriber)
            if check_email.verified == False:
                page_message = "Check email to confirm your email"
            else:
                page_message = "Your account is already subscribed"
            flag = False
        else:
            flag = True
            token = str(uuid.uuid4())
            save_subscriber = Subscriber.objects.create(email_address=subscriber, token=token)
            subject = 'BookShelf: Confirmation email for subscriber'
            message = 'Welcome to our website, please click on the link bellow to confirm subscription to our shop \
                       basedjango.herokuapp.com/subscribe/confirm/'
            send_mail(subject, message + token, EMAIL_HOST_USER, [subscriber], fail_silently = False)
            page_message = "Email sent successfully to your account <br> \
                            Thank you for subscribing!<br> \
                            Please check your e-mail inbox to confirm your subscription. <br>"
        context = {
            'subscriber': subscriber,
            'message': page_message,
            'flag': flag,
        }

        return render(request, 'bookshop/subscriber.html', context)

def subscription_confirm(request, token):
    email = Subscriber.objects.get(token=token)
    email.verified = True
    email.subscribed = True
    email.save()

    context = {
        'email': email,
    }

    return render(request, 'bookshop/subscription_confirm.html', context)

def admin(request):
    return HttpResponse('success')

def user(request):
    return render(request, 'bookshop/user.html')