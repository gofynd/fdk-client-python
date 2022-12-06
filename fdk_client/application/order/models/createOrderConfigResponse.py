"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class createOrderConfigResponse(BaseSchema):
    #  swagger.json

    
    is_upserted = fields.Boolean(required=False)
    
    acknowledged = fields.Boolean(required=False)
    
    is_inserted = fields.Boolean(required=False)
    
