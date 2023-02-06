"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SuppressStoreModel import SuppressStoreModel



from .KafkaMetaModel import KafkaMetaModel



class SuppressStorePayload(BaseSchema):
    #  swagger.json

    
    payload = fields.List(fields.Nested(SuppressStoreModel, required=False), required=False)
    
    meta = fields.Nested(KafkaMetaModel, required=False)
    
