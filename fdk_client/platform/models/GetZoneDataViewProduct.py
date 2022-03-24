"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class GetZoneDataViewProduct(BaseSchema):
    # Serviceability swagger.json

    
    count = fields.Int(required=False)
    
    type = fields.Str(required=False)
    

