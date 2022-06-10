"""Provides preparations vocabulary for the package"""


# Third-Party
import rdflib

# Local
from abis_mapping import utils


# Terms
ALCOHOL = utils.vocabs.Term(
    labels=("ALCOHOL", ),
    iri=utils.rdf.uri("preparations/alcohol", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)
DEEPFROZEN = utils.vocabs.Term(
    labels=("DEEPFROZEN", "DEEP FROZEN", "DEEP_FROZEN", "DEEP-FROZEN"),
    iri=utils.rdf.uri("preparations/deepFrozen", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)
DRIED = utils.vocabs.Term(
    labels=("DRIED", ),
    iri=utils.rdf.uri("preparations/dried", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)
DRIEDANDPRESSED = utils.vocabs.Term(
    labels=("DRIEDANDPRESSED", "DRIED AND PRESSED", "DRIED_AND_PRESSED", "DRIED-AND-PRESSED"),
    iri=utils.rdf.uri("preparations/driedAndPressed", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)
FORMALIN = utils.vocabs.Term(
    labels=("FORMALIN", ),
    iri=utils.rdf.uri("preparations/formalin", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)
FREEZEDRIED = utils.vocabs.Term(
    labels=("FREEZEDRIED", "FREEZE DRIED", "FREEZE_DRIED", "FREEZE-DRIED"),
    iri=utils.rdf.uri("preparations/freezeDried", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)
GLYCERIN = utils.vocabs.Term(
    labels=("GLYCERIN", ),
    iri=utils.rdf.uri("preparations/glycerin", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)
GUMARABIC = utils.vocabs.Term(
    labels=("GUMARABIC", ),
    iri=utils.rdf.uri("preparations/gumArabic", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)
MICROSCOPICPREPARATION = utils.vocabs.Term(
    labels=("MICROSCOPICPREPARATION", "MICROSCOPIC PREPARATION", "MICROSCOPIC_PREPARATION", "MICROSCOPIC-PREPARATION"),
    iri=utils.rdf.uri("preparations/microscopicPreparation", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)
MOUNTED = utils.vocabs.Term(
    labels=("MOUNTED", ),
    iri=utils.rdf.uri("preparations/mounted", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)
NOTREATMENT = utils.vocabs.Term(
    labels=("NOTREATMENT", "NO TREATMENT", "NO_TREATMENT", "NO-TREATMENT"),
    iri=utils.rdf.uri("preparations/noTreatment", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)
OTHER = utils.vocabs.Term(
    labels=("OTHER", ),
    iri=utils.rdf.uri("preparations/other", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)
PINNED = utils.vocabs.Term(
    labels=("PINNED", ),
    iri=utils.rdf.uri("preparations/pinned", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)
REFRIGERATED = utils.vocabs.Term(
    labels=("REFRIGERATED", ),
    iri=utils.rdf.uri("preparations/refrigerated", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
)

# Vocabulary
PREPARATIONS = utils.vocabs.FlexibleVocabulary(
    definition=rdflib.Literal("A type of preparations."),
    base=utils.rdf.uri("bdr-cv/attribute/preparations/"),
    scheme=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/dd085299-ae86-4371-ae15-61dfa432f924"),
    broader=utils.rdf.uri("bdr-cv/attribute/preparations", utils.namespaces.EXAMPLE),  # TODO -> Need real URI
    default=None,  # No default, ommitted if not provided
    terms=(
        ALCOHOL,
        DEEPFROZEN,
        DRIED,
        DRIEDANDPRESSED,
        FORMALIN,
        FREEZEDRIED,
        GLYCERIN,
        GUMARABIC,
        MICROSCOPICPREPARATION,
        MOUNTED,
        NOTREATMENT,
        OTHER,
        PINNED,
        REFRIGERATED,
    ),
)
