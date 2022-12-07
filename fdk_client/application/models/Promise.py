"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TimeStampData import TimeStampData




class Promise(BaseSchema):
    # Order swagger.json

    
    timestamp = fields.Nested(TimeStampData, required=False)
    
    show_promise = fields.Boolean(required=False)
    

