"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .GetCatalogConfigurationDetailsProduct import GetCatalogConfigurationDetailsProduct



from .MetaDataListingResponse import MetaDataListingResponse



class GetCatalogConfigurationMetaData(BaseSchema):
    #  swagger.json

    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    
    listing = fields.Nested(MetaDataListingResponse, required=False)
    
