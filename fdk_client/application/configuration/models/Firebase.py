"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Credentials import Credentials





class Firebase(BaseSchema):
    #  swagger.json

    
    credentials = fields.Nested(Credentials, required=False)
    
    enabled = fields.Boolean(required=False)
    
