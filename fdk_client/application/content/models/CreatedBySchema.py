"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class CreatedBySchema(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
