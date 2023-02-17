"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class PostHistoryFilters(BaseSchema):
    #  swagger.json

    
    identifier = fields.Str(required=False)
    
    line_number = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
