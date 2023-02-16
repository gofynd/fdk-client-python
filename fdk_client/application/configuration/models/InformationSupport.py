"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class InformationSupport(BaseSchema):
    #  swagger.json

    
    phone = fields.List(fields.Str(required=False), required=False)
    
    email = fields.List(fields.Str(required=False), required=False)
    
    timing = fields.Str(required=False)
    
