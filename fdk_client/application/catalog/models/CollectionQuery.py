"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class CollectionQuery(BaseSchema):
    #  swagger.json

    
    op = fields.Str(required=False)
    
    attribute = fields.Str(required=False)
    
    value = fields.List(fields.Raw(required=False), required=False)
    
