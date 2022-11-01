"""Theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .GlobalSchemaProps import GlobalSchemaProps



class GlobalSchema(BaseSchema):
    #  swagger.json

    
    props = fields.List(fields.Nested(GlobalSchemaProps, required=False), required=False)
    
