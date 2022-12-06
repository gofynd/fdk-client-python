"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CreateOrderConfig import CreateOrderConfig



class CreateOrderConfigData(BaseSchema):
    #  swagger.json

    
    config_data = fields.Nested(CreateOrderConfig, required=False)
    
