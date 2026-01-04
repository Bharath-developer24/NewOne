from django.shortcuts import render

# Create your views here.

def home_view(request):
    context = """Feane is all about serving tasty food with an Indian touch. We use fresh ingredients and authentic spices to create flavors that everyone loves. Fast service, great taste, and affordable meals — perfect for every mood and moment.Dine in, take away, or order online — enjoy food that feels familiar and satisfying."""
    return render(request, 'index.html',{"title":context})