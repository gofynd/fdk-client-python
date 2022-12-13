"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class SharedCartDetails(BaseSchema):
    #  swagger.json

    
    token = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    source = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    user = fields.Dict(required=False)
    
