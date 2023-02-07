"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductListingActionPage import ProductListingActionPage





class ProductListingAction(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(ProductListingActionPage, required=False)
    
    type = fields.Str(required=False)
    
