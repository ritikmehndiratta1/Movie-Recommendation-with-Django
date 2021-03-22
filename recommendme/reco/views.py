from django.shortcuts import render
from . import model
import os
# Create your views here.

# index or home view
def index(request):
    # renders index.html
    return render(request,'reco/index.html')

# renders form_page.html when called
def formPage(request):
    return render(request,'reco/form_page.html')

# renders result.html
def result(request):

    # lis holds the input coming from form_page.html
    lis=[]
    lis.append(request.GET['movie_title_1'])
    lis.append(request.GET['movie_title_2'])
    lis.append(request.GET['movie_title_3'])
    
    try:
        # context_dict stores the resulting recommendationsd according to the input
        context_dict = model.movie_reco(lis[0],lis[1],lis[2])
        # result.html is rendered and the results of recommendation are passed alongwith
        return render(request,'reco/result.html',context=context_dict)
    except:
        # if the user inputs a name of the movie which is not in the database
        # or if the user inputs a garbage value redirect him to ooindex.html
        return render(request,'reco/ooindex.html')