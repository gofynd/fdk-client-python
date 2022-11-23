"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Statuses import Statuses



class Filters(BaseSchema):
    #  swagger.json

    
    statuses = fields.List(fields.Nested(Statuses, required=False), required=False)
    
