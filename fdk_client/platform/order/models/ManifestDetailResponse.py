"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ManifestPage import ManifestPage



from .ManifestDetailItem import ManifestDetailItem



from .ManifestDetail import ManifestDetail



class ManifestDetailResponse(BaseSchema):
    #  swagger.json

    
    additional_shipment_count = fields.Int(required=False)
    
    page = fields.Nested(ManifestPage, required=False)
    
    items = fields.List(fields.Nested(ManifestDetailItem, required=False), required=False)
    
    manifest_details = fields.List(fields.Nested(ManifestDetail, required=False), required=False)
    
