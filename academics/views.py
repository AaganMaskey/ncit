from django.shortcuts import render
from .models import Program, Semester

"""
    This module contains the methods and classes to handle HTTPRequest and 
    generate appropriate HTTPResponse.
"""


def program(request, code):
    """
    :type request: HTTPRequest
    :param request: carries request info

    :type code: int
    :param code: program code

    -> filters out the program on the basis of given program code
    -> if no program exists with that code, return 404
    -> otherwise, render program.html with context current_program


    """
    current_program = Program.objects.get(code=code)

    if current_program is None:
        return render(request, 'academics/404.html', {'error': '404 Page Not Found '})


    return render(request, 'academics/program.html', {'current_program': current_program})


def home(request):
    """

    :type request: HTTPRequest
    :param request: carries request info
    :return: renders home.html

    """
    return render(request, 'academics/home.html')


def facility(request):
    """

        :type request: HTTPRequest
        :param request: carries request info
        :return: renders facilities.html

        """
    return render(request, 'academics/facilities.html')


def scholarship(request):
    """

        :type request: HTTPRequest
        :param request: carries request info
        :return: renders scholarship.html

        """
    return render(request, 'academics/scholarship.html')


def handle404(request):
    """

           :type request: HTTPRequest
           :param request: carries request info
           :return: renders 404.html

           """
    return render(request, 'academics/404.html', {'error': '404 Page Not Found'})


