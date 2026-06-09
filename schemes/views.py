from django.shortcuts import get_object_or_404, render
from .models import Schemes
from users.models import userProfile
from django.db.models import Q

def scheme_list(request):
    schemes = Schemes.objects.all()

    # Filters from GET request
    lang = request.GET.get('lang', 'en')
    search_query = request.GET.get('search', '')  # Get search query
    category = request.GET.get('category')
    age = request.GET.get('age')
    state = request.GET.get('state')
    caste = request.GET.get('caste')
    profession = request.GET.get('profession')
    scheme_type = request.GET.get('type')  # Government or Private

    # Apply search filter using Q objects for OR conditions
    if search_query:
        schemes = schemes.filter(
            Q(title_en__icontains=search_query) | Q(description_en__icontains=search_query)
        )

    # Apply other filters
    if category:
        schemes = schemes.filter(category=category)
    if age:
        try:
            age = int(age)
            schemes = schemes.filter(age_limit__gte=age)
        except ValueError:
            pass  # ignore invalid age input
    if state:
        schemes = schemes.filter(state__icontains=state)
    if caste:
        schemes = schemes.filter(caste__icontains=caste)
    if profession:
        schemes = schemes.filter(profession__icontains=profession)
    if scheme_type:
        schemes = schemes.filter(scheme_type__iexact=scheme_type)

    # Language Translation for titles and descriptions
    localized_schemes = []
    for scheme in schemes:
        localized_schemes.append({
            'id': scheme.id,
            'title': getattr(scheme, f"title_{lang}", scheme.title_en),
            'description': getattr(scheme, f"description_{lang}", scheme.description_en),
            'category': scheme.category,
            'age_limit': scheme.age_limit,
            'income_limit': scheme.income_limit,
            'caste': scheme.caste,
            'state': scheme.state,
            'profession': scheme.profession,
            'scheme_type': scheme.get_localized_title(lang),
        })

    return render(request, 'schemes/scheme_list.html', {
        'schemes': localized_schemes,
        'selected_lang': lang
    })


def recommended_schemes(request):
    if request.user.is_authenticated:
        try:
            profile = userProfile.objects.get(user=request.user)
            # Match schemes where:
            # - User's age is less than or equal to the scheme's age limit (or age limit is 0 / unset)
            # - User's income is less than or equal to the scheme's income limit (or income limit is 0 / unset)
            # - Caste matches (or is 'All' or 'Open')
            # - State matches (or is 'All' or 'Central')
            # - Profession matches (or is 'All' or 'Any')
            schemes = Schemes.objects.filter(
                Q(age_limit__gte=profile.age) | Q(age_limit=0),
                Q(income_limit__gte=profile.income) | Q(income_limit=0),
                Q(caste__iexact=profile.cast) | Q(caste__iexact='all') | Q(caste__iexact='open'),
                Q(state__iexact=profile.state) | Q(state__iexact='all') | Q(state__iexact='central'),
                Q(profession__iexact=profile.profession) | Q(profession__iexact='all') | Q(profession__iexact='any')
            )

            # Boost recommendations based on life_stage or education_level if they match category
            if profile.life_stage or profile.education_level:
                schemes = schemes.filter(
                    Q(category__iexact=profile.life_stage) |
                    Q(category__iexact=profile.education_level) |
                    Q(category__isnull=True) |
                    Q(category='') |
                    Q(category__iexact='general')
                )

            scheme_type = request.GET.get('type')
            if scheme_type:
                schemes = schemes.filter(scheme_type__iexact=scheme_type)
        except userProfile.DoesNotExist:
            schemes = Schemes.objects.none()
    else:
        schemes = Schemes.objects.none()

    lang = request.GET.get('lang', 'en')
    if request.user.is_authenticated and not request.GET.get('lang'):
        if hasattr(request.user, 'userprofile') and request.user.userprofile.preferred_language:
            lang = request.user.userprofile.preferred_language

    localized_schemes = []
    for scheme in schemes:
        localized_schemes.append({
            'id': scheme.id,
            'title': getattr(scheme, f"title_{lang}", scheme.title_en),
            'description': getattr(scheme, f"description_{lang}", scheme.description_en),
            'scheme_type': scheme.scheme_type,
            'age_limit': scheme.age_limit,
            'income_limit': scheme.income_limit,
            'caste': scheme.caste,
            'state': scheme.state,
            'profession': scheme.profession,
        })

    return render(request, 'schemes/recommended_scheme.html', {
        'schemes': localized_schemes,
        'selected_lang': lang
    })



def scheme_detail(request, pk):
    lang = request.GET.get('lang', 'en')  # Default language is English
    if request.user.is_authenticated and not request.GET.get('lang'):
        if hasattr(request.user, 'userprofile') and request.user.userprofile.preferred_language:
            lang = request.user.userprofile.preferred_language
            
    scheme = get_object_or_404(Schemes, pk=pk)

    return render(request, 'schemes/scheme_details_page.html', {
        'scheme': scheme,
        'title': scheme.get_localized_title(lang),
        'description': scheme.get_localized_description(lang),
        'scheme_type': scheme.scheme_type,
        'age_limit': scheme.age_limit,
        'income_limit': scheme.income_limit,
        'caste': scheme.caste,
        'state': scheme.state,
        'profession': scheme.profession,
        'required_documents': scheme.required_documents.all(),
        'selected_lang': lang
    })
