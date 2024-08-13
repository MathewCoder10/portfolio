from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def home(request):
    return render (request,"home.html")

def about (request):
    return render (request,"about.html")

def projects (request):
    projects_show=[
        {
            'title': 'Leaf Shield - Android App ',
            'path': 'images/android2.11.jpeg',
        },
        {
            'title': 'Leaf Shield - Web App',
            'path': 'images/leaf.JPG',
        },
        {
            'title': 'Movie Recommender System',
            'path': 'images/movie.JPG',
        },

        {
            'title': 'Student Placement Predictor',
            'path': 'images/place.JPG',
        },
        {
            'title': 'Fashion Recommendation System',
            'path': 'images/fashion.JPG',
        },
        
        {
            'title': 'Portfolio',
            'path': 'images/port.JPG',
        },

    ]
    return render (request,"projects.html",{"projects_show": projects_show})

def experience(request):
    experience=[
        {"company":"ICT Academy of Kerala - Workshop",
         "position":"Learn Python by developing a website."},
        {"company":"Technovalley Software India Private Limited - Internship",
         "position":"python developer"},
        {"company":"BAABTRA, Kozhikode - Industrial Visit",
         "position":"python developer"},
        {"company":"Expertzlab Kochi - Course",
         "position":"Data Science with AI."}
    ]
    return render (request,"experience.html",{"experience":experience})

def certificate(request):
    return render (request, "certificate.html")

def contact(request):
    return render (request,"contact.html")
def resume(request):
    resume_path="myapp/MathewGeorge.pdf.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="MathewGeorge.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)



from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page after saving
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



def success(request):
    return render(request, 'success.html')
