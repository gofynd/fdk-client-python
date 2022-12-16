"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class SupportedLanguage(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    