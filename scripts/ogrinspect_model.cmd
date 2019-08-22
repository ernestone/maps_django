docker-compose run web python manage.py ogrinspect data/repo_gis/generals/GEOJSON/event_entitat_gis_vigents-punt_localitzacio.geo.json events_centre --srid=4326 --geom-name=pto_loc --mapping >> maps/models.py

docker-compose run web python manage.py ogrinspect /vsizip/data/repo_gis/versions/CSV/edificacio_ve.zip edificacio_ve --srid=4326 --geom-name=perimetre_base --mapping >> maps/models.py

docker-compose run web python manage.py ogrinspect data/repo_gis/versions/GPKG/repo_gis_versions.gpkg edificacio_ve-perimetre_base --srid=4326 --geom-name=perimetre_base --mapping >> maps/models.py