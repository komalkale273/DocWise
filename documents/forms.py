from django import forms
from .models import Documents

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['title_en', 'title_hi', 'title_mr', 
                  'description_en', 'description_hi', 'description_mr', 
                  'category', 'preferred_age', 'image', 
                  'required_for_application', 
                  'how_to_get_document_en', 'how_to_get_document_hi', 'how_to_get_document_mr', 
                  'issuing_authority']

    # You may want to include validation logic for the language fields here
