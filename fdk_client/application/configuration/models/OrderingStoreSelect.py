"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class OrderingStoreSelect(BaseSchema):
    #  swagger.json

    
    uid = fields.Int(required=False)
    
