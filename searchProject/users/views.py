import json
import os
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def search_users(request):
    query = request.GET.get('first_name')

    if query is None:
        return JsonResponse({
            'error': '''Missing "name" parameter''',
            'details': '''Query parameter "name" is required'''
        }, status = 400)
    
    query = query.strip();

    if not query:
        return JsonResponse({
            'error': "Empty search query",
            "details": 'Search query cannot be empty'
        }, status = 400)

    json_path = os.path.join(settings.BASE_DIR, 'static', 'data', 'users.json');

    try:
        with open(json_path, 'r') as file:
            users = json.load(file);
        
        results = []
        for user in users:
            if query.lower() in user['first_name'].lower():
                results.append(user);

        return JsonResponse({
            'result': results,
            'count': len(results)
        });

    except FileNotFoundError:
        return JsonResponse({'error' : "Users file not found"}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON file'}, status=500)