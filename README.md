## (Run DB)

settings.py

 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'irr',
         'USER': 'user',
         'PASSWORD': 'postgres',
         'HOST': '127.0.0.1',
         'PORT': '5432',
     }
 }

docker run --name hunting_postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=user -e POSTGRES_DB=irr -p 5432:5432 -d postgres:13.0-alpine
