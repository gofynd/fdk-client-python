"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class StatusesBody(BaseSchema):
    #  swagger.json

    
    status = fields.Str(required=False)
    
    exclude_bags_next_state = fields.Str(required=False)
    
    shipments = fields.Dict(required=False)
    
