from django.http import HttpResponse
import os
import sys


def index(request):
    return HttpResponse('Hello World')


# if __name__ == '__main__':
#     from django.core.management import execute_from_command_line
#     execute_from_command_line(sys.argv)
