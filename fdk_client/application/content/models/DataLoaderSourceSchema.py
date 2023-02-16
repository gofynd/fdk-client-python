"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class DataLoaderSourceSchema(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
