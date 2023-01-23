"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BulkInventoryGetItems import BulkInventoryGetItems



from .Page import Page



class BulkInventoryGet(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(BulkInventoryGetItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
