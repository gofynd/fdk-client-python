"""share Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class RedirectDevice(BaseSchema):
    #  swagger.json

    
    link = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
