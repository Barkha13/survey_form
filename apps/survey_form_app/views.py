from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request,"survey_form_app/index.html")

def survey_process(request):
    if 'name' not in request.session:
        request.session['name'] = ""
    if 'location' not in request.session:
        request.session['location']= "" 
    if 'language' not in request.session:    
        request.session['language'] = ""
    if 'comment' not in request.session:
        request.session['comment'] = ""
    if request.method == "POST":
        request.session['name'] = request.POST['your_name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

    return redirect('/result')

def result(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if request.method == "POST":
        request.session['count'] +=1
        del request.session['name']
        del request.session['location']
        del request.session['language']
        del request.session['comment']
        return redirect('/')
    else:
        return render(request,"survey_form_app/result.html")
