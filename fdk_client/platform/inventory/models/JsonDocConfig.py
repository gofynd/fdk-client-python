"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PropBeanConfig import PropBeanConfig



class JsonDocConfig(BaseSchema):
    #  swagger.json

    
    prop_bean_configs = fields.List(fields.Nested(PropBeanConfig, required=False), required=False)
    
