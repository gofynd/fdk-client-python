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


class GeneratePOSReceipts(BaseSchema):
    pass


class SuccessResponseGeneratePOSReceipts(BaseSchema):
    pass


class BadRequestResponseGeneratePOSReceipts(BaseSchema):
    pass


class InternalErrorResponseGeneratePOSReceipts(BaseSchema):
    pass


class UserDetailsData(BaseSchema):
    pass


class LockData(BaseSchema):
    pass


class ShipmentTimeStamp(BaseSchema):
    pass


class BuyerDetails(BaseSchema):
    pass


class EInvoice(BaseSchema):
    pass


class EinvoiceInfo(BaseSchema):
    pass


class DebugInfo(BaseSchema):
    pass


class Formatted(BaseSchema):
    pass


class ShipmentMeta(BaseSchema):
    pass


class PDFLinks(BaseSchema):
    pass


class AffiliateMeta(BaseSchema):
    pass


class AffiliateDetails(BaseSchema):
    pass


class PlatformItem(BaseSchema):
    pass


class GSTDetailsData(BaseSchema):
    pass


class Prices(BaseSchema):
    pass


class BagStateMapper(BaseSchema):
    pass


class DPDetailsData(BaseSchema):
    pass


class Dimensions(BaseSchema):
    pass


class Meta(BaseSchema):
    pass


class OrderingStore(BaseSchema):
    pass


class FulfillingStore(BaseSchema):
    pass


class OrderBagArticle(BaseSchema):
    pass


class CurrentStatus(BaseSchema):
    pass


class BagGST(BaseSchema):
    pass


class PlatformDeliveryAddress(BaseSchema):
    pass


class Identifier(BaseSchema):
    pass


class FinancialBreakup(BaseSchema):
    pass


class BagConfigs(BaseSchema):
    pass


class DiscountRules(BaseSchema):
    pass


class ItemCriterias(BaseSchema):
    pass


class BuyRules(BaseSchema):
    pass


class AppliedPromos(BaseSchema):
    pass


class OrderBrandName(BaseSchema):
    pass


class OrderBags(BaseSchema):
    pass


class BagStatusHistory(BaseSchema):
    pass


class InvoiceInfo(BaseSchema):
    pass


class TrackingList(BaseSchema):
    pass


class ShipmentPayments(BaseSchema):
    pass


class OrderDetailsData(BaseSchema):
    pass


class ShipmentStatusData(BaseSchema):
    pass


class PlatformShipment(BaseSchema):
    pass


class OrderMeta(BaseSchema):
    pass


class OrderDict(BaseSchema):
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
    


class GeneratePOSReceipts(BaseSchema):
    # DocumentEngine swagger.json

    
    order = fields.Nested(OrderDict, required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    


class SuccessResponseGeneratePOSReceipts(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    invoice_receipt = fields.Str(required=False)
    
    payment_receipt = fields.Str(required=False)
    


class BadRequestResponseGeneratePOSReceipts(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.List(fields.Dict(required=False), required=False)
    


class InternalErrorResponseGeneratePOSReceipts(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    error = fields.Str(required=False)
    


class UserDetailsData(BaseSchema):
    # DocumentEngine swagger.json

    
    city = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    


class LockData(BaseSchema):
    # DocumentEngine swagger.json

    
    mto = fields.Boolean(required=False)
    
    locked = fields.Boolean(required=False)
    
    lock_message = fields.Str(required=False)
    


class ShipmentTimeStamp(BaseSchema):
    # DocumentEngine swagger.json

    
    t_min = fields.Str(required=False)
    
    t_max = fields.Str(required=False)
    


class BuyerDetails(BaseSchema):
    # DocumentEngine swagger.json

    
    ajio_site_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    


class EInvoice(BaseSchema):
    # DocumentEngine swagger.json

    
    signed_qr_code = fields.Str(required=False)
    
    signed_invoice = fields.Str(required=False)
    
    error_code = fields.Str(required=False)
    
    acknowledge_no = fields.Int(required=False)
    
    error_message = fields.Str(required=False)
    
    irn = fields.Str(required=False)
    
    acknowledge_date = fields.Str(required=False)
    


class EinvoiceInfo(BaseSchema):
    # DocumentEngine swagger.json

    
    credit_note = fields.Nested(EInvoice, required=False)
    
    invoice = fields.Nested(EInvoice, required=False)
    


class DebugInfo(BaseSchema):
    # DocumentEngine swagger.json

    
    stormbreaker_uuid = fields.Str(required=False)
    


class Formatted(BaseSchema):
    # DocumentEngine swagger.json

    
    f_max = fields.Str(required=False)
    
    f_min = fields.Str(required=False)
    


class ShipmentMeta(BaseSchema):
    # DocumentEngine swagger.json

    
    assign_dp_from_sb = fields.Boolean(required=False)
    
    shipment_volumetric_weight = fields.Float(required=False)
    
    lock_data = fields.Nested(LockData, required=False)
    
    shipment_weight = fields.Float(required=False)
    
    auto_trigger_dp_assignment_acf = fields.Boolean(required=False)
    
    dp_id = fields.Str(required=False)
    
    timestamp = fields.Nested(ShipmentTimeStamp, required=False)
    
    return_affiliate_shipment_id = fields.Str(required=False)
    
    store_invoice_updated_date = fields.Str(required=False)
    
    bag_weight = fields.Dict(required=False)
    
    forward_affiliate_order_id = fields.Str(required=False)
    
    b2b_buyer_details = fields.Nested(BuyerDetails, required=False)
    
    external = fields.Dict(required=False)
    
    dp_sort_key = fields.Str(required=False)
    
    ewaybill_info = fields.Dict(required=False)
    
    dp_options = fields.Dict(required=False)
    
    return_awb_number = fields.Str(required=False)
    
    dp_name = fields.Str(required=False)
    
    po_number = fields.Str(required=False)
    
    weight = fields.Int(required=False)
    
    due_date = fields.Str(required=False)
    
    same_store_available = fields.Boolean(required=False)
    
    packaging_name = fields.Str(required=False)
    
    fulfilment_priority_text = fields.Str(required=False)
    
    einvoice_info = fields.Nested(EinvoiceInfo, required=False)
    
    forward_affiliate_shipment_id = fields.Str(required=False)
    
    marketplace_store_id = fields.Str(required=False)
    
    return_affiliate_order_id = fields.Str(required=False)
    
    debug_info = fields.Nested(DebugInfo, required=False)
    
    awb_number = fields.Str(required=False)
    
    b2c_buyer_details = fields.Dict(required=False)
    
    order_type = fields.Str(required=False)
    
    formatted = fields.Nested(Formatted, required=False)
    
    return_details = fields.Dict(required=False)
    
    return_store_node = fields.Int(required=False)
    
    box_type = fields.Str(required=False)
    


class PDFLinks(BaseSchema):
    # DocumentEngine swagger.json

    
    credit_note_url = fields.Str(required=False)
    
    b2b = fields.Str(required=False)
    
    invoice_a4 = fields.Str(required=False)
    
    invoice = fields.Str(required=False)
    
    invoice_type = fields.Str(required=False)
    
    label_type = fields.Str(required=False)
    
    po_invoice = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    label_a6 = fields.Str(required=False)
    
    label_pos = fields.Str(required=False)
    
    label_a4 = fields.Str(required=False)
    
    invoice_pos = fields.Str(required=False)
    
    invoice_a6 = fields.Str(required=False)
    


class AffiliateMeta(BaseSchema):
    # DocumentEngine swagger.json

    
    coupon_code = fields.Str(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    size_level_total_qty = fields.Int(required=False)
    
    due_date = fields.Str(required=False)
    
    employee_discount = fields.Float(required=False)
    
    channel_shipment_id = fields.Str(required=False)
    
    is_priority = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    box_type = fields.Str(required=False)
    
    channel_order_id = fields.Str(required=False)
    
    order_item_id = fields.Str(required=False)
    


class AffiliateDetails(BaseSchema):
    # DocumentEngine swagger.json

    
    ad_id = fields.Str(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    shipment_meta = fields.Nested(ShipmentMeta, required=False)
    
    pdf_links = fields.Nested(PDFLinks, required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    company_affiliate_tag = fields.Str(required=False)
    
    affiliate_store_id = fields.Str(required=False)
    
    affiliate_meta = fields.Nested(AffiliateMeta, required=False)
    
    affiliate_bag_id = fields.Str(required=False)
    


class PlatformItem(BaseSchema):
    # DocumentEngine swagger.json

    
    size = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    l3_category_name = fields.Str(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Int(required=False)
    
    l3_category = fields.Int(required=False)
    
    department_id = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    images = fields.List(fields.Str(required=False), required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    


class GSTDetailsData(BaseSchema):
    # DocumentEngine swagger.json

    
    brand_calculated_amount = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    gstin_code = fields.Str(required=False)
    
    tax_collected_at_source = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    


class Prices(BaseSchema):
    # DocumentEngine swagger.json

    
    cod_charges = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    cashback = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    tax_collected_at_source = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    


class BagStateMapper(BaseSchema):
    # DocumentEngine swagger.json

    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    notify_customer = fields.Boolean(required=False)
    
    state_type = fields.Str(required=False)
    
    app_display_name = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    app_state_name = fields.Str(required=False)
    
    app_facing = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    bs_id = fields.Int(required=False)
    


class DPDetailsData(BaseSchema):
    # DocumentEngine swagger.json

    
    awb_no = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    amount_handling_charges = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    dp_charges = fields.Int(required=False)
    
    dp_return_charges = fields.Int(required=False)
    
    gst_tag = fields.Str(required=False)
    
    track_url = fields.Str(required=False)
    
    eway_bill_number = fields.Int(required=False)
    
    pincode = fields.Str(required=False)
    
    eway_bill_id = fields.Str(required=False)
    


class Dimensions(BaseSchema):
    # DocumentEngine swagger.json

    
    is_default = fields.Boolean(required=False)
    
    length = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    height = fields.Int(required=False)
    
    width = fields.Int(required=False)
    


class Meta(BaseSchema):
    # DocumentEngine swagger.json

    
    dimension = fields.Nested(Dimensions, required=False)
    


class OrderingStore(BaseSchema):
    # DocumentEngine swagger.json

    
    meta = fields.Dict(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    store_name = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    


class FulfillingStore(BaseSchema):
    # DocumentEngine swagger.json

    
    meta = fields.Dict(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    fulfillment_channel = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    store_name = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    


class OrderBagArticle(BaseSchema):
    # DocumentEngine swagger.json

    
    identifiers = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    return_config = fields.Dict(required=False)
    


class CurrentStatus(BaseSchema):
    # DocumentEngine swagger.json

    
    kafka_sync = fields.Boolean(required=False)
    
    store_id = fields.Int(required=False)
    
    state_id = fields.Int(required=False)
    
    delivery_awb_number = fields.Str(required=False)
    
    delivery_partner_id = fields.Int(required=False)
    
    bag_state_mapper = fields.Nested(BagStateMapper, required=False)
    
    bag_id = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    current_status_id = fields.Int(required=False)
    
    state_type = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    


class BagGST(BaseSchema):
    # DocumentEngine swagger.json

    
    hsn_code = fields.Str(required=False)
    
    gst_tax_percentage = fields.Int(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    gst_tag = fields.Str(required=False)
    
    gstin_code = fields.Str(required=False)
    
    gst_fee = fields.Float(required=False)
    
    is_default_hsn_code = fields.Boolean(required=False)
    


class PlatformDeliveryAddress(BaseSchema):
    # DocumentEngine swagger.json

    
    longitude = fields.Int(required=False)
    
    address_category = fields.Str(required=False)
    
    latitude = fields.Int(required=False)
    
    city = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    


class Identifier(BaseSchema):
    # DocumentEngine swagger.json

    
    ean = fields.Str(required=False)
    


class FinancialBreakup(BaseSchema):
    # DocumentEngine swagger.json

    
    item_name = fields.Str(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    price_effective = fields.Int(required=False)
    
    price_marked = fields.Int(required=False)
    
    fynd_credits = fields.Int(required=False)
    
    hsn_code = fields.Str(required=False)
    
    refund_credit = fields.Int(required=False)
    
    amount_paid = fields.Float(required=False)
    
    cashback = fields.Int(required=False)
    
    tax_collected_at_source = fields.Int(required=False)
    
    cashback_applied = fields.Int(required=False)
    
    discount = fields.Int(required=False)
    
    gst_tag = fields.Str(required=False)
    
    amount_paid_roundoff = fields.Int(required=False)
    
    total_units = fields.Int(required=False)
    
    coupon_value = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    
    cod_charges = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    gst_tax_percentage = fields.Int(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    transfer_price = fields.Int(required=False)
    
    delivery_charge = fields.Int(required=False)
    


class BagConfigs(BaseSchema):
    # DocumentEngine swagger.json

    
    enable_tracking = fields.Boolean(required=False)
    
    can_be_cancelled = fields.Boolean(required=False)
    
    allow_force_return = fields.Boolean(required=False)
    
    is_returnable = fields.Boolean(required=False)
    
    is_customer_return_allowed = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    


class DiscountRules(BaseSchema):
    # DocumentEngine swagger.json

    
    value = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class ItemCriterias(BaseSchema):
    # DocumentEngine swagger.json

    
    item_brand = fields.List(fields.Int(required=False), required=False)
    


class BuyRules(BaseSchema):
    # DocumentEngine swagger.json

    
    item_criteria = fields.Nested(ItemCriterias, required=False)
    
    cart_conditions = fields.Dict(required=False)
    


class AppliedPromos(BaseSchema):
    # DocumentEngine swagger.json

    
    promotion_name = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRules, required=False), required=False)
    
    promo_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    article_quantity = fields.Int(required=False)
    


class OrderBrandName(BaseSchema):
    # DocumentEngine swagger.json

    
    modified_on = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    


class OrderBags(BaseSchema):
    # DocumentEngine swagger.json

    
    bag_id = fields.Int(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    line_number = fields.Int(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    entity_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    quantity = fields.Int(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    identifier = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    can_return = fields.Boolean(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    


class BagStatusHistory(BaseSchema):
    # DocumentEngine swagger.json

    
    kafka_sync = fields.Boolean(required=False)
    
    store_id = fields.Int(required=False)
    
    state_id = fields.Int(required=False)
    
    delivery_awb_number = fields.Str(required=False)
    
    delivery_partner_id = fields.Int(required=False)
    
    bag_state_mapper = fields.Nested(BagStateMapper, required=False)
    
    bag_id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    app_display_name = fields.Str(required=False)
    
    state_type = fields.Str(required=False)
    
    bsh_id = fields.Int(required=False)
    
    forward = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    


class InvoiceInfo(BaseSchema):
    # DocumentEngine swagger.json

    
    store_invoice_id = fields.Str(required=False)
    
    credit_note_id = fields.Str(required=False)
    
    updated_date = fields.Str(required=False)
    
    label_url = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    


class TrackingList(BaseSchema):
    # DocumentEngine swagger.json

    
    time = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    
    text = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    is_current = fields.Boolean(required=False)
    


class ShipmentPayments(BaseSchema):
    # DocumentEngine swagger.json

    
    source = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class OrderDetailsData(BaseSchema):
    # DocumentEngine swagger.json

    
    cod_charges = fields.Str(required=False)
    
    order_value = fields.Str(required=False)
    
    tax_details = fields.Dict(required=False)
    
    order_date = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    ordering_channel_logo = fields.Dict(required=False)
    
    ordering_channel = fields.Str(required=False)
    


class ShipmentStatusData(BaseSchema):
    # DocumentEngine swagger.json

    
    id = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    bag_list = fields.List(fields.Str(required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    


class PlatformShipment(BaseSchema):
    # DocumentEngine swagger.json

    
    shipment_status = fields.Str(required=False)
    
    platform_logo = fields.Str(required=False)
    
    operational_status = fields.Str(required=False)
    
    ordering_store = fields.Nested(OrderingStore, required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    invoice_id = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    bags = fields.List(fields.Nested(OrderBags, required=False), required=False)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    packaging_type = fields.Str(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    invoice = fields.Nested(InvoiceInfo, required=False)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    lock_status = fields.Boolean(required=False)
    
    enable_dp_tracking = fields.Boolean(required=False)
    
    total_items = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    user_agent = fields.Str(required=False)
    
    vertical = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    priority_text = fields.Str(required=False)
    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    fulfilment_priority = fields.Int(required=False)
    
    coupon = fields.Dict(required=False)
    
    meta = fields.Nested(Meta, required=False)
    
    picked_date = fields.Str(required=False)
    
    total_bags = fields.Int(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    payment_mode = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    


class OrderMeta(BaseSchema):
    # DocumentEngine swagger.json

    
    cart_id = fields.Int(required=False)
    
    order_platform = fields.Str(required=False)
    
    mongo_cart_id = fields.Int(required=False)
    
    ordering_store = fields.Int(required=False)
    
    payment_type = fields.Str(required=False)
    
    order_child_entities = fields.List(fields.Str(required=False), required=False)
    
    order_tags = fields.List(fields.Dict(required=False), required=False)
    
    files = fields.List(fields.Dict(required=False), required=False)
    
    order_type = fields.Str(required=False)
    
    employee_id = fields.Int(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    customer_note = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    staff = fields.Dict(required=False)
    


class OrderDict(BaseSchema):
    # DocumentEngine swagger.json

    
    meta = fields.Nested(OrderMeta, required=False)
    
    payment_methods = fields.Dict(required=False)
    
    tax_details = fields.Dict(required=False)
    
    order_date = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    fynd_order_id = fields.Str(required=False)
    


