from django.shortcuts import render

# Create your views here.
# from django.views.decorators.cache import cache_page # we can do from url darect

# @cache_page(30)
def Home_page(request):
    # recipes = Recipe.objects.all()
    return render(request, 'per_viewaCache.html', {
        # 'recipes': recipes
    })


def Content_Page(request):
    return render(request,'content.html')


def view_Page(request):
    return render(request,'view.html')



