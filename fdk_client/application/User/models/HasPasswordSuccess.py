"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class HasPasswordSuccess(BaseSchema):
    #  swagger.json

    
    result = fields.Boolean(required=False)
    
