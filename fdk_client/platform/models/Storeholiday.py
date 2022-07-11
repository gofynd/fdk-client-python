"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class Storeholiday(BaseSchema):
    # CompanyProfile swagger.json

    
    name = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    year = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    

