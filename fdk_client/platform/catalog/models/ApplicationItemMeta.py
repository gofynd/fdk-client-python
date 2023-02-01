"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .MetaFields import MetaFields



from .ApplicationItemMOQ import ApplicationItemMOQ





from .ApplicationItemSEO import ApplicationItemSEO









class ApplicationItemMeta(BaseSchema):
    #  swagger.json

    
    _custom_meta = fields.List(fields.Nested(MetaFields, required=False), required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    is_cod = fields.Boolean(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    alt_text = fields.Dict(required=False)
    
    is_gift = fields.Boolean(required=False)
    
