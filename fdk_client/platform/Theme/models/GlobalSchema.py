"""Theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .GlobalSchemaProps import GlobalSchemaProps



class GlobalSchema(BaseSchema):
    #  swagger.json

    
    props = fields.List(fields.Nested(GlobalSchemaProps, required=False), required=False)
    
