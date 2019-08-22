docker-compose run web python manage.py makemigrations
rem # Migra todas las apps la database 'default'
rem docker-compose run web python manage.py migrate
rem # Migra aplicacion sobre database si hay multiples databases aplicadas (uso recomendado DATABASE_ROUTERS)
rem docker-compose run web python manage.py migrate maps --database db_postgis

rem Show migrations
rem docker-compose run web python manage.py showmigrations