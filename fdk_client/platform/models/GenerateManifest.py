"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class GenerateManifest(BaseSchema):
    # DocumentEngine swagger.json

    
    store_id = fields.Float(required=False)
    
    from_date = fields.Str(required=False)
    
    to_date = fields.Str(required=False)
    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    

