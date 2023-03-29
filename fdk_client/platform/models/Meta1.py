"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Meta1(BaseSchema):
    # Order swagger.json

    
    state_manager_used = fields.Str(required=False)
    
    kafka_emission_status = fields.Int(required=False)
    

