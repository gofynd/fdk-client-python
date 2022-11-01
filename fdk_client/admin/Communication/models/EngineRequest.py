"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PayloadStructure import PayloadStructure



from .MetaStructure import MetaStructure



class EngineRequest(BaseSchema):
    #  swagger.json

    
    payload = fields.Nested(PayloadStructure, required=False)
    
    meta = fields.Nested(MetaStructure, required=False)
    
