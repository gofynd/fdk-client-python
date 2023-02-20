"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ListViewItems import ListViewItems



from .ZoneDataItem import ZoneDataItem



from .ListViewSummary import ListViewSummary



class ListViewResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    
    summary = fields.List(fields.Nested(ListViewSummary, required=False), required=False)
    
