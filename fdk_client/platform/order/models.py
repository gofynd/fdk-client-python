"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class InvalidateShipmentCachePayload(BaseSchema):
    pass


class InvalidateShipmentCacheNestedResponse(BaseSchema):
    pass


class InvalidateShipmentCacheResponse(BaseSchema):
    pass


class UpdatePackingErrorResponse(BaseSchema):
    pass


class ErrorResponse(BaseSchema):
    pass


class LogErrorResponse(BaseSchema):
    pass


class QuestionErrorResponse(BaseSchema):
    pass


class RefundStateConfigurationByPaymentType(BaseSchema):
    pass


class PostRefundStateConfiguration(BaseSchema):
    pass


class PostRefundStateConfigurationResponse(BaseSchema):
    pass


class GetRefundStateConfigurationResponse(BaseSchema):
    pass


class RefundStates(BaseSchema):
    pass


class GetRefundStates(BaseSchema):
    pass


class RefundStateManualWithoutMessage(BaseSchema):
    pass


class RefundStateManualWithMessage(BaseSchema):
    pass


class RefundStateManualWithMessageData(BaseSchema):
    pass


class RefundStateConfigurationManualSchema(BaseSchema):
    pass


class RefundStateConfigurationManualSchemaResponse(BaseSchema):
    pass


class RefundSubOption(BaseSchema):
    pass


class RefundBreakup(BaseSchema):
    pass


class RefundOptionShipmentResponse(BaseSchema):
    pass


class CurrencySchema(BaseSchema):
    pass


class RefundOptionsSchemaResponse(BaseSchema):
    pass


class StoreReassign(BaseSchema):
    pass


class StoreReassignResponse(BaseSchema):
    pass


class LockManagerEntities(BaseSchema):
    pass


class UpdateShipmentLockPayload(BaseSchema):
    pass


class OriginalFilter(BaseSchema):
    pass


class Bags(BaseSchema):
    pass


class CheckResponse(BaseSchema):
    pass


class UpdateShipmentLockResponse(BaseSchema):
    pass


class AnnouncementResponse(BaseSchema):
    pass


class AnnouncementsResponse(BaseSchema):
    pass


class Click2CallResponse(BaseSchema):
    pass


class BaseResponse(BaseSchema):
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


class RepricedProductsDataUpdates(BaseSchema):
    pass


class DataUpdates(BaseSchema):
    pass


class TransitionComments(BaseSchema):
    pass


class ShipmentsRequest(BaseSchema):
    pass


class StatuesRequest(BaseSchema):
    pass


class ActionRequest(BaseSchema):
    pass


class UpdateShipmentStatusRequestSchema(BaseSchema):
    pass


class UpdateShipmentActionRequest(BaseSchema):
    pass


class ShipmentsResponse(BaseSchema):
    pass


class StatuesResponse(BaseSchema):
    pass


class UpdateShipmentStatusResponseBody(BaseSchema):
    pass


class DPConfiguration(BaseSchema):
    pass


class PaymentConfig(BaseSchema):
    pass


class CreateOrderConfig(BaseSchema):
    pass


class CreateOrderResponse(BaseSchema):
    pass


class DispatchManifest(BaseSchema):
    pass


class SuccessResponseSchema(BaseSchema):
    pass


class ActionInfo(BaseSchema):
    pass


class GetActionsResponse(BaseSchema):
    pass


class RefundInformation(BaseSchema):
    pass


class HistoryReason(BaseSchema):
    pass


class HistoryMeta(BaseSchema):
    pass


class HistoryDict(BaseSchema):
    pass


class ShipmentHistoryResponse(BaseSchema):
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


class SendSmsResponse(BaseSchema):
    pass


class Dimension(BaseSchema):
    pass


class UpdatePackagingDimensionsPayload(BaseSchema):
    pass


class UpdatePackagingDimensionsResponse(BaseSchema):
    pass


class Tax(BaseSchema):
    pass


class Charge(BaseSchema):
    pass


class CurrencyValueSchema(BaseSchema):
    pass


class AmountSchema(BaseSchema):
    pass


class DynamicChargeTaxSchema(BaseSchema):
    pass


class RuleConditionsSchema(BaseSchema):
    pass


class RuleSchema(BaseSchema):
    pass


class DistributionSchema(BaseSchema):
    pass


class DistributionLogicSchema(BaseSchema):
    pass


class DynamicChargeSchema(BaseSchema):
    pass


class LineItem(BaseSchema):
    pass


class ProcessingDates(BaseSchema):
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


class CurrencyInfoCurrency(BaseSchema):
    pass


class CurrencyInfoConversionRate(BaseSchema):
    pass


class CurrencyInfo(BaseSchema):
    pass


class ConfigPayment(BaseSchema):
    pass


class ConfigDpConfiguration(BaseSchema):
    pass


class ConfigApplication(BaseSchema):
    pass


class CreateOrderAPI(BaseSchema):
    pass


class CreateOrderErrorReponse(BaseSchema):
    pass


class DpConfiguration(BaseSchema):
    pass


class PaymentMethods(BaseSchema):
    pass


class CreateChannelPaymentInfo(BaseSchema):
    pass


class CreateChannelConfig(BaseSchema):
    pass


class UploadManifestConsent(BaseSchema):
    pass


class PlatformOrderUpdate(BaseSchema):
    pass


class ResponseDetail(BaseSchema):
    pass


class OrderData(BaseSchema):
    pass


class OrderUpdatePayload(BaseSchema):
    pass


class OrderUpdateResponseDetail(BaseSchema):
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


class RefundModeInfoFormat(BaseSchema):
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


class AttachOrderUserResponse(BaseSchema):
    pass


class AttachOrderUserErrorResponse(BaseSchema):
    pass


class SendUserMobileOTP(BaseSchema):
    pass


class PointBlankOtpData(BaseSchema):
    pass


class SendUserMobileOtpResponse(BaseSchema):
    pass


class VerifyOtpData(BaseSchema):
    pass


class VerifyMobileOTP(BaseSchema):
    pass


class VerifyOtpResponseData(BaseSchema):
    pass


class VerifyOtpResponse(BaseSchema):
    pass


class VerifyOtpErrorResponseData(BaseSchema):
    pass


class VerifyOtpErrorResponse(BaseSchema):
    pass


class BulkReportsDownloadRequest(BaseSchema):
    pass


class BulkReportsDownloadResponse(BaseSchema):
    pass


class APIFailedResponse(BaseSchema):
    pass


class BulkFailedResponse(BaseSchema):
    pass


class BulkStateTransistionRequestSchema(BaseSchema):
    pass


class BulkStateTransistionResponse(BaseSchema):
    pass


class ShipmentActionInfo(BaseSchema):
    pass


class BulkActionListingData(BaseSchema):
    pass


class BulkListinPage(BaseSchema):
    pass


class BulkListingResponse(BaseSchema):
    pass


class JobDetailsData(BaseSchema):
    pass


class JobDetailsResponse(BaseSchema):
    pass


class JobFailedResponse(BaseSchema):
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


class FiltersRequest(BaseSchema):
    pass


class ProcessManifest(BaseSchema):
    pass


class ProcessManifestResponse(BaseSchema):
    pass


class ProcessManifestItemResponse(BaseSchema):
    pass


class FilterInfoOption(BaseSchema):
    pass


class FiltersInfo(BaseSchema):
    pass


class ManifestFiltersResponse(BaseSchema):
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


class EInvoiceRetryResponse(BaseSchema):
    pass


class EInvoiceErrorInfo(BaseSchema):
    pass


class EInvoiceErrorResponseData(BaseSchema):
    pass


class EInvoiceErrorResponse(BaseSchema):
    pass


class EInvoiceErrorResponseDetails(BaseSchema):
    pass


class EInvoiceRetryShipmentData(BaseSchema):
    pass


class CourierPartnerTrackingDetails(BaseSchema):
    pass


class CourierPartnerTrackingResponse(BaseSchema):
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


class OptionItem(BaseSchema):
    pass


class SuperLaneItem(BaseSchema):
    pass


class RuleLaneConfigResponse(BaseSchema):
    pass


class RuleLaneConfigResponseSchema(BaseSchema):
    pass


class RuleLaneConfigErrorResponse(BaseSchema):
    pass


class QuestionSetItem(BaseSchema):
    pass


class GenerateInvoiceIDRequestSchema(BaseSchema):
    pass


class Reason(BaseSchema):
    pass


class RuleRequest(BaseSchema):
    pass


class RuleResponse(BaseSchema):
    pass


class RuleUpdateRequest(BaseSchema):
    pass


class Condition(BaseSchema):
    pass


class RuleMeta(BaseSchema):
    pass


class RuleAction(BaseSchema):
    pass


class Department(BaseSchema):
    pass


class L3(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class RuleSuccessResponse(BaseSchema):
    pass


class UpdateRulePositionRequest(BaseSchema):
    pass


class RuleListResponse(BaseSchema):
    pass


class RuleItem(BaseSchema):
    pass


class RuleParametersResponse(BaseSchema):
    pass


class ParameterResponse(BaseSchema):
    pass


class RuleListRequest(BaseSchema):
    pass


class ErrorGenericWithStatus(BaseSchema):
    pass


class ManifestResponseSchema(BaseSchema):
    pass


class ProcessManifestRequestSchema(BaseSchema):
    pass


class ManifestItems(BaseSchema):
    pass


class ManifestErrorResponse(BaseSchema):
    pass


class RuleListItem(BaseSchema):
    pass


class RuleError(BaseSchema):
    pass


class RuleErrorResponse(BaseSchema):
    pass


class PageInfo(BaseSchema):
    pass


class ConfigData(BaseSchema):
    pass


class ConfigUpdatedResponse(BaseSchema):
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


class CommonErrorResponse(BaseSchema):
    pass


class ExceptionErrorResponse(BaseSchema):
    pass


class ProductDetails(BaseSchema):
    pass


class RePromise(BaseSchema):
    pass


class PackagingDimensions(BaseSchema):
    pass


class ConsolidateShipmentPayload(BaseSchema):
    pass


class ConsolidateShipmentResponse(BaseSchema):
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


class Identifier(BaseSchema):
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


class ShipmentItem(BaseSchema):
    pass


class ShipmentInternalPlatformViewResponse(BaseSchema):
    pass


class TrackingList(BaseSchema):
    pass


class InvoiceInfo(BaseSchema):
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


class AffiliateConfig(BaseSchema):
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


class ShipmentPaymentInfoData(BaseSchema):
    pass


class PlatformShipment(BaseSchema):
    pass


class ShipmentInfoResponse(BaseSchema):
    pass


class TaxDetails(BaseSchema):
    pass


class PaymentInfoData(BaseSchema):
    pass


class OrderDetailsResponse(BaseSchema):
    pass


class SubLane(BaseSchema):
    pass


class SuperLane(BaseSchema):
    pass


class LaneConfigResponse(BaseSchema):
    pass


class PlatformBreakupValues(BaseSchema):
    pass


class PlatformChannel(BaseSchema):
    pass


class PlatformOrderItems(BaseSchema):
    pass


class OrderListingResponse(BaseSchema):
    pass


class PlatformTrack(BaseSchema):
    pass


class PlatformShipmentTrack(BaseSchema):
    pass


class AdvanceFilterInfo(BaseSchema):
    pass


class FilterOptions(BaseSchema):
    pass


class FiltersList(BaseSchema):
    pass


class GlobalFiltersResponse(BaseSchema):
    pass


class ViewDetails(BaseSchema):
    pass


class ParentViews(BaseSchema):
    pass


class UserViewsResponse(BaseSchema):
    pass


class UserViewPosition(BaseSchema):
    pass


class CreateUpdateDeleteResponse(BaseSchema):
    pass


class FiltersResponse(BaseSchema):
    pass


class URL(BaseSchema):
    pass


class FileResponse(BaseSchema):
    pass


class BulkActionTemplate(BaseSchema):
    pass


class BulkActionTemplateResponse(BaseSchema):
    pass


class PlatformShipmentReasonsResponse(BaseSchema):
    pass


class ShipmentResponseReasons(BaseSchema):
    pass


class ShipmentReasonsResponse(BaseSchema):
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


class Attributes(BaseSchema):
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


class ShipmentDetails(BaseSchema):
    pass


class UserDetails(BaseSchema):
    pass


class WeightData(BaseSchema):
    pass


class BagDetails(BaseSchema):
    pass


class BagDetailsPlatformResponse(BaseSchema):
    pass


class BagsPage(BaseSchema):
    pass


class BagData(BaseSchema):
    pass


class GetBagsPlatformResponse(BaseSchema):
    pass


class GeneratePosOrderReceiptResponse(BaseSchema):
    pass


class Templates(BaseSchema):
    pass


class AllowedTemplatesResponse(BaseSchema):
    pass


class CDN(BaseSchema):
    pass


class Upload(BaseSchema):
    pass


class TemplateDownloadResponse(BaseSchema):
    pass





class InvalidateShipmentCachePayload(BaseSchema):
    # Order swagger.json

    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    
    affiliate_bag_ids = fields.List(fields.Str(required=False), required=False)
    
    bag_ids = fields.List(fields.Str(required=False), required=False)
    


class InvalidateShipmentCacheNestedResponse(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    error = fields.Str(required=False)
    


class InvalidateShipmentCacheResponse(BaseSchema):
    # Order swagger.json

    
    response = fields.List(fields.Nested(InvalidateShipmentCacheNestedResponse, required=False), required=False)
    


class UpdatePackingErrorResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False, allow_none=True)
    
    error = fields.Str(required=False, allow_none=True)
    


class ErrorResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False, allow_none=True)
    
    success = fields.Boolean(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    error_trace = fields.Str(required=False, allow_none=True)
    
    error = fields.Str(required=False, allow_none=True)
    
    remarks = fields.Str(required=False, allow_none=True)
    
    status_code = fields.Int(required=False, allow_none=True)
    


class LogErrorResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    


class QuestionErrorResponse(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False, allow_none=True)
    
    message = fields.Dict(required=False, allow_none=True)
    


class RefundStateConfigurationByPaymentType(BaseSchema):
    # Order swagger.json

    
    states = fields.List(fields.Str(required=False), required=False)
    
    allow_refund_initiate = fields.Boolean(required=False)
    


class PostRefundStateConfiguration(BaseSchema):
    # Order swagger.json

    
    prepaid = fields.Nested(RefundStateConfigurationByPaymentType, required=False)
    
    non_prepaid = fields.Nested(RefundStateConfigurationByPaymentType, required=False)
    
    mix_mop = fields.Nested(RefundStateConfigurationByPaymentType, required=False)
    


class PostRefundStateConfigurationResponse(BaseSchema):
    # Order swagger.json

    
    refund_config = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class GetRefundStateConfigurationResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    config = fields.Nested(PostRefundStateConfiguration, required=False)
    


class RefundStates(BaseSchema):
    # Order swagger.json

    
    state = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class GetRefundStates(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(RefundStates, required=False), required=False)
    
    status = fields.Int(required=False)
    


class RefundStateManualWithoutMessage(BaseSchema):
    # Order swagger.json

    
    is_manual = fields.Boolean(required=False)
    


class RefundStateManualWithMessage(BaseSchema):
    # Order swagger.json

    
    is_manual = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class RefundStateManualWithMessageData(BaseSchema):
    # Order swagger.json

    
    prepaid = fields.Nested(RefundStateManualWithMessage, required=False)
    
    non_prepaid = fields.Nested(RefundStateManualWithMessage, required=False)
    
    mix_mop = fields.Nested(RefundStateManualWithMessage, required=False)
    


class RefundStateConfigurationManualSchema(BaseSchema):
    # Order swagger.json

    
    prepaid = fields.Nested(RefundStateManualWithoutMessage, required=False)
    
    non_prepaid = fields.Nested(RefundStateManualWithoutMessage, required=False)
    
    mix_mop = fields.Nested(RefundStateManualWithoutMessage, required=False)
    


class RefundStateConfigurationManualSchemaResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(RefundStateManualWithMessageData, required=False)
    


class RefundSubOption(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class RefundBreakup(BaseSchema):
    # Order swagger.json

    
    mode = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    display_name = fields.Str(required=False)
    
    offline = fields.Boolean(required=False)
    


class RefundOptionShipmentResponse(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    breakups = fields.List(fields.Nested(RefundBreakup, required=False), required=False)
    
    option = fields.List(fields.Nested(RefundSubOption, required=False), required=False)
    
    offline = fields.Boolean(required=False)
    
    amount = fields.Float(required=False)
    
    slug = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class CurrencySchema(BaseSchema):
    # Order swagger.json

    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class RefundOptionsSchemaResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    currency = fields.Nested(CurrencySchema, required=False)
    
    refund_options = fields.List(fields.Nested(RefundOptionShipmentResponse, required=False), required=False)
    


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
    


class StoreReassignResponse(BaseSchema):
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
    
    user_id = fields.Str(required=False)
    
    entities = fields.List(fields.Nested(LockManagerEntities, required=False), required=False)
    
    resume_tasks_after_unlock = fields.Boolean(required=False, allow_none=True)
    
    lock_after_transition = fields.Boolean(required=False)
    
    unlock_before_transition = fields.Boolean(required=False)
    


class OriginalFilter(BaseSchema):
    # Order swagger.json

    
    affiliate_shipment_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    


class Bags(BaseSchema):
    # Order swagger.json

    
    bag_id = fields.Int(required=False)
    
    affiliate_bag_id = fields.Str(required=False)
    
    is_locked = fields.Boolean(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    


class CheckResponse(BaseSchema):
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
    


class UpdateShipmentLockResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    check_response = fields.List(fields.Nested(CheckResponse, required=False), required=False)
    
    status = fields.Int(required=False)
    


class AnnouncementResponse(BaseSchema):
    # Order swagger.json

    
    to_datetime = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    platform_name = fields.Str(required=False)
    
    from_datetime = fields.Str(required=False)
    
    platform_id = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    company_id = fields.Int(required=False, allow_none=True)
    
    logo_url = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    


class AnnouncementsResponse(BaseSchema):
    # Order swagger.json

    
    announcements = fields.List(fields.Nested(AnnouncementResponse, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Int(required=False)
    


class Click2CallResponse(BaseSchema):
    # Order swagger.json

    
    call_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class BaseResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ErrorDetail(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Float(required=False)
    


class ProductsReasonsFilters(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    quantity = fields.Float(required=False)
    


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
    
    quantity = fields.Float(required=False)
    


class OrderItemDataUpdates(BaseSchema):
    # Order swagger.json

    
    data = fields.Dict(required=False)
    


class ProductsDataUpdatesFilters(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    quantity = fields.Float(required=False)
    


class ProductsDataUpdates(BaseSchema):
    # Order swagger.json

    
    filters = fields.List(fields.Nested(ProductsDataUpdatesFilters, required=False), required=False)
    
    data = fields.Dict(required=False)
    


class EntitiesDataUpdates(BaseSchema):
    # Order swagger.json

    
    filters = fields.List(fields.Dict(required=False), required=False)
    
    data = fields.Dict(required=False)
    


class RepricedProductsDataUpdates(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    price = fields.Int(required=False)
    


class DataUpdates(BaseSchema):
    # Order swagger.json

    
    order_item_status = fields.List(fields.Nested(OrderItemDataUpdates, required=False), required=False)
    
    products = fields.List(fields.Nested(ProductsDataUpdates, required=False), required=False)
    
    entities = fields.List(fields.Nested(EntitiesDataUpdates, required=False), required=False)
    
    repriced_products = fields.List(fields.Nested(RepricedProductsDataUpdates, required=False), required=False)
    


class TransitionComments(BaseSchema):
    # Order swagger.json

    
    title = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class ShipmentsRequest(BaseSchema):
    # Order swagger.json

    
    identifier = fields.Str(required=False)
    
    reasons = fields.Nested(ReasonsData, required=False)
    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    data_updates = fields.Nested(DataUpdates, required=False)
    
    transition_comments = fields.List(fields.Nested(TransitionComments, required=False), required=False)
    


class StatuesRequest(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentsRequest, required=False), required=False)
    
    exclude_bags_next_state = fields.Str(required=False)
    
    split_shipment = fields.Boolean(required=False)
    


class ActionRequest(BaseSchema):
    # Order swagger.json

    
    action = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentsRequest, required=False), required=False)
    
    exclude_bags_next_state = fields.Str(required=False)
    
    split_shipment = fields.Boolean(required=False)
    


class UpdateShipmentStatusRequestSchema(BaseSchema):
    # Order swagger.json

    
    force_transition = fields.Boolean(required=False)
    
    statuses = fields.List(fields.Nested(StatuesRequest, required=False), required=False)
    
    lock_after_transition = fields.Boolean(required=False)
    
    unlock_before_transition = fields.Boolean(required=False)
    
    task = fields.Boolean(required=False)
    
    resume_tasks_after_unlock = fields.Boolean(required=False)
    


class UpdateShipmentActionRequest(BaseSchema):
    # Order swagger.json

    
    force_transition = fields.Boolean(required=False)
    
    statuses = fields.List(fields.Nested(ActionRequest, required=False), required=False)
    
    lock_after_transition = fields.Boolean(required=False)
    
    unlock_before_transition = fields.Boolean(required=False)
    
    task = fields.Boolean(required=False)
    


class ShipmentsResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False, allow_none=True)
    
    final_state = fields.Dict(required=False, allow_none=True)
    
    identifier = fields.Str(required=False, allow_none=True)
    
    stack_trace = fields.Str(required=False, allow_none=True)
    
    code = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    exception = fields.Str(required=False, allow_none=True)
    


class StatuesResponse(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(ShipmentsResponse, required=False), required=False)
    


class UpdateShipmentStatusResponseBody(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(StatuesResponse, required=False), required=False)
    


class DPConfiguration(BaseSchema):
    # Order swagger.json

    
    shipping_by = fields.Str(required=False)
    


class PaymentConfig(BaseSchema):
    # Order swagger.json

    
    mode_of_payment = fields.Str(required=False)
    
    source = fields.Str(required=False)
    


class CreateOrderConfig(BaseSchema):
    # Order swagger.json

    
    dp_configuration = fields.Nested(DPConfiguration, required=False)
    
    integration_type = fields.Str(required=False)
    
    location_reassignment = fields.Boolean(required=False)
    
    payment = fields.Nested(PaymentConfig, required=False)
    
    optimal_shipment_creation = fields.Boolean(required=False)
    


class CreateOrderResponse(BaseSchema):
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
    


class GetActionsResponse(BaseSchema):
    # Order swagger.json

    
    permissions = fields.List(fields.Nested(ActionInfo, required=False), required=False)
    


class RefundInformation(BaseSchema):
    # Order swagger.json

    
    mode = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    merchant_transaction_id = fields.Str(required=False)
    
    refund_status = fields.Str(required=False)
    


class HistoryReason(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False, allow_none=True)
    
    category = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False, allow_none=True)
    
    dislay_name = fields.Str(required=False, allow_none=True)
    
    code = fields.Int(required=False, allow_none=True)
    
    quantity = fields.Int(required=False, allow_none=True)
    


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
    
    channel_type = fields.Str(required=False)
    
    activity_comment = fields.Str(required=False, allow_none=True)
    
    activity_type = fields.Str(required=False, allow_none=True)
    
    receiver = fields.Str(required=False, allow_none=True)
    
    recipient = fields.Str(required=False, allow_none=True)
    
    slug = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False, allow_none=True)
    
    prev_store_name = fields.Str(required=False, allow_none=True)
    
    prev_store_code = fields.Str(required=False, allow_none=True)
    
    prev_store_id = fields.Str(required=False, allow_none=True)
    
    refund_to = fields.Str(required=False, allow_none=True)
    
    refund_information = fields.List(fields.Nested(RefundInformation, required=False), required=False)
    


class HistoryDict(BaseSchema):
    # Order swagger.json

    
    user_details = fields.Dict(required=False)
    
    display_message = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    ticket_url = fields.Str(required=False, allow_none=True)
    
    l3_detail = fields.Str(required=False, allow_none=True)
    
    createdat = fields.Str(required=False)
    
    created_ts = fields.Str(required=False, allow_none=True)
    
    ticket_id = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    
    l2_detail = fields.Str(required=False, allow_none=True)
    
    assigned_agent = fields.Str(required=False, allow_none=True)
    
    meta = fields.Nested(HistoryMeta, required=False)
    
    l1_detail = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False)
    
    user = fields.Str(required=False)
    


class ShipmentHistoryResponse(BaseSchema):
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

    
    days = fields.Int(required=False)
    
    reason = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    amount_paid = fields.Float(required=False)
    
    order_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    customer_name = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class SendSmsPayload(BaseSchema):
    # Order swagger.json

    
    bag_id = fields.Str(required=False)
    
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

    
    status_code = fields.Int(required=False)
    
    remarks = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    result = fields.List(fields.Nested(OrderStatusData, required=False), required=False)
    


class SendSmsResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class Dimension(BaseSchema):
    # Order swagger.json

    
    packaging_type = fields.Str(required=False)
    
    weight = fields.Str(required=False)
    
    height = fields.Str(required=False)
    
    length = fields.Float(required=False)
    
    width = fields.Float(required=False)
    


class UpdatePackagingDimensionsPayload(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    dimension = fields.List(fields.Nested(Dimension, required=False), required=False)
    


class UpdatePackagingDimensionsResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    


class Tax(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    rate = fields.Float(required=False)
    
    breakup = fields.List(fields.Dict(required=False), required=False)
    
    amount = fields.Nested(AmountSchema, required=False)
    


class Charge(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    amount = fields.Nested(AmountSchema, required=False)
    
    tax = fields.Nested(Tax, required=False)
    
    code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class CurrencyValueSchema(BaseSchema):
    # Order swagger.json

    
    value = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    


class AmountSchema(BaseSchema):
    # Order swagger.json

    
    ordering_currency = fields.Nested(CurrencyValueSchema, required=False)
    
    base_currency = fields.Nested(CurrencyValueSchema, required=False)
    


class DynamicChargeTaxSchema(BaseSchema):
    # Order swagger.json

    
    reporting_hsn_code = fields.Str(required=False)
    


class RuleConditionsSchema(BaseSchema):
    # Order swagger.json

    
    article_tag = fields.Str(required=False)
    
    department = fields.List(fields.Str(required=False), required=False)
    


class RuleSchema(BaseSchema):
    # Order swagger.json

    
    conditions = fields.Nested(RuleConditionsSchema, required=False)
    


class DistributionSchema(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    logic = fields.Str(required=False)
    
    rule = fields.Nested(RuleSchema, required=False)
    


class DistributionLogicSchema(BaseSchema):
    # Order swagger.json

    
    distribution_level = fields.Str(required=False)
    
    distribution = fields.Nested(DistributionSchema, required=False)
    


class DynamicChargeSchema(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    amount = fields.Nested(AmountSchema, required=False)
    
    taxes = fields.Nested(DynamicChargeTaxSchema, required=False)
    
    meta = fields.Dict(required=False)
    
    distribution_logic = fields.Nested(DistributionLogicSchema, required=False)
    


class LineItem(BaseSchema):
    # Order swagger.json

    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    custom_message = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    external_line_id = fields.Str(required=False)
    
    dynamic_charges = fields.List(fields.Nested(DynamicChargeSchema, required=False), required=False)
    


class ProcessingDates(BaseSchema):
    # Order swagger.json

    
    dp_pickup_slot = fields.Dict(required=False)
    
    dispatch_after_date = fields.Str(required=False)
    
    dispatch_by_date = fields.Str(required=False)
    
    confirm_by_date = fields.Str(required=False)
    
    customer_pickup_slot = fields.Dict(required=False)
    
    pack_by_date = fields.Str(required=False)
    


class Shipment(BaseSchema):
    # Order swagger.json

    
    line_items = fields.List(fields.Nested(LineItem, required=False), required=False)
    
    external_shipment_id = fields.Str(required=False)
    
    external_location_id = fields.Str(required=False)
    
    processing_dates = fields.Nested(ProcessingDates, required=False)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    priority = fields.Int(required=False)
    
    location_id = fields.Int(required=False)
    
    order_type = fields.Str(required=False)
    
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
    
    tags = fields.List(fields.Str(required=False), required=False)
    
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

    
    phone = fields.Str(required=False)
    
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

    
    phone = fields.Str(required=False)
    
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
    
    landmark = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class UserInfo(BaseSchema):
    # Order swagger.json

    
    user_id = fields.Str(required=False)
    
    user_type = fields.Str(required=False)
    
    primary_email = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    primary_mobile_number = fields.Str(required=False)
    
    is_authenticated = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    


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
    
    collected = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    merchant_transaction_id = fields.Str(required=False)
    


class PaymentInfo(BaseSchema):
    # Order swagger.json

    
    primary_mode = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMethod, required=False), required=False)
    


class CurrencyInfoCurrency(BaseSchema):
    # Order swagger.json

    
    currency_code = fields.Str(required=False)
    
    currency_name = fields.Str(required=False)
    
    currency_sub_unit = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class CurrencyInfoConversionRate(BaseSchema):
    # Order swagger.json

    
    rates = fields.Dict(required=False)
    
    base = fields.Str(required=False)
    
    timestamp = fields.Float(required=False)
    


class CurrencyInfo(BaseSchema):
    # Order swagger.json

    
    currency = fields.Nested(CurrencyInfoCurrency, required=False)
    
    order_currency = fields.Str(required=False)
    
    conversion_rate = fields.Nested(ConversionRate, required=False)
    
    ordering_currency = fields.Nested(OrderingCurrency, required=False)
    


class ConfigPayment(BaseSchema):
    # Order swagger.json

    
    source = fields.Str(required=False)
    
    mode_of_payment = fields.Str(required=False)
    


class ConfigDpConfiguration(BaseSchema):
    # Order swagger.json

    
    shipping_by = fields.Str(required=False)
    
    refund_by = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    


class ConfigApplication(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class CreateOrderAPI(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    
    shipping_info = fields.Nested(ShippingInfo, required=False)
    
    billing_info = fields.Nested(ShippingInfo, required=False)
    
    currency_info = fields.Nested(CurrencyInfo, required=False)
    
    external_order_id = fields.Str(required=False)
    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    external_creation_date = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    tax_info = fields.Nested(TaxInfo, required=False)
    
    config = fields.Nested(CreateOrderConfig, required=False)
    
    payment_info = fields.Nested(PaymentInfo, required=False)
    
    user_info = fields.Nested(UserInfo, required=False)
    
    unlock_before_transition = fields.Boolean(required=False)
    
    lock_after_transition = fields.Boolean(required=False)
    
    dynamic_charges = fields.List(fields.Nested(DynamicChargeSchema, required=False), required=False)
    
    ordering_store_id = fields.Int(required=False)
    
    order_platform = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    external_shipment_id = fields.Str(required=False)
    
    custom_json = fields.Dict(required=False, allow_none=True)
    


class CreateOrderErrorReponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    errors = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    


class DpConfiguration(BaseSchema):
    # Order swagger.json

    
    shipping_by = fields.Str(required=False)
    


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

    
    dp_configuration = fields.Nested(DpConfiguration, required=False)
    
    shipment_assignment = fields.Str(required=False)
    
    location_reassignment = fields.Boolean(required=False)
    
    errors = fields.Str(required=False)
    
    status_code = fields.Float(required=False)
    
    fynd_order_id = fields.Str(required=False)
    


class UploadManifestConsent(BaseSchema):
    # Order swagger.json

    
    consent_url = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    


class PlatformOrderUpdate(BaseSchema):
    # Order swagger.json

    
    order_id = fields.Str(required=False)
    


class ResponseDetail(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Int(required=False)
    


class OrderData(BaseSchema):
    # Order swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Raw(required=False)
    
    order_date = fields.Str(required=False, allow_none=True)
    
    created_ts = fields.Str(required=False)
    
    tax_details = fields.Nested(TaxDetails, required=False)
    
    meta = fields.Dict(required=False)
    
    fynd_order_id = fields.Str(required=False, allow_none=True)
    
    prices = fields.Nested(Prices, required=False)
    
    charges = fields.List(fields.Nested(PriceAdjustmentCharge, required=False), required=False)
    
    payment_methods = fields.Dict(required=False, allow_none=True)
    
    payment_info = fields.List(fields.Nested(PaymentInfoData, required=False), required=False)
    
    affiliate_order_id = fields.Str(required=False, allow_none=True)
    


class OrderUpdatePayload(BaseSchema):
    # Order swagger.json

    
    data = fields.List(fields.Nested(OrderData, required=False), required=False)
    


class OrderUpdateResponseDetail(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    validation_errors = fields.Dict(required=False)
    


class FyndOrderIdList(BaseSchema):
    # Order swagger.json

    
    fynd_order_id = fields.List(fields.Str(required=False), required=False)
    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    mobile = fields.Int(required=False)
    


class OrderStatus(BaseSchema):
    # Order swagger.json

    
    order_details = fields.List(fields.Nested(FyndOrderIdList, required=False), required=False)
    


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
    
    seller_id = fields.Int(required=False)
    
    customer_mobile_number = fields.Str(required=False)
    


class CreditBalanceInfo(BaseSchema):
    # Order swagger.json

    
    total_credited_balance = fields.Float(required=False)
    
    reason = fields.Str(required=False)
    
    customer_mobile_number = fields.Str(required=False)
    
    is_cn_locked = fields.Boolean(required=False)
    
    total_locked_amount = fields.Float(required=False)
    
    allowed_redemption_amount = fields.Float(required=False)
    


class FetchCreditBalanceResponsePayload(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    status = fields.Float(required=False)
    
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
    


class RefundModeInfoFormat(BaseSchema):
    # Order swagger.json

    
    refund_to = fields.Str(required=False)
    
    manual_refund_data = fields.Dict(required=False)
    


class RefundModeInfo(BaseSchema):
    # Order swagger.json

    
    format = fields.Nested(RefundModeInfoFormat, required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    options = fields.List(fields.Nested(RefundOption, required=False), required=False)
    
    display_name = fields.Str(required=False)
    


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
    


class AttachOrderUserResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Int(required=False)
    


class AttachOrderUserErrorResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    status = fields.Int(required=False)
    
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
    


class SendUserMobileOtpResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Nested(PointBlankOtpData, required=False)
    


class VerifyOtpData(BaseSchema):
    # Order swagger.json

    
    request_id = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    otp_code = fields.Str(required=False)
    


class VerifyMobileOTP(BaseSchema):
    # Order swagger.json

    
    otp_data = fields.Nested(VerifyOtpData, required=False)
    
    fynd_order_id = fields.Str(required=False)
    


class VerifyOtpResponseData(BaseSchema):
    # Order swagger.json

    
    mobile = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class VerifyOtpResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Nested(VerifyOtpResponseData, required=False)
    


class VerifyOtpErrorResponseData(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class VerifyOtpErrorResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Nested(VerifyOtpErrorResponseData, required=False)
    


class BulkReportsDownloadRequest(BaseSchema):
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
    
    filters = fields.Dict(required=False)
    


class BulkReportsDownloadResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    batch_id = fields.Str(required=False)
    


class APIFailedResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    status = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    


class BulkFailedResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    


class BulkStateTransistionRequestSchema(BaseSchema):
    # Order swagger.json

    
    url = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    


class BulkStateTransistionResponse(BaseSchema):
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
    
    total_shipments_count = fields.Int(required=False)
    
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
    


class BulkListingResponse(BaseSchema):
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
    


class JobDetailsResponse(BaseSchema):
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
    


class JobFailedResponse(BaseSchema):
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
    
    item_total = fields.Int(required=False)
    


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
    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    


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
    
    type = fields.Str(required=False)
    


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
    


class FiltersRequest(BaseSchema):
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

    
    filters = fields.Nested(FiltersRequest, required=False)
    
    action = fields.Str(required=False)
    
    unique_id = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    


class ProcessManifestResponse(BaseSchema):
    # Order swagger.json

    
    company_id = fields.Int(required=False)
    
    filters = fields.Nested(Filters, required=False)
    
    user_id = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    


class ProcessManifestItemResponse(BaseSchema):
    # Order swagger.json

    
    items = fields.Nested(ProcessManifestResponse, required=False)
    


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
    


class ManifestFiltersResponse(BaseSchema):
    # Order swagger.json

    
    advance = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    


class PageDetails(BaseSchema):
    # Order swagger.json

    
    current = fields.Int(required=False, allow_none=True)
    
    has_next = fields.Boolean(required=False, allow_none=True)
    
    has_previous = fields.Boolean(required=False, allow_none=True)
    
    item_total = fields.Int(required=False, allow_none=True)
    
    size = fields.Int(required=False, allow_none=True)
    
    total = fields.Int(required=False, allow_none=True)
    
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
    


class EInvoiceRetryResponse(BaseSchema):
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
    


class EInvoiceErrorResponse(BaseSchema):
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
    
    meta = fields.Dict(required=False, allow_none=True)
    
    operational_status = fields.Str(required=False)
    
    promised_delivery_date = fields.Str(required=False, allow_none=True)
    
    remark = fields.Str(required=False, allow_none=True)
    
    shipment_id = fields.Str(required=False)
    


class CourierPartnerTrackingResponse(BaseSchema):
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
    
    error_message = fields.Str(required=False, allow_none=True)
    
    display_message = fields.Str(required=False, allow_none=True)
    
    method_name = fields.Str(required=False)
    
    meta = fields.Dict(required=False, allow_none=True)
    


class FailedOrderLogs(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(FailedOrdersItem, required=False), required=False)
    
    page = fields.Nested(PageDetails, required=False)
    


class FailedOrderLogDetails(BaseSchema):
    # Order swagger.json

    
    error_trace = fields.Str(required=False, allow_none=True)
    
    exception = fields.Str(required=False, allow_none=True)
    


class OptionItem(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    total_items = fields.Int(required=False)
    


class SuperLaneItem(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    options = fields.List(fields.Nested(OptionItem, required=False), required=False)
    
    total_items = fields.Int(required=False)
    


class RuleLaneConfigResponse(BaseSchema):
    # Order swagger.json

    
    super_lanes = fields.List(fields.Nested(SuperLaneItem, required=False), required=False)
    


class RuleLaneConfigResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    


class RuleLaneConfigErrorResponse(BaseSchema):
    # Order swagger.json

    
    response = fields.Nested(RuleLaneConfigResponseSchema, required=False)
    


class QuestionSetItem(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    


class GenerateInvoiceIDRequestSchema(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    


class Reason(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    remark_required = fields.Boolean(required=False)
    
    show_text_area = fields.Boolean(required=False, allow_none=True)
    
    reasons = fields.List(fields.Nested(lambda: Reason(exclude=('reasons')), required=False), required=False)
    
    qc_type = fields.List(fields.Str(required=False), required=False)
    
    question_set = fields.List(fields.Nested(QuestionSet, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_deleted = fields.Boolean(required=False)
    


class RuleRequest(BaseSchema):
    # Order swagger.json

    
    flow_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    channel = fields.Str(required=False)
    
    rule_type = fields.Str(required=False)
    
    is_deleted = fields.Boolean(required=False)
    
    restrict_forward_serviceability = fields.Boolean(required=False)
    
    conditions = fields.List(fields.Nested(Condition, required=False), required=False)
    
    meta = fields.Nested(RuleMeta, required=False)
    
    qc_enabled = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    actions = fields.Nested(RuleAction, required=False)
    


class RuleResponse(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    items = fields.Nested(RuleItem, required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(RuleError, required=False)
    


class RuleUpdateRequest(BaseSchema):
    # Order swagger.json

    
    flow_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    channel = fields.Str(required=False)
    
    rule_type = fields.Str(required=False)
    
    is_deleted = fields.Boolean(required=False)
    
    position = fields.Int(required=False)
    
    restrict_forward_serviceability = fields.Boolean(required=False)
    
    conditions = fields.List(fields.Nested(Condition, required=False), required=False)
    
    meta = fields.Nested(RuleMeta, required=False)
    
    qc_enabled = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    actions = fields.Nested(RuleAction, required=False)
    


class Condition(BaseSchema):
    # Order swagger.json

    
    variable = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    


class RuleMeta(BaseSchema):
    # Order swagger.json

    
    department = fields.Nested(Department, required=False)
    
    l3 = fields.Nested(L3, required=False)
    
    restrict_forward_serviceability = fields.Boolean(required=False, allow_none=True)
    


class RuleAction(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(Reason, required=False), required=False)
    


class Department(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class L3(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class Error(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class RuleSuccessResponse(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(RuleError, required=False)
    


class UpdateRulePositionRequest(BaseSchema):
    # Order swagger.json

    
    rule_id = fields.Int(required=False)
    
    page_no = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    
    position = fields.Int(required=False)
    
    flow_type = fields.Str(required=False)
    


class RuleListResponse(BaseSchema):
    # Order swagger.json

    
    page = fields.Nested(PageInfo, required=False)
    
    items = fields.List(fields.Nested(RuleItem, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(RuleError, required=False)
    


class RuleItem(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    value = fields.Str(required=False, allow_none=True)
    
    channel = fields.Str(required=False)
    
    actions = fields.Nested(RuleAction, required=False)
    
    qc_enabled = fields.Boolean(required=False)
    
    is_deleted = fields.Boolean(required=False)
    
    restrict_forward_serviceability = fields.Boolean(required=False)
    
    conditions = fields.List(fields.Nested(Condition, required=False), required=False)
    
    meta = fields.Nested(RuleMeta, required=False)
    
    rule_type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    flow_type = fields.Str(required=False)
    
    position = fields.Int(required=False)
    


class RuleParametersResponse(BaseSchema):
    # Order swagger.json

    
    response = fields.List(fields.Nested(ParameterResponse, required=False), required=False)
    


class ParameterResponse(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class RuleListRequest(BaseSchema):
    # Order swagger.json

    
    page_size = fields.Int(required=False)
    
    page_no = fields.Int(required=False)
    
    flow_type = fields.Str(required=False)
    
    lane_type = fields.Str(required=False)
    


class ErrorGenericWithStatus(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Float(required=False)
    


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
    


class ManifestErrorResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Float(required=False)
    
    error = fields.Str(required=False)
    


class RuleListItem(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    channel = fields.Str(required=False)
    
    actions = fields.Nested(RuleAction, required=False)
    
    qc_enabled = fields.Boolean(required=False)
    
    is_deleted = fields.Boolean(required=False)
    
    conditions = fields.Nested(Condition, required=False)
    
    meta = fields.Nested(Meta, required=False)
    
    rule_type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    flow_type = fields.Str(required=False)
    
    position = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(RuleError, required=False)
    


class RuleError(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    


class RuleErrorResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False, allow_none=True)
    
    error = fields.Str(required=False, allow_none=True)
    


class PageInfo(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    page_size = fields.Int(required=False)
    


class ConfigData(BaseSchema):
    # Order swagger.json

    
    acknowledged = fields.Boolean(required=False)
    
    is_upserted = fields.Boolean(required=False)
    
    is_inserted = fields.Boolean(required=False)
    


class ConfigUpdatedResponse(BaseSchema):
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
    
    entity = fields.Str(required=False)
    


class TransitionConfigData(BaseSchema):
    # Order swagger.json

    
    conditions = fields.Nested(TransitionConfigCondition, required=False)
    
    configs = fields.List(fields.Nested(Config, required=False), required=False)
    


class TransitionConfigPayload(BaseSchema):
    # Order swagger.json

    
    data = fields.Nested(TransitionConfigData, required=False)
    


class CommonErrorResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    


class ExceptionErrorResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    


class ProductDetails(BaseSchema):
    # Order swagger.json

    
    identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    line_number = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    


class RePromise(BaseSchema):
    # Order swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class PackagingDimensions(BaseSchema):
    # Order swagger.json

    
    width = fields.Float(required=False)
    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    weight = fields.Float(required=False)
    
    packaging_type = fields.Str(required=False)
    


class ConsolidateShipmentPayload(BaseSchema):
    # Order swagger.json

    
    consolidated_shipment_id = fields.Str(required=False)
    
    products = fields.List(fields.Nested(ProductDetails, required=False), required=False)
    
    revise_promise = fields.Nested(RePromise, required=False)
    
    packaging_dimensions = fields.Nested(PackagingDimensions, required=False)
    


class ConsolidateShipmentResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    


class Page(BaseSchema):
    # Order swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


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
    


class ShipmentStatus(BaseSchema):
    # Order swagger.json

    
    current_shipment_status = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    shipment_status_id = fields.Int(required=False, allow_none=True)
    
    bag_list = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    created_at = fields.Str(required=False, allow_none=True)
    
    created_ts = fields.Str(required=False, allow_none=True)
    
    shipment_id = fields.Str(required=False, allow_none=True)
    
    status_created_at = fields.Str(required=False, allow_none=True)
    
    status_created_ts = fields.Str(required=False, allow_none=True)
    
    status = fields.Str(required=False, allow_none=True)
    


class UserDataInfo(BaseSchema):
    # Order swagger.json

    
    uid = fields.Int(required=False, allow_none=True)
    
    user_oid = fields.Str(required=False, allow_none=True)
    
    external_customer_id = fields.Str(required=False, allow_none=True)
    
    first_name = fields.Str(required=False, allow_none=True)
    
    last_name = fields.Str(required=False, allow_none=True)
    
    mobile = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False, allow_none=True)
    
    is_anonymous_user = fields.Boolean(required=False, allow_none=True)
    
    avis_user_id = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    gender = fields.Str(required=False, allow_none=True)
    


class Address(BaseSchema):
    # Order swagger.json

    
    phone = fields.Str(required=False, allow_none=True)
    
    address2 = fields.Str(required=False, allow_none=True)
    
    longitude = fields.Int(required=False, allow_none=True)
    
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
    
    latitude = fields.Int(required=False, allow_none=True)
    
    contact_person = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False, allow_none=True)
    
    city = fields.Str(required=False, allow_none=True)
    


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
    
    name = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False, allow_none=True)
    
    amount = fields.Nested(ChargeAmount, required=False)
    
    distribution_logic = fields.Nested(ChargeDistributionLogic, required=False)
    


class Identifier(BaseSchema):
    # Order swagger.json

    
    alu = fields.Str(required=False, allow_none=True)
    
    ean = fields.Str(required=False, allow_none=True)
    
    sku_code = fields.Str(required=False, allow_none=True)
    
    upc = fields.Str(required=False, allow_none=True)
    
    isbn = fields.Str(required=False, allow_none=True)
    


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
    
    state_type = fields.Str(required=False, allow_none=True)
    
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

    
    child_details = fields.Dict(required=False, allow_none=True)
    
    seller_identifier = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    a_set = fields.Dict(required=False, allow_none=True)
    
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
    
    variants = fields.Dict(required=False, allow_none=True)
    


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
    
    loyalty_discount = fields.Float(required=False, allow_none=True)
    
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
    
    loyalty_discount = fields.Float(required=False, allow_none=True)
    


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
    
    variants = fields.Dict(required=False, allow_none=True)
    


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
    
    company_id = fields.Int(required=False)
    


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
    
    is_active = fields.Boolean(required=False)
    
    channel = fields.Nested(ShipmentListingChannel, required=False)
    
    previous_shipment_id = fields.Str(required=False, allow_none=True)
    
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
    
    order_id = fields.Str(required=False)
    
    ordering_channnel = fields.Str(required=False, allow_none=True)
    
    shipment_id = fields.Str(required=False, allow_none=True)
    
    customer_note = fields.Str(required=False, allow_none=True)
    
    total_bags = fields.Int(required=False, allow_none=True)
    
    shipment_created_at = fields.Str(required=False)
    
    mode_of_payment = fields.Str(required=False)
    
    shipment_created_ts = fields.Str(required=False)
    
    currency = fields.Nested(Currency, required=False)
    
    currency_info = fields.Nested(CurrencyInfo, required=False)
    
    logistics_meta = fields.Dict(required=False, allow_none=True)
    
    affiliate_shipment_id = fields.Str(required=False, allow_none=True)
    
    affiliate_order_id = fields.Str(required=False, allow_none=True)
    


class ShipmentInternalPlatformViewResponse(BaseSchema):
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
    
    address = fields.Str(required=False, allow_none=True)
    
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
    


class AffiliateConfig(BaseSchema):
    # Order swagger.json

    
    app_company_id = fields.Int(required=False, allow_none=True)
    


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
    
    ad_id = fields.Str(required=False, allow_none=True)
    


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
    
    variants = fields.Dict(required=False, allow_none=True)
    


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
    
    quantity = fields.Float(required=False, allow_none=True)
    
    identifier = fields.Str(required=False, allow_none=True)
    
    can_return = fields.Boolean(required=False, allow_none=True)
    
    can_cancel = fields.Boolean(required=False, allow_none=True)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    line_number = fields.Int(required=False, allow_none=True)
    
    meta = fields.Dict(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    charges = fields.List(fields.Nested(PriceAdjustmentCharge, required=False), required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    bag_id = fields.Int(required=False)
    
    entity_type = fields.Str(required=False, allow_none=True)
    
    is_parent = fields.Boolean(required=False, allow_none=True)
    
    variants = fields.Dict(required=False, allow_none=True)
    


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
    


class ShipmentPaymentInfoData(BaseSchema):
    # Order swagger.json

    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    collect_by = fields.Str(required=False)
    
    refund_by = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    amount = fields.Float(required=False)
    
    unique_identifier = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    transaction_data = fields.Dict(required=False)
    


class PlatformShipment(BaseSchema):
    # Order swagger.json

    
    logistics_meta = fields.Dict(required=False, allow_none=True)
    
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
    
    lock_status = fields.Boolean(required=False, allow_none=True)
    
    platform_logo = fields.Str(required=False, allow_none=True)
    
    user_agent = fields.Str(required=False, allow_none=True)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    invoice_id = fields.Str(required=False, allow_none=True)
    
    payment_methods = fields.Dict(required=False, allow_none=True)
    
    payment_info = fields.List(fields.Nested(ShipmentPaymentInfoData, required=False), required=False)
    
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
    
    affiliate_shipment_id = fields.Str(required=False, allow_none=True)
    
    tracking_url = fields.Str(required=False, allow_none=True)
    


class ShipmentInfoResponse(BaseSchema):
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
    
    transaction_data = fields.Dict(required=False)
    


class OrderDetailsResponse(BaseSchema):
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
    


class LaneConfigResponse(BaseSchema):
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
    
    affiliate_order_id = fields.Str(required=False, allow_none=True)
    


class OrderListingResponse(BaseSchema):
    # Order swagger.json

    
    filters = fields.Nested(Filters, required=False)
    
    total_count = fields.Int(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False, allow_none=True)
    
    items = fields.List(fields.Nested(PlatformOrderItems, required=False), required=False)
    
    lane = fields.Str(required=False, allow_none=True)
    
    page = fields.Nested(Page, required=False)
    


class PlatformTrack(BaseSchema):
    # Order swagger.json

    
    last_location_recieved_at = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    raw_status = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_time = fields.Str(required=False)
    
    awb = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
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
    


class FilterOptions(BaseSchema):
    # Order swagger.json

    
    label = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    state_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    min_search_size = fields.Int(required=False)
    
    placeholder_text = fields.Str(required=False)
    
    show_ui = fields.Boolean(required=False)
    


class FiltersList(BaseSchema):
    # Order swagger.json

    
    label = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    filter_type = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    placeholder_text = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    options = fields.List(fields.Nested(FilterOptions, required=False), required=False)
    


class GlobalFiltersResponse(BaseSchema):
    # Order swagger.json

    
    config = fields.Str(required=False)
    
    filters = fields.List(fields.Nested(FiltersList, required=False), required=False)
    
    company_id = fields.Int(required=False, allow_none=True)
    
    show_in = fields.Str(required=False)
    
    request_source = fields.Str(required=False)
    


class ViewDetails(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    filters = fields.List(fields.Nested(FiltersList, required=False), required=False)
    
    is_editable = fields.Boolean(required=False)
    
    position = fields.Int(required=False)
    
    show_in = fields.Str(required=False)
    


class ParentViews(BaseSchema):
    # Order swagger.json

    
    views = fields.List(fields.Nested(ViewDetails, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    is_editable = fields.Boolean(required=False)
    
    position = fields.Int(required=False)
    
    show_in = fields.Str(required=False)
    


class UserViewsResponse(BaseSchema):
    # Order swagger.json

    
    parent_views = fields.List(fields.Nested(ParentViews, required=False), required=False)
    


class UserViewPosition(BaseSchema):
    # Order swagger.json

    
    view_type = fields.Str(required=False)
    
    view_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    new_position = fields.Int(required=False)
    
    show_in = fields.Str(required=False)
    


class CreateUpdateDeleteResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    errors = fields.List(fields.Str(required=False), required=False)
    


class FiltersResponse(BaseSchema):
    # Order swagger.json

    
    advance_filter = fields.Nested(AdvanceFilterInfo, required=False)
    
    global_filter = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    


class URL(BaseSchema):
    # Order swagger.json

    
    url = fields.Str(required=False)
    


class FileResponse(BaseSchema):
    # Order swagger.json

    
    file_name = fields.Str(required=False)
    
    cdn = fields.Nested(URL, required=False)
    


class BulkActionTemplate(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False)
    
    text = fields.Str(required=False)
    


class BulkActionTemplateResponse(BaseSchema):
    # Order swagger.json

    
    template_x_slug = fields.List(fields.Nested(BulkActionTemplate, required=False), required=False)
    


class PlatformShipmentReasonsResponse(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(Reason, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ShipmentResponseReasons(BaseSchema):
    # Order swagger.json

    
    reason_id = fields.Int(required=False)
    
    reason = fields.Str(required=False)
    


class ShipmentReasonsResponse(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(ShipmentResponseReasons, required=False), required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class StoreAddress(BaseSchema):
    # Order swagger.json

    
    phone = fields.Str(required=False, allow_none=True)
    
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
    
    ds_type = fields.Str(required=False)
    
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
    
    address1 = fields.Str(required=False, allow_none=True)
    
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
    


class Attributes(BaseSchema):
    # Order swagger.json

    
    primary_material = fields.Str(required=False, allow_none=True)
    
    essential = fields.Str(required=False, allow_none=True)
    
    marketer_name = fields.Str(required=False, allow_none=True)
    
    primary_color = fields.Str(required=False, allow_none=True)
    
    marketer_address = fields.Str(required=False, allow_none=True)
    
    primary_color_hex = fields.Str(required=False, allow_none=True)
    
    brand_name = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    gender = fields.List(fields.Str(required=False), required=False)
    


class Item(BaseSchema):
    # Order swagger.json

    
    attributes = fields.Nested(Attributes, required=False)
    
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
    


class ShipmentDetails(BaseSchema):
    # Order swagger.json

    
    dp_id = fields.Str(required=False, allow_none=True)
    
    dp_options = fields.Dict(required=False, allow_none=True)
    
    lock_status = fields.Boolean(required=False, allow_none=True)
    
    action_to_status = fields.Dict(required=False, allow_none=True)
    


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
    


class BagDetailsPlatformResponse(BaseSchema):
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
    


class GetBagsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    status_code = fields.Int(required=False)
    
    data = fields.Nested(BagData, required=False)
    


class GeneratePosOrderReceiptResponse(BaseSchema):
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
    


class AllowedTemplatesResponse(BaseSchema):
    # Order swagger.json

    
    template_x_slug = fields.List(fields.Nested(Templates, required=False), required=False)
    


class CDN(BaseSchema):
    # Order swagger.json

    
    url = fields.Str(required=False)
    
    absolute_url = fields.Str(required=False)
    
    relative_url = fields.Str(required=False)
    


class Upload(BaseSchema):
    # Order swagger.json

    
    expiry = fields.Int(required=False)
    
    url = fields.Str(required=False)
    


class TemplateDownloadResponse(BaseSchema):
    # Order swagger.json

    
    file_name = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    upload = fields.Nested(Upload, required=False)
    
    cdn = fields.Nested(CDN, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


