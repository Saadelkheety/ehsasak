#!/usr/bin/env python
import os
import sys

from dotenv import load_dotenv

if __name__ == "__main__":

    # Read .env file and set key/value inside it as environement variables
    # see: http://github.com/theskumar/python-dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portofolio.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
