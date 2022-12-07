"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class StatusesBodyResponse(BaseSchema):
    #  swagger.json

    
    shipments = fields.List(fields.Dict(required=False), required=False)
    
