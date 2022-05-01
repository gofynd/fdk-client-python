"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .KafkaMetaModel import KafkaMetaModel


class SuppressStorePayload(BaseSchema):
    # Inventory swagger.json

    
    payload = fields.List(fields.Nested(lambda: SuppressStorePayload(exclude=('payload')), required=False), required=False)
    
    meta = fields.Nested(KafkaMetaModel, required=False)
    

