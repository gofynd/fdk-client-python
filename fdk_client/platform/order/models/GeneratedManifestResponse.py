"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ManifestPage import ManifestPage



from .GeneratedManifestItem import GeneratedManifestItem



class GeneratedManifestResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(ManifestPage, required=False)
    
    items = fields.List(fields.Nested(GeneratedManifestItem, required=False), required=False)
    
