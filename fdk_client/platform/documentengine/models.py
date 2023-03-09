"""DocumentEngine Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ..PlatformModel import BaseSchema





class GenerateBulkInvoiceLabelShipment(BaseSchema):
    pass


class GenerateBulkInvoiceOrLabelUrl(BaseSchema):
    pass


class DocumentType(BaseSchema):
    pass


class BulkListBadRequestResponse(BaseSchema):
    pass


class BulkListFailedResponse(BaseSchema):
    pass


class SuccessResponseGenerateBulkShipment(BaseSchema):
    pass


class SuccessResponseBulkStatus(BaseSchema):
    pass


class GenerateBulkUrlSuccessResponse(BaseSchema):
    pass


class InternalErrorResponseGenerateBulkShipment(BaseSchema):
    pass


class BadRequestResponseGenerateBulkUrl(BaseSchema):
    pass


class InternalErrorResponseGenerateBulkUrl(BaseSchema):
    pass


class GenerateBulkShipment(BaseSchema):
    pass


class GenerateBulkUrl(BaseSchema):
    pass


class GetBulkStatusRequest(BaseSchema):
    pass


class BadRequestResponseGenerateBulkItemParameters(BaseSchema):
    pass


class BadRequestResponseGenerateBulkItem(BaseSchema):
    pass


class SuccessResponseGenerateBulk(BaseSchema):
    pass


class BadRequestResponseGenerateBulk(BaseSchema):
    pass


class InternalErrorResponseGenerateBulk(BaseSchema):
    pass


class ShippingToAddress(BaseSchema):
    pass


class SellerAddress(BaseSchema):
    pass


class BoxDetails(BaseSchema):
    pass


class ShipmentDetails(BaseSchema):
    pass


class GenerateBulkBoxLabel(BaseSchema):
    pass


class GenerateBulkShipmentLabel(BaseSchema):
    pass


class GenerateNoc(BaseSchema):
    pass


class PackageDetails(BaseSchema):
    pass


class PackageItemDetails(BaseSchema):
    pass


class GenerateBulkPackageLabel(BaseSchema):
    pass


class SignedSuccessResponse(BaseSchema):
    pass


class BulkPresignedSuccessResponse(BaseSchema):
    pass


class SignedBadRequestResponse(BaseSchema):
    pass


class SignedFailedResponse(BaseSchema):
    pass


class StatusSuccessResponse(BaseSchema):
    pass


class StatusBadRequestResponse(BaseSchema):
    pass


class StatusFailedResponse(BaseSchema):
    pass


class GenerateManifest(BaseSchema):
    pass


class GeneratePresignedManifestUrl(BaseSchema):
    pass


class ManifestLink(BaseSchema):
    pass


class GenerateManifestUrlSuccessResponse(BaseSchema):
    pass


class ManifestListFailedResponse(BaseSchema):
    pass


class InvoiceLabelPresignedRequestBody(BaseSchema):
    pass





class GenerateBulkInvoiceLabelShipment(BaseSchema):
    # DocumentEngine swagger.json

    
    store_id = fields.Float(required=False)
    
    from_date = fields.Str(required=False)
    
    to_date = fields.Str(required=False)
    
    document_type = fields.Str(required=False)
    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    


class GenerateBulkInvoiceOrLabelUrl(BaseSchema):
    # DocumentEngine swagger.json

    
    uid = fields.Str(required=False)
    
    document_type = fields.Str(required=False)
    
    batch_id = fields.Float(required=False)
    


class DocumentType(BaseSchema):
    # DocumentEngine swagger.json

    
    invoice = fields.Str(required=False)
    
    label = fields.Str(required=False)
    


class BulkListBadRequestResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    


class BulkListFailedResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    


class SuccessResponseGenerateBulkShipment(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    job_id = fields.Float(required=False)
    
    trace_id = fields.Str(required=False)
    


class SuccessResponseBulkStatus(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    


class GenerateBulkUrlSuccessResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    url = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    expires_in = fields.Float(required=False)
    
    presigned_type = fields.Str(required=False)
    


class InternalErrorResponseGenerateBulkShipment(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    


class BadRequestResponseGenerateBulkUrl(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class InternalErrorResponseGenerateBulkUrl(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class GenerateBulkShipment(BaseSchema):
    # DocumentEngine swagger.json

    
    uid = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    document_type = fields.Str(required=False)
    


class GenerateBulkUrl(BaseSchema):
    # DocumentEngine swagger.json

    
    expires_in = fields.Float(required=False)
    
    document_type = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    


class GetBulkStatusRequest(BaseSchema):
    # DocumentEngine swagger.json

    
    batch_id = fields.Str(required=False)
    


class BadRequestResponseGenerateBulkItemParameters(BaseSchema):
    # DocumentEngine swagger.json

    
    missing_property = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class BadRequestResponseGenerateBulkItem(BaseSchema):
    # DocumentEngine swagger.json

    
    keyword = fields.Str(required=False)
    
    data_path = fields.Str(required=False)
    
    schema_path = fields.Str(required=False)
    
    parameters = fields.Nested(BadRequestResponseGenerateBulkItemParameters, required=False)
    
    message = fields.Str(required=False)
    


class SuccessResponseGenerateBulk(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    


class BadRequestResponseGenerateBulk(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error_message = fields.List(fields.Nested(BadRequestResponseGenerateBulkItem, required=False), required=False)
    


class InternalErrorResponseGenerateBulk(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error_message = fields.Str(required=False)
    


class ShippingToAddress(BaseSchema):
    # DocumentEngine swagger.json

    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    


class SellerAddress(BaseSchema):
    # DocumentEngine swagger.json

    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    


class BoxDetails(BaseSchema):
    # DocumentEngine swagger.json

    
    box_id = fields.Str(required=False)
    
    total_quantity = fields.Str(required=False)
    
    package_count = fields.Str(required=False)
    
    dimension = fields.Str(required=False)
    
    weight = fields.Str(required=False)
    


class ShipmentDetails(BaseSchema):
    # DocumentEngine swagger.json

    
    shipment_no = fields.Str(required=False)
    
    appointment_no = fields.Str(required=False)
    
    total_sku = fields.Str(required=False)
    
    item_qty = fields.Str(required=False)
    
    no_of_boxes = fields.Str(required=False)
    
    shipping_to = fields.Str(required=False)
    
    seller_name = fields.Str(required=False)
    
    gstin_number = fields.Str(required=False)
    
    shipping_address = fields.Nested(ShippingToAddress, required=False)
    
    seller_address = fields.Nested(SellerAddress, required=False)
    


class GenerateBulkBoxLabel(BaseSchema):
    # DocumentEngine swagger.json

    
    stock_transfer_id = fields.Str(required=False)
    
    label_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    seller_name = fields.Str(required=False)
    
    template_id = fields.Float(required=False)
    
    box_details = fields.List(fields.Nested(BoxDetails, required=False), required=False)
    


class GenerateBulkShipmentLabel(BaseSchema):
    # DocumentEngine swagger.json

    
    label_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    template_id = fields.Float(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentDetails, required=False), required=False)
    


class GenerateNoc(BaseSchema):
    # DocumentEngine swagger.json

    
    uid = fields.Str(required=False)
    
    seller_name = fields.Str(required=False)
    
    seller_gstin = fields.Str(required=False)
    
    fc_gstin = fields.Str(required=False)
    
    template_id = fields.Float(required=False)
    
    fc_address = fields.Nested(SellerAddress, required=False)
    
    seller_address = fields.Nested(SellerAddress, required=False)
    


class PackageDetails(BaseSchema):
    # DocumentEngine swagger.json

    
    package_id = fields.Str(required=False)
    
    item_quantity = fields.Str(required=False)
    
    package_type = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False)
    
    dimension = fields.Str(required=False)
    
    weight = fields.Str(required=False)
    


class PackageItemDetails(BaseSchema):
    # DocumentEngine swagger.json

    
    jio_code = fields.Str(required=False)
    
    item_name = fields.Str(required=False)
    
    mrp = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    best_before_date = fields.Str(required=False)
    
    ean = fields.Str(required=False)
    
    package_details = fields.List(fields.Nested(PackageDetails, required=False), required=False)
    


class GenerateBulkPackageLabel(BaseSchema):
    # DocumentEngine swagger.json

    
    stock_transfer_id = fields.Str(required=False)
    
    label_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    seller_name = fields.Str(required=False)
    
    template_id = fields.Float(required=False)
    
    item_details = fields.List(fields.Nested(PackageItemDetails, required=False), required=False)
    


class SignedSuccessResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    uid = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    expires_in = fields.Float(required=False)
    


class BulkPresignedSuccessResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    presigned_type = fields.Str(required=False)
    
    presigned_url = fields.Str(required=False)
    
    expires_in = fields.Float(required=False)
    


class SignedBadRequestResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error_message = fields.Str(required=False)
    


class SignedFailedResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error_message = fields.Str(required=False)
    


class StatusSuccessResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    


class StatusBadRequestResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error_message = fields.Str(required=False)
    


class StatusFailedResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error_message = fields.Str(required=False)
    


class GenerateManifest(BaseSchema):
    # DocumentEngine swagger.json

    
    store_id = fields.Float(required=False)
    
    from_date = fields.Str(required=False)
    
    to_date = fields.Str(required=False)
    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    


class GeneratePresignedManifestUrl(BaseSchema):
    # DocumentEngine swagger.json

    
    manifest_id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class ManifestLink(BaseSchema):
    # DocumentEngine swagger.json

    
    name = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    


class GenerateManifestUrlSuccessResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    url = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    
    expires_in = fields.Float(required=False)
    
    presigned_type = fields.Str(required=False)
    


class ManifestListFailedResponse(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    


class InvoiceLabelPresignedRequestBody(BaseSchema):
    # DocumentEngine swagger.json

    
    document_type = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    expires_in = fields.Float(required=False)
    


