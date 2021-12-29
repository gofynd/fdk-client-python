"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class Priority(BaseSchema):
    # Lead swagger.json

    
    key = fields.Str(required=False, validate=OneOf([val.value for val in PriorityEnum.__members__.values()]))
    
    display = fields.Str(required=False)
    
    color = fields.Str(required=False)
    

