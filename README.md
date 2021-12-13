
python manage.py shell_plus

from galleries.models import *
gallery = Gallery.objects.all()

Photo.objects.filter(gallery__title__contains="st")


HEROCU

brew install heroku/brew/heroku  
heroku create 
git push heroku gallery

nano Procfile  
nano runtime.txt    
heroku ps:scale web=1 
heroku config:set DISABLE_COLLECTSTATIC=1
heroku run manage.py createsuperuser
heroku logs --tail
heroku open  