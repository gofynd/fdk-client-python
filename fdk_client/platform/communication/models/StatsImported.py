"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class StatsImported(BaseSchema):
    #  swagger.json

    
    count = fields.Int(required=False)
    
