"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Application import Application



from .ApplicationInventory import ApplicationInventory



class CreateAppResponse(BaseSchema):
    #  swagger.json

    
    app = fields.Nested(Application, required=False)
    
    configuration = fields.Nested(ApplicationInventory, required=False)
    
