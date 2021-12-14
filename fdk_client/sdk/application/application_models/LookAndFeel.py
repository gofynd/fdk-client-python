"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class LookAndFeel(BaseSchema):
    # User swagger.json

    
    card_position = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    

