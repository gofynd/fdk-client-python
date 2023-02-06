"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class KafkaMetaModel(BaseSchema):
    #  swagger.json

    
    job_type = fields.Str(required=False)
    
    batch_id = fields.Int(required=False)
    
    action = fields.Str(required=False)
    
    trace = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    created_timestamp = fields.Int(required=False)
    
