"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Store import Store



from .Page import Page



class StoreListingResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(Store, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
