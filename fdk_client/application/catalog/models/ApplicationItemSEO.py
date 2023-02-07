"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ApplicationItemSEO(BaseSchema):
    #  swagger.json

    
    title = fields.Raw(required=False)
    
    description = fields.Raw(required=False)
    
