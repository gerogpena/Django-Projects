from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from .models import Product, Cart, CartItem, Order, OrderItem, Review, Category, UserProfile, ProductImage
from .forms import OrderForm, ProductForm, CategoryForm, ReviewForm, ProductImageForm


def add_product(request):
    
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)

        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()

            images = request.FILES.getlist('image')
            for index, image in enumerate(images):
                is_primary = False
                if index == 0:
                    is_primary = True

                product_image = ProductImage(product=product, image=image, is_primary=is_primary)
                product_image.save()

            return redirect('e_commerce:product_list')
    else:
        product_form = ProductForm()
        image_form = ProductImageForm()
    
    context ={
        'product_form': product_form, 
        'image_form': image_form,
    }

    return render(request, "e_commerce/add_product.html", context)

def add_category(request):
    
    if request.method == 'POST':
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            #instance = form.save()
            #instance.save()
            return redirect('e_commerce:product_list')

    else:
        form = CategoryForm()
    
    context ={
        'form':form
    }
    
    return render(request, "e_commerce/add_product_category.html", context)


def product_list(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        parent_categories = Category.objects.filter(parent=None).prefetch_related('children')
        
        primary_images = []
        for product in products:
            primary_image = product.images.filter(is_primary=True).first()
            primary_images.append(primary_image)
        zipped_data = zip(products, primary_images)

        try:
            # Get the cart for the specific user
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            # Cart does not exist, return 0 or handle the case accordingly
            cart = Cart.objects.create(user=request.user)


        item_count = CartItem.objects.filter(cart=cart).count()

        context = {
            'zipped_data': zipped_data,
            'parent_categories': parent_categories,
            'item_count' : item_count,
        }
        return render(request, "e_commerce/product_list.html", context)
    else:
        return redirect('users:login')


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    images = product.images.all()
    context ={
        'product': product,
        'images' : images,
    }
    return render(request, "e_commerce/product_detail.html", context)


def add_to_cart(request, slug):
    product = Product.objects.get(slug=slug)
    cart, created = Cart.objects.get_or_create(user=request.user)
    if request.user.is_authenticated:
        if request.method == 'POST':
           
            # Get the desired quantity from the request POST data
            quantity = int(request.POST['quantity'])

            # Check if the product is already in the cart
            cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product, quantity=quantity)

            # Update the quantity if the item is already in the cart
            if not item_created:
                cart_item.quantity += quantity
                cart_item.save()

            return redirect('e_commerce:product_list')
        
        context ={
                'product':product,
            }
        return render(request, "e_commerce/add_to_cart.html",context)

    else:
        return redirect('users:login')
    

def view_cart(request):
    if request.user.is_authenticated:
        try:
            cart_user=Cart.objects.get(user=request.user)
            cart_items = CartItem.objects.filter(cart=cart_user)

            total_price = sum(item.product.price * item.quantity for item in cart_items)
            if cart_items.exists():
                context ={
                    'cart_items' : cart_items,
                    'total_price': total_price,
                }
            else:
                context = {
                    'message': 'No records yet.'
                }
        
        except Cart.DoesNotExist:
              
            context = {
                'message': 'Cart is empty! ',
            }
            
        return render(request, "e_commerce/cart.html", context)
    
    else:
        return redirect('users:login')

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


def confirm_order(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.get(user=user)

        # Retrieve cart items
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        if request.method =='POST':

            order = Order.objects.get(cart=cart)
            order.total_amount = total_price
            order.save()

            # Place cart items into order items
            order_items = []
            for cart_item in cart_items:
                order_item = OrderItem(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )
                order_items.append(order_item)

             # Save the order items
            OrderItem.objects.bulk_create(order_items)

            # Clear the cart
            cart_items.delete()
            cart.order = order
            cart.save()
            
            return redirect('e_commerce:product_list')
        else:
            
            context = {
                'cart_items': cart_items,
                'total_price': total_price
            }

        return render(request,"e_commerce/confirm_order.html", context) 
     
    else:
        return redirect('users:login')  # Redirect to the login page if the user is not authenticated