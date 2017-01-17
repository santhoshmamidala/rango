from django.shortcuts import render
from RangoApp.models import Category
from RangoApp.models import Page
from RangoApp.form import CategoryForm, PageForm
#from django.http import HttpResponse

def index(request):
    #return HttpResponse("Rango says 'Hey there world!'<br/> "
    #                    "<a href='/RangoApp/about'>About</a><br/>"
    #                    "<a href='/RangoApp/contact'>Contact</a>")
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}
    return render(request, 'RangoApp/index.html', context_dict)

def category(request, category_name_slug):
    # context dictionary which is passed to template rendering engine.
    context_dict = {'category_name_slug': category_name_slug}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages

        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        pass

    return render(request, 'RangoApp/category.html', context_dict)

def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()
    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'RangoApp/add_category.html', {'form': form})

def add_page(request, category_name_slug):

    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()

                return category(request, category_name_slug)

        else:
            print form.errors

    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat}

    return render(request, 'RangoApp/add_page.html', context_dict)