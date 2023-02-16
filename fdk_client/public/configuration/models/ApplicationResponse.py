"""configuration Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema




from .ApplicationData import ApplicationData



class ApplicationResponse(BaseSchema):
    #  swagger.json

    
    application = fields.Nested(ApplicationData, required=False)
    
