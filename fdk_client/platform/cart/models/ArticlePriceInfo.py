"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BasePrice import BasePrice



from .BasePrice import BasePrice



class ArticlePriceInfo(BaseSchema):
    #  swagger.json

    
    converted = fields.Nested(BasePrice, required=False)
    
    base = fields.Nested(BasePrice, required=False)
    
