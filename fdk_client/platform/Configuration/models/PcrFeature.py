"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class PcrFeature(BaseSchema):
    #  swagger.json

    
    staff_selection = fields.Boolean(required=False)
    
