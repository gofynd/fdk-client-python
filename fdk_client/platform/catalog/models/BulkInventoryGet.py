"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Page import Page



from .BulkInventoryGetItems import BulkInventoryGetItems



class BulkInventoryGet(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(BulkInventoryGetItems, required=False), required=False)
    
