# CMS

HOW TO RUN

1. add your ssh key to the settings
2. go to local --> git init --> then clone the repository
3. install pip3
4. install pipenv
5. run command --> pipenv shell
6. pip3 install -r requirements.txt
7. if you get some error like (unknown locale: UTF-8) run command --> export LC_ALL=en_US.UTF-8\nexport LANG=en_US.UTF-8
8. python3 manage.py createsuperuser
9. python3 manage.py makemigrations
10. python3 manage.py migrate
11. python3 manage.py runserver
