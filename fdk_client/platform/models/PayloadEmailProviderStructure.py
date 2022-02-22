"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class PayloadEmailProviderStructure(BaseSchema):
    # Communication swagger.json

    
    _id = fields.Str(required=False)
    

