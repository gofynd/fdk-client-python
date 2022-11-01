"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Stage import Stage



from .Stages import Stages



class Filters(BaseSchema):
    #  swagger.json

    
    stage = fields.Nested(Stage, required=False)
    
    stages = fields.Nested(Stages, required=False)
    
