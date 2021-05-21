import logging

from django.db import connections

logger = logging.getLogger(__name__)


def species_list(request):

    species = []
    try:
        with connections['geosci'].cursor() as cursor:
            cursor.execute("SELECT species FROM observation")
            species = [row[0] for row in cursor.fetchall()]
    except Exception:
        logger.exception("Failed to query 'geosci' database")
    return {
        'species': species
    }
