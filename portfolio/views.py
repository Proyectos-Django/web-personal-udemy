from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    #=======================================================    
    # return HttpResponse(html_base + """
    #     <h2>Portafolio</h2>
    #     <p>Alguno de mis trabajos</p>
    # """)

    #========================================================
    #=> inyectar a la plantilla html el modelo de datos
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects': projects})