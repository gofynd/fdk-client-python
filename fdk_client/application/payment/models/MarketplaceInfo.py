"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class MarketplaceInfo(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    date_of_joining = fields.Str(required=False)
    
    membership_id = fields.Str(required=False)
    
