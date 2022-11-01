"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class ApefaceApiError(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
