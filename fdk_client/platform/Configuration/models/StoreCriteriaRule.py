"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class StoreCriteriaRule(BaseSchema):
    #  swagger.json

    
    companies = fields.List(fields.Int(required=False), required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    
