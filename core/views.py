from django.shortcuts import render, HttpResponse

# Create your views here.

#===============================================
#=> plantilla html de forma cruda en views
# html_base = """
# <h1>Mi web personal</h1>
# <ul>
#     <li><a href="/">Portada</a></li>
#     <li><a href="/about-me/">Acerca de</a></li>
#     <li><a href="/portfolio/">Portafolio</a></li>
#     <li><a href="/contact/">Contacto</a></li>
# </ul>
# """

def home(request):
    #============================================
    # html_response = "<h1>Mi web personal</h1>"
    # for i in range(10):
    #     html_response += "<h2>Portada</h2>"
    # return HttpResponse(html_response)

    #============================================
    #return HttpResponse("<h2>Portada</h2>")
    
    #============================================
    # return HttpResponse(html_base + """
    #     <h2>Portada</h2>
    #     <p>Esto es la portada</p>
    # """)

    #===========================================
    return render(request, "core/home.html")

def about(request):
    #=============================================================================================================
    #return HttpResponse("<h1>Mi web personal</h1><h2>Acerca de</h2><p>Me llamo Jhon Jairo y soy programador.</p>")
    #========================================================
    # return HttpResponse(html_base + """
    #     <h2>Acerca de</h2>
    #     <p>Me llamo Jhon Jairo y soy programador</p>
    # """)
    return render(request, "core/about.html")

def contact(request):
    #===============================================================================================================
    # return HttpResponse(html_base + """
    #     <h2>Contacto</h2>
    #     <p>Aqui dejo mi correo para preguntar dudas: <a href="jjmuesesq@unal.edu.co">jjmuesesq@unal.edu.co</a></p>
    # """)
    return render(request, "core/contact.html")
