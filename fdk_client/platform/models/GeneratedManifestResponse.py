"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GeneratedManifestItem import GeneratedManifestItem

from .ManifestPage import ManifestPage


class GeneratedManifestResponse(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(GeneratedManifestItem, required=False), required=False)
    
    page = fields.Nested(ManifestPage, required=False)
    

