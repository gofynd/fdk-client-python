"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class ProductListingActionPage(BaseSchema):
    #  swagger.json

    
    params = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
