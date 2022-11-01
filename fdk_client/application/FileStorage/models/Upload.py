"""FileStorage Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class Upload(BaseSchema):
    #  swagger.json

    
    expiry = fields.Int(required=False)
    
    url = fields.Str(required=False)
    
