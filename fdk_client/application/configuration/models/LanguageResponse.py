"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .SupportedLanguage import SupportedLanguage



class LanguageResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(SupportedLanguage, required=False), required=False)
    
