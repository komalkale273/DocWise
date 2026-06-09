from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Documents, ServiceCenter
from deep_translator import GoogleTranslator

def translate_text(text, target_lang):
    if not text or target_lang == 'en':
        return text
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        return text

def get_localized_document_data(document, lang):
    title = document.get_localized_title(lang)
    description = document.get_localized_description(lang)
    how_to_get = document.get_localized_how_to_get_document(lang)

    # For other regional languages, fallback to dynamic translation of the English content
    if lang not in ['en', 'hi', 'mr']:
        title = translate_text(document.title_en, lang)
        description = translate_text(document.description_en, lang)
        how_to_get = translate_text(document.how_to_get_document_en, lang)

    return title, description, how_to_get

def document_list(request):
    documents = Documents.objects.all()

    # Get filter parameters
    category = request.GET.get('category')
    query = request.GET.get('search')
    user_age = request.GET.get('age')
    state = request.GET.get('state')
    caste = request.GET.get('caste')
    profession = request.GET.get('profession')

    # Determine user's preferred language
    lang = 'en'
    if request.user.is_authenticated:
        if hasattr(request.user, 'userprofile') and request.user.userprofile.preferred_language:
            lang = request.user.userprofile.preferred_language

    # Apply filters
    if category:
        documents = documents.filter(category__icontains=category)

    if query:
        documents = documents.filter(Q(title_en__icontains=query) | Q(title_hi__icontains=query) | Q(title_mr__icontains=query))

    if user_age:
        try:
            user_age = int(user_age)
            documents = documents.filter(
                Q(min_age__lte=user_age) | Q(min_age__isnull=True),
                Q(max_age__gte=user_age) | Q(max_age__isnull=True)
            )
        except ValueError:
            pass

    if state:
        documents = documents.filter(Q(state__iexact=state) | Q(state__isnull=True) | Q(state=''))
    
    if caste:
        documents = documents.filter(Q(caste__iexact=caste) | Q(caste__isnull=True) | Q(caste=''))

    if profession:
        documents = documents.filter(Q(profession__iexact=profession) | Q(profession__isnull=True) | Q(profession=''))

    # Prepare localized documents
    localized_documents = []
    for document in documents:
        title, description, _ = get_localized_document_data(document, lang)
        localized_documents.append({
            'id': document.id,
            'title': title,
            'description': description,
            'category': document.category,
            'preferred_age': document.preferred_age,
            'image': document.image,
            'required_for_application': document.required_for_application,
            'issuing_authority': document.issuing_authority,
            'date_created': document.date_created,
        })

    return render(request, 'documents/document_list.html', {
        'documents': localized_documents,
        'category': category,
        'search_query': query,
        'user_age': user_age,
        'state': state,
        'caste': caste,
        'profession': profession,
        'selected_lang': lang,
    })

def document_detail(request, pk):
    document = get_object_or_404(Documents, pk=pk)

    # Determine user's preferred language
    lang = 'en'
    if request.user.is_authenticated:
        if hasattr(request.user, 'userprofile') and request.user.userprofile.preferred_language:
            lang = request.user.userprofile.preferred_language

    title, description, how_to_get = get_localized_document_data(document, lang)

    return render(request, 'documents/document_detail_page.html', {
        'title': title,
        'description': description,
        'how_to_get_document': how_to_get,
        'category': document.category,
        'preferred_age': document.preferred_age,
        'image': document.image,
        'issuing_authority': document.issuing_authority,
        'date_created': document.date_created,
        'selected_lang': lang,
    })

def center_list(request):
    centers = ServiceCenter.objects.all()

    # Get filter parameters
    state = request.GET.get('state', '')
    city = request.GET.get('city', '')
    center_type = request.GET.get('type', '')
    query = request.GET.get('search', '')

    if state:
        centers = centers.filter(state__icontains=state)
    if city:
        centers = centers.filter(city__icontains=city)
    if center_type:
        centers = centers.filter(center_type__iexact=center_type)
    if query:
        centers = centers.filter(
            Q(name__icontains=query) | Q(services_offered__icontains=query) | Q(address__icontains=query)
        )

    # Determine language for rendering consistency
    lang = 'en'
    if request.user.is_authenticated:
        if hasattr(request.user, 'userprofile') and request.user.userprofile.preferred_language:
            lang = request.user.userprofile.preferred_language

    return render(request, 'center_list.html', {
        'centers': centers,
        'state': state,
        'city': city,
        'center_type': center_type,
        'search_query': query,
        'selected_lang': lang,
    })
