"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class AppLogisticsConfig(BaseSchema):
    #  swagger.json

    
    logistics_by_seller = fields.Boolean(required=False)
    
    serviceability_check = fields.Boolean(required=False)
    
    same_day_delivery = fields.Boolean(required=False)
    
    dp_assignment = fields.Boolean(required=False)
    
