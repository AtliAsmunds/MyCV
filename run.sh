#!/bin/bash
kill $(ps aux | grep -E 'py(thon)? manage.py' | awk '{print $2}')

python manage.py sass-compiler --watch -nb &
python manage.py livereload &
yarn tsc --watch > /dev/null &
python manage.py runserver 

trap `kill $(ps aux | grep -E 'py(thon)? manage.py' | awk '{print $2}')` SIGINT