"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .App import App



from .AppInventory import AppInventory



from .AppDomain import AppDomain



class CreateApplicationRequest(BaseSchema):
    #  swagger.json

    
    app = fields.Nested(App, required=False)
    
    configuration = fields.Nested(AppInventory, required=False)
    
    domain = fields.Nested(AppDomain, required=False)
    
