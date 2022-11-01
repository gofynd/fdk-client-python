"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class MarketplaceInfo(BaseSchema):
    #  swagger.json

    
    membership_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    date_of_joining = fields.Str(required=False)
    
