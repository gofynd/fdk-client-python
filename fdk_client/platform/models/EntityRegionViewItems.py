"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class EntityRegionViewItems(BaseSchema):
    # Serviceability swagger.json

    
    uid = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    

