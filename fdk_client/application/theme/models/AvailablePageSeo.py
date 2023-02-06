"""theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class AvailablePageSeo(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
