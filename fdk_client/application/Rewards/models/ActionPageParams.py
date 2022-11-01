"""Rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class ActionPageParams(BaseSchema):
    #  swagger.json

    
    slug = fields.List(fields.Str(required=False), required=False)
    
