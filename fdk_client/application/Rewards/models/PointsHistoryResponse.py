"""Rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PointsHistory import PointsHistory



from .Page import Page



class PointsHistoryResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(PointsHistory, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
