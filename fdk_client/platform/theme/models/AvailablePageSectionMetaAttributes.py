"""theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class AvailablePageSectionMetaAttributes(BaseSchema):
    #  swagger.json

    
    attributes = fields.Dict(required=False)
    
