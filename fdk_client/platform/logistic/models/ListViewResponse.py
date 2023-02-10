"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ZoneDataItem import ZoneDataItem



from .ListViewSummary import ListViewSummary



from .ListViewItems import ListViewItems



class ListViewResponse(BaseSchema):
    #  swagger.json

    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    
    summary = fields.List(fields.Nested(ListViewSummary, required=False), required=False)
    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    
