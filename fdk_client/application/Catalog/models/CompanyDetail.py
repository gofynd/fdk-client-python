"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class CompanyDetail(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
