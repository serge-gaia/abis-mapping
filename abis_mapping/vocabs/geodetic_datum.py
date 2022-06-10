"""Provides geodetic datum vocabulary for the package"""


# Third-Party
import rdflib

# Local
from abis_mapping import utils


# Terms
AGD84 = utils.vocabs.Term(
    labels=("AGD84", "EPSG:4203"),
    iri=rdflib.URIRef("http://www.opengis.net/def/crs/EPSG/9.9.1/4203"),
)
GDA2020 = utils.vocabs.Term(
    labels=("GDA2020", "EPSG:7844"),
    iri=rdflib.URIRef("http://www.opengis.net/def/crs/EPSG/9.9.1/7844"),
)
GDA94 = utils.vocabs.Term(
    labels=("GDA94", "EPSG:4283"),
    iri=rdflib.URIRef("http://www.opengis.net/def/crs/EPSG/9.9.1/4283"),
)
WGS84 = utils.vocabs.Term(
    labels=("WGS84", "EPSG:4326"),
    iri=rdflib.URIRef("http://www.opengis.net/def/crs/EPSG/0/4326"),
)

# Vocabulary
GEODETIC_DATUM = utils.vocabs.RestrictedVocabulary(
    terms=(AGD84, GDA2020, GDA94, WGS84),
)
