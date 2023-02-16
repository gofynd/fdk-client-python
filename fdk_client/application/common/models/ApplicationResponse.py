"""common Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ApplicationData import ApplicationData



class ApplicationResponse(BaseSchema):
    #  swagger.json

    
    application = fields.Nested(ApplicationData, required=False)
    
