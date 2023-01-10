"""rewards Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PointsHistory import PointsHistory



from .Page import Page





class HistoryRes(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(PointsHistory, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    points = fields.Float(required=False)
    
