# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class events_centre(models.Model):
    seqevent = models.IntegerField(primary_key=True)
    seqentitat = models.IntegerField()
    idtipus = models.IntegerField()
    seqorigen = models.IntegerField()
    seqorigen_fi = models.IntegerField(null=True, blank=True)
    fecha_validez = models.DateTimeField()
    fecha_invalidez = models.DateTimeField(null=True, blank=True)
    pto_loc = models.PointField(srid=4326)

    class Meta:
        ordering = ['seqentitat', 'idtipus']

    def __str__(self):
        return f"[SEQENTITAT={self.seqentitat}, SEQORIGEN={self.seqorigen}](tipus={self.idtipus})"


# Auto-generated `LayerMapping` dictionary for events_centre model
events_centre_mapping = {
    'seqevent': 'SEQEVENT',
    'seqentitat': 'SEQENTITAT',
    'idtipus': 'IDTIPUS',
    'seqorigen': 'SEQORIGEN',
    'seqorigen_fi': 'SEQORIGEN_FI',
    'fecha_validez': 'FECHA_VALIDEZ',
    'fecha_invalidez': 'FECHA_INVALIDEZ',
    'pto_loc': 'POINT',
}
