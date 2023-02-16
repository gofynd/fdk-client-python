"""common Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Application import Application



class ApplicationResponse(BaseSchema):
    #  swagger.json

    
    application = fields.Nested(Application, required=False)
    
