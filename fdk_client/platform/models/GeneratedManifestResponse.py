"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ManifestPage import ManifestPage

from .GeneratedManifestItem import GeneratedManifestItem


class GeneratedManifestResponse(BaseSchema):
    # Orders swagger.json

    
    page = fields.Nested(ManifestPage, required=False)
    
    items = fields.List(fields.Nested(GeneratedManifestItem, required=False), required=False)
    

