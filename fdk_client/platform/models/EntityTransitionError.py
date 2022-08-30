"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class EntityTransitionError(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    error = fields.Str(required=False)
    
