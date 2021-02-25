#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings.dev") 

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


#ssh -i ~/Downloads/legalWay_keypair_prod.pem ubuntu@13.233.15.198
#python3 manage.py runserver --settings=cms.settings.production