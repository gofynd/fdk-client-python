"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .EInvoicePortalDetails import EInvoicePortalDetails





from .StoreGstCredentials import StoreGstCredentials







from .StoreDocuments import StoreDocuments





class StoreMeta(BaseSchema):
    #  swagger.json

    
    gst_number = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    timing = fields.List(fields.Dict(required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    einvoice_portal_details = fields.Nested(EInvoicePortalDetails, required=False)
    
    product_return_config = fields.Dict(required=False)
    
    gst_credentials = fields.Nested(StoreGstCredentials, required=False)
    
    additional_contact_details = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    documents = fields.Nested(StoreDocuments, required=False)
    
    ewaybill_portal_details = fields.Dict(required=False)
    
