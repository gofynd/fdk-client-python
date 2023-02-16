"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ShipmentItemFulFillingStore(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
