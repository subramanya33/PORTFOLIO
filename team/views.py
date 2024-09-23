from django.shortcuts import render, get_object_or_404
from .models import Teammate

# View to list all teammates
# View to list all teammates
def teammate_list(request):
    teammates = Teammate.objects.all()
    return render(request, 'teammate_list.html', {'teammates': teammates})

# View to display a specific teammate's resume
def teammate_detail(request, pk):
    teammate = get_object_or_404(Teammate, pk=pk)
    return render(request, 'teammate_detail.html', {'teammate': teammate})


