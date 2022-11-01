"""Inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PropBeanDTO import PropBeanDTO



from .PropBeanDTO import PropBeanDTO



from .PropBeanDTO import PropBeanDTO



from .PropBeanDTO import PropBeanDTO



class DefaultHeadersDTO(BaseSchema):
    #  swagger.json

    
    store = fields.Nested(PropBeanDTO, required=False)
    
    intf_article_id = fields.Nested(PropBeanDTO, required=False)
    
    price_effective = fields.Nested(PropBeanDTO, required=False)
    
    quantity = fields.Nested(PropBeanDTO, required=False)
    
