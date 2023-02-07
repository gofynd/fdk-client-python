"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Language import Language



from .Language import Language



from .Language import Language



class LocaleLanguage(BaseSchema):
    #  swagger.json

    
    hi = fields.Nested(Language, required=False)
    
    ar = fields.Nested(Language, required=False)
    
    en_us = fields.Nested(Language, required=False)
    
