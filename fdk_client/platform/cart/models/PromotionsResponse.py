"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PromotionListItem import PromotionListItem



from .Page import Page



class PromotionsResponse(BaseSchema):
    #  swagger.json

    
    items = fields.Nested(PromotionListItem, required=False)
    
    page = fields.Nested(Page, required=False)
    
