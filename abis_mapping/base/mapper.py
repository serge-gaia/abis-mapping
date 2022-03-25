"""Provides Mapper Base Class for the Package"""


# Standard
import abc
import functools
import inspect
import json
import pathlib

# Third-Party
import frictionless
import rdflib

# Local
from . import types

# Typing
from typing import Any, Optional, final


class ABISMapper(abc.ABC):
    """ABIS Mapper Base Class"""

    # ABIS Mapper Registry
    registry: dict[str, type["ABISMapper"]] = {}

    # ABIS Mapper Template ID
    template_id: str = NotImplemented  # Must be implemented

    @abc.abstractmethod
    def apply_validation(
        self,
        data: types.CSVType,
        ) -> frictionless.Resource:
        """Applies Frictionless Validation to CSV.

        Args:
            data (CSVType): Readable CSV Type.

        Returns:
            frictionless.Resource: Validated CSV as a Frictionless Resource.
        """

    @abc.abstractmethod
    def apply_mapping(
        self,
        table: frictionless.Resource,
        ) -> rdflib.Graph:
        """Applies Mapping from Frictionless Resource to ABIS conformant RDF.

        Args:
            table (frictionless.Resource): Validated Frictionless Table.

        Returns:
            rdflib.Graph: ABIS Conformant RDF Graph.
        """

    @final
    @classmethod
    @functools.lru_cache
    def metadata(cls) -> dict[str, Any]:
        """Retrieves and Caches the Template Metadata for this Template

        Returns:
            dict[str, Any]: Template Metadata for this Template
        """
        # Retrieve Metadata Filepath
        directory = pathlib.Path(inspect.getfile(cls)).parent
        metadata_file = directory / "metadata.json"

        # Read Metadata and Return
        return json.loads(metadata_file.read_text())

    @final
    @classmethod
    @functools.lru_cache
    def schema(cls) -> dict[str, Any]:
        """Retrieves and Caches the Frictionless Schema for this Template

        Returns:
            dict[str, Any]: Frictionless Schema for this Template
        """
        # Retrieve Schema Filepath
        directory = pathlib.Path(inspect.getfile(cls)).parent
        schema_file = directory / "schema.json"

        # Read Schema and Return
        return json.loads(schema_file.read_text())

    @final
    @classmethod
    def register_mapper(
        cls,
        mapper: type["ABISMapper"],
        ) -> None:
        """Registers a concrete ABIS Mapper with the Base Class

        Args:
            mapper (type[ABISMapper]): Mapper to be registered.
        """
        # Register the mapper with its template id
        cls.registry[mapper.template_id] = mapper


def get_mapper(template_id: str) -> Optional[type[ABISMapper]]:
    """Retrieves ABIS Mapper class for the specified template ID.

    Args:
        template_id (str): Template ID to retrieve the mapper for.

    Returns:
        Optional[type[ABISMapper]]: ABIS mapper class associated with the
            specified template ID if found, otherwise `None`.
    """
    # Retrieve and return the mapper
    return ABISMapper.registry.get(template_id)


def get_mappers() -> dict[str, type[ABISMapper]]:
    """Retrieves the full registry of ABIS Mappers.

    Returns:
        dict[str, type[ABISMapper]]: Dictionary of template ID to ABIS Mapper.
    """
    # Retrieve and return the mappers
    return ABISMapper.registry
