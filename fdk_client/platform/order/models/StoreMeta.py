"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .EInvoicePortalDetails import EInvoicePortalDetails



from .StoreDocuments import StoreDocuments















from .StoreGstCredentials import StoreGstCredentials







class StoreMeta(BaseSchema):
    #  swagger.json

    
    einvoice_portal_details = fields.Nested(EInvoicePortalDetails, required=False)
    
    documents = fields.Nested(StoreDocuments, required=False)
    
    gst_number = fields.Str(required=False)
    
    product_return_config = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    additional_contact_details = fields.Dict(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    gst_credentials = fields.Nested(StoreGstCredentials, required=False)
    
    timing = fields.List(fields.Dict(required=False), required=False)
    
    ewaybill_portal_details = fields.Dict(required=False)
    
