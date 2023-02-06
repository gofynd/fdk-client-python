"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class KafkaResponse(BaseSchema):
    #  swagger.json

    
    offset = fields.Int(required=False)
    
    partition = fields.Int(required=False)
    
