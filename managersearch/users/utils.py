from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Skill, Profile



def search_profiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)


    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) | 
    Q(short_intro__icontains=search_query)|
    Q(skill__in=skills))



    return profiles, search_query


def paginate_profiles(request, profiles, results):

    page = request.GET.get('page')
    results = results
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages #give last page
        profiles = paginator.page(page)

    #deal with long page numbers
    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 3)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)



    return custom_range, profiles