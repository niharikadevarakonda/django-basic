from django.shortcuts import render

def student(request):
    data = {
        'name': 'Niharika',
        'age': 20,
        'course': 'B.Tech',
        'college': 'ISTS'
    }

    return render(request, 'student.html', data)