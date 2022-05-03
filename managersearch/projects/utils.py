from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def search_projects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)


    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query)|
        Q(owner__name__icontains = search_query)|
        Q(tags__in=tags)
    )

    return projects, search_query


def paginate_projects(request, projects, results):

    page = request.GET.get('page')
    results = results
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages #give last page
        projects = paginator.page(page)

    #deal with long page numbers
    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 3)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)



    return custom_range, projects