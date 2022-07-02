from django.shortcuts import render
from django.http import JsonResponse

from .models import Counter

# Create your views here.
def play(request):
    # question = get_object_or_404(Question, id=1)
    # clicked_bool = Clicker.objects.get(id=request.POST["clicked"])
    # if clicked_bool:
    #     c = Clicker.objects.get(id=1)
    #     c.clicks += 1
    #     c.save()
    if request.method == 'POST':
        counter = Counter.objects.get(id=1)
        counter.count += 1
        counter.save()
        return JsonResponse({"count": counter.count})
    else:
        context = {
            "counter": Counter.objects.get(id=1)
        }
        return render(request, 'game/game.html', context)
