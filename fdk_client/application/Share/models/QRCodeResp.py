"""Share Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class QRCodeResp(BaseSchema):
    #  swagger.json

    
    link = fields.Str(required=False)
    
    svg = fields.Str(required=False)
    
