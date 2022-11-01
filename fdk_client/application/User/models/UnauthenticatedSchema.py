"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class UnauthenticatedSchema(BaseSchema):
    #  swagger.json

    
    authenticated = fields.Boolean(required=False)
    
