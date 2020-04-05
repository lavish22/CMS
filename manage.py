#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings.dev") 

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


#sudo ssh -i ec2_key_pair.pem ubuntu@18.234.240.181
