"""Theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AvailablePageSchema import AvailablePageSchema



class AllAvailablePageSchema(BaseSchema):
    #  swagger.json

    
    pages = fields.List(fields.Nested(AvailablePageSchema, required=False), required=False)
    