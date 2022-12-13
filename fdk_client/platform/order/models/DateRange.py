"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DateRange(BaseSchema):
    #  swagger.json

    
    to_date = fields.Str(required=False)
    
    from_date = fields.Str(required=False)
    
