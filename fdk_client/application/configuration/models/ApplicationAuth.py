"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class ApplicationAuth(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
