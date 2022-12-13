"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BagDetailsPlatformResponse import BagDetailsPlatformResponse



from .Page1 import Page1



class GetBagsPlatformResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(BagDetailsPlatformResponse, required=False), required=False)
    
    page = fields.Nested(Page1, required=False)
    
