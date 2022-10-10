"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class PackageDetails(BaseSchema):
    # DocumentEngine swagger.json

    
    package_id = fields.Str(required=False)
    
    item_quantity = fields.Str(required=False)
    
    package_type = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False)
    
    dimension = fields.Str(required=False)
    
    weight = fields.Str(required=False)
    

