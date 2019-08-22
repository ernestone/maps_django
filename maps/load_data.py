import os
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource


def load_gpkg_lyr_to_model(model, model_mapping, path_gpkg, nom_lyr, verbose=True, progress=True):
    """

    Args:
        model:
        model_mapping:
        path_gpkg:
        nom_lyr:
        verbose:
        progress:
    """
    ds = DataSource(path_gpkg)
    lm = LayerMapping(model, ds, model_mapping, layer=nom_lyr, transform=False)
    lm.save(strict=True, verbose=verbose, progress=progress)
