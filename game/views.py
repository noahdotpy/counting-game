from django.shortcuts import render
from django.http import JsonResponse

from .models import Counter

# Create your views here.


def play(request):
    counter = Counter.objects.get(id=1)
    if request.method == 'POST':
        counter.count += 1
        counter.save()
        context = {"count": counter.count,
                   "formatted_count": "{:,}".format(counter.count)
                   }
        return JsonResponse(context)
    else:
        context = {
            "counter": counter.count,
            "formatted_count": "{:,}".format(counter.count),
        }
        return render(request, 'game/game.html', context)
