"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class Page(BaseSchema):
    pass


class ReplacementDetails(BaseSchema):
    pass


class AffiliateMeta(BaseSchema):
    pass


class AffiliateBagDetails(BaseSchema):
    pass


class PlatformArticleAttributes(BaseSchema):
    pass


class PlatformItem(BaseSchema):
    pass


class BagStateMapper(BaseSchema):
    pass


class BagStatusHistory(BaseSchema):
    pass


class ReturnConfig(BaseSchema):
    pass


class Weight(BaseSchema):
    pass


class Dimensions(BaseSchema):
    pass


class Article(BaseSchema):
    pass


class Dates(BaseSchema):
    pass


class GSTDetailsData(BaseSchema):
    pass


class ShipmentListingBrand(BaseSchema):
    pass


class Identifier(BaseSchema):
    pass


class FinancialBreakup(BaseSchema):
    pass


class BagReturnableCancelableStatus(BaseSchema):
    pass


class Prices(BaseSchema):
    pass


class BagUnit(BaseSchema):
    pass


class PlatformDeliveryAddress(BaseSchema):
    pass


class ShipmentStatus(BaseSchema):
    pass


class ShipmentTimeStamp(BaseSchema):
    pass


class Formatted(BaseSchema):
    pass


class LockData(BaseSchema):
    pass


class ShipmentTags(BaseSchema):
    pass


class ShipmentItemMeta(BaseSchema):
    pass


class ShipmentItemFulFillingStore(BaseSchema):
    pass


class UserDataInfo(BaseSchema):
    pass


class ShipmentListingChannel(BaseSchema):
    pass


class ShipmentItem(BaseSchema):
    pass


class ShipmentInternalPlatformViewResponse(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class AffiliateBagsDetails(BaseSchema):
    pass


class ReturnConfig1(BaseSchema):
    pass


class OrderBagArticle(BaseSchema):
    pass


class OrderBrandName(BaseSchema):
    pass


class CurrentStatus(BaseSchema):
    pass


class GiftCard(BaseSchema):
    pass


class B2BPODetails(BaseSchema):
    pass


class BagMeta(BaseSchema):
    pass


class ItemCriterias(BaseSchema):
    pass


class BuyRules(BaseSchema):
    pass


class DiscountRules(BaseSchema):
    pass


class AppliedPromos(BaseSchema):
    pass


class BagConfigs(BaseSchema):
    pass


class BagGST(BaseSchema):
    pass


class OrderBags(BaseSchema):
    pass


class PhoneDetails(BaseSchema):
    pass


class ContactDetails(BaseSchema):
    pass


class CompanyDetails(BaseSchema):
    pass


class TrackingList(BaseSchema):
    pass


class OrderingStoreDetails(BaseSchema):
    pass


class UserDetailsData(BaseSchema):
    pass


class ShipmentPayments(BaseSchema):
    pass


class EinvoiceInfo(BaseSchema):
    pass


class DebugInfo(BaseSchema):
    pass


class BuyerDetails(BaseSchema):
    pass


class ShipmentMeta(BaseSchema):
    pass


class InvoiceInfo(BaseSchema):
    pass


class PDFLinks(BaseSchema):
    pass


class AffiliateDetails(BaseSchema):
    pass


class OrderDetailsData(BaseSchema):
    pass


class DPDetailsData(BaseSchema):
    pass


class ShipmentDetails(BaseSchema):
    pass


class FulfillingStore(BaseSchema):
    pass


class ShipmentStatusData(BaseSchema):
    pass


class PlatformShipment(BaseSchema):
    pass


class ShipmentInfoResponse(BaseSchema):
    pass


class AssetByShipment(BaseSchema):
    pass


class ResponseGetAssetShipment(BaseSchema):
    pass


class PlatformUserDetails(BaseSchema):
    pass


class TransactionData(BaseSchema):
    pass


class BillingStaffDetails(BaseSchema):
    pass


class OrderMeta(BaseSchema):
    pass


class TaxDetails(BaseSchema):
    pass


class OrderDict(BaseSchema):
    pass


class ShipmentDetailsResponse(BaseSchema):
    pass


class SubLane(BaseSchema):
    pass


class SuperLane(BaseSchema):
    pass


class LaneConfigResponse(BaseSchema):
    pass


class PlatformChannel(BaseSchema):
    pass


class PlatformBreakupValues(BaseSchema):
    pass


class PlatformOrderItems(BaseSchema):
    pass


class OrderListingResponse(BaseSchema):
    pass


class Options(BaseSchema):
    pass


class MetricsCount(BaseSchema):
    pass


class MetricCountResponse(BaseSchema):
    pass


class PlatformTrack(BaseSchema):
    pass


class PlatformShipmentTrack(BaseSchema):
    pass


class FilterInfoOption(BaseSchema):
    pass


class FiltersInfo(BaseSchema):
    pass


class AdvanceFilterInfo(BaseSchema):
    pass


class FiltersResponse(BaseSchema):
    pass


class Success(BaseSchema):
    pass


class OmsReports(BaseSchema):
    pass


class JioCodeUpsertDataSet(BaseSchema):
    pass


class JioCodeUpsertPayload(BaseSchema):
    pass


class NestedErrorSchemaDataSet(BaseSchema):
    pass


class JioCodeUpsertResponse(BaseSchema):
    pass


class URL(BaseSchema):
    pass


class FileUploadResponse(BaseSchema):
    pass


class FileResponse(BaseSchema):
    pass


class BulkActionTemplate(BaseSchema):
    pass


class BulkActionTemplateResponse(BaseSchema):
    pass


class QuestionSet(BaseSchema):
    pass


class Reason(BaseSchema):
    pass


class PlatformShipmentReasonsResponse(BaseSchema):
    pass


class Attributes(BaseSchema):
    pass


class Item(BaseSchema):
    pass


class Brand(BaseSchema):
    pass


class ArticleDetails(BaseSchema):
    pass


class StoreAddress(BaseSchema):
    pass


class EInvoicePortalDetails(BaseSchema):
    pass


class StoreEinvoice(BaseSchema):
    pass


class StoreEwaybill(BaseSchema):
    pass


class StoreGstCredentials(BaseSchema):
    pass


class Document(BaseSchema):
    pass


class StoreDocuments(BaseSchema):
    pass


class StoreMeta(BaseSchema):
    pass


class Store(BaseSchema):
    pass


class BagGSTDetails(BaseSchema):
    pass


class BagReturnableCancelableStatus1(BaseSchema):
    pass


class BagDetailsPlatformResponse(BaseSchema):
    pass


class ErrorResponse(BaseSchema):
    pass


class BagsPage(BaseSchema):
    pass


class GetBagsPlatformResponse(BaseSchema):
    pass


class GeneratePosOrderReceiptResponse(BaseSchema):
    pass


class InvalidateShipmentCachePayload(BaseSchema):
    pass


class InvalidateShipmentCacheNestedResponse(BaseSchema):
    pass


class InvalidateShipmentCacheResponse(BaseSchema):
    pass


class ErrorResponse1(BaseSchema):
    pass


class StoreReassign(BaseSchema):
    pass


class StoreReassignResponse(BaseSchema):
    pass


class Entities(BaseSchema):
    pass


class UpdateShipmentLockPayload(BaseSchema):
    pass


class Bags(BaseSchema):
    pass


class OriginalFilter(BaseSchema):
    pass


class CheckResponse(BaseSchema):
    pass


class UpdateShipmentLockResponse(BaseSchema):
    pass


class AnnouncementResponse(BaseSchema):
    pass


class AnnouncementsResponse(BaseSchema):
    pass


class BaseResponse(BaseSchema):
    pass


class Click2CallResponse(BaseSchema):
    pass


class Products(BaseSchema):
    pass


class ProductsDataUpdatesFilters(BaseSchema):
    pass


class ProductsDataUpdates(BaseSchema):
    pass


class EntitiesDataUpdates(BaseSchema):
    pass


class DataUpdates(BaseSchema):
    pass


class ProductsReasonsData(BaseSchema):
    pass


class ProductsReasonsFilters(BaseSchema):
    pass


class ProductsReasons(BaseSchema):
    pass


class EntityReasonData(BaseSchema):
    pass


class EntitiesReasons(BaseSchema):
    pass


class ReasonsData(BaseSchema):
    pass


class ShipmentsRequest(BaseSchema):
    pass


class StatuesRequest(BaseSchema):
    pass


class UpdateShipmentStatusRequest(BaseSchema):
    pass


class ShipmentsResponse(BaseSchema):
    pass


class StatuesResponse(BaseSchema):
    pass


class UpdateShipmentStatusResponseBody(BaseSchema):
    pass


class OrderUser(BaseSchema):
    pass


class ArticleDetails1(BaseSchema):
    pass


class ShipmentDetails1(BaseSchema):
    pass


class LocationDetails(BaseSchema):
    pass


class ShipmentConfig(BaseSchema):
    pass


class ShipmentData(BaseSchema):
    pass


class MarketPlacePdf(BaseSchema):
    pass


class AffiliateBag(BaseSchema):
    pass


class UserData(BaseSchema):
    pass


class OrderPriority(BaseSchema):
    pass


class OrderInfo(BaseSchema):
    pass


class AffiliateStoreIdMapping(BaseSchema):
    pass


class AffiliateAppConfigMeta(BaseSchema):
    pass


class AffiliateAppConfig(BaseSchema):
    pass


class AffiliateInventoryOrderConfig(BaseSchema):
    pass


class AffiliateInventoryPaymentConfig(BaseSchema):
    pass


class AffiliateInventoryStoreConfig(BaseSchema):
    pass


class AffiliateInventoryArticleAssignmentConfig(BaseSchema):
    pass


class AffiliateInventoryLogisticsConfig(BaseSchema):
    pass


class AffiliateInventoryConfig(BaseSchema):
    pass


class AffiliateConfig(BaseSchema):
    pass


class Affiliate(BaseSchema):
    pass


class OrderConfig(BaseSchema):
    pass


class CreateOrderPayload(BaseSchema):
    pass


class CreateOrderResponse(BaseSchema):
    pass


class DispatchManifest(BaseSchema):
    pass


class SuccessResponse(BaseSchema):
    pass


class ActionInfo(BaseSchema):
    pass


class GetActionsResponse(BaseSchema):
    pass


class PostHistoryData(BaseSchema):
    pass


class PostHistoryFilters(BaseSchema):
    pass


class PostActivityHistory(BaseSchema):
    pass


class PostHistoryDict(BaseSchema):
    pass


class PostShipmentHistory(BaseSchema):
    pass


class HistoryDict(BaseSchema):
    pass


class ShipmentHistoryResponse(BaseSchema):
    pass


class ErrorDetail(BaseSchema):
    pass


class SmsDataPayload(BaseSchema):
    pass


class SendSmsPayload(BaseSchema):
    pass


class Meta(BaseSchema):
    pass


class ShipmentDetail(BaseSchema):
    pass


class OrderDetails(BaseSchema):
    pass


class OrderStatusData(BaseSchema):
    pass


class OrderStatusResult(BaseSchema):
    pass


class ManualAssignDPToShipment(BaseSchema):
    pass


class ManualAssignDPToShipmentResponse(BaseSchema):
    pass


class PaymentMethod(BaseSchema):
    pass


class PaymentInfo(BaseSchema):
    pass


class TaxInfo(BaseSchema):
    pass


class Tax(BaseSchema):
    pass


class Charge(BaseSchema):
    pass


class LineItem(BaseSchema):
    pass


class ProcessingDates(BaseSchema):
    pass


class Shipment(BaseSchema):
    pass


class ShippingInfo(BaseSchema):
    pass


class BillingInfo(BaseSchema):
    pass


class CreateOrderAPI(BaseSchema):
    pass


class CreateOrderErrorReponse(BaseSchema):
    pass


class PaymentMethods(BaseSchema):
    pass


class CreateChannelPaymentInfo(BaseSchema):
    pass


class DpConfiguration(BaseSchema):
    pass


class CreateChannelConfig(BaseSchema):
    pass


class CreateChannelConfigData(BaseSchema):
    pass


class CreateChannelConfigResponse(BaseSchema):
    pass


class CreateChannelConifgErrorResponse(BaseSchema):
    pass


class UploadConsent(BaseSchema):
    pass


class PlatformOrderUpdate(BaseSchema):
    pass


class ResponseDetail(BaseSchema):
    pass


class FyndOrderIdList(BaseSchema):
    pass


class OrderStatus(BaseSchema):
    pass





class Page(BaseSchema):
    # Order swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class ReplacementDetails(BaseSchema):
    # Order swagger.json

    
    original_affiliate_order_id = fields.Str(required=False)
    
    replacement_type = fields.Str(required=False)
    


class AffiliateMeta(BaseSchema):
    # Order swagger.json

    
    box_type = fields.Str(required=False)
    
    is_priority = fields.Boolean(required=False)
    
    channel_shipment_id = fields.Str(required=False)
    
    due_date = fields.Str(required=False)
    
    marketplace_invoice_id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    employee_discount = fields.Float(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    order_item_id = fields.Str(required=False)
    
    size_level_total_qty = fields.Int(required=False)
    
    channel_order_id = fields.Str(required=False)
    
    replacement_details = fields.Nested(ReplacementDetails, required=False)
    
    coupon_code = fields.Str(required=False)
    


class AffiliateBagDetails(BaseSchema):
    # Order swagger.json

    
    affiliate_bag_id = fields.Str(required=False)
    
    affiliate_meta = fields.Nested(AffiliateMeta, required=False)
    
    employee_discount = fields.Float(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    


class PlatformArticleAttributes(BaseSchema):
    # Order swagger.json

    
    currency = fields.Str(required=False)
    


class PlatformItem(BaseSchema):
    # Order swagger.json

    
    l3_category = fields.Int(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    brand_id = fields.Int(required=False)
    
    slug_key = fields.Str(required=False)
    
    brand = fields.Str(required=False)
    
    department_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    attributes = fields.Nested(PlatformArticleAttributes, required=False)
    
    branch_url = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    l2_category = fields.List(fields.Str(required=False), required=False)
    
    last_updated_at = fields.Str(required=False)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    images = fields.List(fields.Str(required=False), required=False)
    
    color = fields.Str(required=False)
    
    l3_category_name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    


class BagStateMapper(BaseSchema):
    # Order swagger.json

    
    display_name = fields.Str(required=False)
    
    app_state_name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    notify_customer = fields.Boolean(required=False)
    
    journey_type = fields.Str(required=False)
    
    state_type = fields.Str(required=False)
    
    app_facing = fields.Boolean(required=False)
    
    app_display_name = fields.Str(required=False)
    
    bs_id = fields.Int(required=False)
    


class BagStatusHistory(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    state_id = fields.Int(required=False)
    
    delivery_awb_number = fields.Str(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    bsh_id = fields.Int(required=False)
    
    kafka_sync = fields.Boolean(required=False)
    
    app_display_name = fields.Str(required=False)
    
    forward = fields.Boolean(required=False)
    
    bag_state_mapper = fields.Nested(BagStateMapper, required=False)
    
    bag_id = fields.Int(required=False)
    
    state_type = fields.Str(required=False)
    
    delivery_partner_id = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    


class ReturnConfig(BaseSchema):
    # Order swagger.json

    
    time = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    returnable = fields.Boolean(required=False)
    


class Weight(BaseSchema):
    # Order swagger.json

    
    is_default = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    
    shipping = fields.Int(required=False)
    


class Dimensions(BaseSchema):
    # Order swagger.json

    
    width = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    


class Article(BaseSchema):
    # Order swagger.json

    
    uid = fields.Str(required=False)
    
    esp_modified = fields.Boolean(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    _id = fields.Str(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    is_set = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    currency = fields.Dict(required=False)
    
    a_set = fields.Dict(required=False)
    
    identifiers = fields.Dict(required=False)
    
    child_details = fields.Dict(required=False)
    
    raw_meta = fields.Str(required=False)
    
    dimensions = fields.Nested(Dimensions, required=False)
    
    seller_identifier = fields.Str(required=False)
    


class Dates(BaseSchema):
    # Order swagger.json

    
    delivery_date = fields.Str(required=False)
    
    order_created = fields.Str(required=False)
    


class GSTDetailsData(BaseSchema):
    # Order swagger.json

    
    is_default_hsn_code = fields.Boolean(required=False)
    
    tax_collected_at_source = fields.Float(required=False)
    
    igst_tax_percentage = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    sgst_tax_percentage = fields.Float(required=False)
    
    igst_gst_fee = fields.Str(required=False)
    
    cgst_gst_fee = fields.Str(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    
    gstin_code = fields.Str(required=False)
    
    gst_tag = fields.Str(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    sgst_gst_fee = fields.Str(required=False)
    
    cgst_tax_percentage = fields.Float(required=False)
    


class ShipmentListingBrand(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo_base64 = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    


class Identifier(BaseSchema):
    # Order swagger.json

    
    sku_code = fields.Str(required=False)
    
    upc = fields.Str(required=False)
    
    alu = fields.Str(required=False)
    
    isbn = fields.Str(required=False)
    
    ean = fields.Str(required=False)
    


class FinancialBreakup(BaseSchema):
    # Order swagger.json

    
    transfer_price = fields.Int(required=False)
    
    cashback_applied = fields.Int(required=False)
    
    delivery_charge = fields.Int(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    fynd_credits = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    amount_paid_roundoff = fields.Int(required=False)
    
    gst_fee = fields.Float(required=False)
    
    gst_tag = fields.Str(required=False)
    
    discount = fields.Int(required=False)
    
    hsn_code = fields.Str(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    refund_credit = fields.Int(required=False)
    
    tax_collected_at_source = fields.Int(required=False)
    
    item_name = fields.Str(required=False)
    
    price_marked = fields.Int(required=False)
    
    cod_charges = fields.Int(required=False)
    
    coupon_value = fields.Float(required=False)
    
    price_effective = fields.Int(required=False)
    
    total_units = fields.Int(required=False)
    
    gst_tax_percentage = fields.Int(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    cashback = fields.Int(required=False)
    


class BagReturnableCancelableStatus(BaseSchema):
    # Order swagger.json

    
    is_active = fields.Boolean(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    can_be_cancelled = fields.Boolean(required=False)
    
    is_customer_return_allowed = fields.Boolean(required=False)
    
    is_returnable = fields.Boolean(required=False)
    


class Prices(BaseSchema):
    # Order swagger.json

    
    transfer_price = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    gift_price = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    pm_price_split = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    
    tax_collected_at_source = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    cashback = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    


class BagUnit(BaseSchema):
    # Order swagger.json

    
    can_cancel = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    size = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    bag_expiry_date = fields.Str(required=False)
    
    article = fields.Nested(Article, required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    gst = fields.Nested(GSTDetailsData, required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    brand = fields.Nested(ShipmentListingBrand, required=False)
    
    display_name = fields.Str(required=False)
    
    product_quantity = fields.Int(required=False)
    
    line_number = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    entity_type = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    bag_type = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    


class PlatformDeliveryAddress(BaseSchema):
    # Order swagger.json

    
    updated_at = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    latitude = fields.Int(required=False)
    
    longitude = fields.Int(required=False)
    
    address_type = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    address_category = fields.Str(required=False)
    


class ShipmentStatus(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    bag_list = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    shipment_id = fields.Str(required=False)
    
    shipment_status_id = fields.Int(required=False)
    
    current_shipment_status = fields.Str(required=False)
    
    status_created_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class ShipmentTimeStamp(BaseSchema):
    # Order swagger.json

    
    t_min = fields.Str(required=False)
    
    t_max = fields.Str(required=False)
    


class Formatted(BaseSchema):
    # Order swagger.json

    
    f_max = fields.Str(required=False)
    
    f_min = fields.Str(required=False)
    


class LockData(BaseSchema):
    # Order swagger.json

    
    locked = fields.Boolean(required=False)
    
    mto = fields.Boolean(required=False)
    
    lock_message = fields.Str(required=False)
    


class ShipmentTags(BaseSchema):
    # Order swagger.json

    
    slug = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    display_text = fields.Str(required=False)
    


class ShipmentItemMeta(BaseSchema):
    # Order swagger.json

    
    timestamp = fields.Nested(ShipmentTimeStamp, required=False)
    
    pdf_media = fields.List(fields.Dict(required=False), required=False)
    
    shipping_zone = fields.Str(required=False)
    
    assign_dp_from_sb = fields.Boolean(required=False)
    
    same_store_available = fields.Boolean(required=False)
    
    bag_weight = fields.Dict(required=False)
    
    dp_sort_key = fields.Str(required=False)
    
    tags = fields.List(fields.Dict(required=False), required=False)
    
    weight = fields.Float(required=False)
    
    dp_options = fields.Dict(required=False)
    
    debug_info = fields.Dict(required=False)
    
    auto_trigger_dp_assignment_acf = fields.Boolean(required=False)
    
    order_type = fields.Str(required=False)
    
    formatted = fields.Nested(Formatted, required=False)
    
    fulfilment_priority_text = fields.Str(required=False)
    
    packaging_name = fields.Str(required=False)
    
    activity_comment = fields.Str(required=False)
    
    ewaybill_info = fields.Dict(required=False)
    
    lock_data = fields.Nested(LockData, required=False)
    
    is_international = fields.Boolean(required=False)
    
    shipment_weight = fields.Float(required=False)
    
    shipment_volumetric_weight = fields.Float(required=False)
    
    existing_dp_list = fields.List(fields.Str(required=False), required=False)
    
    sla = fields.Float(required=False)
    
    shipment_tags = fields.List(fields.Nested(ShipmentTags, required=False), required=False)
    
    shipment_chargeable_weight = fields.Float(required=False)
    
    parent_dp_id = fields.Str(required=False)
    
    store_invoice_updated_date = fields.Str(required=False)
    
    external = fields.Dict(required=False)
    


class ShipmentItemFulFillingStore(BaseSchema):
    # Order swagger.json

    
    address = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    store_email = fields.Str(required=False)
    
    brand_store_tags = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    fulfilling_store_id = fields.Int(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    location_type = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    


class UserDataInfo(BaseSchema):
    # Order swagger.json

    
    uid = fields.Int(required=False)
    
    last_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    is_anonymous_user = fields.Boolean(required=False)
    
    avis_user_id = fields.Str(required=False)
    


class ShipmentListingChannel(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False)
    
    is_affiliate = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    channel_shipment_id = fields.Str(required=False)
    


class ShipmentItem(BaseSchema):
    # Order swagger.json

    
    previous_shipment_id = fields.Str(required=False)
    
    can_process = fields.Boolean(required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    ordering_channnel = fields.Str(required=False)
    
    total_bags = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    status_created_at = fields.Str(required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    meta = fields.Nested(ShipmentItemMeta, required=False)
    
    customer_note = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
    payment_mode = fields.Str(required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    shipment_id = fields.Str(required=False)
    
    estimated_sla_time = fields.Str(required=False)
    
    invoice_id = fields.Str(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    channel = fields.Nested(ShipmentListingChannel, required=False)
    
    order_date = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    payment_methods = fields.Dict(required=False)
    


class ShipmentInternalPlatformViewResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    lane = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    
    message = fields.Str(required=False)
    
    total_count = fields.Int(required=False)
    
    items = fields.List(fields.Nested(ShipmentItem, required=False), required=False)
    


class Error(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class AffiliateBagsDetails(BaseSchema):
    # Order swagger.json

    
    affiliate_bag_id = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    


class ReturnConfig1(BaseSchema):
    # Order swagger.json

    
    time = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
    returnable = fields.Boolean(required=False)
    


class OrderBagArticle(BaseSchema):
    # Order swagger.json

    
    size = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    identifiers = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    


class OrderBrandName(BaseSchema):
    # Order swagger.json

    
    modified_on = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class CurrentStatus(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    state_id = fields.Int(required=False)
    
    delivery_awb_number = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    kafka_sync = fields.Boolean(required=False)
    
    current_status_id = fields.Int(required=False)
    
    bag_state_mapper = fields.Nested(BagStateMapper, required=False)
    
    bag_id = fields.Int(required=False)
    
    state_type = fields.Str(required=False)
    
    delivery_partner_id = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    


class GiftCard(BaseSchema):
    # Order swagger.json

    
    gift_message = fields.Str(required=False)
    
    is_gift_applied = fields.Boolean(required=False)
    
    gift_price = fields.Int(required=False)
    
    display_text = fields.Str(required=False)
    


class B2BPODetails(BaseSchema):
    # Order swagger.json

    
    total_gst_percentage = fields.Float(required=False)
    
    po_line_amount = fields.Float(required=False)
    
    docker_number = fields.Str(required=False)
    
    po_tax_amount = fields.Float(required=False)
    
    partial_can_ret = fields.Boolean(required=False)
    
    item_base_price = fields.Float(required=False)
    


class BagMeta(BaseSchema):
    # Order swagger.json

    
    partial_can_ret = fields.Boolean(required=False)
    
    gift_card = fields.Nested(GiftCard, required=False)
    
    docket_number = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    group_id = fields.Str(required=False)
    
    custom_json = fields.Dict(required=False)
    
    b2b_po_details = fields.Nested(B2BPODetails, required=False)
    
    custom_message = fields.Str(required=False)
    


class ItemCriterias(BaseSchema):
    # Order swagger.json

    
    item_brand = fields.List(fields.Int(required=False), required=False)
    


class BuyRules(BaseSchema):
    # Order swagger.json

    
    item_criteria = fields.Nested(ItemCriterias, required=False)
    
    cart_conditions = fields.Dict(required=False)
    


class DiscountRules(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Int(required=False)
    


class AppliedPromos(BaseSchema):
    # Order swagger.json

    
    mrp_promotion = fields.Boolean(required=False)
    
    amount = fields.Float(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    article_quantity = fields.Int(required=False)
    
    promotion_type = fields.Str(required=False)
    
    promo_id = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRules, required=False), required=False)
    


class BagConfigs(BaseSchema):
    # Order swagger.json

    
    is_active = fields.Boolean(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    can_be_cancelled = fields.Boolean(required=False)
    
    is_returnable = fields.Boolean(required=False)
    
    is_customer_return_allowed = fields.Boolean(required=False)
    
    allow_force_return = fields.Boolean(required=False)
    


class BagGST(BaseSchema):
    # Order swagger.json

    
    is_default_hsn_code = fields.Boolean(required=False)
    
    igst_tax_percentage = fields.Float(required=False)
    
    tax_collected_at_source = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    sgst_tax_percentage = fields.Float(required=False)
    
    igst_gst_fee = fields.Str(required=False)
    
    cgst_gst_fee = fields.Str(required=False)
    
    gst_tax_percentage = fields.Int(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    gst_tag = fields.Str(required=False)
    
    gstin_code = fields.Str(required=False)
    
    gst_fee = fields.Float(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    sgst_gst_fee = fields.Str(required=False)
    
    cgst_tax_percentage = fields.Float(required=False)
    


class OrderBags(BaseSchema):
    # Order swagger.json

    
    can_cancel = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagsDetails, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    quantity = fields.Int(required=False)
    
    bag_id = fields.Int(required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    identifier = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    line_number = fields.Int(required=False)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    entity_type = fields.Str(required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    group_id = fields.Str(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    prices = fields.Nested(Prices, required=False)
    


class PhoneDetails(BaseSchema):
    # Order swagger.json

    
    country_code = fields.Int(required=False)
    
    mobile_number = fields.Str(required=False)
    


class ContactDetails(BaseSchema):
    # Order swagger.json

    
    emails = fields.List(fields.Str(required=False), required=False)
    
    phone = fields.List(fields.Nested(PhoneDetails, required=False), required=False)
    


class CompanyDetails(BaseSchema):
    # Order swagger.json

    
    company_name = fields.Str(required=False)
    
    company_cin = fields.Str(required=False)
    
    address = fields.Dict(required=False)
    
    company_contact = fields.Nested(ContactDetails, required=False)
    
    company_gst = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    


class TrackingList(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    
    time = fields.Str(required=False)
    
    is_current = fields.Boolean(required=False)
    
    text = fields.Str(required=False)
    


class OrderingStoreDetails(BaseSchema):
    # Order swagger.json

    
    address = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    store_name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    ordering_store_id = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    


class UserDetailsData(BaseSchema):
    # Order swagger.json

    
    address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    


class ShipmentPayments(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    


class EinvoiceInfo(BaseSchema):
    # Order swagger.json

    
    credit_note = fields.Dict(required=False)
    
    invoice = fields.Dict(required=False)
    


class DebugInfo(BaseSchema):
    # Order swagger.json

    
    stormbreaker_uuid = fields.Str(required=False)
    


class BuyerDetails(BaseSchema):
    # Order swagger.json

    
    address = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    ajio_site_id = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    


class ShipmentMeta(BaseSchema):
    # Order swagger.json

    
    awb_number = fields.Str(required=False)
    
    timestamp = fields.Nested(ShipmentTimeStamp, required=False)
    
    einvoice_info = fields.Nested(EinvoiceInfo, required=False)
    
    dp_id = fields.Str(required=False)
    
    return_affiliate_shipment_id = fields.Str(required=False)
    
    marketplace_store_id = fields.Str(required=False)
    
    assign_dp_from_sb = fields.Boolean(required=False)
    
    dimension = fields.Nested(Dimensions, required=False)
    
    same_store_available = fields.Boolean(required=False)
    
    bag_weight = fields.Dict(required=False)
    
    return_store_node = fields.Int(required=False)
    
    dp_sort_key = fields.Str(required=False)
    
    dp_name = fields.Str(required=False)
    
    weight = fields.Int(required=False)
    
    dp_options = fields.Dict(required=False)
    
    debug_info = fields.Nested(DebugInfo, required=False)
    
    store_invoice_updated_date = fields.Str(required=False)
    
    auto_trigger_dp_assignment_acf = fields.Boolean(required=False)
    
    order_type = fields.Str(required=False)
    
    formatted = fields.Nested(Formatted, required=False)
    
    box_type = fields.Str(required=False)
    
    fulfilment_priority_text = fields.Str(required=False)
    
    due_date = fields.Str(required=False)
    
    return_affiliate_order_id = fields.Str(required=False)
    
    packaging_name = fields.Str(required=False)
    
    return_awb_number = fields.Str(required=False)
    
    b2b_buyer_details = fields.Nested(BuyerDetails, required=False)
    
    ewaybill_info = fields.Dict(required=False)
    
    return_details = fields.Dict(required=False)
    
    lock_data = fields.Nested(LockData, required=False)
    
    po_number = fields.Str(required=False)
    
    shipment_weight = fields.Float(required=False)
    
    shipment_volumetric_weight = fields.Float(required=False)
    
    shipment_tags = fields.List(fields.Nested(ShipmentTags, required=False), required=False)
    
    b2c_buyer_details = fields.Dict(required=False)
    
    parent_dp_id = fields.Str(required=False)
    
    forward_affiliate_shipment_id = fields.Str(required=False)
    
    forward_affiliate_order_id = fields.Str(required=False)
    
    external = fields.Dict(required=False)
    


class InvoiceInfo(BaseSchema):
    # Order swagger.json

    
    updated_date = fields.Str(required=False)
    
    store_invoice_id = fields.Str(required=False)
    
    label_url = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    
    external_invoice_id = fields.Str(required=False)
    
    credit_note_id = fields.Str(required=False)
    


class PDFLinks(BaseSchema):
    # Order swagger.json

    
    invoice_a6 = fields.Str(required=False)
    
    b2b = fields.Str(required=False)
    
    invoice = fields.Str(required=False)
    
    label_a6 = fields.Str(required=False)
    
    invoice_a4 = fields.Str(required=False)
    
    invoice_pos = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    label_a4 = fields.Str(required=False)
    
    delivery_challan_a4 = fields.Str(required=False)
    
    credit_note_url = fields.Str(required=False)
    
    label_type = fields.Str(required=False)
    
    invoice_type = fields.Str(required=False)
    
    label_pos = fields.Str(required=False)
    
    po_invoice = fields.Str(required=False)
    


class AffiliateDetails(BaseSchema):
    # Order swagger.json

    
    affiliate_bag_id = fields.Str(required=False)
    
    company_affiliate_tag = fields.Str(required=False)
    
    affiliate_meta = fields.Nested(AffiliateMeta, required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    shipment_meta = fields.Nested(ShipmentMeta, required=False)
    
    ad_id = fields.Str(required=False)
    
    pdf_links = fields.Nested(PDFLinks, required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    affiliate_store_id = fields.Str(required=False)
    


class OrderDetailsData(BaseSchema):
    # Order swagger.json

    
    ordering_channel = fields.Str(required=False)
    
    ordering_channel_logo = fields.Dict(required=False)
    
    order_value = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    cod_charges = fields.Str(required=False)
    
    order_date = fields.Str(required=False)
    
    tax_details = fields.Dict(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    


class DPDetailsData(BaseSchema):
    # Order swagger.json

    
    awb_no = fields.Str(required=False)
    
    track_url = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    gst_tag = fields.Str(required=False)
    
    eway_bill_id = fields.Str(required=False)
    


class ShipmentDetails(BaseSchema):
    # Order swagger.json

    
    action_to_status = fields.Dict(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    lock_message = fields.Str(required=False)
    


class FulfillingStore(BaseSchema):
    # Order swagger.json

    
    address = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    store_name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    fulfillment_channel = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    


class ShipmentStatusData(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    bag_list = fields.List(fields.Str(required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    id = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    


class PlatformShipment(BaseSchema):
    # Order swagger.json

    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    bags = fields.List(fields.Nested(OrderBags, required=False), required=False)
    
    coupon = fields.Dict(required=False)
    
    journey_type = fields.Str(required=False)
    
    vertical = fields.Str(required=False)
    
    user_agent = fields.Str(required=False)
    
    enable_dp_tracking = fields.Boolean(required=False)
    
    company_details = fields.Nested(CompanyDetails, required=False)
    
    total_bags = fields.Int(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    operational_status = fields.Str(required=False)
    
    fulfilment_priority = fields.Int(required=False)
    
    packaging_type = fields.Str(required=False)
    
    priority_text = fields.Str(required=False)
    
    ordering_store = fields.Nested(OrderingStoreDetails, required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    dp_assignment = fields.Boolean(required=False)
    
    total_items = fields.Int(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    shipment_status = fields.Str(required=False)
    
    is_dp_assign_enabled = fields.Boolean(required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    meta = fields.Nested(ShipmentMeta, required=False)
    
    invoice = fields.Nested(InvoiceInfo, required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    shipment_details = fields.Nested(ShipmentDetails, required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    payment_mode = fields.Str(required=False)
    
    custom_message = fields.Str(required=False)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    shipment_id = fields.Str(required=False)
    
    picked_date = fields.Str(required=False)
    
    estimated_sla_time = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    invoice_id = fields.Str(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    can_update_dimension = fields.Boolean(required=False)
    
    forward_shipment_id = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    payment_methods = fields.Dict(required=False)
    
    platform_logo = fields.Str(required=False)
    


class ShipmentInfoResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    


class AssetByShipment(BaseSchema):
    # Order swagger.json

    
    assets = fields.Dict(required=False)
    
    shipment_id = fields.Str(required=False)
    
    expires_in = fields.Str(required=False)
    


class ResponseGetAssetShipment(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    presigned_type = fields.Str(required=False)
    
    result = fields.List(fields.Nested(AssetByShipment, required=False), required=False)
    


class PlatformUserDetails(BaseSchema):
    # Order swagger.json

    
    platform_user_last_name = fields.Str(required=False)
    
    platform_user_employee_code = fields.Str(required=False)
    
    platform_user_first_name = fields.Str(required=False)
    
    platform_user_id = fields.Str(required=False)
    


class TransactionData(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    amount_paid = fields.Float(required=False)
    
    entity = fields.Str(required=False)
    
    terminal_id = fields.Str(required=False)
    
    unique_reference_number = fields.Str(required=False)
    
    transaction_id = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    


class BillingStaffDetails(BaseSchema):
    # Order swagger.json

    
    user = fields.Str(required=False)
    
    employee_code = fields.Str(required=False)
    
    staff_id = fields.Int(required=False)
    
    last_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    


class OrderMeta(BaseSchema):
    # Order swagger.json

    
    comment = fields.Str(required=False)
    
    mongo_cart_id = fields.Int(required=False)
    
    cart_id = fields.Int(required=False)
    
    order_child_entities = fields.List(fields.Str(required=False), required=False)
    
    ordering_store = fields.Int(required=False)
    
    payment_type = fields.Str(required=False)
    
    employee_id = fields.Int(required=False)
    
    order_type = fields.Str(required=False)
    
    files = fields.List(fields.Dict(required=False), required=False)
    
    currency_symbol = fields.Str(required=False)
    
    order_platform = fields.Str(required=False)
    
    platform_user_details = fields.Nested(PlatformUserDetails, required=False)
    
    customer_note = fields.Str(required=False)
    
    staff = fields.Dict(required=False)
    
    transaction_data = fields.Nested(TransactionData, required=False)
    
    extra_meta = fields.Dict(required=False)
    
    billing_staff_details = fields.Nested(BillingStaffDetails, required=False)
    
    order_tags = fields.List(fields.Dict(required=False), required=False)
    
    company_logo = fields.Str(required=False)
    


class TaxDetails(BaseSchema):
    # Order swagger.json

    
    gstin = fields.Str(required=False)
    
    pan_no = fields.Str(required=False)
    


class OrderDict(BaseSchema):
    # Order swagger.json

    
    meta = fields.Nested(OrderMeta, required=False)
    
    order_date = fields.Str(required=False)
    
    tax_details = fields.Nested(TaxDetails, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    payment_methods = fields.Dict(required=False)
    
    fynd_order_id = fields.Str(required=False)
    


class ShipmentDetailsResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    order = fields.Nested(OrderDict, required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    


class SubLane(BaseSchema):
    # Order swagger.json

    
    total_items = fields.Int(required=False)
    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    actions = fields.List(fields.Dict(required=False), required=False)
    
    index = fields.Int(required=False)
    


class SuperLane(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False)
    
    options = fields.List(fields.Nested(SubLane, required=False), required=False)
    
    total_items = fields.Int(required=False)
    
    text = fields.Str(required=False)
    


class LaneConfigResponse(BaseSchema):
    # Order swagger.json

    
    super_lanes = fields.List(fields.Nested(SuperLane, required=False), required=False)
    


class PlatformChannel(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class PlatformBreakupValues(BaseSchema):
    # Order swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class PlatformOrderItems(BaseSchema):
    # Order swagger.json

    
    total_order_value = fields.Float(required=False)
    
    order_created_time = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    
    user_info = fields.Nested(UserDataInfo, required=False)
    
    order_id = fields.Str(required=False)
    
    order_value = fields.Float(required=False)
    
    channel = fields.Nested(PlatformChannel, required=False)
    
    breakup_values = fields.List(fields.Nested(PlatformBreakupValues, required=False), required=False)
    
    payment_mode = fields.Str(required=False)
    


class OrderListingResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    lane = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    
    message = fields.Str(required=False)
    
    total_count = fields.Int(required=False)
    
    items = fields.List(fields.Nested(PlatformOrderItems, required=False), required=False)
    


class Options(BaseSchema):
    # Order swagger.json

    
    value = fields.Int(required=False)
    
    text = fields.Str(required=False)
    


class MetricsCount(BaseSchema):
    # Order swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    options = fields.List(fields.Nested(Options, required=False), required=False)
    
    text = fields.Str(required=False)
    


class MetricCountResponse(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(MetricsCount, required=False), required=False)
    


class PlatformTrack(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    updated_at = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    awb = fields.Str(required=False)
    
    updated_time = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    raw_status = fields.Str(required=False)
    
    account_name = fields.Str(required=False)
    
    last_location_recieved_at = fields.Str(required=False)
    


class PlatformShipmentTrack(BaseSchema):
    # Order swagger.json

    
    results = fields.List(fields.Nested(PlatformTrack, required=False), required=False)
    
    meta = fields.Dict(required=False)
    


class FilterInfoOption(BaseSchema):
    # Order swagger.json

    
    placeholder_text = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    min_search_size = fields.Int(required=False)
    
    show_ui = fields.Boolean(required=False)
    
    value = fields.Raw(required=False)
    


class FiltersInfo(BaseSchema):
    # Order swagger.json

    
    options = fields.List(fields.Nested(FilterInfoOption, required=False), required=False)
    
    placeholder_text = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    
    text = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class AdvanceFilterInfo(BaseSchema):
    # Order swagger.json

    
    unfulfilled = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    page = fields.Dict(required=False)
    
    returned = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    filters = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    applied_filters = fields.Dict(required=False)
    
    action_centre = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    processed = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    


class FiltersResponse(BaseSchema):
    # Order swagger.json

    
    global_filter = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    advance_filter = fields.Nested(AdvanceFilterInfo, required=False)
    


class Success(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class OmsReports(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    report_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    report_name = fields.Str(required=False)
    
    report_requested_at = fields.Str(required=False)
    
    request_details = fields.Dict(required=False)
    
    report_created_at = fields.Str(required=False)
    
    report_id = fields.Str(required=False)
    
    s3_key = fields.Str(required=False)
    


class JioCodeUpsertDataSet(BaseSchema):
    # Order swagger.json

    
    article_id = fields.Str(required=False)
    
    jio_code = fields.Str(required=False)
    
    item_id = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    


class JioCodeUpsertPayload(BaseSchema):
    # Order swagger.json

    
    data = fields.List(fields.Nested(JioCodeUpsertDataSet, required=False), required=False)
    


class NestedErrorSchemaDataSet(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class JioCodeUpsertResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    trace_id = fields.Str(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    error = fields.List(fields.Nested(NestedErrorSchemaDataSet, required=False), required=False)
    
    identifier = fields.Str(required=False)
    


class URL(BaseSchema):
    # Order swagger.json

    
    url = fields.Str(required=False)
    


class FileUploadResponse(BaseSchema):
    # Order swagger.json

    
    expiry = fields.Int(required=False)
    
    url = fields.Str(required=False)
    


class FileResponse(BaseSchema):
    # Order swagger.json

    
    cdn = fields.Nested(URL, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    upload = fields.Nested(FileUploadResponse, required=False)
    
    method = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    content_type = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    


class BulkActionTemplate(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False)
    
    text = fields.Str(required=False)
    


class BulkActionTemplateResponse(BaseSchema):
    # Order swagger.json

    
    template_x_slug = fields.List(fields.Nested(BulkActionTemplate, required=False), required=False)
    


class QuestionSet(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    


class Reason(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    question_set = fields.List(fields.Nested(QuestionSet, required=False), required=False)
    
    qc_type = fields.List(fields.Str(required=False), required=False)
    


class PlatformShipmentReasonsResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    reasons = fields.List(fields.Nested(Reason, required=False), required=False)
    


class Attributes(BaseSchema):
    # Order swagger.json

    
    marketer_name = fields.Str(required=False)
    
    primary_color = fields.Str(required=False)
    
    primary_color_hex = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    marketer_address = fields.Str(required=False)
    
    gender = fields.List(fields.Str(required=False), required=False)
    
    brand_name = fields.Str(required=False)
    
    primary_material = fields.Str(required=False)
    
    essential = fields.Str(required=False)
    


class Item(BaseSchema):
    # Order swagger.json

    
    l3_category = fields.Int(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    webstore_product_url = fields.Str(required=False)
    
    l1_category_id = fields.Int(required=False)
    
    brand_id = fields.Int(required=False)
    
    slug_key = fields.Str(required=False)
    
    brand = fields.Str(required=False)
    
    department_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    attributes = fields.Nested(Attributes, required=False)
    
    branch_url = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    l2_category = fields.List(fields.Str(required=False), required=False)
    
    last_updated_at = fields.Str(required=False)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    item_id = fields.Int(required=False)
    
    color = fields.Str(required=False)
    
    l2_category_id = fields.Int(required=False)
    
    l3_category_name = fields.Str(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    gender = fields.Str(required=False)
    


class Brand(BaseSchema):
    # Order swagger.json

    
    pickup_location = fields.Str(required=False)
    
    script_last_ran = fields.Str(required=False)
    
    invoice_prefix = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    credit_note_expiry_days = fields.Int(required=False)
    
    modified_on = fields.Int(required=False)
    
    created_on = fields.Int(required=False)
    
    is_virtual_invoice = fields.Boolean(required=False)
    
    company = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    brand_id = fields.Int(required=False)
    
    credit_note_allowed = fields.Boolean(required=False)
    


class ArticleDetails(BaseSchema):
    # Order swagger.json

    
    status = fields.Dict(required=False)
    


class StoreAddress(BaseSchema):
    # Order swagger.json

    
    country = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    address_category = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    landmark = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    country_code = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    contact_person = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    


class EInvoicePortalDetails(BaseSchema):
    # Order swagger.json

    
    user = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    


class StoreEinvoice(BaseSchema):
    # Order swagger.json

    
    enabled = fields.Boolean(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    user = fields.Str(required=False)
    


class StoreEwaybill(BaseSchema):
    # Order swagger.json

    
    enabled = fields.Boolean(required=False)
    


class StoreGstCredentials(BaseSchema):
    # Order swagger.json

    
    e_invoice = fields.Nested(StoreEinvoice, required=False)
    
    e_waybill = fields.Nested(StoreEwaybill, required=False)
    


class Document(BaseSchema):
    # Order swagger.json

    
    verified = fields.Boolean(required=False)
    
    url = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    legal_name = fields.Str(required=False)
    
    ds_type = fields.Str(required=False)
    


class StoreDocuments(BaseSchema):
    # Order swagger.json

    
    gst = fields.Nested(Document, required=False)
    


class StoreMeta(BaseSchema):
    # Order swagger.json

    
    einvoice_portal_details = fields.Nested(EInvoicePortalDetails, required=False)
    
    gst_credentials = fields.Nested(StoreGstCredentials, required=False)
    
    display_name = fields.Str(required=False)
    
    ewaybill_portal_details = fields.Dict(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    product_return_config = fields.Dict(required=False)
    
    gst_number = fields.Str(required=False)
    
    timing = fields.List(fields.Dict(required=False), required=False)
    
    additional_contact_details = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    documents = fields.Nested(StoreDocuments, required=False)
    


class Store(BaseSchema):
    # Order swagger.json

    
    store_email = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    country = fields.Str(required=False)
    
    mall_area = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    store_address_json = fields.Nested(StoreAddress, required=False)
    
    state = fields.Str(required=False)
    
    location_type = fields.Str(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    brand_id = fields.Raw(required=False)
    
    alohomora_user_id = fields.Int(required=False)
    
    packaging_material_count = fields.Int(required=False)
    
    address2 = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    mall_name = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    is_enabled_for_recon = fields.Boolean(required=False)
    
    login_username = fields.Str(required=False)
    
    phone = fields.Int(required=False)
    
    meta = fields.Nested(StoreMeta, required=False)
    
    vat_no = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    s_id = fields.Str(required=False)
    
    parent_store_id = fields.Int(required=False)
    
    store_active_from = fields.Str(required=False)
    
    order_integration_id = fields.Str(required=False)
    
    brand_store_tags = fields.List(fields.Str(required=False), required=False)
    
    fulfillment_channel = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    contact_person = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    


class BagGSTDetails(BaseSchema):
    # Order swagger.json

    
    is_default_hsn_code = fields.Boolean(required=False)
    
    tax_collected_at_source = fields.Float(required=False)
    
    igst_tax_percentage = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    sgst_tax_percentage = fields.Float(required=False)
    
    igst_gst_fee = fields.Str(required=False)
    
    cgst_gst_fee = fields.Str(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    gst_tag = fields.Str(required=False)
    
    gstin_code = fields.Str(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    gst_fee = fields.Float(required=False)
    
    hsn_code = fields.Str(required=False)
    
    sgst_gst_fee = fields.Str(required=False)
    
    cgst_tax_percentage = fields.Float(required=False)
    


class BagReturnableCancelableStatus1(BaseSchema):
    # Order swagger.json

    
    is_active = fields.Boolean(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    can_be_cancelled = fields.Boolean(required=False)
    
    is_customer_return_allowed = fields.Boolean(required=False)
    
    is_returnable = fields.Boolean(required=False)
    


class BagDetailsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    journey_type = fields.Str(required=False)
    
    item = fields.Nested(Item, required=False)
    
    quantity = fields.Float(required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    restore_promos = fields.Dict(required=False)
    
    article = fields.Nested(Article, required=False)
    
    identifier = fields.Str(required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    b_id = fields.Int(required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    operational_status = fields.Str(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    display_name = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    article_details = fields.Nested(ArticleDetails, required=False)
    
    ordering_store = fields.Nested(Store, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    line_number = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    entity_type = fields.Str(required=False)
    
    bag_update_time = fields.Float(required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus1, required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    
    order_integration_id = fields.Str(required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    qc_required = fields.Raw(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    b_type = fields.Str(required=False)
    


class ErrorResponse(BaseSchema):
    # Order swagger.json

    
    error = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class BagsPage(BaseSchema):
    # Order swagger.json

    
    item_total = fields.Int(required=False)
    
    page_type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class GetBagsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    page = fields.Nested(BagsPage, required=False)
    
    items = fields.List(fields.Nested(BagDetailsPlatformResponse, required=False), required=False)
    


class GeneratePosOrderReceiptResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    payment_receipt = fields.Str(required=False)
    
    invoice_receipt = fields.Str(required=False)
    


class InvalidateShipmentCachePayload(BaseSchema):
    # Order swagger.json

    
    bag_ids = fields.List(fields.Str(required=False), required=False)
    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    
    affiliate_bag_ids = fields.List(fields.Str(required=False), required=False)
    


class InvalidateShipmentCacheNestedResponse(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    error = fields.Str(required=False)
    


class InvalidateShipmentCacheResponse(BaseSchema):
    # Order swagger.json

    
    response = fields.List(fields.Nested(InvalidateShipmentCacheNestedResponse, required=False), required=False)
    


class ErrorResponse1(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    error_trace = fields.Str(required=False)
    


class StoreReassign(BaseSchema):
    # Order swagger.json

    
    mongo_article_id = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    item_id = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    set_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    reason_ids = fields.List(fields.Int(required=False), required=False)
    
    affiliate_bag_id = fields.Str(required=False)
    


class StoreReassignResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class Entities(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    reason_text = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    affiliate_bag_id = fields.Str(required=False)
    


class UpdateShipmentLockPayload(BaseSchema):
    # Order swagger.json

    
    entities = fields.List(fields.Nested(Entities, required=False), required=False)
    
    action = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    action_type = fields.Str(required=False)
    


class Bags(BaseSchema):
    # Order swagger.json

    
    is_locked = fields.Boolean(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    affiliate_bag_id = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    


class OriginalFilter(BaseSchema):
    # Order swagger.json

    
    affiliate_id = fields.Str(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    


class CheckResponse(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    is_bag_locked = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    is_shipment_locked = fields.Boolean(required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    lock_status = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    original_filter = fields.Nested(OriginalFilter, required=False)
    


class UpdateShipmentLockResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    check_response = fields.List(fields.Nested(CheckResponse, required=False), required=False)
    
    message = fields.Str(required=False)
    


class AnnouncementResponse(BaseSchema):
    # Order swagger.json

    
    platform_id = fields.Str(required=False)
    
    to_datetime = fields.Str(required=False)
    
    logo_url = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    title = fields.Str(required=False)
    
    platform_name = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    from_datetime = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class AnnouncementsResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    announcements = fields.List(fields.Nested(AnnouncementResponse, required=False), required=False)
    
    message = fields.Str(required=False)
    


class BaseResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class Click2CallResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Boolean(required=False)
    
    call_id = fields.Str(required=False)
    


class Products(BaseSchema):
    # Order swagger.json

    
    identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    line_number = fields.Int(required=False)
    


class ProductsDataUpdatesFilters(BaseSchema):
    # Order swagger.json

    
    identifier = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    


class ProductsDataUpdates(BaseSchema):
    # Order swagger.json

    
    data = fields.Dict(required=False)
    
    filters = fields.List(fields.Nested(ProductsDataUpdatesFilters, required=False), required=False)
    


class EntitiesDataUpdates(BaseSchema):
    # Order swagger.json

    
    data = fields.Dict(required=False)
    
    filters = fields.List(fields.Dict(required=False), required=False)
    


class DataUpdates(BaseSchema):
    # Order swagger.json

    
    products = fields.List(fields.Nested(ProductsDataUpdates, required=False), required=False)
    
    entities = fields.List(fields.Nested(EntitiesDataUpdates, required=False), required=False)
    


class ProductsReasonsData(BaseSchema):
    # Order swagger.json

    
    reason_text = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    


class ProductsReasonsFilters(BaseSchema):
    # Order swagger.json

    
    identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    line_number = fields.Int(required=False)
    


class ProductsReasons(BaseSchema):
    # Order swagger.json

    
    data = fields.Nested(ProductsReasonsData, required=False)
    
    filters = fields.List(fields.Nested(ProductsReasonsFilters, required=False), required=False)
    


class EntityReasonData(BaseSchema):
    # Order swagger.json

    
    reason_text = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    


class EntitiesReasons(BaseSchema):
    # Order swagger.json

    
    data = fields.Nested(EntityReasonData, required=False)
    
    filters = fields.List(fields.Dict(required=False), required=False)
    


class ReasonsData(BaseSchema):
    # Order swagger.json

    
    products = fields.List(fields.Nested(ProductsReasons, required=False), required=False)
    
    entities = fields.List(fields.Nested(EntitiesReasons, required=False), required=False)
    


class ShipmentsRequest(BaseSchema):
    # Order swagger.json

    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    data_updates = fields.Nested(DataUpdates, required=False)
    
    identifier = fields.Str(required=False)
    
    reasons = fields.Nested(ReasonsData, required=False)
    


class StatuesRequest(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(ShipmentsRequest, required=False), required=False)
    
    status = fields.Str(required=False)
    
    exclude_bags_next_state = fields.Str(required=False)
    


class UpdateShipmentStatusRequest(BaseSchema):
    # Order swagger.json

    
    unlock_before_transition = fields.Boolean(required=False)
    
    task = fields.Boolean(required=False)
    
    force_transition = fields.Boolean(required=False)
    
    statuses = fields.List(fields.Nested(StatuesRequest, required=False), required=False)
    
    lock_after_transition = fields.Boolean(required=False)
    


class ShipmentsResponse(BaseSchema):
    # Order swagger.json

    
    meta = fields.Dict(required=False)
    
    exception = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    final_state = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    


class StatuesResponse(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(ShipmentsResponse, required=False), required=False)
    


class UpdateShipmentStatusResponseBody(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(StatuesResponse, required=False), required=False)
    


class OrderUser(BaseSchema):
    # Order swagger.json

    
    address1 = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    phone = fields.Int(required=False)
    
    mobile = fields.Int(required=False)
    
    last_name = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    city = fields.Str(required=False)
    


class ArticleDetails1(BaseSchema):
    # Order swagger.json

    
    attributes = fields.Dict(required=False)
    
    category = fields.Dict(required=False)
    
    brand_id = fields.Int(required=False)
    
    dimension = fields.Dict(required=False)
    
    weight = fields.Dict(required=False)
    
    _id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class ShipmentDetails1(BaseSchema):
    # Order swagger.json

    
    meta = fields.Dict(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    box_type = fields.Str(required=False)
    
    dp_id = fields.Int(required=False)
    
    shipments = fields.Int(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(ArticleDetails1, required=False), required=False)
    


class LocationDetails(BaseSchema):
    # Order swagger.json

    
    articles = fields.List(fields.Nested(ArticleDetails1, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    fulfillment_type = fields.Str(required=False)
    


class ShipmentConfig(BaseSchema):
    # Order swagger.json

    
    payment_mode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    shipment = fields.List(fields.Nested(ShipmentDetails1, required=False), required=False)
    
    journey = fields.Str(required=False)
    
    location_details = fields.Nested(LocationDetails, required=False)
    
    action = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    


class ShipmentData(BaseSchema):
    # Order swagger.json

    
    shipment_data = fields.Nested(ShipmentConfig, required=False)
    


class MarketPlacePdf(BaseSchema):
    # Order swagger.json

    
    invoice = fields.Str(required=False)
    
    label = fields.Str(required=False)
    


class AffiliateBag(BaseSchema):
    # Order swagger.json

    
    store_id = fields.Int(required=False)
    
    avl_qty = fields.Int(required=False)
    
    pdf_links = fields.Nested(MarketPlacePdf, required=False)
    
    company_id = fields.Int(required=False)
    
    price_effective = fields.Float(required=False)
    
    modified_on = fields.Str(required=False)
    
    price_marked = fields.Float(required=False)
    
    quantity = fields.Int(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    item_id = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    transfer_price = fields.Int(required=False)
    
    fynd_store_id = fields.Str(required=False)
    
    amount_paid = fields.Float(required=False)
    
    sku = fields.Str(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    affiliate_store_id = fields.Str(required=False)
    
    unit_price = fields.Float(required=False)
    
    item_size = fields.Str(required=False)
    
    affiliate_meta = fields.Dict(required=False)
    
    identifier = fields.Dict(required=False)
    


class UserData(BaseSchema):
    # Order swagger.json

    
    shipping_user = fields.Nested(OrderUser, required=False)
    
    billing_user = fields.Nested(OrderUser, required=False)
    


class OrderPriority(BaseSchema):
    # Order swagger.json

    
    fulfilment_priority = fields.Int(required=False)
    
    affiliate_priority_code = fields.Str(required=False)
    
    fulfilment_priority_text = fields.Str(required=False)
    


class OrderInfo(BaseSchema):
    # Order swagger.json

    
    payment_mode = fields.Str(required=False)
    
    items = fields.Dict(required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    payment = fields.Dict(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    coupon = fields.Str(required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    discount = fields.Float(required=False)
    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    order_value = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    user = fields.Nested(UserData, required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
    delivery_charges = fields.Float(required=False)
    


class AffiliateStoreIdMapping(BaseSchema):
    # Order swagger.json

    
    store_id = fields.Int(required=False)
    
    marketplace_store_id = fields.Str(required=False)
    


class AffiliateAppConfigMeta(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class AffiliateAppConfig(BaseSchema):
    # Order swagger.json

    
    meta = fields.List(fields.Nested(AffiliateAppConfigMeta, required=False), required=False)
    
    owner = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class AffiliateInventoryOrderConfig(BaseSchema):
    # Order swagger.json

    
    force_reassignment = fields.Boolean(required=False)
    


class AffiliateInventoryPaymentConfig(BaseSchema):
    # Order swagger.json

    
    mode_of_payment = fields.Str(required=False)
    
    source = fields.Str(required=False)
    


class AffiliateInventoryStoreConfig(BaseSchema):
    # Order swagger.json

    
    store = fields.Dict(required=False)
    


class AffiliateInventoryArticleAssignmentConfig(BaseSchema):
    # Order swagger.json

    
    post_order_reassignment = fields.Boolean(required=False)
    


class AffiliateInventoryLogisticsConfig(BaseSchema):
    # Order swagger.json

    
    dp_assignment = fields.Boolean(required=False)
    


class AffiliateInventoryConfig(BaseSchema):
    # Order swagger.json

    
    order = fields.Nested(AffiliateInventoryOrderConfig, required=False)
    
    payment = fields.Nested(AffiliateInventoryPaymentConfig, required=False)
    
    inventory = fields.Nested(AffiliateInventoryStoreConfig, required=False)
    
    article_assignment = fields.Nested(AffiliateInventoryArticleAssignmentConfig, required=False)
    
    logistics = fields.Nested(AffiliateInventoryLogisticsConfig, required=False)
    


class AffiliateConfig(BaseSchema):
    # Order swagger.json

    
    app = fields.Nested(AffiliateAppConfig, required=False)
    
    inventory = fields.Nested(AffiliateInventoryConfig, required=False)
    


class Affiliate(BaseSchema):
    # Order swagger.json

    
    config = fields.Nested(AffiliateConfig, required=False)
    
    token = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class OrderConfig(BaseSchema):
    # Order swagger.json

    
    store_lookup = fields.Str(required=False)
    
    affiliate_store_id_mapping = fields.List(fields.Nested(AffiliateStoreIdMapping, required=False), required=False)
    
    bag_end_state = fields.Str(required=False)
    
    article_lookup = fields.Str(required=False)
    
    create_user = fields.Boolean(required=False)
    
    affiliate = fields.Nested(Affiliate, required=False)
    


class CreateOrderPayload(BaseSchema):
    # Order swagger.json

    
    affiliate_id = fields.Str(required=False)
    
    order_info = fields.Nested(OrderInfo, required=False)
    
    order_config = fields.Nested(OrderConfig, required=False)
    


class CreateOrderResponse(BaseSchema):
    # Order swagger.json

    
    fynd_order_id = fields.Str(required=False)
    


class DispatchManifest(BaseSchema):
    # Order swagger.json

    
    manifest_id = fields.Str(required=False)
    


class SuccessResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ActionInfo(BaseSchema):
    # Order swagger.json

    
    slug = fields.Str(required=False)
    
    display_text = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class GetActionsResponse(BaseSchema):
    # Order swagger.json

    
    permissions = fields.Nested(ActionInfo, required=False)
    


class PostHistoryData(BaseSchema):
    # Order swagger.json

    
    user_name = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class PostHistoryFilters(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    line_number = fields.Str(required=False)
    


class PostActivityHistory(BaseSchema):
    # Order swagger.json

    
    data = fields.Nested(PostHistoryData, required=False)
    
    filters = fields.List(fields.Nested(PostHistoryFilters, required=False), required=False)
    


class PostHistoryDict(BaseSchema):
    # Order swagger.json

    
    activity_history = fields.Nested(PostActivityHistory, required=False)
    


class PostShipmentHistory(BaseSchema):
    # Order swagger.json

    
    activity_history = fields.List(fields.Nested(PostHistoryDict, required=False), required=False)
    


class HistoryDict(BaseSchema):
    # Order swagger.json

    
    meta = fields.Dict(required=False)
    
    assigned_agent = fields.Str(required=False)
    
    l2_detail = fields.Str(required=False)
    
    ticket_url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    l3_detail = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    user = fields.Str(required=False)
    
    ticket_id = fields.Str(required=False)
    
    l1_detail = fields.Str(required=False)
    
    display_message = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    createdat = fields.Str(required=False)
    


class ShipmentHistoryResponse(BaseSchema):
    # Order swagger.json

    
    activity_history = fields.List(fields.Nested(HistoryDict, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ErrorDetail(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class SmsDataPayload(BaseSchema):
    # Order swagger.json

    
    payment_mode = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    shipment_id = fields.Int(required=False)
    
    amount_paid = fields.Int(required=False)
    
    phone_number = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    customer_name = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    


class SendSmsPayload(BaseSchema):
    # Order swagger.json

    
    data = fields.Nested(SmsDataPayload, required=False)
    
    slug = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    


class Meta(BaseSchema):
    # Order swagger.json

    
    kafka_emission_status = fields.Int(required=False)
    
    state_manager_used = fields.Str(required=False)
    


class ShipmentDetail(BaseSchema):
    # Order swagger.json

    
    remarks = fields.Str(required=False)
    
    meta = fields.Nested(Meta, required=False)
    
    shipment_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    bag_list = fields.List(fields.Int(required=False), required=False)
    
    id = fields.Int(required=False)
    


class OrderDetails(BaseSchema):
    # Order swagger.json

    
    created_at = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    


class OrderStatusData(BaseSchema):
    # Order swagger.json

    
    shipment_details = fields.List(fields.Nested(ShipmentDetail, required=False), required=False)
    
    order_details = fields.Nested(OrderDetails, required=False)
    
    errors = fields.List(fields.Str(required=False), required=False)
    


class OrderStatusResult(BaseSchema):
    # Order swagger.json

    
    result = fields.List(fields.Nested(OrderStatusData, required=False), required=False)
    
    success = fields.Str(required=False)
    


class ManualAssignDPToShipment(BaseSchema):
    # Order swagger.json

    
    dp_id = fields.Int(required=False)
    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    
    order_type = fields.Str(required=False)
    
    qc_required = fields.Str(required=False)
    


class ManualAssignDPToShipmentResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Str(required=False)
    
    errors = fields.List(fields.Str(required=False), required=False)
    


class PaymentMethod(BaseSchema):
    # Order swagger.json

    
    meta = fields.Dict(required=False)
    
    amount = fields.Float(required=False)
    
    refund_by = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    collect_by = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    transaction_data = fields.Dict(required=False)
    


class PaymentInfo(BaseSchema):
    # Order swagger.json

    
    payment_methods = fields.List(fields.Nested(PaymentMethod, required=False), required=False)
    
    primary_mode = fields.Str(required=False)
    


class TaxInfo(BaseSchema):
    # Order swagger.json

    
    gstin = fields.Str(required=False)
    
    b2b_gstin_number = fields.Str(required=False)
    


class Tax(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    amount = fields.Dict(required=False)
    
    breakup = fields.List(fields.Dict(required=False), required=False)
    
    rate = fields.Float(required=False)
    


class Charge(BaseSchema):
    # Order swagger.json

    
    amount = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    tax = fields.Nested(Tax, required=False)
    


class LineItem(BaseSchema):
    # Order swagger.json

    
    meta = fields.Dict(required=False)
    
    custom_messasge = fields.Str(required=False)
    
    external_line_id = fields.Str(required=False)
    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    seller_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class ProcessingDates(BaseSchema):
    # Order swagger.json

    
    confirm_by_date = fields.Str(required=False)
    
    dp_pickup_slot = fields.Dict(required=False)
    
    dispatch_after_date = fields.Str(required=False)
    
    customer_pickup_slot = fields.Dict(required=False)
    
    pack_by_date = fields.Str(required=False)
    
    dispatch_by_date = fields.Str(required=False)
    


class Shipment(BaseSchema):
    # Order swagger.json

    
    meta = fields.Dict(required=False)
    
    location_id = fields.Int(required=False)
    
    line_items = fields.List(fields.Nested(LineItem, required=False), required=False)
    
    processing_dates = fields.Nested(ProcessingDates, required=False)
    
    priority = fields.Int(required=False)
    
    external_shipment_id = fields.Str(required=False)
    


class ShippingInfo(BaseSchema):
    # Order swagger.json

    
    country_code = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    external_customer_code = fields.Str(required=False)
    
    geo_location = fields.Dict(required=False)
    
    floor_no = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    shipping_type = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    alternate_email = fields.Str(required=False)
    
    customer_code = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    middle_name = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    alternate_mobile_number = fields.Str(required=False)
    
    house_no = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    primary_email = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    primary_mobile_number = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    slot = fields.List(fields.Dict(required=False), required=False)
    


class BillingInfo(BaseSchema):
    # Order swagger.json

    
    country_code = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    external_customer_code = fields.Str(required=False)
    
    floor_no = fields.Str(required=False)
    
    alternate_email = fields.Str(required=False)
    
    customer_code = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    middle_name = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    alternate_mobile_number = fields.Str(required=False)
    
    house_no = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    primary_email = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    primary_mobile_number = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    


class CreateOrderAPI(BaseSchema):
    # Order swagger.json

    
    meta = fields.Dict(required=False)
    
    payment_info = fields.Nested(PaymentInfo, required=False)
    
    external_order_id = fields.Str(required=False)
    
    tax_info = fields.Nested(TaxInfo, required=False)
    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    external_creation_date = fields.Str(required=False)
    
    config = fields.Dict(required=False)
    
    currency_info = fields.Dict(required=False)
    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    
    shipping_info = fields.Nested(ShippingInfo, required=False)
    
    billing_info = fields.Nested(BillingInfo, required=False)
    


class CreateOrderErrorReponse(BaseSchema):
    # Order swagger.json

    
    meta = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    
    info = fields.Raw(required=False)
    
    request_id = fields.Str(required=False)
    


class PaymentMethods(BaseSchema):
    # Order swagger.json

    
    mode = fields.Str(required=False)
    
    refund_by = fields.Str(required=False)
    
    collect_by = fields.Str(required=False)
    


class CreateChannelPaymentInfo(BaseSchema):
    # Order swagger.json

    
    mode_of_payment = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMethods, required=False), required=False)
    
    source = fields.Str(required=False)
    


class DpConfiguration(BaseSchema):
    # Order swagger.json

    
    shipping_by = fields.Str(required=False)
    


class CreateChannelConfig(BaseSchema):
    # Order swagger.json

    
    lock_states = fields.List(fields.Str(required=False), required=False)
    
    payment_info = fields.Nested(CreateChannelPaymentInfo, required=False)
    
    logo_url = fields.Dict(required=False)
    
    dp_configuration = fields.Nested(DpConfiguration, required=False)
    
    location_reassignment = fields.Boolean(required=False)
    
    shipment_assignment = fields.Str(required=False)
    


class CreateChannelConfigData(BaseSchema):
    # Order swagger.json

    
    config_data = fields.Nested(CreateChannelConfig, required=False)
    


class CreateChannelConfigResponse(BaseSchema):
    # Order swagger.json

    
    is_inserted = fields.Boolean(required=False)
    
    is_upserted = fields.Boolean(required=False)
    
    acknowledged = fields.Boolean(required=False)
    


class CreateChannelConifgErrorResponse(BaseSchema):
    # Order swagger.json

    
    error = fields.Str(required=False)
    


class UploadConsent(BaseSchema):
    # Order swagger.json

    
    manifest_id = fields.Str(required=False)
    
    consent_url = fields.Str(required=False)
    


class PlatformOrderUpdate(BaseSchema):
    # Order swagger.json

    
    order_id = fields.Str(required=False)
    


class ResponseDetail(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.List(fields.Str(required=False), required=False)
    


class FyndOrderIdList(BaseSchema):
    # Order swagger.json

    
    fynd_order_id = fields.List(fields.Str(required=False), required=False)
    


class OrderStatus(BaseSchema):
    # Order swagger.json

    
    mobile = fields.Int(required=False)
    
    order_details = fields.List(fields.Nested(FyndOrderIdList, required=False), required=False)
    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    


