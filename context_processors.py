from fundraise.models import Category

def category_list(request):
    categories = Category.objects.all() # or whatever object you need
    return {'categories':categories}