"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class PagePublishRequest(BaseSchema):
    #  swagger.json

    
    publish = fields.Boolean(required=False)
    
