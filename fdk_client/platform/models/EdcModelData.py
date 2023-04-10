"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class EdcModelData(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    models = fields.List(fields.Str(required=False), required=False)
    
    aggregator_id = fields.Int(required=False)
    

