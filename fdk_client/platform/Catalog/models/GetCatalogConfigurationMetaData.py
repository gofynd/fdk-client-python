"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .MetaDataListingResponse import MetaDataListingResponse



from .GetCatalogConfigurationDetailsProduct import GetCatalogConfigurationDetailsProduct



class GetCatalogConfigurationMetaData(BaseSchema):
    #  swagger.json

    
    listing = fields.Nested(MetaDataListingResponse, required=False)
    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    
