"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app import models as amod
from app import forms as aforms
import json
import urllib2

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def dashboard(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/dashboard.html',
        context_instance = RequestContext(request,
        {
            'title':'Dashboard',
            'message':'Data visualization powered by tableau',
        })
    )

def recommender(request):

    if request.body is not '':
        """Renders the recommender page."""
        user_id = 123
        data =  {
            "Inputs": {
                    "input1":
                    [
                        {
                                'book_id': request.POST.get('book_id'),
                                'user_id': user_id,
                                'rating': request.POST.get('rating'),
                        }
                    ],
            },
            "GlobalParameters":  {
            }
        }


        print('this is the data', data)

        body = str.encode(json.dumps(data))
        #change made added comment to push

        url = 'https://ussouthcentral.services.azureml.net/workspaces/1e5abc25594a4bfd8883528a2a6de4c0/services/8d38b183a3e446e19c0965b062196786/execute?api-version=2.0&format=swagger'
        api_key = 'FJhBLD2a3OHxabfD7fwpf5w8FwrnaGOHQ8KEMg+ymQgHife/biyzV6Cl9nE3Arn8Ystsp0nfjXjK+R/zlffENA==' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib2.Request(url, body, headers)

        try:
            response = urllib2.urlopen(req)

            result = response.read()
            result_data = json.loads(result)
            result_data=result_data['Results']
            result = result_data['output1']
            result = result[0]
            print(result)
            for book in result:
                print(book)


        except urllib2.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))
        assert isinstance(request, HttpRequest)

    if request.method == "POST":
        form = aforms.recommendForm(request.POST)

    else:
        result = None;
        form = aforms.recommendForm()

    return render(
        request,
        'app/recommender.html',
        context_instance = RequestContext(request,
        {
            'title':'Recommender',
            'message':'Find a few new books to try.',
            'form': form,
            'result': result,
        })

    )
