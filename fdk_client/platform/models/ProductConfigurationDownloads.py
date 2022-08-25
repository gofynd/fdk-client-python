"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ProductConfigurationDownloads(BaseSchema):
    # Catalog swagger.json

    
    multivalue = fields.Boolean(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    

