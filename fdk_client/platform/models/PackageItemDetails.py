"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .PackageDetails import PackageDetails


class PackageItemDetails(BaseSchema):
    # DocumentEngine swagger.json

    
    jio_code = fields.Str(required=False)
    
    item_name = fields.Str(required=False)
    
    mrp = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    best_before_date = fields.Str(required=False)
    
    ean = fields.Str(required=False)
    
    package_details = fields.List(fields.Nested(PackageDetails, required=False), required=False)
    

