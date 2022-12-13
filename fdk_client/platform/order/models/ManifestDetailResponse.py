"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ManifestDetail import ManifestDetail



from .ManifestPage import ManifestPage





from .ManifestDetailItem import ManifestDetailItem



class ManifestDetailResponse(BaseSchema):
    #  swagger.json

    
    manifest_details = fields.List(fields.Nested(ManifestDetail, required=False), required=False)
    
    page = fields.Nested(ManifestPage, required=False)
    
    additional_shipment_count = fields.Int(required=False)
    
    items = fields.List(fields.Nested(ManifestDetailItem, required=False), required=False)
    
