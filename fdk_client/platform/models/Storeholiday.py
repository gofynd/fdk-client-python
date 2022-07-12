"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class Storeholiday(BaseSchema):
    # CompanyProfile swagger.json

    
    end_date = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    year = fields.Int(required=False)
    
    start_date = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

