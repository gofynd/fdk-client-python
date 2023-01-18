"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class SharedCartDetails(BaseSchema):
    #  swagger.json

    
    created_on = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    source = fields.Dict(required=False)
    
    token = fields.Str(required=False)
    
