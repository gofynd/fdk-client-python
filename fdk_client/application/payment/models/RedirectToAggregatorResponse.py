"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .RedirectURL import RedirectURL





class RedirectToAggregatorResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(RedirectURL, required=False)
    
    success = fields.Boolean(required=False)
    
