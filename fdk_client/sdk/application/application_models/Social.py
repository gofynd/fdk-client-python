"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class Social(BaseSchema):
    # User swagger.json

    
    account_kit = fields.Boolean(required=False)
    
    facebook = fields.Boolean(required=False)
    
    google = fields.Boolean(required=False)
    
    apple = fields.Boolean(required=False)
    

