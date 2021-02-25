# CMS

HOW TO RUN

1. add your ssh key to the settings
2. go to local --> `git init` --> then clone the repository
3. install pip3
4. install pipenv
5. run command --> `pipenv shell`
6. `pip3 install -r requirements.txt` make sure python3 in there in your `$PATH`
7. if you get some error like (unknown locale: UTF-8) run command --> `export LC_ALL=en_US.UTF-8 && export LANG=en_US.UTF-8`
8. `python3 manage.py createsuperuser`
9. `python3 manage.py makemigrations`
10. `python3 manage.py migrate`
11. `python3 manage.py runserver`
12. make sure you chg AWS credentials in code OR in `cat ~/.aws/credentials`
13. see the network call and create the S3 bucket accourdingly (give public access)
14. run `python manage.py collectstatic` to save the static files in S3 bucket
15. taking a regular backup is necessary - https://www.thegeekdiary.com/how-to-backup-and-restore-docker-containers/

