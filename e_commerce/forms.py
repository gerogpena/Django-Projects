from django import forms
from .models import Product, Category, CartItem, Order, UserProfile, Review, ProductImage
from django.utils.text import slugify


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price']

    def __init__(self, *args,  **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        #self.fields['image'].widget.attrs['class'] = 'form-control'
        
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name:
            slug = slugify(name)
            cleaned_data['slug'] = slug
        return cleaned_data

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
        widgets = {'image': forms.ClearableFileInput(attrs={'multiple': True})}

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'parent']

    def __init__(self, *args,  **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['parent'].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name:
            slug = slugify(name)
            cleaned_data['slug'] = slug
        return cleaned_data



class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        # Exclude 'user' and 'total_amount' if you want to handle them programmatically


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        #fields = ('user', 'address', 'phone_number')
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)

