""" Common Models for Public """

from marshmallow import EXCLUDE, Schema

"""Base Schema for Serializers."""
class BaseSchema(Schema):
    """Base Schema for marshmallow."""
    class Meta:
        """Meta to not throw error on unknown keys."""
        unknown = EXCLUDE
