"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class UpdateDialog(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    interval = fields.Int(required=False)
    
