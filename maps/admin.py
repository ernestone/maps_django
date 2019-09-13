from django.contrib.gis import admin
from .models import events_centre
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
#admin.site.register(events_centre, admin.GeoModelAdmin)
#admin.site.register(events_centre, admin.OSMGeoAdmin)

@admin.register(events_centre)
class event_centreAdmin(LeafletGeoAdmin):
    list_display = ['seqevent', 'seqentitat', 'idtipus', 'seqorigen', 'fecha_validez', 'seqorigen_fi']
    date_hierarchy = 'fecha_validez'

