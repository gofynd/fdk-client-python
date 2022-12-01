"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .AppFeature import AppFeature



class AppFeatureRequest(BaseSchema):
    #  swagger.json

    
    feature = fields.Nested(AppFeature, required=False)
    
