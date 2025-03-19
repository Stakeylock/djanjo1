from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignupForm

def home_view(request):
    # Sample product list for demonstration
    products = [
        { 'id': 1, 'name': 'Wireless Headphones', 'price': 5999.00, 'image': 'headphones.jpg' },
        { 'id': 2, 'name': 'Smart Watch', 'price': 9999.00, 'image': 'smart_watch.jpg' },
        { 'id': 3, 'name': 'Bluetooth Speaker', 'price': 3999.00, 'image': 'bluetooth.jpg' },
        { 'id': 4, 'name': 'HD Webcam', 'price': 7999.00, 'image': 'cam.jpg' },
        { 'id': 5, 'name': 'Gaming Laptop', 'price': 75000.00, 'image': 'laptop.jpg' },
        { 'id': 6, 'name': 'Smartphone', 'price': 20000.00, 'image': 'smartphone.jpg' },
        { 'id': 7, 'name': 'Tablet', 'price': 15000.00, 'image': 'tablet.jpg' },
        { 'id': 8, 'name': 'Portable Charger', 'price': 2999.00, 'image': 'charger.jpg' },
        { 'id': 9, 'name': 'Gaming Mouse', 'price': 1999.00, 'image': 'mouse.jpg' },
        { 'id': 10, 'name': 'Mechanical Keyboard', 'price': 3499.00, 'image': 'keyboard.jpg' },
    ]
    return render(request, 'main_app/home.html', {'products': products})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'main_app/signup.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'main_app/profile.html')
