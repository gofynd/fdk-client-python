"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class HasPasswordSuccess(BaseSchema):
    #  swagger.json

    
    result = fields.Boolean(required=False)
    
