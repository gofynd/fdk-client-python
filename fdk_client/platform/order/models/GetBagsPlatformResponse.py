"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Page1 import Page1



from .BagDetailsPlatformResponse import BagDetailsPlatformResponse



class GetBagsPlatformResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page1, required=False)
    
    items = fields.List(fields.Nested(BagDetailsPlatformResponse, required=False), required=False)
    
