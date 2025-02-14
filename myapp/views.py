from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')


def results_page(request):
    print('results_page')
    if request.method == 'GET':
        # Assuming the form data is JSON and contains 'countries' and 'weights'
        form_data = request.GET
        countries = list(form_data.getlist('country'))
        weights = form_data.get('weight')
        _type = form_data.get('type')
        profile = form_data.get('profile')
        envelope = form_data.get('envelope')
        autonomy = form_data.get('autonomy')
        safety = form_data.get('safety')
        if weights == 'other':
            weights = form_data.get('otherWeight')
        if _type == 'other':
            _type = form_data.get('otherType')
        if profile == 'other':
            profile = form_data.get('otherProfile')
        if envelope == 'other':
            envelope = form_data.get('otherEnvelope')
        if autonomy == 'other':
            autonomy = form_data.get('otherAutonomy')
        if safety == 'other':
            safety = form_data.get('otherSafety')

        if "other" in countries:
            countries.remove('other')
            countries.append(form_data.get('otherCountry', ''))
        
        
        # Render results page with context data
        context = {
            'countries': countries,
            'weights': weights,
            'type': _type,
            'profile': profile,
            'envelope': envelope,
            'autonomy': autonomy,
            'safety': safety,
            'obj_file_url': '/static/D8_V1.obj',  # Path to your .obj file
        }

        print(context)
        return render(request, 'results.html', context)
    else:
        return render(request, 'results.html')
