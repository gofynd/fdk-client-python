"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class Meta(BaseSchema):
    #  swagger.json

    
    source = fields.Str(required=False)
    
