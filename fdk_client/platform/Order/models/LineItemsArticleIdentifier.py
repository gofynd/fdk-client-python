"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class LineItemsArticleIdentifier(BaseSchema):
    #  swagger.json

    
    sku_code = fields.Str(required=False)
    
