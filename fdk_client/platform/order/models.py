"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema


from .enums import *



class InvalidateShipmentCachePayload(BaseSchema):
    pass


class InvalidateShipmentCacheNestedResponseSchema(BaseSchema):
    pass


class InvalidateShipmentCacheResponseSchema(BaseSchema):
    pass


class UpdatePackingErrorResponseSchema(BaseSchema):
    pass


class ErrorResponseSchema(BaseSchema):
    pass


class StoreReassign(BaseSchema):
    pass


class StoreReassignResponseSchema(BaseSchema):
    pass


class LockManagerEntities(BaseSchema):
    pass


class UpdateShipmentLockPayload(BaseSchema):
    pass


class OriginalFilter(BaseSchema):
    pass


class Bags(BaseSchema):
    pass


class CheckResponseSchema(BaseSchema):
    pass


class UpdateShipmentLockResponseSchema(BaseSchema):
    pass


class AnnouncementResponseSchema(BaseSchema):
    pass


class AnnouncementsResponseSchema(BaseSchema):
    pass


class BaseResponseSchema(BaseSchema):
    pass


class ErrorDetail(BaseSchema):
    pass


class ProductsReasonsFilters(BaseSchema):
    pass


class ProductsReasonsData(BaseSchema):
    pass


class ProductsReasons(BaseSchema):
    pass


class EntityReasonData(BaseSchema):
    pass


class EntitiesReasons(BaseSchema):
    pass


class ReasonsData(BaseSchema):
    pass


class Products(BaseSchema):
    pass


class OrderItemDataUpdates(BaseSchema):
    pass


class ProductsDataUpdatesFilters(BaseSchema):
    pass


class ProductsDataUpdates(BaseSchema):
    pass


class EntitiesDataUpdates(BaseSchema):
    pass


class OrderDataUpdates(BaseSchema):
    pass


class SellerQCDetailsSchema(BaseSchema):
    pass


class EntityStatusDataSchema(BaseSchema):
    pass


class DataUpdatesFiltersSchema(BaseSchema):
    pass


class EntityStatusDataUpdates(BaseSchema):
    pass


class DataUpdates(BaseSchema):
    pass


class TransitionComments(BaseSchema):
    pass


class ShipmentsRequestSchema(BaseSchema):
    pass


class UpdatedAddressSchema(BaseSchema):
    pass


class UpdateAddressRequestBody(BaseSchema):
    pass


class StatuesRequestSchema(BaseSchema):
    pass


class UpdateShipmentStatusRequestSchema(BaseSchema):
    pass


class ShipmentsResponseSchema(BaseSchema):
    pass


class DPConfiguration(BaseSchema):
    pass


class PaymentConfig(BaseSchema):
    pass


class LockStateMessage(BaseSchema):
    pass


class CreateOrderConfig(BaseSchema):
    pass


class StatuesResponseSchema(BaseSchema):
    pass


class UpdateShipmentStatusResponseBody(BaseSchema):
    pass


class OrderUser(BaseSchema):
    pass


class OrderPriority(BaseSchema):
    pass


class ArticleDetails(BaseSchema):
    pass


class LocationDetails(BaseSchema):
    pass


class ShipmentDetails(BaseSchema):
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


class OrderInfo(BaseSchema):
    pass


class AffiliateAppConfigMeta(BaseSchema):
    pass


class AffiliateAppConfig(BaseSchema):
    pass


class AffiliateInventoryArticleAssignmentConfig(BaseSchema):
    pass


class AffiliateInventoryPaymentConfig(BaseSchema):
    pass


class AffiliateInventoryStoreConfig(BaseSchema):
    pass


class AffiliateInventoryOrderConfig(BaseSchema):
    pass


class AffiliateInventoryLogisticsConfig(BaseSchema):
    pass


class AffiliateInventoryConfig(BaseSchema):
    pass


class AffiliateConfig(BaseSchema):
    pass


class Affiliate(BaseSchema):
    pass


class AffiliateStoreIdMapping(BaseSchema):
    pass


class OrderConfig(BaseSchema):
    pass


class CreateOrderResponseSchema(BaseSchema):
    pass


class DispatchManifest(BaseSchema):
    pass


class SuccessResponseSchema(BaseSchema):
    pass


class ActionInfo(BaseSchema):
    pass


class GetActionsResponseSchema(BaseSchema):
    pass


class HistoryReason(BaseSchema):
    pass


class RefundInformation(BaseSchema):
    pass


class HistoryMeta(BaseSchema):
    pass


class HistoryDict(BaseSchema):
    pass


class ShipmentHistoryResponseSchema(BaseSchema):
    pass


class PostHistoryFilters(BaseSchema):
    pass


class PostHistoryData(BaseSchema):
    pass


class PostHistoryDict(BaseSchema):
    pass


class PostShipmentHistory(BaseSchema):
    pass


class SmsDataPayload(BaseSchema):
    pass


class SendSmsPayload(BaseSchema):
    pass


class OrderDetails(BaseSchema):
    pass


class Meta(BaseSchema):
    pass


class ShipmentDetail(BaseSchema):
    pass


class OrderStatusData(BaseSchema):
    pass


class OrderStatusResult(BaseSchema):
    pass


class SendSmsResponseSchema(BaseSchema):
    pass


class Dimension(BaseSchema):
    pass


class UpdatePackagingDimensionsPayload(BaseSchema):
    pass


class UpdatePackagingDimensionsResponseSchema(BaseSchema):
    pass


class Tax(BaseSchema):
    pass


class AmountSchema(BaseSchema):
    pass


class Charge(BaseSchema):
    pass


class LineItem(BaseSchema):
    pass


class ProcessingDates(BaseSchema):
    pass


class Tag(BaseSchema):
    pass


class ProcessAfterConfig(BaseSchema):
    pass


class SystemMessages(BaseSchema):
    pass


class Shipment(BaseSchema):
    pass


class GeoLocationSchema(BaseSchema):
    pass


class ShippingInfo(BaseSchema):
    pass


class BillingInfo(BaseSchema):
    pass


class UserInfo(BaseSchema):
    pass


class TaxInfo(BaseSchema):
    pass


class PaymentMethod(BaseSchema):
    pass


class PaymentInfo(BaseSchema):
    pass


class CreateOrderAPI(BaseSchema):
    pass


class CreateOrderErrorReponse(BaseSchema):
    pass


class PaymentMethods(BaseSchema):
    pass


class CreateChannelPaymentInfo(BaseSchema):
    pass


class CreateChannelConfig(BaseSchema):
    pass


class CreateChannelConfigData(BaseSchema):
    pass


class CreateChannelConifgErrorResponseSchema(BaseSchema):
    pass


class UploadManifestConsent(BaseSchema):
    pass


class CreateChannelConfigResponseSchema(BaseSchema):
    pass


class PlatformOrderUpdate(BaseSchema):
    pass


class ResponseDetail(BaseSchema):
    pass


class FyndOrderIdList(BaseSchema):
    pass


class OrderStatus(BaseSchema):
    pass


class BagStateTransitionMap(BaseSchema):
    pass


class RoleBaseStateTransitionMapping(BaseSchema):
    pass


class FetchCreditBalanceRequestPayload(BaseSchema):
    pass


class CreditBalanceInfo(BaseSchema):
    pass


class FetchCreditBalanceResponsePayload(BaseSchema):
    pass


class RefundModeConfigRequestPayload(BaseSchema):
    pass


class RefundOption(BaseSchema):
    pass


class RefundModeFormat(BaseSchema):
    pass


class RefundModeInfo(BaseSchema):
    pass


class RefundModeConfigResponsePayload(BaseSchema):
    pass


class AttachUserOtpData(BaseSchema):
    pass


class AttachUserInfo(BaseSchema):
    pass


class AttachOrderUser(BaseSchema):
    pass


class AttachOrderUserResponseSchema(BaseSchema):
    pass


class SendUserMobileOTP(BaseSchema):
    pass


class PointBlankOtpData(BaseSchema):
    pass


class SendUserMobileOtpResponseSchema(BaseSchema):
    pass


class VerifyOtpData(BaseSchema):
    pass


class VerifyMobileOTP(BaseSchema):
    pass


class VerifyOtpResponseData(BaseSchema):
    pass


class VerifyOtpResponseSchema(BaseSchema):
    pass


class BulkReportsFiltersSchema(BaseSchema):
    pass


class BulkReportsDownloadRequestSchema(BaseSchema):
    pass


class BulkReportsDownloadResponseSchema(BaseSchema):
    pass


class APIFailedResponseSchema(BaseSchema):
    pass


class BulkStateTransistionRequestSchema(BaseSchema):
    pass


class BulkStateTransistionResponseSchema(BaseSchema):
    pass


class ShipmentActionInfo(BaseSchema):
    pass


class BulkActionListingData(BaseSchema):
    pass


class BulkListinPage(BaseSchema):
    pass


class BulkListingResponseSchema(BaseSchema):
    pass


class JobDetailsData(BaseSchema):
    pass


class JobDetailsResponseSchema(BaseSchema):
    pass


class JobFailedResponseSchema(BaseSchema):
    pass


class ManifestPageInfo(BaseSchema):
    pass


class ManifestItemDetails(BaseSchema):
    pass


class ManifestShipmentListing(BaseSchema):
    pass


class DateRange(BaseSchema):
    pass


class Filters(BaseSchema):
    pass


class ManifestFile(BaseSchema):
    pass


class ManifestMediaUpdate(BaseSchema):
    pass


class PDFMeta(BaseSchema):
    pass


class TotalShipmentPricesCount(BaseSchema):
    pass


class ManifestMeta(BaseSchema):
    pass


class Manifest(BaseSchema):
    pass


class ManifestList(BaseSchema):
    pass


class ManifestDetails(BaseSchema):
    pass


class FiltersRequestSchema(BaseSchema):
    pass


class ProcessManifest(BaseSchema):
    pass


class ProcessManifestResponseSchema(BaseSchema):
    pass


class ProcessManifestItemResponseSchema(BaseSchema):
    pass


class FilterInfoOption(BaseSchema):
    pass


class FiltersInfo(BaseSchema):
    pass


class ManifestFiltersResponseSchema(BaseSchema):
    pass


class PageDetails(BaseSchema):
    pass


class EInvoiceIrnDetails(BaseSchema):
    pass


class EInvoiceErrorDetails(BaseSchema):
    pass


class EInvoiceDetails(BaseSchema):
    pass


class EInvoiceResponseData(BaseSchema):
    pass


class EInvoiceRetry(BaseSchema):
    pass


class EInvoiceRetryResponseSchema(BaseSchema):
    pass


class EInvoiceErrorInfo(BaseSchema):
    pass


class EInvoiceErrorResponseData(BaseSchema):
    pass


class EInvoiceErrorResponseSchema(BaseSchema):
    pass


class EInvoiceErrorResponseDetails(BaseSchema):
    pass


class EInvoiceRetryShipmentData(BaseSchema):
    pass


class CourierPartnerTrackingDetails(BaseSchema):
    pass


class CourierPartnerTrackingResponseSchema(BaseSchema):
    pass


class LogsChannelDetails(BaseSchema):
    pass


class LogPaymentDetails(BaseSchema):
    pass


class FailedOrdersItem(BaseSchema):
    pass


class FailedOrderLogs(BaseSchema):
    pass


class FailedOrderLogDetails(BaseSchema):
    pass


class GenerateInvoiceIDResponseData(BaseSchema):
    pass


class GenerateInvoiceIDErrorResponseData(BaseSchema):
    pass


class GenerateInvoiceIDRequestSchema(BaseSchema):
    pass


class GenerateInvoiceIDResponseSchema(BaseSchema):
    pass


class GenerateInvoiceIDErrorResponseSchema(BaseSchema):
    pass


class ManifestResponseSchema(BaseSchema):
    pass


class ProcessManifestRequestSchema(BaseSchema):
    pass


class ManifestItems(BaseSchema):
    pass


class ManifestErrorResponseSchema(BaseSchema):
    pass


class ConfigData(BaseSchema):
    pass


class ConfigUpdatedResponseSchema(BaseSchema):
    pass


class FlagData(BaseSchema):
    pass


class Flags(BaseSchema):
    pass


class Filter(BaseSchema):
    pass


class PostHook(BaseSchema):
    pass


class PreHook(BaseSchema):
    pass


class Config(BaseSchema):
    pass


class TransitionConfigCondition(BaseSchema):
    pass


class TransitionConfigData(BaseSchema):
    pass


class TransitionConfigPayload(BaseSchema):
    pass


class RuleListRequestSchema(BaseSchema):
    pass


class RuleErrorResponseSchema(BaseSchema):
    pass


class RMAPageInfo(BaseSchema):
    pass


class RuleAction(BaseSchema):
    pass


class QuestionSetItem(BaseSchema):
    pass


class Reason(BaseSchema):
    pass


class Conditions(BaseSchema):
    pass


class RuleItem(BaseSchema):
    pass


class RuleError(BaseSchema):
    pass


class RuleListResponseSchema(BaseSchema):
    pass


class UpdateShipmentPaymentMode(BaseSchema):
    pass


class CommonErrorResponseSchema(BaseSchema):
    pass


class ExceptionErrorResponseSchema(BaseSchema):
    pass


class ProductSchema(BaseSchema):
    pass


class PaymentMethodSchema(BaseSchema):
    pass


class ActionDetailSchema(BaseSchema):
    pass


class PaymentMetaDataSchema(BaseSchema):
    pass


class PaymentMetaLogoURLSchema(BaseSchema):
    pass


class ValidationError(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class BagReasonMeta(BaseSchema):
    pass


class QuestionSet(BaseSchema):
    pass


class BagReasons(BaseSchema):
    pass


class ShipmentBagReasons(BaseSchema):
    pass


class ShipmentStatus(BaseSchema):
    pass


class UserDataInfo(BaseSchema):
    pass


class Address(BaseSchema):
    pass


class ShipmentListingChannel(BaseSchema):
    pass


class Prices(BaseSchema):
    pass


class ChargeDistributionSchema(BaseSchema):
    pass


class ChargeDistributionLogic(BaseSchema):
    pass


class ChargeAmountCurrency(BaseSchema):
    pass


class ChargeAmount(BaseSchema):
    pass


class PriceAdjustmentCharge(BaseSchema):
    pass


class OrderingCurrencyPrices(BaseSchema):
    pass


class Identifier(BaseSchema):
    pass


class TaxComponent(BaseSchema):
    pass


class FinancialBreakup(BaseSchema):
    pass


class GSTDetailsData(BaseSchema):
    pass


class BagStateMapper(BaseSchema):
    pass


class BagStatusHistory(BaseSchema):
    pass


class Dimensions(BaseSchema):
    pass


class ReturnConfig(BaseSchema):
    pass


class Weight(BaseSchema):
    pass


class Article(BaseSchema):
    pass


class ShipmentListingBrand(BaseSchema):
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


class Dates(BaseSchema):
    pass


class BagReturnableCancelableStatus(BaseSchema):
    pass


class BagUnit(BaseSchema):
    pass


class ShipmentItemFulFillingStore(BaseSchema):
    pass


class Currency(BaseSchema):
    pass


class OrderingCurrency(BaseSchema):
    pass


class ConversionRate(BaseSchema):
    pass


class CurrencyInfo(BaseSchema):
    pass


class ShipmentItem(BaseSchema):
    pass


class ShipmentInternalPlatformViewResponseSchema(BaseSchema):
    pass


class TrackingList(BaseSchema):
    pass


class InvoiceInfo(BaseSchema):
    pass


class LoyaltyDiscountDetails(BaseSchema):
    pass


class OrderDetailsData(BaseSchema):
    pass


class UserDetailsData(BaseSchema):
    pass


class PhoneDetails(BaseSchema):
    pass


class ContactDetails(BaseSchema):
    pass


class CompanyDetails(BaseSchema):
    pass


class OrderingStoreDetails(BaseSchema):
    pass


class DPDetailsData(BaseSchema):
    pass


class BuyerDetails(BaseSchema):
    pass


class DebugInfo(BaseSchema):
    pass


class EinvoiceInfo(BaseSchema):
    pass


class Formatted(BaseSchema):
    pass


class ShipmentTags(BaseSchema):
    pass


class LockData(BaseSchema):
    pass


class ShipmentTimeStamp(BaseSchema):
    pass


class ShipmentMeta(BaseSchema):
    pass


class PDFLinks(BaseSchema):
    pass


class AffiliateDetails(BaseSchema):
    pass


class BagConfigs(BaseSchema):
    pass


class OrderBagArticle(BaseSchema):
    pass


class OrderBrandName(BaseSchema):
    pass


class AffiliateBagsDetails(BaseSchema):
    pass


class BagPaymentMethods(BaseSchema):
    pass


class DiscountRules(BaseSchema):
    pass


class ItemCriterias(BaseSchema):
    pass


class BuyRules(BaseSchema):
    pass


class PriceMinMax(BaseSchema):
    pass


class ItemPriceDetails(BaseSchema):
    pass


class FreeGiftItems(BaseSchema):
    pass


class AppliedFreeArticles(BaseSchema):
    pass


class AppliedPromos(BaseSchema):
    pass


class CurrentStatus(BaseSchema):
    pass


class OrderBags(BaseSchema):
    pass


class FulfillingStore(BaseSchema):
    pass


class ShipmentPayments(BaseSchema):
    pass


class ShipmentStatusData(BaseSchema):
    pass


class ShipmentLockDetails(BaseSchema):
    pass


class FulfillmentOption(BaseSchema):
    pass


class PlatformShipment(BaseSchema):
    pass


class ShipmentInfoResponseSchema(BaseSchema):
    pass


class TaxDetails(BaseSchema):
    pass


class PaymentInfoData(BaseSchema):
    pass


class CurrencySchema(BaseSchema):
    pass


class OrderData(BaseSchema):
    pass


class OrderDetailsResponseSchema(BaseSchema):
    pass


class SubLane(BaseSchema):
    pass


class SuperLane(BaseSchema):
    pass


class LaneConfigResponseSchema(BaseSchema):
    pass


class PlatformBreakupValues(BaseSchema):
    pass


class PlatformChannel(BaseSchema):
    pass


class PlatformOrderItems(BaseSchema):
    pass


class OrderListingResponseSchema(BaseSchema):
    pass


class PlatformTrack(BaseSchema):
    pass


class PlatformShipmentTrack(BaseSchema):
    pass


class AdvanceFilterInfo(BaseSchema):
    pass


class FiltersResponseSchema(BaseSchema):
    pass


class URL(BaseSchema):
    pass


class FileResponseSchema(BaseSchema):
    pass


class BulkActionTemplate(BaseSchema):
    pass


class BulkActionTemplateResponseSchema(BaseSchema):
    pass


class PlatformShipmentReasonsResponseSchema(BaseSchema):
    pass


class ShipmentResponseReasons(BaseSchema):
    pass


class ShipmentReasonsResponseSchema(BaseSchema):
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


class Brand(BaseSchema):
    pass


class Item(BaseSchema):
    pass


class ArticleStatusDetails(BaseSchema):
    pass


class Company(BaseSchema):
    pass


class ShipmentGstDetails(BaseSchema):
    pass


class DeliverySlotDetails(BaseSchema):
    pass


class InvoiceDetails(BaseSchema):
    pass


class UserDetails(BaseSchema):
    pass


class WeightData(BaseSchema):
    pass


class BagDetails(BaseSchema):
    pass


class BagDetailsPlatformResponseSchema(BaseSchema):
    pass


class BagsPage(BaseSchema):
    pass


class BagData(BaseSchema):
    pass


class GetBagsPlatformResponseSchema(BaseSchema):
    pass


class GeneratePosOrderReceiptResponseSchema(BaseSchema):
    pass


class Templates(BaseSchema):
    pass


class AllowedTemplatesResponseSchema(BaseSchema):
    pass


class TemplateDownloadResponseSchema(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class BulkFailedResponseSchema(BaseSchema):
    pass





class InvalidateShipmentCachePayload(BaseSchema):
    # Order swagger.json

    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    
    affiliate_bag_ids = fields.List(fields.Str(required=False), required=False)
    
    bag_ids = fields.List(fields.Str(required=False), required=False)
    


class InvalidateShipmentCacheNestedResponseSchema(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    error = fields.Str(required=False)
    


class InvalidateShipmentCacheResponseSchema(BaseSchema):
    # Order swagger.json

    
    response = fields.List(fields.Nested(InvalidateShipmentCacheNestedResponseSchema, required=False), required=False)
    


class UpdatePackingErrorResponseSchema(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False, allow_none=True)
    
    error = fields.Str(required=False, allow_none=True)
    


class ErrorResponseSchema(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False, allow_none=True)
    
    success = fields.Boolean(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    error_trace = fields.Str(required=False, allow_none=True)
    
    error = fields.Str(required=False)
    


class StoreReassign(BaseSchema):
    # Order swagger.json

    
    store_id = fields.Int(required=False)
    
    bag_id = fields.Int(required=False, allow_none=True)
    
    affiliate_order_id = fields.Str(required=False, allow_none=True)
    
    affiliate_id = fields.Str(required=False, allow_none=True)
    
    item_id = fields.Str(required=False, allow_none=True)
    
    fynd_order_id = fields.Str(required=False, allow_none=True)
    
    set_id = fields.Str(required=False, allow_none=True)
    
    affiliate_bag_id = fields.Str(required=False, allow_none=True)
    
    reason_ids = fields.List(fields.Int(required=False), required=False)
    
    mongo_article_id = fields.Str(required=False, allow_none=True)
    


class StoreReassignResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class LockManagerEntities(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    reason_text = fields.Str(required=False)
    
    affiliate_bag_id = fields.Str(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    


class UpdateShipmentLockPayload(BaseSchema):
    # Order swagger.json

    
    entity_type = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    action_type = fields.Str(required=False)
    
    entities = fields.List(fields.Nested(LockManagerEntities, required=False), required=False)
    
    resume_tasks_after_unlock = fields.Boolean(required=False, allow_none=True)
    
    lock_after_transition = fields.Boolean(required=False)
    
    unlock_before_transition = fields.Boolean(required=False)
    


class OriginalFilter(BaseSchema):
    # Order swagger.json

    
    affiliate_shipment_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    


class Bags(BaseSchema):
    # Order swagger.json

    
    bag_id = fields.Int(required=False)
    
    affiliate_bag_id = fields.Str(required=False)
    
    is_locked = fields.Boolean(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    


class CheckResponseSchema(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    is_bag_locked = fields.Boolean(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    original_filter = fields.Nested(OriginalFilter, required=False)
    
    is_shipment_locked = fields.Boolean(required=False)
    
    lock_status = fields.Str(required=False, allow_none=True)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    


class UpdateShipmentLockResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    check_response = fields.List(fields.Nested(CheckResponseSchema, required=False), required=False)
    


class AnnouncementResponseSchema(BaseSchema):
    # Order swagger.json

    
    to_datetime = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    platform_name = fields.Str(required=False)
    
    from_datetime = fields.Str(required=False)
    
    platform_id = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    logo_url = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    


class AnnouncementsResponseSchema(BaseSchema):
    # Order swagger.json

    
    announcements = fields.List(fields.Nested(AnnouncementResponseSchema, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    


class BaseResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ErrorDetail(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ProductsReasonsFilters(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class ProductsReasonsData(BaseSchema):
    # Order swagger.json

    
    reason_text = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    


class ProductsReasons(BaseSchema):
    # Order swagger.json

    
    filters = fields.List(fields.Nested(ProductsReasonsFilters, required=False), required=False)
    
    data = fields.Nested(ProductsReasonsData, required=False)
    


class EntityReasonData(BaseSchema):
    # Order swagger.json

    
    reason_text = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    


class EntitiesReasons(BaseSchema):
    # Order swagger.json

    
    filters = fields.List(fields.Dict(required=False), required=False)
    
    data = fields.Nested(EntityReasonData, required=False)
    


class ReasonsData(BaseSchema):
    # Order swagger.json

    
    products = fields.List(fields.Nested(ProductsReasons, required=False), required=False)
    
    entities = fields.List(fields.Nested(EntitiesReasons, required=False), required=False)
    


class Products(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class OrderItemDataUpdates(BaseSchema):
    # Order swagger.json

    
    data = fields.Dict(required=False)
    


class ProductsDataUpdatesFilters(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class ProductsDataUpdates(BaseSchema):
    # Order swagger.json

    
    filters = fields.List(fields.Nested(ProductsDataUpdatesFilters, required=False), required=False)
    
    data = fields.Dict(required=False)
    


class EntitiesDataUpdates(BaseSchema):
    # Order swagger.json

    
    filters = fields.List(fields.Dict(required=False), required=False)
    
    data = fields.Dict(required=False)
    


class OrderDataUpdates(BaseSchema):
    # Order swagger.json

    
    data = fields.Dict(required=False)
    


class SellerQCDetailsSchema(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    good_quantity = fields.Int(required=False)
    
    bad_quantity = fields.Int(required=False)
    


class EntityStatusDataSchema(BaseSchema):
    # Order swagger.json

    
    seller_qc_details = fields.List(fields.Nested(SellerQCDetailsSchema, required=False), required=False)
    


class DataUpdatesFiltersSchema(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    


class EntityStatusDataUpdates(BaseSchema):
    # Order swagger.json

    
    filters = fields.List(fields.Nested(DataUpdatesFiltersSchema, required=False), required=False)
    
    data = fields.Nested(EntityStatusDataSchema, required=False)
    


class DataUpdates(BaseSchema):
    # Order swagger.json

    
    order_item_status = fields.List(fields.Nested(OrderItemDataUpdates, required=False), required=False)
    
    products = fields.List(fields.Nested(ProductsDataUpdates, required=False), required=False)
    
    entities = fields.List(fields.Nested(EntitiesDataUpdates, required=False), required=False)
    
    order = fields.List(fields.Nested(OrderDataUpdates, required=False), required=False)
    
    entity_status = fields.List(fields.Nested(EntityStatusDataUpdates, required=False), required=False)
    


class TransitionComments(BaseSchema):
    # Order swagger.json

    
    title = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class ShipmentsRequestSchema(BaseSchema):
    # Order swagger.json

    
    identifier = fields.Str(required=False)
    
    reasons = fields.Nested(ReasonsData, required=False)
    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    data_updates = fields.Nested(DataUpdates, required=False)
    
    transition_comments = fields.List(fields.Nested(TransitionComments, required=False), required=False)
    


class UpdatedAddressSchema(BaseSchema):
    # Order swagger.json

    
    address = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    


class UpdateAddressRequestBody(BaseSchema):
    # Order swagger.json

    
    updated_address = fields.Nested(UpdatedAddressSchema, required=False)
    
    address_type = fields.Str(required=False)
    
    address_category = fields.Str(required=False)
    


class StatuesRequestSchema(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentsRequestSchema, required=False), required=False)
    
    exclude_bags_next_state = fields.Str(required=False)
    
    split_shipment = fields.Boolean(required=False)
    


class UpdateShipmentStatusRequestSchema(BaseSchema):
    # Order swagger.json

    
    force_transition = fields.Boolean(required=False)
    
    statuses = fields.List(fields.Nested(StatuesRequestSchema, required=False), required=False)
    
    lock_after_transition = fields.Boolean(required=False)
    
    unlock_before_transition = fields.Boolean(required=False)
    
    task = fields.Boolean(required=False)
    
    resume_tasks_after_unlock = fields.Boolean(required=False)
    


class ShipmentsResponseSchema(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False, allow_none=True)
    
    final_state = fields.Dict(required=False, allow_none=True)
    
    identifier = fields.Str(required=False, allow_none=True)
    
    stack_trace = fields.Str(required=False, allow_none=True)
    
    code = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    exception = fields.Str(required=False, allow_none=True)
    


class DPConfiguration(BaseSchema):
    # Order swagger.json

    
    shipping_by = fields.Str(required=False)
    


class PaymentConfig(BaseSchema):
    # Order swagger.json

    
    mode_of_payment = fields.Str(required=False)
    
    source = fields.Str(required=False)
    


class LockStateMessage(BaseSchema):
    # Order swagger.json

    
    state = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class CreateOrderConfig(BaseSchema):
    # Order swagger.json

    
    dp_configuration = fields.Nested(DPConfiguration, required=False)
    
    location_reassignment = fields.Boolean(required=False)
    
    payment = fields.Nested(PaymentConfig, required=False)
    
    optimal_shipment_creation = fields.Boolean(required=False)
    
    lock_state_messages = fields.List(fields.Nested(LockStateMessage, required=False), required=False)
    
    integration_type = fields.Str(required=False)
    


class StatuesResponseSchema(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(ShipmentsResponseSchema, required=False), required=False)
    


class UpdateShipmentStatusResponseBody(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(StatuesResponseSchema, required=False), required=False)
    


class OrderUser(BaseSchema):
    # Order swagger.json

    
    phone = fields.Int(required=False)
    
    last_name = fields.Str(required=False)
    
    address1 = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    mobile = fields.Int(required=False)
    
    address2 = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    city = fields.Str(required=False)
    


class OrderPriority(BaseSchema):
    # Order swagger.json

    
    fulfilment_priority_text = fields.Str(required=False)
    
    affiliate_priority_code = fields.Str(required=False, allow_none=True)
    
    fulfilment_priority = fields.Int(required=False, allow_none=True)
    


class ArticleDetails(BaseSchema):
    # Order swagger.json

    
    _id = fields.Str(required=False)
    
    brand_id = fields.Int(required=False)
    
    dimension = fields.Dict(required=False)
    
    category = fields.Dict(required=False)
    
    weight = fields.Dict(required=False)
    
    attributes = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    


class LocationDetails(BaseSchema):
    # Order swagger.json

    
    fulfillment_type = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(ArticleDetails, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    


class ShipmentDetails(BaseSchema):
    # Order swagger.json

    
    box_type = fields.Str(required=False, allow_none=True)
    
    shipments = fields.Int(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    articles = fields.List(fields.Nested(ArticleDetails, required=False), required=False)
    
    dp_id = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    dp_options = fields.Dict(required=False, allow_none=True)
    
    lock_status = fields.Boolean(required=False, allow_none=True)
    
    action_to_status = fields.Dict(required=False, allow_none=True)
    


class ShipmentConfig(BaseSchema):
    # Order swagger.json

    
    location_details = fields.Nested(LocationDetails, required=False)
    
    source = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    
    shipment = fields.List(fields.Nested(ShipmentDetails, required=False), required=False)
    
    identifier = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    


class ShipmentData(BaseSchema):
    # Order swagger.json

    
    shipment_data = fields.Nested(ShipmentConfig, required=False)
    


class MarketPlacePdf(BaseSchema):
    # Order swagger.json

    
    invoice = fields.Str(required=False, allow_none=True)
    
    label = fields.Str(required=False, allow_none=True)
    


class AffiliateBag(BaseSchema):
    # Order swagger.json

    
    pdf_links = fields.Nested(MarketPlacePdf, required=False)
    
    store_id = fields.Int(required=False)
    
    sku = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    unit_price = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    affiliate_store_id = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    item_size = fields.Str(required=False)
    
    amount_paid = fields.Float(required=False)
    
    fynd_store_id = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    avl_qty = fields.Int(required=False)
    
    price_marked = fields.Float(required=False)
    
    quantity = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    affiliate_meta = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    transfer_price = fields.Int(required=False)
    


class UserData(BaseSchema):
    # Order swagger.json

    
    shipping_user = fields.Nested(OrderUser, required=False)
    
    billing_user = fields.Nested(OrderUser, required=False)
    


class OrderInfo(BaseSchema):
    # Order swagger.json

    
    affiliate_order_id = fields.Str(required=False)
    
    cod_charges = fields.Float(required=False)
    
    items = fields.Dict(required=False)
    
    discount = fields.Float(required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    payment = fields.Dict(required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    delivery_charges = fields.Float(required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    order_value = fields.Float(required=False)
    
    payment_mode = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    user = fields.Nested(UserData, required=False)
    
    coupon = fields.Str(required=False, allow_none=True)
    


class AffiliateAppConfigMeta(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class AffiliateAppConfig(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    meta = fields.List(fields.Nested(AffiliateAppConfigMeta, required=False), required=False)
    
    owner = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    


class AffiliateInventoryArticleAssignmentConfig(BaseSchema):
    # Order swagger.json

    
    post_order_reassignment = fields.Boolean(required=False)
    


class AffiliateInventoryPaymentConfig(BaseSchema):
    # Order swagger.json

    
    source = fields.Str(required=False)
    
    mode_of_payment = fields.Str(required=False)
    


class AffiliateInventoryStoreConfig(BaseSchema):
    # Order swagger.json

    
    store = fields.Dict(required=False)
    


class AffiliateInventoryOrderConfig(BaseSchema):
    # Order swagger.json

    
    force_reassignment = fields.Boolean(required=False)
    


class AffiliateInventoryLogisticsConfig(BaseSchema):
    # Order swagger.json

    
    dp_assignment = fields.Boolean(required=False)
    


class AffiliateInventoryConfig(BaseSchema):
    # Order swagger.json

    
    article_assignment = fields.Nested(AffiliateInventoryArticleAssignmentConfig, required=False)
    
    payment = fields.Nested(AffiliateInventoryPaymentConfig, required=False)
    
    inventory = fields.Nested(AffiliateInventoryStoreConfig, required=False)
    
    order = fields.Nested(AffiliateInventoryOrderConfig, required=False)
    
    logistics = fields.Nested(AffiliateInventoryLogisticsConfig, required=False)
    


class AffiliateConfig(BaseSchema):
    # Order swagger.json

    
    app = fields.Nested(AffiliateAppConfig, required=False)
    
    inventory = fields.Nested(AffiliateInventoryConfig, required=False)
    
    app_company_id = fields.Int(required=False, allow_none=True)
    


class Affiliate(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    
    config = fields.Nested(AffiliateConfig, required=False)
    
    token = fields.Str(required=False)
    


class AffiliateStoreIdMapping(BaseSchema):
    # Order swagger.json

    
    store_id = fields.Int(required=False)
    
    marketplace_store_id = fields.Str(required=False)
    


class OrderConfig(BaseSchema):
    # Order swagger.json

    
    create_user = fields.Boolean(required=False)
    
    article_lookup = fields.Str(required=False)
    
    bag_end_state = fields.Str(required=False)
    
    affiliate = fields.Nested(Affiliate, required=False)
    
    store_lookup = fields.Str(required=False)
    
    affiliate_store_id_mapping = fields.List(fields.Nested(AffiliateStoreIdMapping, required=False), required=False)
    


class CreateOrderResponseSchema(BaseSchema):
    # Order swagger.json

    
    fynd_order_id = fields.Str(required=False)
    


class DispatchManifest(BaseSchema):
    # Order swagger.json

    
    manifest_id = fields.Str(required=False)
    


class SuccessResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ActionInfo(BaseSchema):
    # Order swagger.json

    
    display_text = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class GetActionsResponseSchema(BaseSchema):
    # Order swagger.json

    
    permissions = fields.List(fields.Nested(ActionInfo, required=False), required=False)
    


class HistoryReason(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False, allow_none=True)
    
    category = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False, allow_none=True)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    code = fields.Int(required=False, allow_none=True)
    
    quantity = fields.Int(required=False, allow_none=True)
    


class RefundInformation(BaseSchema):
    # Order swagger.json

    
    mode = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    merchant_transaction_id = fields.Str(required=False)
    
    refund_status = fields.Str(required=False)
    


class HistoryMeta(BaseSchema):
    # Order swagger.json

    
    store_id = fields.Int(required=False, allow_none=True)
    
    status = fields.Str(required=False, allow_none=True)
    
    status1 = fields.Str(required=False, allow_none=True)
    
    call_id = fields.Str(required=False, allow_none=True)
    
    starttime = fields.Str(required=False, allow_none=True)
    
    reason = fields.Nested(HistoryReason, required=False)
    
    short_link = fields.Str(required=False, allow_none=True)
    
    endtime = fields.Str(required=False, allow_none=True)
    
    store_name = fields.Str(required=False, allow_none=True)
    
    caller = fields.Str(required=False, allow_none=True)
    
    store_code = fields.Str(required=False, allow_none=True)
    
    billsec = fields.Str(required=False, allow_none=True)
    
    recordpath = fields.Str(required=False, allow_none=True)
    
    status2 = fields.Str(required=False, allow_none=True)
    
    callerid = fields.Str(required=False, allow_none=True)
    
    duration = fields.Str(required=False, allow_none=True)
    
    channel_type = fields.Str(required=False, allow_none=True)
    
    activity_comment = fields.Str(required=False, allow_none=True)
    
    activity_type = fields.Str(required=False, allow_none=True)
    
    receiver = fields.Str(required=False, allow_none=True)
    
    recipient = fields.Str(required=False, allow_none=True)
    
    slug = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    prev_store_name = fields.Str(required=False, allow_none=True)
    
    prev_store_code = fields.Str(required=False, allow_none=True)
    
    prev_store_id = fields.Str(required=False, allow_none=True)
    
    refund_to = fields.Str(required=False, allow_none=True)
    
    refund_information = fields.List(fields.Nested(RefundInformation, required=False), required=False)
    


class HistoryDict(BaseSchema):
    # Order swagger.json

    
    display_message = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    ticket_url = fields.Str(required=False)
    
    l3_detail = fields.Str(required=False)
    
    createdat = fields.Str(required=False)
    
    created_ts = fields.Str(required=False)
    
    ticket_id = fields.Str(required=False)
    
    activity_type = fields.Str(required=False)
    
    l2_detail = fields.Str(required=False)
    
    assigned_agent = fields.Str(required=False)
    
    meta = fields.Nested(HistoryMeta, required=False)
    
    l1_detail = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    user = fields.Str(required=False)
    


class ShipmentHistoryResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    activity_history = fields.List(fields.Nested(HistoryDict, required=False), required=False)
    


class PostHistoryFilters(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    line_number = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    


class PostHistoryData(BaseSchema):
    # Order swagger.json

    
    user_name = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class PostHistoryDict(BaseSchema):
    # Order swagger.json

    
    filters = fields.List(fields.Nested(PostHistoryFilters, required=False), required=False)
    
    data = fields.Nested(PostHistoryData, required=False)
    


class PostShipmentHistory(BaseSchema):
    # Order swagger.json

    
    activity_history = fields.List(fields.Nested(PostHistoryDict, required=False), required=False)
    


class SmsDataPayload(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    amount_paid = fields.Int(required=False)
    
    order_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    customer_name = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class SendSmsPayload(BaseSchema):
    # Order swagger.json

    
    bag_id = fields.Int(required=False)
    
    data = fields.Nested(SmsDataPayload, required=False)
    
    slug = fields.Str(required=False)
    


class OrderDetails(BaseSchema):
    # Order swagger.json

    
    fynd_order_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    user_id = fields.Str(required=False, allow_none=True)
    
    tax_details = fields.Nested(TaxDetails, required=False)
    
    mongo_cart_id = fields.Float(required=False, allow_none=True)
    
    delivery_charges = fields.Float(required=False, allow_none=True)
    
    transaction_id = fields.Str(required=False, allow_none=True)
    
    collect_by = fields.Str(required=False)
    
    headers = fields.Dict(required=False, allow_none=True)
    
    coupon_value = fields.Float(required=False, allow_none=True)
    
    order_value = fields.Float(required=False)
    
    created_time = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    total_order_value = fields.Float(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    ordering_source = fields.Str(required=False)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    cod_charges = fields.Float(required=False, allow_none=True)
    
    cashback_value = fields.Float(required=False, allow_none=True)
    
    refund_by = fields.Str(required=False)
    
    affiliate_order_date = fields.Str(required=False, allow_none=True)
    
    payment_methods = fields.Dict(required=False, allow_none=True)
    
    affiliate_order_id = fields.Str(required=False)
    
    payment_mode_id = fields.Float(required=False, allow_none=True)
    
    promotion_effective_discount = fields.Float(required=False, allow_none=True)
    
    mode_of_payment = fields.Str(required=False)
    
    discount = fields.Float(required=False, allow_none=True)
    
    cashback_applied = fields.Float(required=False, allow_none=True)
    
    fynd_credits = fields.Float(required=False, allow_none=True)
    
    affiliate_id = fields.Str(required=False)
    
    ordering_channel_logo = fields.Str(required=False, allow_none=True)
    
    prices = fields.Nested(Prices, required=False)
    
    charges = fields.List(fields.Nested(PriceAdjustmentCharge, required=False), required=False)
    
    loyalty_discount_details = fields.Nested(LoyaltyDiscountDetails, required=False)
    


class Meta(BaseSchema):
    # Order swagger.json

    
    kafka_emission_status = fields.Int(required=False)
    
    state_manager_used = fields.Str(required=False)
    


class ShipmentDetail(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    bag_list = fields.List(fields.Int(required=False), required=False)
    
    meta = fields.Nested(Meta, required=False)
    
    remarks = fields.Str(required=False)
    


class OrderStatusData(BaseSchema):
    # Order swagger.json

    
    order_details = fields.Nested(OrderDetails, required=False)
    
    errors = fields.List(fields.Str(required=False), required=False)
    
    shipment_details = fields.List(fields.Nested(ShipmentDetail, required=False), required=False)
    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    color_code = fields.Str(required=False)
    
    expected_delivery_date = fields.Str(required=False)
    


class OrderStatusResult(BaseSchema):
    # Order swagger.json

    
    success = fields.Str(required=False)
    
    result = fields.List(fields.Nested(OrderStatusData, required=False), required=False)
    


class SendSmsResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class Dimension(BaseSchema):
    # Order swagger.json

    
    packaging_type = fields.Str(required=False)
    
    weight = fields.Float(required=False)
    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    width = fields.Float(required=False)
    


class UpdatePackagingDimensionsPayload(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    dimension = fields.List(fields.Nested(Dimension, required=False), required=False)
    


class UpdatePackagingDimensionsResponseSchema(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    


class Tax(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    rate = fields.Float(required=False)
    
    breakup = fields.List(fields.Dict(required=False), required=False)
    
    amount = fields.Dict(required=False)
    


class AmountSchema(BaseSchema):
    # Order swagger.json

    
    currency = fields.Str(required=False)
    
    value = fields.Float(required=False)
    


class Charge(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    amount = fields.Nested(AmountSchema, required=False)
    
    tax = fields.Nested(Tax, required=False)
    
    code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class LineItem(BaseSchema):
    # Order swagger.json

    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    custom_message = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    external_line_id = fields.Str(required=False)
    


class ProcessingDates(BaseSchema):
    # Order swagger.json

    
    dp_pickup_slot = fields.Dict(required=False)
    
    dispatch_after_date = fields.Str(required=False)
    
    dispatch_by_date = fields.Str(required=False)
    
    confirm_by_date = fields.Str(required=False)
    
    customer_pickup_slot = fields.Dict(required=False)
    
    pack_by_date = fields.Str(required=False)
    


class Tag(BaseSchema):
    # Order swagger.json

    
    slug = fields.Str(required=False)
    
    display_text = fields.Str(required=False)
    


class ProcessAfterConfig(BaseSchema):
    # Order swagger.json

    
    is_scheduled_shipment = fields.Boolean(required=False)
    
    enable_processing_after = fields.Str(required=False)
    


class SystemMessages(BaseSchema):
    # Order swagger.json

    
    message_type = fields.Str(required=False)
    
    priority = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    inject_at = fields.List(fields.Str(required=False), required=False)
    


class Shipment(BaseSchema):
    # Order swagger.json

    
    line_items = fields.List(fields.Nested(LineItem, required=False), required=False)
    
    external_shipment_id = fields.Str(required=False)
    
    processing_dates = fields.Nested(ProcessingDates, required=False)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    priority = fields.Int(required=False)
    
    location_id = fields.Int(required=False)
    
    order_type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    system_messages = fields.List(fields.Nested(SystemMessages, required=False), required=False)
    
    process_after_config = fields.Nested(ProcessAfterConfig, required=False)
    
    parent_type = fields.Str(required=False, allow_none=True)
    
    store_invoice_id = fields.Str(required=False, allow_none=True)
    
    lock_status = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False, allow_none=True)
    
    billing_address_json = fields.Nested(Address, required=False)
    
    id = fields.Str(required=False)
    
    fulfilment_priority = fields.Int(required=False, allow_none=True)
    
    is_active = fields.Boolean(required=False)
    
    previous_shipment_id = fields.Str(required=False, allow_none=True)
    
    pdf_links = fields.Dict(required=False, allow_none=True)
    
    delivery_address_json = fields.Nested(Address, required=False)
    
    eway_bill_id = fields.Str(required=False, allow_none=True)
    
    affiliate_shipment_id = fields.Str(required=False, allow_none=True)
    
    fynd_order_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    delivery_awb_number = fields.Str(required=False, allow_none=True)
    
    hand_over_contact_json = fields.Nested(Address, required=False)
    
    credit_note_id = fields.Str(required=False, allow_none=True)
    
    parent_id = fields.Str(required=False, allow_none=True)
    
    affiliate_id = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False, allow_none=True)
    
    vertical = fields.Str(required=False, allow_none=True)
    
    quantity = fields.Float(required=False, allow_none=True)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    price = fields.Nested(Prices, required=False)
    
    gst = fields.Nested(ShipmentGstDetails, required=False)
    


class GeoLocationSchema(BaseSchema):
    # Order swagger.json

    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    


class ShippingInfo(BaseSchema):
    # Order swagger.json

    
    alternate_mobile_number = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    customer_code = fields.Str(required=False)
    
    shipping_type = fields.Str(required=False)
    
    middle_name = fields.Str(required=False)
    
    primary_mobile_number = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    geo_location = fields.Nested(GeoLocationSchema, required=False)
    
    gender = fields.Str(required=False)
    
    house_no = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    external_customer_code = fields.Str(required=False)
    
    floor_no = fields.Str(required=False)
    
    alternate_email = fields.Str(required=False)
    
    slot = fields.List(fields.Dict(required=False), required=False)
    
    address = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    primary_email = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    


class BillingInfo(BaseSchema):
    # Order swagger.json

    
    alternate_mobile_number = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    customer_code = fields.Str(required=False)
    
    middle_name = fields.Str(required=False)
    
    primary_mobile_number = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    house_no = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    external_customer_code = fields.Str(required=False)
    
    floor_no = fields.Str(required=False)
    
    alternate_email = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    primary_email = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    


class UserInfo(BaseSchema):
    # Order swagger.json

    
    user_id = fields.Str(required=False)
    
    user_type = fields.Str(required=False)
    
    primary_email = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    primary_mobile_number = fields.Str(required=False)
    


class TaxInfo(BaseSchema):
    # Order swagger.json

    
    b2b_gstin_number = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    pan_no = fields.Str(required=False)
    


class PaymentMethod(BaseSchema):
    # Order swagger.json

    
    collect_by = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    refund_by = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    meta = fields.Dict(required=False)
    
    transaction_data = fields.Dict(required=False)
    


class PaymentInfo(BaseSchema):
    # Order swagger.json

    
    primary_mode = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMethod, required=False), required=False)
    


class CreateOrderAPI(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    
    shipping_info = fields.Nested(ShippingInfo, required=False)
    
    billing_info = fields.Nested(ShippingInfo, required=False)
    
    currency_info = fields.Dict(required=False)
    
    external_order_id = fields.Str(required=False)
    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    external_creation_date = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    tax_info = fields.Nested(TaxInfo, required=False)
    
    config = fields.Nested(CreateOrderConfig, required=False)
    
    payment_info = fields.Nested(PaymentInfo, required=False)
    
    user_info = fields.Nested(UserInfo, required=False)
    
    ordering_store_id = fields.Int(required=False)
    
    order_platform = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    system_messages = fields.List(fields.Nested(SystemMessages, required=False), required=False)
    
    order_type = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    external_shipment_id = fields.Str(required=False)
    


class CreateOrderErrorReponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    errors = fields.Str(required=False)
    
    status_code = fields.Float(required=False)
    
    fynd_order_id = fields.Str(required=False)
    


class PaymentMethods(BaseSchema):
    # Order swagger.json

    
    collect_by = fields.Str(required=False)
    
    refund_by = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    


class CreateChannelPaymentInfo(BaseSchema):
    # Order swagger.json

    
    source = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMethods, required=False), required=False)
    
    mode_of_payment = fields.Str(required=False)
    


class CreateChannelConfig(BaseSchema):
    # Order swagger.json

    
    dp_configuration = fields.Nested(DPConfiguration, required=False)
    
    shipment_assignment = fields.Str(required=False)
    
    location_reassignment = fields.Boolean(required=False)
    
    logo_url = fields.Dict(required=False)
    
    payment_info = fields.Nested(CreateChannelPaymentInfo, required=False)
    
    lock_states = fields.List(fields.Str(required=False), required=False)
    


class CreateChannelConfigData(BaseSchema):
    # Order swagger.json

    
    config_data = fields.Nested(CreateChannelConfig, required=False)
    


class CreateChannelConifgErrorResponseSchema(BaseSchema):
    # Order swagger.json

    
    error = fields.Str(required=False)
    
    request_id = fields.Str(required=False, allow_none=True)
    
    status = fields.Int(required=False)
    
    info = fields.Raw(required=False)
    
    stack_trace = fields.Str(required=False, allow_none=True)
    
    code = fields.Str(required=False, allow_none=True)
    
    meta = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False)
    
    exception = fields.Str(required=False, allow_none=True)
    


class UploadManifestConsent(BaseSchema):
    # Order swagger.json

    
    consent_url = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    


class CreateChannelConfigResponseSchema(BaseSchema):
    # Order swagger.json

    
    is_inserted = fields.Boolean(required=False)
    
    is_upserted = fields.Boolean(required=False)
    
    acknowledged = fields.Boolean(required=False)
    


class PlatformOrderUpdate(BaseSchema):
    # Order swagger.json

    
    order_id = fields.Str(required=False)
    


class ResponseDetail(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Int(required=False)
    


class FyndOrderIdList(BaseSchema):
    # Order swagger.json

    
    fynd_order_id = fields.List(fields.Str(required=False), required=False)
    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    mobile = fields.Int(required=False)
    


class OrderStatus(BaseSchema):
    # Order swagger.json

    
    order_details = fields.List(fields.Nested(FyndOrderIdList, required=False), required=False)
    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    mobile = fields.Int(required=False)
    


class BagStateTransitionMap(BaseSchema):
    # Order swagger.json

    
    fynd = fields.Dict(required=False)
    
    affiliate = fields.Dict(required=False)
    


class RoleBaseStateTransitionMapping(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    next_statuses = fields.List(fields.Str(required=False), required=False)
    


class FetchCreditBalanceRequestPayload(BaseSchema):
    # Order swagger.json

    
    affiliate_id = fields.Str(required=False)
    
    seller_id = fields.Str(required=False)
    
    customer_mobile_number = fields.Str(required=False)
    


class CreditBalanceInfo(BaseSchema):
    # Order swagger.json

    
    total_credited_balance = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    customer_mobile_number = fields.Str(required=False)
    


class FetchCreditBalanceResponsePayload(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(CreditBalanceInfo, required=False)
    


class RefundModeConfigRequestPayload(BaseSchema):
    # Order swagger.json

    
    fynd_order_id = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    customer_mobile_number = fields.Float(required=False)
    


class RefundOption(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class RefundModeFormat(BaseSchema):
    # Order swagger.json

    
    refund_to = fields.Str(required=False)
    


class RefundModeInfo(BaseSchema):
    # Order swagger.json

    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    options = fields.List(fields.Nested(RefundOption, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    format = fields.Nested(RefundModeFormat, required=False)
    


class RefundModeConfigResponsePayload(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(RefundModeInfo, required=False), required=False)
    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    


class AttachUserOtpData(BaseSchema):
    # Order swagger.json

    
    request_id = fields.Str(required=False)
    


class AttachUserInfo(BaseSchema):
    # Order swagger.json

    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class AttachOrderUser(BaseSchema):
    # Order swagger.json

    
    otp_data = fields.Nested(AttachUserOtpData, required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    user_info = fields.Nested(AttachUserInfo, required=False)
    


class AttachOrderUserResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class SendUserMobileOTP(BaseSchema):
    # Order swagger.json

    
    mobile = fields.Float(required=False)
    
    country_code = fields.Str(required=False)
    


class PointBlankOtpData(BaseSchema):
    # Order swagger.json

    
    request_id = fields.Str(required=False)
    
    resend_timer = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    mobile = fields.Int(required=False)
    


class SendUserMobileOtpResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Nested(PointBlankOtpData, required=False)
    


class VerifyOtpData(BaseSchema):
    # Order swagger.json

    
    request_id = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    otp_code = fields.Int(required=False)
    


class VerifyMobileOTP(BaseSchema):
    # Order swagger.json

    
    otp_data = fields.Nested(VerifyOtpData, required=False)
    
    fynd_order_id = fields.Str(required=False)
    


class VerifyOtpResponseData(BaseSchema):
    # Order swagger.json

    
    mobile = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class VerifyOtpResponseSchema(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Nested(VerifyOtpResponseData, required=False)
    


class BulkReportsFiltersSchema(BaseSchema):
    # Order swagger.json

    
    bag_status = fields.Str(required=False)
    
    operational_status = fields.Str(required=False)
    
    stores = fields.Str(required=False)
    
    time_to_dispatch = fields.Str(required=False)
    
    payment_methods = fields.Str(required=False)
    
    dp_ids = fields.Str(required=False)
    
    sales_channels = fields.Str(required=False)
    
    tags = fields.Str(required=False)
    
    lock_status = fields.Str(required=False)
    


class BulkReportsDownloadRequestSchema(BaseSchema):
    # Order swagger.json

    
    store_ids = fields.List(fields.Str(required=False), required=False)
    
    lane_type = fields.Str(required=False)
    
    custom_headers = fields.List(fields.Str(required=False), required=False)
    
    report_type = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    entities = fields.List(fields.Str(required=False), required=False)
    
    filter_type = fields.Str(required=False)
    
    is_cross_company_enabled = fields.Boolean(required=False)
    
    custom_filters_for_lane = fields.Dict(required=False)
    
    filters = fields.Nested(BulkReportsFiltersSchema, required=False)
    


class BulkReportsDownloadResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    batch_id = fields.Str(required=False)
    


class APIFailedResponseSchema(BaseSchema):
    # Order swagger.json

    
    status = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    


class BulkStateTransistionRequestSchema(BaseSchema):
    # Order swagger.json

    
    url = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    


class BulkStateTransistionResponseSchema(BaseSchema):
    # Order swagger.json

    
    status = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    


class ShipmentActionInfo(BaseSchema):
    # Order swagger.json

    
    label = fields.List(fields.Str(required=False), required=False)
    
    invoice = fields.List(fields.Str(required=False), required=False)
    
    failed_shipments = fields.List(fields.Dict(required=False), required=False)
    
    processing_shipments = fields.List(fields.Str(required=False), required=False)
    
    successful_shipments = fields.List(fields.Str(required=False), required=False)
    
    invoiceable_shipments = fields.List(fields.Str(required=False), required=False)
    
    failed_invoiced_shipments = fields.Dict(required=False)
    
    processing_invoice_shipments = fields.List(fields.Str(required=False), required=False)
    
    successful_invoiced_shipments = fields.List(fields.Str(required=False), required=False)
    


class BulkActionListingData(BaseSchema):
    # Order swagger.json

    
    store_id = fields.Int(required=False)
    
    uploaded_on = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    shipments_action_info = fields.Nested(ShipmentActionInfo, required=False)
    
    is_invoiceable = fields.Boolean(required=False)
    
    user_name = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    invoice_document_type = fields.Str(required=False)
    
    label_document_type = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    store_name = fields.Str(required=False)
    
    updated_ts = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    bulk_action_type = fields.Str(required=False)
    
    created_ts = fields.Str(required=False)
    
    invoice_status = fields.Str(required=False)
    
    do_invoice_label_generated = fields.Boolean(required=False)
    
    id = fields.Int(required=False)
    
    user_id = fields.Str(required=False)
    
    last_selected_invoice_label_type = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    uploaded_by = fields.Str(required=False)
    
    invoicelabel_document_type = fields.Str(required=False)
    
    failed_sh_count = fields.Int(required=False)
    
    successful_sh_count = fields.Int(required=False)
    
    total_count = fields.Int(required=False)
    
    failed_shipments = fields.List(fields.Str(required=False), required=False)
    
    successful_invoiced_count = fields.Int(required=False)
    
    failed_invoiced_count = fields.Int(required=False)
    
    total_invoiced_count = fields.Int(required=False)
    


class BulkListinPage(BaseSchema):
    # Order swagger.json

    
    current = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    total = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class BulkListingResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(BulkActionListingData, required=False), required=False)
    
    page = fields.Nested(BulkListinPage, required=False)
    
    total_count = fields.Int(required=False)
    


class JobDetailsData(BaseSchema):
    # Order swagger.json

    
    batch_id = fields.Str(required=False)
    
    total_shipments_count = fields.Int(required=False)
    
    successful_shipment_ids = fields.List(fields.Str(required=False), required=False)
    
    successful_shipments_count = fields.Int(required=False)
    
    failed_shipments_count = fields.Int(required=False)
    
    processing_shipments_count = fields.Int(required=False)
    
    company_id = fields.Str(required=False)
    


class JobDetailsResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(JobDetailsData, required=False), required=False)
    
    file_url = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    failed_records = fields.List(fields.Dict(required=False), required=False)
    
    uploaded_by = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    created_ts = fields.Str(required=False)
    
    uploaded_on = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class JobFailedResponseSchema(BaseSchema):
    # Order swagger.json

    
    file_name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class ManifestPageInfo(BaseSchema):
    # Order swagger.json

    
    current = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    size = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class ManifestItemDetails(BaseSchema):
    # Order swagger.json

    
    quantity = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    awb_number = fields.Str(required=False)
    
    invoice_id = fields.Str(required=False)
    
    shipment_created_at = fields.Str(required=False)
    


class ManifestShipmentListing(BaseSchema):
    # Order swagger.json

    
    total_count = fields.Int(required=False)
    
    lane = fields.Str(required=False)
    
    page = fields.Nested(ManifestPageInfo, required=False)
    
    success = fields.Boolean(required=False)
    
    status = fields.Int(required=False)
    
    items = fields.List(fields.Nested(ManifestItemDetails, required=False), required=False)
    
    message = fields.Str(required=False)
    


class DateRange(BaseSchema):
    # Order swagger.json

    
    from_date = fields.Str(required=False)
    
    to_date = fields.Str(required=False)
    


class Filters(BaseSchema):
    # Order swagger.json

    
    date_range = fields.Nested(DateRange, required=False)
    
    logo = fields.Str(required=False)
    
    from_date = fields.Str(required=False)
    
    stores = fields.Int(required=False)
    
    to_date = fields.Str(required=False)
    
    dp_name = fields.Str(required=False)
    
    dp_ids = fields.Str(required=False)
    
    lane = fields.Str(required=False)
    
    selected_shipments = fields.Str(required=False)
    
    store_name = fields.Str(required=False)
    
    deselected_shipments = fields.Str(required=False)
    


class ManifestFile(BaseSchema):
    # Order swagger.json

    
    key = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    bucket = fields.Str(required=False)
    


class ManifestMediaUpdate(BaseSchema):
    # Order swagger.json

    
    entity = fields.Str(required=False)
    
    link = fields.Str(required=False)
    
    code = fields.Int(required=False)
    
    media_type = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    
    file = fields.Nested(ManifestFile, required=False)
    


class PDFMeta(BaseSchema):
    # Order swagger.json

    
    consent = fields.Str(required=False, allow_none=True)
    
    media_updates = fields.List(fields.Nested(ManifestMediaUpdate, required=False), required=False)
    


class TotalShipmentPricesCount(BaseSchema):
    # Order swagger.json

    
    total_price = fields.Float(required=False)
    
    shipment_count = fields.Int(required=False)
    


class ManifestMeta(BaseSchema):
    # Order swagger.json

    
    filters = fields.Nested(Filters, required=False)
    
    total_shipment_prices_count = fields.Nested(TotalShipmentPricesCount, required=False)
    


class Manifest(BaseSchema):
    # Order swagger.json

    
    company_id = fields.Int(required=False)
    
    filters = fields.Nested(Filters, required=False)
    
    pdf_meta = fields.Nested(PDFMeta, required=False)
    
    meta = fields.Nested(ManifestMeta, required=False)
    
    is_active = fields.Boolean(required=False)
    
    user_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    created_ts = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    


class ManifestList(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(Manifest, required=False), required=False)
    
    page = fields.Nested(ManifestPageInfo, required=False)
    


class ManifestDetails(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(ManifestItemDetails, required=False), required=False)
    
    page = fields.Nested(ManifestPageInfo, required=False)
    
    additional_shipment_count = fields.Int(required=False)
    
    manifest_details = fields.List(fields.Nested(Manifest, required=False), required=False)
    


class FiltersRequestSchema(BaseSchema):
    # Order swagger.json

    
    date_range = fields.Nested(DateRange, required=False)
    
    logo = fields.Str(required=False)
    
    stores = fields.Int(required=False)
    
    dp_name = fields.Str(required=False)
    
    dp_ids = fields.Int(required=False)
    
    lane = fields.Str(required=False)
    
    store_name = fields.Str(required=False)
    


class ProcessManifest(BaseSchema):
    # Order swagger.json

    
    filters = fields.Nested(FiltersRequestSchema, required=False)
    
    action = fields.Str(required=False)
    
    unique_id = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    


class ProcessManifestResponseSchema(BaseSchema):
    # Order swagger.json

    
    company_id = fields.Int(required=False)
    
    filters = fields.Nested(Filters, required=False)
    
    user_id = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    


class ProcessManifestItemResponseSchema(BaseSchema):
    # Order swagger.json

    
    items = fields.Nested(ProcessManifestResponseSchema, required=False)
    


class FilterInfoOption(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    placeholder_text = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False, allow_none=True)
    
    min_search_size = fields.Int(required=False, allow_none=True)
    
    show_ui = fields.Boolean(required=False, allow_none=True)
    


class FiltersInfo(BaseSchema):
    # Order swagger.json

    
    options = fields.List(fields.Nested(FilterInfoOption, required=False), required=False)
    
    text = fields.Str(required=False)
    
    placeholder_text = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False)
    
    required = fields.Boolean(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    


class ManifestFiltersResponseSchema(BaseSchema):
    # Order swagger.json

    
    advance_filter = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    global_filter = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    


class PageDetails(BaseSchema):
    # Order swagger.json

    
    current = fields.Int(required=False, allow_none=True)
    
    has_next = fields.Boolean(required=False, allow_none=True)
    
    has_previous = fields.Boolean(required=False, allow_none=True)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False, allow_none=True)
    
    type = fields.Str(required=False, allow_none=True)
    


class EInvoiceIrnDetails(BaseSchema):
    # Order swagger.json

    
    ack_dt = fields.Str(required=False)
    
    ack_no = fields.Str(required=False)
    
    irn = fields.Str(required=False)
    
    signed_invoice = fields.Str(required=False)
    
    signed_qr_code = fields.Str(required=False)
    


class EInvoiceErrorDetails(BaseSchema):
    # Order swagger.json

    
    error_code = fields.Str(required=False)
    
    error_message = fields.Str(required=False)
    


class EInvoiceDetails(BaseSchema):
    # Order swagger.json

    
    irn_details = fields.Nested(EInvoiceIrnDetails, required=False)
    
    error_details = fields.List(fields.Nested(EInvoiceErrorDetails, required=False), required=False)
    


class EInvoiceResponseData(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    einvoice_type = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    einvoice_info = fields.Nested(EInvoiceDetails, required=False)
    


class EInvoiceRetry(BaseSchema):
    # Order swagger.json

    
    shipments_data = fields.List(fields.Nested(EInvoiceRetryShipmentData, required=False), required=False)
    


class EInvoiceRetryResponseSchema(BaseSchema):
    # Order swagger.json

    
    response_data = fields.List(fields.Nested(EInvoiceResponseData, required=False), required=False)
    


class EInvoiceErrorInfo(BaseSchema):
    # Order swagger.json

    
    error_details = fields.List(fields.Nested(EInvoiceErrorDetails, required=False), required=False)
    


class EInvoiceErrorResponseData(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    einvoice_type = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    einvoice_info = fields.Nested(EInvoiceErrorInfo, required=False)
    


class EInvoiceErrorResponseSchema(BaseSchema):
    # Order swagger.json

    
    response_data = fields.List(fields.Nested(EInvoiceErrorResponseData, required=False), required=False)
    
    message = fields.Str(required=False)
    


class EInvoiceErrorResponseDetails(BaseSchema):
    # Order swagger.json

    
    response_data = fields.List(fields.Nested(EInvoiceErrorResponseData, required=False), required=False)
    
    message = fields.Str(required=False)
    


class EInvoiceRetryShipmentData(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    einvoice_type = fields.Str(required=False)
    


class CourierPartnerTrackingDetails(BaseSchema):
    # Order swagger.json

    
    awb = fields.Str(required=False)
    
    dp_location = fields.Str(required=False, allow_none=True)
    
    dp_name = fields.Str(required=False)
    
    dp_status = fields.Str(required=False)
    
    dp_status_updated_at = fields.Str(required=False)
    
    estimated_delivery_date = fields.Str(required=False, allow_none=True)
    
    id = fields.Int(required=False)
    
    journey = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    operational_status = fields.Str(required=False)
    
    promised_delivery_date = fields.Str(required=False, allow_none=True)
    
    remark = fields.Str(required=False, allow_none=True)
    
    shipment_id = fields.Str(required=False)
    


class CourierPartnerTrackingResponseSchema(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(CourierPartnerTrackingDetails, required=False), required=False)
    
    page = fields.Nested(PageDetails, required=False)
    


class LogsChannelDetails(BaseSchema):
    # Order swagger.json

    
    channel_id = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    logo = fields.Str(required=False, allow_none=True)
    
    channel_shipment_id = fields.Str(required=False, allow_none=True)
    


class LogPaymentDetails(BaseSchema):
    # Order swagger.json

    
    payment_mode = fields.Str(required=False, allow_none=True)
    
    amount_paid = fields.Str(required=False, allow_none=True)
    


class FailedOrdersItem(BaseSchema):
    # Order swagger.json

    
    log_id = fields.Int(required=False)
    
    order_id = fields.Str(required=False)
    
    channel = fields.Nested(LogsChannelDetails, required=False)
    
    payment = fields.Nested(LogPaymentDetails, required=False)
    
    created_at = fields.Str(required=False)
    
    error_message = fields.Str(required=False)
    
    display_message = fields.Str(required=False)
    
    method_name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class FailedOrderLogs(BaseSchema):
    # Order swagger.json

    
    items = fields.Nested(FailedOrdersItem, required=False)
    
    page = fields.Nested(PageDetails, required=False)
    


class FailedOrderLogDetails(BaseSchema):
    # Order swagger.json

    
    error_trace = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    


class GenerateInvoiceIDResponseData(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    invoice_id = fields.Str(required=False, allow_none=True)
    
    error_message = fields.Boolean(required=False, allow_none=True)
    


class GenerateInvoiceIDErrorResponseData(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    invoice_id = fields.Boolean(required=False, allow_none=True)
    
    error_message = fields.Str(required=False, allow_none=True)
    


class GenerateInvoiceIDRequestSchema(BaseSchema):
    # Order swagger.json

    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    


class GenerateInvoiceIDResponseSchema(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(GenerateInvoiceIDResponseData, required=False), required=False)
    


class GenerateInvoiceIDErrorResponseSchema(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(GenerateInvoiceIDErrorResponseData, required=False), required=False)
    


class ManifestResponseSchema(BaseSchema):
    # Order swagger.json

    
    items = fields.Nested(ManifestItems, required=False)
    


class ProcessManifestRequestSchema(BaseSchema):
    # Order swagger.json

    
    action = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    
    filters = fields.Nested(Filters, required=False)
    
    unique_id = fields.Str(required=False)
    


class ManifestItems(BaseSchema):
    # Order swagger.json

    
    filters = fields.Nested(Filters, required=False)
    
    manifest_id = fields.Str(required=False)
    
    unique_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    dp_id = fields.Str(required=False, allow_none=True)
    
    courier_partner_slug = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class ManifestErrorResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    


class ConfigData(BaseSchema):
    # Order swagger.json

    
    acknowledged = fields.Boolean(required=False)
    
    is_upserted = fields.Boolean(required=False)
    
    is_inserted = fields.Boolean(required=False)
    


class ConfigUpdatedResponseSchema(BaseSchema):
    # Order swagger.json

    
    data = fields.List(fields.Nested(ConfigData, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class FlagData(BaseSchema):
    # Order swagger.json

    
    filter = fields.Dict(required=False)
    


class Flags(BaseSchema):
    # Order swagger.json

    
    allow_partial_transition = fields.List(fields.Nested(FlagData, required=False), required=False)
    
    can_break_entity = fields.List(fields.Nested(FlagData, required=False), required=False)
    
    allowed_bag_updates = fields.List(fields.Nested(FlagData, required=False), required=False)
    
    allowed_bag_status_updates = fields.List(fields.Nested(FlagData, required=False), required=False)
    
    allowed_entity_updates = fields.List(fields.Nested(FlagData, required=False), required=False)
    
    allowed_entity_status_updates = fields.List(fields.Nested(FlagData, required=False), required=False)
    
    status_update_type = fields.List(fields.Nested(FlagData, required=False), required=False)
    
    is_bag_status_reason_allowed = fields.List(fields.Nested(FlagData, required=False), required=False)
    
    is_entity_status_reason_allowed = fields.List(fields.Nested(FlagData, required=False), required=False)
    
    transition_strategy = fields.List(fields.Nested(FlagData, required=False), required=False)
    


class Filter(BaseSchema):
    # Order swagger.json

    
    order_type = fields.Str(required=False)
    
    is_partial_transition = fields.Boolean(required=False)
    
    auto_trigger_dp_assignment_acf = fields.Boolean(required=False)
    
    lock_status = fields.Str(required=False)
    
    lock_after_transition = fields.Boolean(required=False)
    
    resume_tasks_after_unlock = fields.Boolean(required=False)
    
    is_invoice_id_present = fields.Boolean(required=False)
    
    is_credit_note_generated = fields.Boolean(required=False)
    
    fulfill_virtual_invoice = fields.Boolean(required=False)
    
    next_status = fields.Str(required=False)
    
    is_hook_enabled = fields.Boolean(required=False)
    
    pos_credit_note_check = fields.Boolean(required=False)
    
    order_platform = fields.Str(required=False)
    
    refund_type = fields.Str(required=False)
    
    is_non_pos_platform = fields.Boolean(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    seller_country_code = fields.Str(required=False)
    
    customer_country_code = fields.Str(required=False)
    
    is_test_order = fields.Boolean(required=False)
    
    task_trigger_condition = fields.List(fields.Str(required=False), required=False)
    


class PostHook(BaseSchema):
    # Order swagger.json

    
    task = fields.Str(required=False)
    
    kwargs = fields.Dict(required=False)
    
    filters = fields.Nested(Filter, required=False)
    


class PreHook(BaseSchema):
    # Order swagger.json

    
    task = fields.Str(required=False)
    
    kwargs = fields.Dict(required=False)
    
    filters = fields.Nested(Filter, required=False)
    


class Config(BaseSchema):
    # Order swagger.json

    
    from_state = fields.Str(required=False)
    
    to_state = fields.Str(required=False)
    
    pre_hooks = fields.List(fields.Nested(PreHook, required=False), required=False)
    
    post_hooks = fields.List(fields.Nested(PostHook, required=False), required=False)
    
    flags = fields.Nested(Flags, required=False)
    


class TransitionConfigCondition(BaseSchema):
    # Order swagger.json

    
    app_id = fields.Str(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    ordering_source = fields.Str(required=False)
    
    entity = fields.Str(required=False)
    


class TransitionConfigData(BaseSchema):
    # Order swagger.json

    
    conditions = fields.Nested(TransitionConfigCondition, required=False)
    
    configs = fields.List(fields.Nested(Config, required=False), required=False)
    


class TransitionConfigPayload(BaseSchema):
    # Order swagger.json

    
    data = fields.Nested(TransitionConfigData, required=False)
    


class RuleListRequestSchema(BaseSchema):
    # Order swagger.json

    
    page_no = fields.Int(required=False)
    
    channel = fields.List(fields.Str(required=False), required=False)
    
    department = fields.List(fields.Str(required=False), required=False)
    
    id = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    


class RuleErrorResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    


class RMAPageInfo(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    


class RuleAction(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(Reason, required=False), required=False)
    


class QuestionSetItem(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    


class Reason(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    reasons = fields.List(fields.Nested(lambda: Reason(exclude=('reasons')), required=False), required=False)
    
    qc_type = fields.List(fields.Str(required=False), required=False)
    
    question_set = fields.List(fields.Nested(QuestionSet, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    


class Conditions(BaseSchema):
    # Order swagger.json

    
    department = fields.Str(required=False)
    
    l3 = fields.Str(required=False)
    


class RuleItem(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    channel = fields.Str(required=False)
    
    actions = fields.Nested(RuleAction, required=False)
    
    qc_enabled = fields.Boolean(required=False)
    
    is_deleted = fields.Boolean(required=False)
    
    conditions = fields.Nested(Conditions, required=False)
    
    meta = fields.Dict(required=False)
    
    rule_type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class RuleError(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class RuleListResponseSchema(BaseSchema):
    # Order swagger.json

    
    page = fields.Nested(RMAPageInfo, required=False)
    
    items = fields.List(fields.Nested(RuleItem, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(RuleError, required=False)
    


class UpdateShipmentPaymentMode(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    products = fields.List(fields.Nested(ProductSchema, required=False), required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMethodSchema, required=False), required=False)
    


class CommonErrorResponseSchema(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    


class ExceptionErrorResponseSchema(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    


class ProductSchema(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMethodSchema, required=False), required=False)
    


class PaymentMethodSchema(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    meta = fields.Nested(PaymentMetaDataSchema, required=False)
    
    identifier = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    action = fields.Nested(ActionDetailSchema, required=False)
    
    refund_by = fields.Str(required=False)
    
    collect_by = fields.Str(required=False)
    


class ActionDetailSchema(BaseSchema):
    # Order swagger.json

    
    name = fields.Raw(required=False)
    
    current_mode = fields.Str(required=False)
    
    current_identifier = fields.Str(required=False)
    
    refund_to = fields.Str(required=False)
    


class PaymentMetaDataSchema(BaseSchema):
    # Order swagger.json

    
    payment_gateway = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    logo_url = fields.Nested(PaymentMetaLogoURLSchema, required=False)
    


class PaymentMetaLogoURLSchema(BaseSchema):
    # Order swagger.json

    
    large = fields.Str(required=False)
    
    small = fields.Str(required=False)
    


class ValidationError(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    field = fields.Str(required=False)
    


class Page(BaseSchema):
    # Order swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    


class BagReasonMeta(BaseSchema):
    # Order swagger.json

    
    show_text_area = fields.Boolean(required=False)
    


class QuestionSet(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    


class BagReasons(BaseSchema):
    # Order swagger.json

    
    qc_type = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    meta = fields.Nested(BagReasonMeta, required=False)
    
    question_set = fields.List(fields.Nested(QuestionSet, required=False), required=False)
    
    reasons = fields.List(fields.Nested(lambda: BagReasons(exclude=('reasons')), required=False), required=False)
    


class ShipmentBagReasons(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(BagReasons, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    rule_id = fields.Int(required=False, allow_none=True)
    


class ShipmentStatus(BaseSchema):
    # Order swagger.json

    
    current_shipment_status = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    id = fields.Int(required=False, allow_none=True)
    
    bag_list = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    created_at = fields.Str(required=False, allow_none=True)
    
    created_ts = fields.Str(required=False, allow_none=True)
    
    shipment_id = fields.Str(required=False, allow_none=True)
    
    status_created_at = fields.Str(required=False, allow_none=True)
    
    updated_ts = fields.Str(required=False, allow_none=True)
    
    status = fields.Str(required=False)
    


class UserDataInfo(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False, allow_none=True)
    
    user_oid = fields.Str(required=False, allow_none=True)
    
    mongo_user_id = fields.Str(required=False, allow_none=True)
    
    external_customer_id = fields.Str(required=False, allow_none=True)
    
    first_name = fields.Str(required=False, allow_none=True)
    
    last_name = fields.Str(required=False, allow_none=True)
    
    mobile = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    is_anonymous_user = fields.Boolean(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    gender = fields.Str(required=False, allow_none=True)
    
    country_phone_code = fields.Str(required=False)
    


class Address(BaseSchema):
    # Order swagger.json

    
    phone = fields.Str(required=False, allow_none=True)
    
    address2 = fields.Str(required=False, allow_none=True)
    
    address = fields.Str(required=False, allow_none=True)
    
    longitude = fields.Float(required=False, allow_none=True)
    
    pincode = fields.Str(required=False, allow_none=True)
    
    area = fields.Str(required=False, allow_none=True)
    
    address_type = fields.Str(required=False, allow_none=True)
    
    country = fields.Str(required=False, allow_none=True)
    
    address_category = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False, allow_none=True)
    
    created_at = fields.Str(required=False, allow_none=True)
    
    address1 = fields.Str(required=False, allow_none=True)
    
    display_address = fields.Str(required=False, allow_none=True)
    
    landmark = fields.Str(required=False, allow_none=True)
    
    updated_at = fields.Str(required=False, allow_none=True)
    
    version = fields.Str(required=False, allow_none=True)
    
    latitude = fields.Float(required=False, allow_none=True)
    
    contact_person = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False, allow_none=True)
    
    city = fields.Str(required=False, allow_none=True)
    
    area_code_slug = fields.Str(required=False, allow_none=True)
    
    country_code = fields.Str(required=False, allow_none=True)
    
    country_iso_code = fields.Str(required=False, allow_none=True)
    
    country_phone_code = fields.Str(required=False, allow_none=True)
    
    delivery_address_id = fields.Int(required=False)
    
    geo_location = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    code = fields.Str(required=False, allow_none=True)
    


class ShipmentListingChannel(BaseSchema):
    # Order swagger.json

    
    channel_shipment_id = fields.Str(required=False, allow_none=True)
    
    is_affiliate = fields.Boolean(required=False, allow_none=True)
    
    logo = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    


class Prices(BaseSchema):
    # Order swagger.json

    
    refund_credit = fields.Float(required=False, allow_none=True)
    
    amount_paid_roundoff = fields.Float(required=False, allow_none=True)
    
    price_effective = fields.Float(required=False, allow_none=True)
    
    promotion_effective_discount = fields.Float(required=False, allow_none=True)
    
    pm_price_split = fields.Float(required=False, allow_none=True)
    
    refund_amount = fields.Float(required=False, allow_none=True)
    
    transfer_price = fields.Float(required=False, allow_none=True)
    
    coupon_effective_discount = fields.Float(required=False, allow_none=True)
    
    tax_collected_at_source = fields.Float(required=False, allow_none=True)
    
    brand_calculated_amount = fields.Float(required=False, allow_none=True)
    
    delivery_charge = fields.Float(required=False, allow_none=True)
    
    cashback = fields.Float(required=False, allow_none=True)
    
    value_of_good = fields.Float(required=False, allow_none=True)
    
    cashback_applied = fields.Float(required=False, allow_none=True)
    
    cod_charges = fields.Float(required=False, allow_none=True)
    
    price_marked = fields.Float(required=False, allow_none=True)
    
    amount_paid = fields.Float(required=False, allow_none=True)
    
    coupon_value = fields.Float(required=False, allow_none=True)
    
    discount = fields.Float(required=False, allow_none=True)
    
    fynd_credits = fields.Float(required=False, allow_none=True)
    
    gift_price = fields.Float(required=False, allow_none=True)
    
    amount_to_be_collected = fields.Float(required=False, allow_none=True)
    
    loyalty_discount = fields.Float(required=False)
    


class ChargeDistributionSchema(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    logic = fields.Str(required=False)
    


class ChargeDistributionLogic(BaseSchema):
    # Order swagger.json

    
    distribution = fields.Nested(ChargeDistributionSchema, required=False)
    
    distribution_level = fields.Str(required=False)
    


class ChargeAmountCurrency(BaseSchema):
    # Order swagger.json

    
    value = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    


class ChargeAmount(BaseSchema):
    # Order swagger.json

    
    base_currency = fields.Nested(ChargeAmountCurrency, required=False)
    
    ordering_currency = fields.Nested(ChargeAmountCurrency, required=False)
    


class PriceAdjustmentCharge(BaseSchema):
    # Order swagger.json

    
    code = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False, allow_none=True)
    
    amount = fields.Nested(ChargeAmount, required=False)
    
    distribution_logic = fields.Nested(ChargeDistributionLogic, required=False)
    


class OrderingCurrencyPrices(BaseSchema):
    # Order swagger.json

    
    refund_credit = fields.Float(required=False, allow_none=True)
    
    amount_paid_roundoff = fields.Float(required=False, allow_none=True)
    
    price_effective = fields.Float(required=False, allow_none=True)
    
    promotion_effective_discount = fields.Float(required=False, allow_none=True)
    
    pm_price_split = fields.Float(required=False, allow_none=True)
    
    refund_amount = fields.Float(required=False, allow_none=True)
    
    transfer_price = fields.Float(required=False, allow_none=True)
    
    coupon_effective_discount = fields.Float(required=False, allow_none=True)
    
    tax_collected_at_source = fields.Float(required=False, allow_none=True)
    
    brand_calculated_amount = fields.Float(required=False, allow_none=True)
    
    delivery_charge = fields.Float(required=False, allow_none=True)
    
    cashback = fields.Float(required=False, allow_none=True)
    
    value_of_good = fields.Float(required=False, allow_none=True)
    
    cashback_applied = fields.Float(required=False, allow_none=True)
    
    cod_charges = fields.Float(required=False, allow_none=True)
    
    price_marked = fields.Float(required=False, allow_none=True)
    
    amount_paid = fields.Float(required=False, allow_none=True)
    
    coupon_value = fields.Float(required=False, allow_none=True)
    
    discount = fields.Float(required=False, allow_none=True)
    
    fynd_credits = fields.Float(required=False, allow_none=True)
    
    gift_price = fields.Float(required=False, allow_none=True)
    
    amount_to_be_collected = fields.Float(required=False, allow_none=True)
    
    loyalty_discount = fields.Float(required=False)
    


class Identifier(BaseSchema):
    # Order swagger.json

    
    alu = fields.Str(required=False, allow_none=True)
    
    ean = fields.Str(required=False, allow_none=True)
    
    sku_code = fields.Str(required=False, allow_none=True)
    
    upc = fields.Str(required=False, allow_none=True)
    
    isbn = fields.Str(required=False, allow_none=True)
    


class TaxComponent(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    rate = fields.Float(required=False)
    
    tax_amount = fields.Float(required=False)
    
    taxable_amount = fields.Float(required=False)
    


class FinancialBreakup(BaseSchema):
    # Order swagger.json

    
    refund_credit = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Int(required=False, allow_none=True)
    
    price_effective = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    transfer_price = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    
    tax_collected_at_source = fields.Float(required=False, allow_none=True)
    
    brand_calculated_amount = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    gst_tag = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    cashback = fields.Float(required=False)
    
    item_name = fields.Str(required=False)
    
    value_of_good = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    amount_paid = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    amount_to_be_collected = fields.Float(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    total_units = fields.Int(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    taxes = fields.List(fields.Nested(TaxComponent, required=False), required=False)
    
    loyalty_discount = fields.Float(required=False)
    


class GSTDetailsData(BaseSchema):
    # Order swagger.json

    
    cgst_tax_percentage = fields.Float(required=False, allow_none=True)
    
    gstin_code = fields.Str(required=False, allow_none=True)
    
    value_of_good = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    
    igst_tax_percentage = fields.Float(required=False, allow_none=True)
    
    gst_tax_percentage = fields.Float(required=False, allow_none=True)
    
    hsn_code_id = fields.Str(required=False, allow_none=True)
    
    igst_gst_fee = fields.Float(required=False, allow_none=True)
    
    is_default_hsn_code = fields.Boolean(required=False, allow_none=True)
    
    sgst_gst_fee = fields.Float(required=False, allow_none=True)
    
    tax_collected_at_source = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    cgst_gst_fee = fields.Float(required=False, allow_none=True)
    
    gst_tag = fields.Str(required=False, allow_none=True)
    
    sgst_tax_percentage = fields.Float(required=False, allow_none=True)
    
    hsn_code = fields.Str(required=False, allow_none=True)
    


class BagStateMapper(BaseSchema):
    # Order swagger.json

    
    is_active = fields.Boolean(required=False, allow_none=True)
    
    app_display_name = fields.Str(required=False, allow_none=True)
    
    state_type = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    journey_type = fields.Str(required=False)
    
    app_state_name = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    
    app_facing = fields.Boolean(required=False, allow_none=True)
    
    notify_customer = fields.Boolean(required=False, allow_none=True)
    
    display_name = fields.Str(required=False)
    


class BagStatusHistory(BaseSchema):
    # Order swagger.json

    
    forward = fields.Boolean(required=False, allow_none=True)
    
    store_id = fields.Int(required=False, allow_none=True)
    
    delivery_awb_number = fields.Str(required=False, allow_none=True)
    
    kafka_sync = fields.Boolean(required=False, allow_none=True)
    
    delivery_partner_id = fields.Int(required=False, allow_none=True)
    
    app_display_name = fields.Str(required=False, allow_none=True)
    
    state_id = fields.Int(required=False, allow_none=True)
    
    state_type = fields.Str(required=False)
    
    bsh_id = fields.Int(required=False, allow_none=True)
    
    created_at = fields.Str(required=False, allow_none=True)
    
    created_ts = fields.Str(required=False, allow_none=True)
    
    shipment_id = fields.Str(required=False, allow_none=True)
    
    updated_at = fields.Str(required=False, allow_none=True)
    
    updated_ts = fields.Str(required=False, allow_none=True)
    
    bag_state_mapper = fields.Nested(BagStateMapper, required=False)
    
    bag_id = fields.Int(required=False, allow_none=True)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    status = fields.Str(required=False)
    
    display_name = fields.Str(required=False, allow_none=True)
    


class Dimensions(BaseSchema):
    # Order swagger.json

    
    height = fields.Float(required=False, allow_none=True)
    
    width = fields.Float(required=False, allow_none=True)
    
    is_default = fields.Boolean(required=False, allow_none=True)
    
    unit = fields.Str(required=False, allow_none=True)
    
    length = fields.Float(required=False, allow_none=True)
    


class ReturnConfig(BaseSchema):
    # Order swagger.json

    
    returnable = fields.Boolean(required=False, allow_none=True)
    
    time = fields.Float(required=False, allow_none=True)
    
    unit = fields.Str(required=False, allow_none=True)
    


class Weight(BaseSchema):
    # Order swagger.json

    
    is_default = fields.Boolean(required=False, allow_none=True)
    
    shipping = fields.Int(required=False, allow_none=True)
    
    unit = fields.Str(required=False, allow_none=True)
    


class Article(BaseSchema):
    # Order swagger.json

    
    seller_identifier = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    set = fields.Dict(required=False, allow_none=True)
    
    dimensions = fields.Nested(Dimensions, required=False)
    
    currency = fields.Dict(required=False, allow_none=True)
    
    esp_modified = fields.Boolean(required=False, allow_none=True)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    code = fields.Str(required=False, allow_none=True)
    
    weight = fields.Nested(Weight, required=False)
    
    _id = fields.Str(required=False)
    
    identifiers = fields.Dict(required=False)
    
    raw_meta = fields.Str(required=False, allow_none=True)
    
    size = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False, allow_none=True)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    


class ShipmentListingBrand(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False, allow_none=True)
    
    created_on = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    logo_base64 = fields.Str(required=False, allow_none=True)
    


class ReplacementDetails(BaseSchema):
    # Order swagger.json

    
    replacement_type = fields.Str(required=False, allow_none=True)
    
    original_affiliate_order_id = fields.Str(required=False, allow_none=True)
    


class AffiliateMeta(BaseSchema):
    # Order swagger.json

    
    order_item_id = fields.Str(required=False, allow_none=True)
    
    channel_order_id = fields.Str(required=False, allow_none=True)
    
    employee_discount = fields.Float(required=False, allow_none=True)
    
    box_type = fields.Str(required=False, allow_none=True)
    
    quantity = fields.Int(required=False, allow_none=True)
    
    size_level_total_qty = fields.Int(required=False, allow_none=True)
    
    loyalty_discount = fields.Float(required=False)
    
    replacement_details = fields.Nested(ReplacementDetails, required=False)
    
    channel_shipment_id = fields.Str(required=False, allow_none=True)
    
    marketplace_invoice_id = fields.Str(required=False, allow_none=True)
    
    due_date = fields.Str(required=False, allow_none=True)
    
    coupon_code = fields.Str(required=False, allow_none=True)
    
    is_priority = fields.Boolean(required=False, allow_none=True)
    
    is_serial_number_required = fields.Boolean(required=False, allow_none=True)
    
    fulfilment_priority = fields.Int(required=False, allow_none=True)
    
    customer_selling_price = fields.Float(required=False, allow_none=True)
    


class AffiliateBagDetails(BaseSchema):
    # Order swagger.json

    
    affiliate_meta = fields.Nested(AffiliateMeta, required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    employee_discount = fields.Float(required=False, allow_none=True)
    
    affiliate_bag_id = fields.Str(required=False)
    
    loyalty_discount = fields.Float(required=False)
    


class PlatformArticleAttributes(BaseSchema):
    # Order swagger.json

    
    currency = fields.Str(required=False, allow_none=True)
    


class PlatformItem(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False, allow_none=True)
    
    attributes = fields.Nested(PlatformArticleAttributes, required=False)
    
    brand_id = fields.Int(required=False, allow_none=True)
    
    slug_key = fields.Str(required=False, allow_none=True)
    
    l3_category = fields.Int(required=False, allow_none=True)
    
    l3_category_name = fields.Str(required=False, allow_none=True)
    
    last_updated_at = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    l2_category = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Str(required=False, allow_none=True)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False, allow_none=True)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    size = fields.Str(required=False, allow_none=True)
    
    can_cancel = fields.Boolean(required=False, allow_none=True)
    
    can_return = fields.Boolean(required=False, allow_none=True)
    
    branch_url = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    color = fields.Str(required=False, allow_none=True)
    
    department_id = fields.Int(required=False, allow_none=True)
    
    images = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class Dates(BaseSchema):
    # Order swagger.json

    
    delivery_date = fields.Str(required=False, allow_none=True)
    
    order_created = fields.Str(required=False, allow_none=True)
    


class BagReturnableCancelableStatus(BaseSchema):
    # Order swagger.json

    
    is_returnable = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    can_be_cancelled = fields.Boolean(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    is_customer_return_allowed = fields.Boolean(required=False)
    


class BagUnit(BaseSchema):
    # Order swagger.json

    
    bag_type = fields.Str(required=False, allow_none=True)
    
    gst = fields.Nested(GSTDetailsData, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    bag_expiry_date = fields.Str(required=False, allow_none=True)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    article = fields.Nested(Article, required=False)
    
    brand = fields.Nested(ShipmentListingBrand, required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    product_quantity = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False, allow_none=True)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    can_cancel = fields.Boolean(required=False, allow_none=True)
    
    size = fields.Str(required=False, allow_none=True)
    
    line_number = fields.Int(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    prices = fields.Nested(Prices, required=False)
    
    ordering_currency_prices = fields.Nested(OrderingCurrencyPrices, required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    bag_id = fields.Int(required=False)
    
    entity_type = fields.Str(required=False, allow_none=True)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    


class ShipmentItemFulFillingStore(BaseSchema):
    # Order swagger.json

    
    phone = fields.Str(required=False, allow_none=True)
    
    brand_store_tags = fields.List(fields.Str(required=False), required=False)
    
    pincode = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    address = fields.Str(required=False, allow_none=True)
    
    address1 = fields.Str(required=False, allow_none=True)
    
    display_address = fields.Str(required=False, allow_none=True)
    
    location_type = fields.Str(required=False, allow_none=True)
    
    id = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    store_email = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False, allow_none=True)
    
    city = fields.Str(required=False, allow_none=True)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class Currency(BaseSchema):
    # Order swagger.json

    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class OrderingCurrency(BaseSchema):
    # Order swagger.json

    
    currency_code = fields.Str(required=False)
    
    currency_name = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    currency_sub_unit = fields.Str(required=False)
    


class ConversionRate(BaseSchema):
    # Order swagger.json

    
    base = fields.Str(required=False)
    
    rates = fields.Dict(required=False)
    


class CurrencyInfo(BaseSchema):
    # Order swagger.json

    
    ordering_currency = fields.Nested(OrderingCurrency, required=False)
    
    conversion_rate = fields.Nested(ConversionRate, required=False)
    


class ShipmentItem(BaseSchema):
    # Order swagger.json

    
    order_date = fields.Str(required=False, allow_none=True)
    
    order_created_ts = fields.Str(required=False, allow_none=True)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    estimated_sla_time = fields.Str(required=False, allow_none=True)
    
    estimated_sla_ts = fields.Str(required=False, allow_none=True)
    
    delivery_address = fields.Nested(Address, required=False)
    
    billing_address = fields.Nested(Address, required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    is_active = fields.Boolean(required=False)
    
    channel = fields.Nested(ShipmentListingChannel, required=False)
    
    previous_shipment_id = fields.Str(required=False, allow_none=True)
    
    forward_end_shipment_id = fields.Str(required=False, allow_none=True)
    
    lock_status = fields.Boolean(required=False, allow_none=True)
    
    invoice_id = fields.Str(required=False, allow_none=True)
    
    payment_methods = fields.Dict(required=False, allow_none=True)
    
    payment_info = fields.List(fields.Dict(required=False), required=False)
    
    status_created_at = fields.Str(required=False)
    
    status_created_ts = fields.Str(required=False)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
    meta = fields.Dict(required=False)
    
    payment_mode = fields.Str(required=False, allow_none=True)
    
    can_process = fields.Boolean(required=False, allow_none=True)
    
    prices = fields.Nested(Prices, required=False)
    
    ordering_currency_prices = fields.Nested(OrderingCurrencyPrices, required=False)
    
    order_id = fields.Str(required=False)
    
    ordering_channnel = fields.Str(required=False, allow_none=True)
    
    ordering_source = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False, allow_none=True)
    
    customer_note = fields.Str(required=False, allow_none=True)
    
    total_bags = fields.Int(required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    mode_of_payment = fields.Str(required=False)
    
    shipment_created_ts = fields.Str(required=False)
    
    currency = fields.Nested(Currency, required=False)
    
    currency_info = fields.Nested(CurrencyInfo, required=False)
    
    is_lapa_enabled = fields.Boolean(required=False)
    
    logistics_meta = fields.Dict(required=False)
    
    fulfillment_option = fields.Nested(FulfillmentOption, required=False)
    


class ShipmentInternalPlatformViewResponseSchema(BaseSchema):
    # Order swagger.json

    
    total_count = fields.Int(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False, allow_none=True)
    
    items = fields.List(fields.Nested(ShipmentItem, required=False), required=False)
    
    lane = fields.Str(required=False, allow_none=True)
    
    page = fields.Nested(Page, required=False)
    


class TrackingList(BaseSchema):
    # Order swagger.json

    
    is_passed = fields.Boolean(required=False, allow_none=True)
    
    text = fields.Str(required=False)
    
    is_current = fields.Boolean(required=False, allow_none=True)
    
    time = fields.Str(required=False, allow_none=True)
    
    created_ts = fields.Str(required=False, allow_none=True)
    
    status = fields.Str(required=False)
    


class InvoiceInfo(BaseSchema):
    # Order swagger.json

    
    store_invoice_id = fields.Str(required=False, allow_none=True)
    
    invoice_url = fields.Str(required=False, allow_none=True)
    
    updated_date = fields.Str(required=False, allow_none=True)
    
    external_invoice_id = fields.Str(required=False, allow_none=True)
    
    label_url = fields.Str(required=False, allow_none=True)
    
    credit_note_id = fields.Str(required=False, allow_none=True)
    
    links = fields.Dict(required=False)
    


class LoyaltyDiscountDetails(BaseSchema):
    # Order swagger.json

    
    discount = fields.Float(required=False)
    
    ownership = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    


class OrderDetailsData(BaseSchema):
    # Order swagger.json

    
    order_date = fields.Str(required=False, allow_none=True)
    
    created_ts = fields.Str(required=False, allow_none=True)
    
    tax_details = fields.Dict(required=False, allow_none=True)
    
    cod_charges = fields.Str(required=False, allow_none=True)
    
    source = fields.Str(required=False, allow_none=True)
    
    fynd_order_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False, allow_none=True)
    
    affiliate_order_id = fields.Str(required=False, allow_none=True)
    
    ordering_channel_logo = fields.Dict(required=False, allow_none=True)
    
    order_value = fields.Str(required=False, allow_none=True)
    
    ordering_channel = fields.Str(required=False, allow_none=True)
    
    ordering_source = fields.Str(required=False)
    
    loyalty_discount_details = fields.Nested(LoyaltyDiscountDetails, required=False)
    
    meta = fields.Dict(required=False)
    


class UserDetailsData(BaseSchema):
    # Order swagger.json

    
    phone = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    area = fields.Str(required=False, allow_none=True)
    
    address_type = fields.Str(required=False, allow_none=True)
    
    country = fields.Str(required=False)
    
    email = fields.Str(required=False, allow_none=True)
    
    address1 = fields.Str(required=False, allow_none=True)
    
    landmark = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    
    country_phone_code = fields.Str(required=False)
    
    display_address = fields.Str(required=False, allow_none=True)
    


class PhoneDetails(BaseSchema):
    # Order swagger.json

    
    country_code = fields.Int(required=False, allow_none=True)
    
    number = fields.Str(required=False, allow_none=True)
    


class ContactDetails(BaseSchema):
    # Order swagger.json

    
    phone = fields.List(fields.Nested(PhoneDetails, required=False), required=False)
    
    emails = fields.List(fields.Str(required=False), required=False)
    


class CompanyDetails(BaseSchema):
    # Order swagger.json

    
    company_name = fields.Str(required=False, allow_none=True)
    
    address = fields.Dict(required=False, allow_none=True)
    
    company_cin = fields.Str(required=False, allow_none=True)
    
    company_id = fields.Int(required=False, allow_none=True)
    
    company_gst = fields.Str(required=False, allow_none=True)
    
    company_contact = fields.Nested(ContactDetails, required=False)
    


class OrderingStoreDetails(BaseSchema):
    # Order swagger.json

    
    phone = fields.Str(required=False, allow_none=True)
    
    pincode = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    address = fields.Str(required=False, allow_none=True)
    
    address1 = fields.Str(required=False, allow_none=True)
    
    display_address = fields.Str(required=False, allow_none=True)
    
    id = fields.Int(required=False, allow_none=True)
    
    code = fields.Str(required=False, allow_none=True)
    
    store_name = fields.Str(required=False, allow_none=True)
    
    country = fields.Str(required=False, allow_none=True)
    
    contact_person = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False, allow_none=True)
    
    city = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    store_email = fields.Str(required=False, allow_none=True)
    


class DPDetailsData(BaseSchema):
    # Order swagger.json

    
    pincode = fields.Str(required=False, allow_none=True)
    
    track_url = fields.Str(required=False, allow_none=True)
    
    eway_bill_id = fields.Str(required=False, allow_none=True)
    
    id = fields.Int(required=False, allow_none=True)
    
    country = fields.Str(required=False, allow_none=True)
    
    awb_no = fields.Str(required=False, allow_none=True)
    
    gst_tag = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    


class BuyerDetails(BaseSchema):
    # Order swagger.json

    
    ajio_site_id = fields.Str(required=False, allow_none=True)
    
    pincode = fields.Int(required=False)
    
    address = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    


class DebugInfo(BaseSchema):
    # Order swagger.json

    
    stormbreaker_uuid = fields.Str(required=False, allow_none=True)
    


class EinvoiceInfo(BaseSchema):
    # Order swagger.json

    
    credit_note = fields.Dict(required=False, allow_none=True)
    
    invoice = fields.Dict(required=False, allow_none=True)
    


class Formatted(BaseSchema):
    # Order swagger.json

    
    max = fields.Str(required=False, allow_none=True)
    
    min = fields.Str(required=False, allow_none=True)
    


class ShipmentTags(BaseSchema):
    # Order swagger.json

    
    slug = fields.Str(required=False, allow_none=True)
    
    entity_type = fields.Str(required=False, allow_none=True)
    
    display_text = fields.Str(required=False, allow_none=True)
    


class LockData(BaseSchema):
    # Order swagger.json

    
    locked = fields.Boolean(required=False, allow_none=True)
    
    mto = fields.Boolean(required=False, allow_none=True)
    
    lock_message = fields.Str(required=False, allow_none=True)
    


class ShipmentTimeStamp(BaseSchema):
    # Order swagger.json

    
    max = fields.Int(required=False, allow_none=True)
    
    min = fields.Int(required=False, allow_none=True)
    


class ShipmentMeta(BaseSchema):
    # Order swagger.json

    
    tracking_url = fields.Str(required=False, allow_none=True)
    
    estimated_delivery_date = fields.Str(required=False, allow_none=True)
    
    same_store_available = fields.Boolean(required=False)
    
    b2b_buyer_details = fields.Nested(BuyerDetails, required=False)
    
    formatted = fields.Nested(Formatted, required=False)
    
    debug_info = fields.Nested(DebugInfo, required=False)
    
    return_awb_number = fields.Str(required=False, allow_none=True)
    
    is_self_ship = fields.Boolean(required=False, allow_none=True)
    
    box_type = fields.Str(required=False, allow_none=True)
    
    einvoice_info = fields.Nested(EinvoiceInfo, required=False)
    
    return_affiliate_shipment_id = fields.Str(required=False, allow_none=True)
    
    parent_dp_id = fields.Str(required=False, allow_none=True)
    
    shipment_weight = fields.Float(required=False, allow_none=True)
    
    dimension = fields.Nested(Dimensions, required=False)
    
    dp_options = fields.Dict(required=False, allow_none=True)
    
    assign_dp_from_sb = fields.Boolean(required=False, allow_none=True)
    
    due_date = fields.Str(required=False, allow_none=True)
    
    store_invoice_updated_date = fields.Str(required=False, allow_none=True)
    
    forward_affiliate_shipment_id = fields.Str(required=False, allow_none=True)
    
    return_store_node = fields.Int(required=False, allow_none=True)
    
    fulfilment_priority_text = fields.Str(required=False, allow_none=True)
    
    shipment_tags = fields.List(fields.Nested(ShipmentTags, required=False), required=False)
    
    external = fields.Dict(required=False, allow_none=True)
    
    awb_number = fields.Str(required=False, allow_none=True)
    
    lock_data = fields.Nested(LockData, required=False)
    
    order_type = fields.Str(required=False, allow_none=True)
    
    ewaybill_info = fields.Dict(required=False, allow_none=True)
    
    dp_id = fields.Str(required=False, allow_none=True)
    
    shipment_volumetric_weight = fields.Float(required=False, allow_none=True)
    
    marketplace_store_id = fields.Str(required=False, allow_none=True)
    
    return_details = fields.Dict(required=False, allow_none=True)
    
    dp_sort_key = fields.Str(required=False, allow_none=True)
    
    packaging_name = fields.Str(required=False, allow_none=True)
    
    timestamp = fields.Nested(ShipmentTimeStamp, required=False)
    
    auto_trigger_dp_assignment_acf = fields.Boolean(required=False, allow_none=True)
    
    dp_name = fields.Str(required=False, allow_none=True)
    
    po_number = fields.Str(required=False, allow_none=True)
    
    weight = fields.Int(required=False)
    
    b2c_buyer_details = fields.Dict(required=False, allow_none=True)
    
    forward_affiliate_order_id = fields.Str(required=False, allow_none=True)
    
    return_affiliate_order_id = fields.Str(required=False, allow_none=True)
    
    bag_weight = fields.Dict(required=False, allow_none=True)
    
    refund_to = fields.Str(required=False, allow_none=True)
    


class PDFLinks(BaseSchema):
    # Order swagger.json

    
    invoice_type = fields.Str(required=False)
    
    label_a6 = fields.Str(required=False, allow_none=True)
    
    invoice = fields.Str(required=False, allow_none=True)
    
    label_pos = fields.Str(required=False, allow_none=True)
    
    invoice_a6 = fields.Str(required=False, allow_none=True)
    
    b2b = fields.Str(required=False, allow_none=True)
    
    label = fields.Str(required=False, allow_none=True)
    
    label_a4 = fields.Str(required=False, allow_none=True)
    
    label_type = fields.Str(required=False)
    
    invoice_export = fields.Str(required=False, allow_none=True)
    
    credit_note_url = fields.Str(required=False, allow_none=True)
    
    delivery_challan_a4 = fields.Str(required=False, allow_none=True)
    
    label_export = fields.Str(required=False, allow_none=True)
    
    invoice_a4 = fields.Str(required=False, allow_none=True)
    
    invoice_pos = fields.Str(required=False, allow_none=True)
    
    po_invoice = fields.Str(required=False, allow_none=True)
    


class AffiliateDetails(BaseSchema):
    # Order swagger.json

    
    shipment_meta = fields.Nested(ShipmentMeta, required=False)
    
    affiliate_meta = fields.Nested(AffiliateMeta, required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    company_affiliate_tag = fields.Str(required=False, allow_none=True)
    
    affiliate_order_id = fields.Str(required=False)
    
    pdf_links = fields.Nested(PDFLinks, required=False)
    
    config = fields.Nested(AffiliateConfig, required=False)
    
    affiliate_id = fields.Str(required=False, allow_none=True)
    
    affiliate_store_id = fields.Str(required=False)
    
    affiliate_bag_id = fields.Str(required=False)
    
    id = fields.Str(required=False, allow_none=True)
    


class BagConfigs(BaseSchema):
    # Order swagger.json

    
    is_returnable = fields.Boolean(required=False)
    
    allow_force_return = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    can_be_cancelled = fields.Boolean(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    is_customer_return_allowed = fields.Boolean(required=False)
    


class OrderBagArticle(BaseSchema):
    # Order swagger.json

    
    identifiers = fields.Dict(required=False, allow_none=True)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    uid = fields.Str(required=False, allow_none=True)
    
    size = fields.Str(required=False, allow_none=True)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False, allow_none=True)
    


class OrderBrandName(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False, allow_none=True)
    
    company = fields.Int(required=False, allow_none=True)
    
    id = fields.Int(required=False)
    
    created_on = fields.Str(required=False, allow_none=True)
    
    brand_name = fields.Str(required=False, allow_none=True)
    
    modified_on = fields.Str(required=False, allow_none=True)
    


class AffiliateBagsDetails(BaseSchema):
    # Order swagger.json

    
    affiliate_bag_id = fields.Str(required=False, allow_none=True)
    
    coupon_code = fields.Str(required=False, allow_none=True)
    
    affiliate_meta = fields.Nested(AffiliateMeta, required=False)
    


class BagPaymentMethods(BaseSchema):
    # Order swagger.json

    
    mode = fields.Str(required=False, allow_none=True)
    
    amount = fields.Float(required=False, allow_none=True)
    


class DiscountRules(BaseSchema):
    # Order swagger.json

    
    value = fields.Int(required=False, allow_none=True)
    
    type = fields.Str(required=False, allow_none=True)
    


class ItemCriterias(BaseSchema):
    # Order swagger.json

    
    item_brand = fields.List(fields.Int(required=False), required=False)
    


class BuyRules(BaseSchema):
    # Order swagger.json

    
    item_criteria = fields.Nested(ItemCriterias, required=False)
    
    cart_conditions = fields.Dict(required=False, allow_none=True)
    


class PriceMinMax(BaseSchema):
    # Order swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    


class ItemPriceDetails(BaseSchema):
    # Order swagger.json

    
    marked = fields.Nested(PriceMinMax, required=False)
    
    effective = fields.Nested(PriceMinMax, required=False)
    
    currency = fields.Str(required=False)
    


class FreeGiftItems(BaseSchema):
    # Order swagger.json

    
    item_slug = fields.Str(required=False)
    
    item_name = fields.Str(required=False)
    
    item_price_details = fields.Nested(ItemPriceDetails, required=False)
    
    item_brand_name = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    


class AppliedFreeArticles(BaseSchema):
    # Order swagger.json

    
    article_id = fields.Str(required=False)
    
    free_gift_item_details = fields.Dict(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
    quantity = fields.Float(required=False)
    


class AppliedPromos(BaseSchema):
    # Order swagger.json

    
    promotion_type = fields.Str(required=False, allow_none=True)
    
    promotion_name = fields.Str(required=False, allow_none=True)
    
    discount_rules = fields.List(fields.Nested(DiscountRules, required=False), required=False)
    
    amount = fields.Float(required=False, allow_none=True)
    
    article_quantity = fields.Int(required=False, allow_none=True)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    promo_id = fields.Str(required=False, allow_none=True)
    
    mrp_promotion = fields.Boolean(required=False, allow_none=True)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    


class CurrentStatus(BaseSchema):
    # Order swagger.json

    
    store_id = fields.Int(required=False, allow_none=True)
    
    delivery_awb_number = fields.Str(required=False, allow_none=True)
    
    kafka_sync = fields.Boolean(required=False, allow_none=True)
    
    delivery_partner_id = fields.Int(required=False, allow_none=True)
    
    state_type = fields.Str(required=False, allow_none=True)
    
    state_id = fields.Int(required=False, allow_none=True)
    
    id = fields.Int(required=False)
    
    created_at = fields.Str(required=False, allow_none=True)
    
    created_ts = fields.Str(required=False, allow_none=True)
    
    shipment_id = fields.Str(required=False, allow_none=True)
    
    updated_at = fields.Str(required=False, allow_none=True)
    
    bag_state_mapper = fields.Nested(BagStateMapper, required=False)
    
    bag_id = fields.Int(required=False, allow_none=True)
    
    status = fields.Str(required=False, allow_none=True)
    


class OrderBags(BaseSchema):
    # Order swagger.json

    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    parent_promo_bags = fields.Dict(required=False, allow_none=True)
    
    financial_breakup = fields.Nested(FinancialBreakup, required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    seller_identifier = fields.Str(required=False, allow_none=True)
    
    delivery_address = fields.Nested(Address, required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    group_id = fields.Str(required=False, allow_none=True)
    
    affiliate_bag_details = fields.Nested(AffiliateBagsDetails, required=False)
    
    item = fields.Nested(PlatformItem, required=False)
    
    payment_methods = fields.List(fields.Nested(BagPaymentMethods, required=False), required=False)
    
    payment_info = fields.List(fields.Nested(BagPaymentMethods, required=False), required=False)
    
    quantity = fields.Int(required=False, allow_none=True)
    
    identifier = fields.Str(required=False, allow_none=True)
    
    can_return = fields.Boolean(required=False, allow_none=True)
    
    can_cancel = fields.Boolean(required=False, allow_none=True)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    line_number = fields.Int(required=False, allow_none=True)
    
    meta = fields.Dict(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    charges = fields.List(fields.Nested(PriceAdjustmentCharge, required=False), required=False)
    
    ordering_currency_prices = fields.Nested(OrderingCurrencyPrices, required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    bag_id = fields.Int(required=False)
    
    entity_type = fields.Str(required=False, allow_none=True)
    
    is_parent = fields.Boolean(required=False, allow_none=True)
    


class FulfillingStore(BaseSchema):
    # Order swagger.json

    
    phone = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    address = fields.Str(required=False)
    
    address1 = fields.Str(required=False, allow_none=True)
    
    display_address = fields.Str(required=False, allow_none=True)
    
    id = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    store_name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    fulfillment_channel = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    store_email = fields.Str(required=False, allow_none=True)
    


class ShipmentPayments(BaseSchema):
    # Order swagger.json

    
    mode = fields.Str(required=False, allow_none=True)
    
    logo = fields.Str(required=False, allow_none=True)
    
    source = fields.Str(required=False, allow_none=True)
    


class ShipmentStatusData(BaseSchema):
    # Order swagger.json

    
    meta = fields.Dict(required=False, allow_none=True)
    
    bag_list = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Int(required=False, allow_none=True)
    
    created_at = fields.Str(required=False, allow_none=True)
    
    created_ts = fields.Str(required=False, allow_none=True)
    
    shipment_id = fields.Str(required=False, allow_none=True)
    
    status = fields.Str(required=False, allow_none=True)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    current_shipment_status = fields.Str(required=False, allow_none=True)
    
    status_created_at = fields.Str(required=False, allow_none=True)
    


class ShipmentLockDetails(BaseSchema):
    # Order swagger.json

    
    lock_status = fields.Boolean(required=False, allow_none=True)
    
    lock_message = fields.Str(required=False, allow_none=True)
    
    action_to_status = fields.Dict(required=False, allow_none=True)
    


class FulfillmentOption(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class PlatformShipment(BaseSchema):
    # Order swagger.json

    
    fulfillment_option = fields.Nested(FulfillmentOption, required=False)
    
    picked_date = fields.Str(required=False, allow_none=True)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    invoice = fields.Nested(InvoiceInfo, required=False)
    
    shipment_status = fields.Str(required=False, allow_none=True)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    order_status = fields.Nested(OrderStatusData, required=False)
    
    delivery_slot = fields.Dict(required=False, allow_none=True)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    enable_dp_tracking = fields.Boolean(required=False, allow_none=True)
    
    custom_message = fields.Str(required=False, allow_none=True)
    
    estimated_sla_time = fields.Str(required=False, allow_none=True)
    
    estimated_sla_ts = fields.Str(required=False, allow_none=True)
    
    can_update_dimension = fields.Boolean(required=False, allow_none=True)
    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    delivery_details = fields.Dict(required=False)
    
    billing_details = fields.Dict(required=False)
    
    forward_shipment_id = fields.Str(required=False, allow_none=True)
    
    fulfilment_priority = fields.Int(required=False, allow_none=True)
    
    shipment_details = fields.Nested(ShipmentLockDetails, required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    shipment_quantity = fields.Int(required=False, allow_none=True)
    
    company_details = fields.Nested(CompanyDetails, required=False)
    
    ordering_store = fields.Nested(OrderingStoreDetails, required=False)
    
    order_platform = fields.Str(required=False)
    
    lock_status = fields.Boolean(required=False, allow_none=True)
    
    platform_logo = fields.Str(required=False, allow_none=True)
    
    user_agent = fields.Str(required=False, allow_none=True)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    invoice_id = fields.Str(required=False, allow_none=True)
    
    payment_methods = fields.Dict(required=False, allow_none=True)
    
    payment_info = fields.List(fields.Dict(required=False), required=False)
    
    coupon = fields.Dict(required=False, allow_none=True)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    priority_text = fields.Str(required=False, allow_none=True)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    is_dp_assign_enabled = fields.Boolean(required=False, allow_none=True)
    
    bags = fields.List(fields.Nested(OrderBags, required=False), required=False)
    
    dp_assignment = fields.Boolean(required=False, allow_none=True)
    
    total_items = fields.Int(required=False, allow_none=True)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    meta = fields.Dict(required=False)
    
    pdf_links = fields.Dict(required=False)
    
    payment_mode = fields.Str(required=False, allow_none=True)
    
    packaging_type = fields.Str(required=False, allow_none=True)
    
    journey_type = fields.Str(required=False, allow_none=True)
    
    prices = fields.Nested(Prices, required=False)
    
    charges = fields.List(fields.Nested(PriceAdjustmentCharge, required=False), required=False)
    
    ordering_currency_prices = fields.Nested(OrderingCurrencyPrices, required=False)
    
    vertical = fields.Str(required=False, allow_none=True)
    
    shipment_id = fields.Str(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    operational_status = fields.Str(required=False, allow_none=True)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    total_bags = fields.Int(required=False, allow_none=True)
    
    shipment_created_at = fields.Str(required=False, allow_none=True)
    
    shipment_created_ts = fields.Str(required=False, allow_none=True)
    
    currency = fields.Nested(Currency, required=False)
    
    currency_info = fields.Nested(CurrencyInfo, required=False)
    
    previous_shipment_id = fields.Str(required=False, allow_none=True)
    
    shipment_update_time = fields.Float(required=False, allow_none=True)
    
    rto_address = fields.Nested(Address, required=False)
    
    credit_note_id = fields.Str(required=False, allow_none=True)
    
    is_self_ship = fields.Boolean(required=False, allow_none=True)
    
    mode_of_payment = fields.Str(required=False, allow_none=True)
    
    is_lapa_enabled = fields.Boolean(required=False)
    
    forward_end_shipment_id = fields.Str(required=False, allow_none=True)
    
    logistics_meta = fields.Dict(required=False)
    


class ShipmentInfoResponseSchema(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    


class TaxDetails(BaseSchema):
    # Order swagger.json

    
    pan_no = fields.Str(required=False, allow_none=True)
    
    gstin = fields.Str(required=False, allow_none=True)
    


class PaymentInfoData(BaseSchema):
    # Order swagger.json

    
    meta = fields.Dict(required=False)
    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    collected = fields.Boolean(required=False)
    
    refund_by = fields.Str(required=False)
    
    collect_by = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    merchant_transaction_id = fields.Str(required=False)
    


class CurrencySchema(BaseSchema):
    # Order swagger.json

    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class OrderData(BaseSchema):
    # Order swagger.json

    
    ordering_channel = fields.Str(required=False)
    
    ordering_source = fields.Str(required=False)
    
    order_date = fields.Str(required=False)
    
    created_ts = fields.Str(required=False)
    
    tax_details = fields.Nested(TaxDetails, required=False)
    
    meta = fields.Dict(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    charges = fields.List(fields.Nested(PriceAdjustmentCharge, required=False), required=False)
    
    ordering_currency_prices = fields.Nested(OrderingCurrencyPrices, required=False)
    
    payment_methods = fields.Dict(required=False, allow_none=True)
    
    payment_info = fields.List(fields.Nested(PaymentInfoData, required=False), required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    currency = fields.Nested(CurrencySchema, required=False)
    
    loyalty_discount_details = fields.Nested(LoyaltyDiscountDetails, required=False)
    


class OrderDetailsResponseSchema(BaseSchema):
    # Order swagger.json

    
    order = fields.Nested(OrderData, required=False)
    
    success = fields.Boolean(required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    


class SubLane(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    total_items = fields.Int(required=False)
    
    actions = fields.List(fields.Dict(required=False), required=False)
    
    index = fields.Int(required=False)
    


class SuperLane(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False)
    
    options = fields.List(fields.Nested(SubLane, required=False), required=False)
    
    text = fields.Str(required=False)
    
    total_items = fields.Int(required=False)
    


class LaneConfigResponseSchema(BaseSchema):
    # Order swagger.json

    
    super_lanes = fields.List(fields.Nested(SuperLane, required=False), required=False)
    


class PlatformBreakupValues(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    display = fields.Str(required=False, allow_none=True)
    


class PlatformChannel(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    


class PlatformOrderItems(BaseSchema):
    # Order swagger.json

    
    breakup_values = fields.List(fields.Nested(PlatformBreakupValues, required=False), required=False)
    
    total_order_value = fields.Float(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    order_created_time = fields.Str(required=False, allow_none=True)
    
    order_created_ts = fields.Str(required=False, allow_none=True)
    
    payment_mode = fields.Str(required=False, allow_none=True)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    
    order_id = fields.Str(required=False, allow_none=True)
    
    channel = fields.Nested(PlatformChannel, required=False)
    
    user_info = fields.Nested(UserDataInfo, required=False)
    
    order_value = fields.Float(required=False, allow_none=True)
    
    currency = fields.Nested(Currency, required=False)
    
    currency_info = fields.Nested(CurrencyInfo, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    ordering_currency_prices = fields.Nested(OrderingCurrencyPrices, required=False)
    
    loyalty_discount_details = fields.Nested(LoyaltyDiscountDetails, required=False)
    


class OrderListingResponseSchema(BaseSchema):
    # Order swagger.json

    
    total_count = fields.Int(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False, allow_none=True)
    
    items = fields.List(fields.Nested(PlatformOrderItems, required=False), required=False)
    
    lane = fields.Str(required=False, allow_none=True)
    
    page = fields.Nested(Page, required=False)
    


class PlatformTrack(BaseSchema):
    # Order swagger.json

    
    last_location_recieved_at = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False)
    
    raw_status = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_time = fields.Str(required=False)
    
    awb = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    reason = fields.Str(required=False, allow_none=True)
    
    account_name = fields.Str(required=False)
    


class PlatformShipmentTrack(BaseSchema):
    # Order swagger.json

    
    meta = fields.Dict(required=False)
    
    results = fields.List(fields.Nested(PlatformTrack, required=False), required=False)
    


class AdvanceFilterInfo(BaseSchema):
    # Order swagger.json

    
    returned = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    action_centre = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    unfulfilled = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    filters = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    processed = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    applied_filters = fields.Dict(required=False, allow_none=True)
    
    page = fields.Dict(required=False, allow_none=True)
    


class FiltersResponseSchema(BaseSchema):
    # Order swagger.json

    
    advance = fields.Nested(AdvanceFilterInfo, required=False)
    
    global_1 = fields.Nested(FiltersInfo, required=False)
    
    advance_filter = fields.Nested(AdvanceFilterInfo, required=False)
    
    global_filter = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    


class URL(BaseSchema):
    # Order swagger.json

    
    url = fields.Str(required=False)
    


class FileResponseSchema(BaseSchema):
    # Order swagger.json

    
    file_name = fields.Str(required=False)
    
    cdn = fields.Nested(URL, required=False)
    


class BulkActionTemplate(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False)
    
    text = fields.Str(required=False)
    


class BulkActionTemplateResponseSchema(BaseSchema):
    # Order swagger.json

    
    template_x_slug = fields.List(fields.Nested(BulkActionTemplate, required=False), required=False)
    


class PlatformShipmentReasonsResponseSchema(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(Reason, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ShipmentResponseReasons(BaseSchema):
    # Order swagger.json

    
    reason_id = fields.Int(required=False)
    
    reason = fields.Str(required=False)
    


class ShipmentReasonsResponseSchema(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(ShipmentResponseReasons, required=False), required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class StoreAddress(BaseSchema):
    # Order swagger.json

    
    phone = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    address_type = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    display_address = fields.Str(required=False, allow_none=True)
    
    version = fields.Str(required=False, allow_none=True)
    
    address_category = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    address2 = fields.Str(required=False)
    
    area = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False, allow_none=True)
    
    updated_at = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    state = fields.Str(required=False)
    


class EInvoicePortalDetails(BaseSchema):
    # Order swagger.json

    
    username = fields.Str(required=False, allow_none=True)
    
    user = fields.Str(required=False, allow_none=True)
    
    password = fields.Str(required=False, allow_none=True)
    


class StoreEinvoice(BaseSchema):
    # Order swagger.json

    
    username = fields.Str(required=False, allow_none=True)
    
    user = fields.Str(required=False, allow_none=True)
    
    password = fields.Str(required=False, allow_none=True)
    
    enabled = fields.Boolean(required=False)
    


class StoreEwaybill(BaseSchema):
    # Order swagger.json

    
    enabled = fields.Boolean(required=False, allow_none=True)
    


class StoreGstCredentials(BaseSchema):
    # Order swagger.json

    
    e_invoice = fields.Nested(StoreEinvoice, required=False)
    
    e_waybill = fields.Nested(StoreEwaybill, required=False)
    


class Document(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    legal_name = fields.Str(required=False)
    
    url = fields.Str(required=False, allow_none=True)
    


class StoreDocuments(BaseSchema):
    # Order swagger.json

    
    gst = fields.Nested(Document, required=False)
    


class StoreMeta(BaseSchema):
    # Order swagger.json

    
    additional_contact_details = fields.Dict(required=False, allow_none=True)
    
    timing = fields.List(fields.Dict(required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    gst_number = fields.Str(required=False, allow_none=True)
    
    ewaybill_portal_details = fields.Dict(required=False, allow_none=True)
    
    einvoice_portal_details = fields.Nested(EInvoicePortalDetails, required=False)
    
    gst_credentials = fields.Nested(StoreGstCredentials, required=False)
    
    stage = fields.Str(required=False)
    
    product_return_config = fields.Dict(required=False, allow_none=True)
    
    documents = fields.Nested(StoreDocuments, required=False)
    
    display_name = fields.Str(required=False)
    


class Store(BaseSchema):
    # Order swagger.json

    
    phone = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False, allow_none=True)
    
    company_id = fields.Int(required=False)
    
    alohomora_user_id = fields.Int(required=False, allow_none=True)
    
    created_at = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    store_email = fields.Str(required=False)
    
    is_enabled_for_recon = fields.Boolean(required=False, allow_none=True)
    
    pincode = fields.Str(required=False)
    
    mall_area = fields.Str(required=False, allow_none=True)
    
    vat_no = fields.Str(required=False, allow_none=True)
    
    address1 = fields.Str(required=False)
    
    display_address = fields.Str(required=False, allow_none=True)
    
    store_active_from = fields.Str(required=False, allow_none=True)
    
    city = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    longitude = fields.Float(required=False, allow_none=True)
    
    brand_store_tags = fields.List(fields.Str(required=False), required=False)
    
    order_integration_id = fields.Str(required=False, allow_none=True)
    
    parent_store_id = fields.Int(required=False, allow_none=True)
    
    location_type = fields.Str(required=False)
    
    code = fields.Str(required=False, allow_none=True)
    
    fulfillment_channel = fields.Str(required=False)
    
    updated_at = fields.Str(required=False, allow_none=True)
    
    store_address_json = fields.Nested(StoreAddress, required=False)
    
    meta = fields.Nested(StoreMeta, required=False)
    
    s_id = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    packaging_material_count = fields.Int(required=False, allow_none=True)
    
    is_archived = fields.Boolean(required=False, allow_none=True)
    
    login_username = fields.Str(required=False, allow_none=True)
    
    mall_name = fields.Str(required=False, allow_none=True)
    
    latitude = fields.Float(required=False, allow_none=True)
    
    address2 = fields.Str(required=False, allow_none=True)
    


class Brand(BaseSchema):
    # Order swagger.json

    
    credit_note_expiry_days = fields.Int(required=False, allow_none=True)
    
    logo = fields.Str(required=False, allow_none=True)
    
    invoice_prefix = fields.Str(required=False, allow_none=True)
    
    credit_note_allowed = fields.Boolean(required=False, allow_none=True)
    
    start_date = fields.Str(required=False, allow_none=True)
    
    company = fields.Str(required=False, allow_none=True)
    
    is_virtual_invoice = fields.Boolean(required=False, allow_none=True)
    
    script_last_ran = fields.Str(required=False, allow_none=True)
    
    pickup_location = fields.Str(required=False, allow_none=True)
    
    created_on = fields.Str(required=False, allow_none=True)
    
    brand_name = fields.Str(required=False)
    
    brand_id = fields.Int(required=False)
    
    modified_on = fields.Str(required=False, allow_none=True)
    
    id = fields.Int(required=False, allow_none=True)
    


class Item(BaseSchema):
    # Order swagger.json

    
    attributes = fields.Dict(required=False)
    
    brand_id = fields.Int(required=False)
    
    slug_key = fields.Str(required=False)
    
    webstore_product_url = fields.Str(required=False, allow_none=True)
    
    l3_category = fields.Int(required=False, allow_none=True)
    
    l3_category_name = fields.Str(required=False, allow_none=True)
    
    last_updated_at = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    
    l2_category = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Str(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False, allow_none=True)
    
    l1_category_id = fields.Int(required=False, allow_none=True)
    
    item_id = fields.Int(required=False)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    gender = fields.Str(required=False, allow_none=True)
    
    can_cancel = fields.Boolean(required=False, allow_none=True)
    
    can_return = fields.Boolean(required=False, allow_none=True)
    
    size = fields.Str(required=False)
    
    branch_url = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    color = fields.Str(required=False, allow_none=True)
    
    department_id = fields.Int(required=False, allow_none=True)
    
    l2_category_id = fields.Int(required=False, allow_none=True)
    


class ArticleStatusDetails(BaseSchema):
    # Order swagger.json

    
    status = fields.Dict(required=False, allow_none=True)
    


class Company(BaseSchema):
    # Order swagger.json

    
    pan_no = fields.Str(required=False, allow_none=True)
    
    created_on = fields.Str(required=False, allow_none=True)
    
    id = fields.Int(required=False, allow_none=True)
    
    company_name = fields.Str(required=False, allow_none=True)
    
    gst_number = fields.Str(required=False, allow_none=True)
    
    company_type = fields.Str(required=False, allow_none=True)
    
    modified_on = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    business_type = fields.Str(required=False, allow_none=True)
    
    agreement_start_date = fields.Str(required=False, allow_none=True)
    


class ShipmentGstDetails(BaseSchema):
    # Order swagger.json

    
    value_of_good = fields.Float(required=False, allow_none=True)
    
    gst_fee = fields.Float(required=False, allow_none=True)
    
    brand_calculated_amount = fields.Float(required=False, allow_none=True)
    
    tax_collected_at_source = fields.Float(required=False, allow_none=True)
    
    gstin_code = fields.Str(required=False, allow_none=True)
    


class DeliverySlotDetails(BaseSchema):
    # Order swagger.json

    
    slot = fields.Str(required=False, allow_none=True)
    
    upper_bound = fields.Str(required=False, allow_none=True)
    
    lower_bound = fields.Str(required=False, allow_none=True)
    
    date = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False, allow_none=True)
    


class InvoiceDetails(BaseSchema):
    # Order swagger.json

    
    updated_date = fields.Str(required=False, allow_none=True)
    
    store_invoice_id = fields.Str(required=False, allow_none=True)
    
    invoice_url = fields.Str(required=False, allow_none=True)
    
    label_url = fields.Str(required=False, allow_none=True)
    


class UserDetails(BaseSchema):
    # Order swagger.json

    
    user_oid = fields.Str(required=False, allow_none=True)
    
    external_customer_id = fields.Str(required=False, allow_none=True)
    
    first_name = fields.Str(required=False, allow_none=True)
    
    last_name = fields.Str(required=False, allow_none=True)
    
    mobile = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False, allow_none=True)
    
    is_anonymous_user = fields.Boolean(required=False, allow_none=True)
    
    gender = fields.Str(required=False, allow_none=True)
    
    mongo_user_id = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    


class WeightData(BaseSchema):
    # Order swagger.json

    
    value = fields.Float(required=False, allow_none=True)
    
    unit = fields.Str(required=False, allow_none=True)
    


class BagDetails(BaseSchema):
    # Order swagger.json

    
    bag_update_time = fields.Float(required=False, allow_none=True)
    
    id = fields.Str(required=False, allow_none=True)
    
    bag_id = fields.Int(required=False, allow_none=True)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    article = fields.Nested(Article, required=False)
    
    article_details = fields.Nested(ArticleStatusDetails, required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    company = fields.Nested(Company, required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    delivery_address = fields.Nested(Address, required=False)
    
    delivery_slot = fields.Nested(DeliverySlotDetails, required=False)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    dp_details = fields.Dict(required=False, allow_none=True)
    
    einvoice_info = fields.Dict(required=False, allow_none=True)
    
    entity_type = fields.Str(required=False, allow_none=True)
    
    fallback_user = fields.Dict(required=False, allow_none=True)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    fulfilling_store = fields.Nested(Store, required=False)
    
    fyndstore_emp = fields.Dict(required=False, allow_none=True)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    invoice = fields.Nested(InvoiceDetails, required=False)
    
    item = fields.Nested(Item, required=False)
    
    journey_type = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    lock_status = fields.Boolean(required=False, allow_none=True)
    
    manifest_id = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False)
    
    mode_of_payment = fields.Str(required=False, allow_none=True)
    
    no_of_bags_order = fields.Int(required=False, allow_none=True)
    
    operational_status = fields.Str(required=False, allow_none=True)
    
    order = fields.Nested(OrderDetails, required=False)
    
    order_integration_id = fields.Str(required=False, allow_none=True)
    
    order_type = fields.Str(required=False, allow_none=True)
    
    order_value = fields.Float(required=False, allow_none=True)
    
    ordering_store = fields.Nested(Store, required=False)
    
    parent_promo_bags = fields.Dict(required=False, allow_none=True)
    
    payment_methods = fields.Dict(required=False, allow_none=True)
    
    payment_type = fields.Str(required=False, allow_none=True)
    
    payments = fields.Dict(required=False, allow_none=True)
    
    prices = fields.Nested(Prices, required=False)
    
    charges = fields.List(fields.Nested(PriceAdjustmentCharge, required=False), required=False)
    
    qc_required = fields.Boolean(required=False, allow_none=True)
    
    quantity = fields.Float(required=False, allow_none=True)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    restore_coupon = fields.Boolean(required=False, allow_none=True)
    
    restore_promos = fields.Dict(required=False, allow_none=True)
    
    rto_address = fields.Nested(Address, required=False)
    
    seller_identifier = fields.Str(required=False, allow_none=True)
    
    shipment = fields.Nested(Shipment, required=False)
    
    shipment_details = fields.Nested(ShipmentDetails, required=False)
    
    shipment_id = fields.Str(required=False, allow_none=True)
    
    shipment_gst = fields.Nested(ShipmentGstDetails, required=False)
    
    shipment_status = fields.Nested(ShipmentStatusData, required=False)
    
    shipment_status_history = fields.List(fields.Nested(ShipmentStatusData, required=False), required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    total_shipment_bags = fields.Int(required=False, allow_none=True)
    
    total_shipments_in_order = fields.Int(required=False, allow_none=True)
    
    transaction_type = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False, allow_none=True)
    
    updated_at = fields.Str(required=False, allow_none=True)
    
    user = fields.Nested(UserDetails, required=False)
    
    weight = fields.Nested(WeightData, required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    identifier = fields.Str(required=False, allow_none=True)
    


class BagDetailsPlatformResponseSchema(BaseSchema):
    # Order swagger.json

    
    status_code = fields.Int(required=False)
    
    data = fields.Nested(BagDetails, required=False)
    


class BagsPage(BaseSchema):
    # Order swagger.json

    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    page_type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    


class BagData(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(BagDetails, required=False), required=False)
    
    page = fields.Nested(BagsPage, required=False)
    


class GetBagsPlatformResponseSchema(BaseSchema):
    # Order swagger.json

    
    status_code = fields.Int(required=False)
    
    data = fields.Nested(BagData, required=False)
    


class GeneratePosOrderReceiptResponseSchema(BaseSchema):
    # Order swagger.json

    
    customer_cn_receipt = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    invoice_receipt = fields.Str(required=False)
    
    payment_receipt = fields.Str(required=False)
    
    merchant_cn_receipt = fields.Str(required=False)
    
    payment_receipt_template = fields.Str(required=False)
    
    customer_cn_receipt_template = fields.Str(required=False)
    
    invoice_receipt_template = fields.Str(required=False)
    


class Templates(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class AllowedTemplatesResponseSchema(BaseSchema):
    # Order swagger.json

    
    template_x_slug = fields.List(fields.Nested(Templates, required=False), required=False)
    


class TemplateDownloadResponseSchema(BaseSchema):
    # Order swagger.json

    
    file_name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class Error(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class BulkFailedResponseSchema(BaseSchema):
    # Order swagger.json

    
    status = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    


