"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .GenericDTO import GenericDTO



class DataTresholdDTO(BaseSchema):
    #  swagger.json

    
    min_price = fields.Float(required=False)
    
    safe_stock = fields.Int(required=False)
    
    period_threshold = fields.Int(required=False)
    
    period_threshold_type = fields.Str(required=False)
    
    period_type_list = fields.List(fields.Nested(GenericDTO, required=False), required=False)
    
