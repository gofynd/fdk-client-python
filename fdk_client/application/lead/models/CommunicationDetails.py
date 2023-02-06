"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class CommunicationDetails(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
