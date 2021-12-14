"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Credentials import Credentials




class Firebase(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(Credentials, required=False)
    
    enabled = fields.Boolean(required=False)
    

