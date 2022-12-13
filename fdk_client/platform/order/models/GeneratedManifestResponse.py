"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .GeneratedManifestItem import GeneratedManifestItem



from .ManifestPage import ManifestPage



class GeneratedManifestResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(GeneratedManifestItem, required=False), required=False)
    
    page = fields.Nested(ManifestPage, required=False)
    
