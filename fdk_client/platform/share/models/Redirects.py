"""share Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .RedirectDevice import RedirectDevice



from .RedirectDevice import RedirectDevice



from .WebRedirect import WebRedirect





class Redirects(BaseSchema):
    #  swagger.json

    
    ios = fields.Nested(RedirectDevice, required=False)
    
    android = fields.Nested(RedirectDevice, required=False)
    
    web = fields.Nested(WebRedirect, required=False)
    
    force_web = fields.Boolean(required=False)
    
