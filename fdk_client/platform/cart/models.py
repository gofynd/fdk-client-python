"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class IdentifierSchema(BaseSchema):
    pass


class CouponDateMetaSchema(BaseSchema):
    pass


class UsesRemainingSchema(BaseSchema):
    pass


class UsesRestrictionSchema(BaseSchema):
    pass


class PriceRangeSchema(BaseSchema):
    pass


class PostOrderSchema(BaseSchema):
    pass


class BulkBundleRestriction(BaseSchema):
    pass


class PaymentAllowValueSchema(BaseSchema):
    pass


class PaymentModesSchema(BaseSchema):
    pass


class RestrictionsSchema(BaseSchema):
    pass


class StateSchema(BaseSchema):
    pass


class RuleDefinitionSchema(BaseSchema):
    pass


class RuleSchema(BaseSchema):
    pass


class CouponScheduleSchema(BaseSchema):
    pass


class CouponActionSchema(BaseSchema):
    pass


class DisplayMetaDictSchema(BaseSchema):
    pass


class DisplayMetaSchema(BaseSchema):
    pass


class OwnershipSchema(BaseSchema):
    pass


class ValidationSchema(BaseSchema):
    pass


class CouponAuthorSchema(BaseSchema):
    pass


class ValiditySchema(BaseSchema):
    pass


class CouponAddSchema(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class CouponsResponse(BaseSchema):
    pass


class SuccessMessage(BaseSchema):
    pass


class OperationErrorResponse(BaseSchema):
    pass


class CouponUpdateSchema(BaseSchema):
    pass


class CouponPartialUpdate(BaseSchema):
    pass


class PromotionDateMetaSchema(BaseSchema):
    pass


class PromotionScheduleSchema(BaseSchema):
    pass


class CompareObjectSchema(BaseSchema):
    pass


class ItemCriteriaSchema(BaseSchema):
    pass


class DiscountOfferSchema(BaseSchema):
    pass


class DiscountRuleSchema(BaseSchema):
    pass


class UsesRemainingSchema1(BaseSchema):
    pass


class UsesRestrictionSchema1(BaseSchema):
    pass


class PaymentAllowValueSchema1(BaseSchema):
    pass


class PromotionPaymentModesSchema(BaseSchema):
    pass


class PostOrderSchema1(BaseSchema):
    pass


class UserRegisteredSchema(BaseSchema):
    pass


class RestrictionsSchema1(BaseSchema):
    pass


class PromotionAuthorSchema(BaseSchema):
    pass


class DisplayMetaSchema1(BaseSchema):
    pass


class VisibilitySchema(BaseSchema):
    pass


class OwnershipSchema1(BaseSchema):
    pass


class PromotionActionSchema(BaseSchema):
    pass


class PromotionListItem(BaseSchema):
    pass


class PromotionsResponse(BaseSchema):
    pass


class PromotionAddSchema(BaseSchema):
    pass


class PromotionUpdateSchema(BaseSchema):
    pass


class PromotionPartialUpdate(BaseSchema):
    pass


class ActivePromosResponse(BaseSchema):
    pass


class CartItemSchema(BaseSchema):
    pass


class OpenapiCartDetailsRequest(BaseSchema):
    pass


class DisplayBreakupSchema(BaseSchema):
    pass


class LoyaltyPoints(BaseSchema):
    pass


class RawBreakupSchema(BaseSchema):
    pass


class CouponBreakupSchema(BaseSchema):
    pass


class CartBreakupSchema(BaseSchema):
    pass


class CartProductIdentifer(BaseSchema):
    pass


class ProductAvailabilitySize(BaseSchema):
    pass


class ProductAvailability(BaseSchema):
    pass


class FreeGiftItemSchema(BaseSchema):
    pass


class AppliedFreeArticlesSchema(BaseSchema):
    pass


class BuyRulesSchema(BaseSchema):
    pass


class Ownership(BaseSchema):
    pass


class DiscountRulesAppSchema(BaseSchema):
    pass


class AppliedPromotion(BaseSchema):
    pass


class PromoMeta(BaseSchema):
    pass


class ProductPrice(BaseSchema):
    pass


class ProductPriceInfo(BaseSchema):
    pass


class PromiseTimestamp(BaseSchema):
    pass


class PromiseFormatted(BaseSchema):
    pass


class ShipmentPromise(BaseSchema):
    pass


class BaseInfo(BaseSchema):
    pass


class ActionQuery(BaseSchema):
    pass


class ProductAction(BaseSchema):
    pass


class ProductImage(BaseSchema):
    pass


class CategoryInfo(BaseSchema):
    pass


class NetQuantity(BaseSchema):
    pass


class CartProduct(BaseSchema):
    pass


class BasePriceSchema(BaseSchema):
    pass


class ArticlePriceInfo(BaseSchema):
    pass


class ProductArticle(BaseSchema):
    pass


class CartProductInfo(BaseSchema):
    pass


class OpenapiCartDetailsResponse(BaseSchema):
    pass


class OpenApiErrorResponse(BaseSchema):
    pass


class ShippingAddressSchema(BaseSchema):
    pass


class OpenApiCartServiceabilityRequest(BaseSchema):
    pass


class OpenApiCartServiceabilityResponse(BaseSchema):
    pass


class MultiTenderPaymentMeta(BaseSchema):
    pass


class MultiTenderPaymentMethod(BaseSchema):
    pass


class OpenApiFilesSchema(BaseSchema):
    pass


class CartItemMeta(BaseSchema):
    pass


class OpenApiOrderItemSchema(BaseSchema):
    pass


class OpenApiPlatformCheckoutReqSchema(BaseSchema):
    pass


class OpenApiCheckoutResponse(BaseSchema):
    pass


class AbandonedCart(BaseSchema):
    pass


class AbandonedCartResponseSchema(BaseSchema):
    pass


class PaymentSelectionLock(BaseSchema):
    pass


class CartCurrencySchema(BaseSchema):
    pass


class CartDetailResponse(BaseSchema):
    pass


class AddProductCart(BaseSchema):
    pass


class AddCartRequest(BaseSchema):
    pass


class AddCartDetailResponse(BaseSchema):
    pass


class UpdateProductCart(BaseSchema):
    pass


class UpdateCartRequest(BaseSchema):
    pass


class UpdateCartDetailResponse(BaseSchema):
    pass


class GetShareCartLinkRequest(BaseSchema):
    pass


class GetShareCartLinkResponse(BaseSchema):
    pass


class SharedCartDetails(BaseSchema):
    pass


class SharedCart(BaseSchema):
    pass


class SharedCartResponse(BaseSchema):
    pass


class CartListSchema(BaseSchema):
    pass


class MultiCartResponseSchema(BaseSchema):
    pass


class UpdateUserCartMapping(BaseSchema):
    pass


class UserInfoSchema(BaseSchema):
    pass


class UserCartMappingResponse(BaseSchema):
    pass


class DeleteCartRequest(BaseSchema):
    pass


class DeleteCartDetailResponse(BaseSchema):
    pass


class CartItemCountResponse(BaseSchema):
    pass


class Coupon(BaseSchema):
    pass


class PageCouponSchema(BaseSchema):
    pass


class GetCouponResponse(BaseSchema):
    pass


class ApplyCouponRequest(BaseSchema):
    pass


class GeoLocation(BaseSchema):
    pass


class PlatformAddress(BaseSchema):
    pass


class PlatformGetAddressesResponse(BaseSchema):
    pass


class SaveAddressResponse(BaseSchema):
    pass


class UpdateAddressResponse(BaseSchema):
    pass


class DeleteAddressResponse(BaseSchema):
    pass


class PlatformSelectCartAddressRequest(BaseSchema):
    pass


class ShipmentResponse(BaseSchema):
    pass


class CartShipmentsResponse(BaseSchema):
    pass


class UpdateCartShipmentItem(BaseSchema):
    pass


class UpdateCartShipmentRequest(BaseSchema):
    pass


class PlatformCartMetaRequest(BaseSchema):
    pass


class CartMetaResponse(BaseSchema):
    pass


class CartMetaMissingResponse(BaseSchema):
    pass


class FilesSchema(BaseSchema):
    pass


class StaffCheckoutSchema(BaseSchema):
    pass


class PlatformCartCheckoutDetailRequest(BaseSchema):
    pass


class CheckCartSchema(BaseSchema):
    pass


class CartCheckoutResponseSchema(BaseSchema):
    pass


class CartDeliveryModesResponse(BaseSchema):
    pass


class PickupStoreDetail(BaseSchema):
    pass


class StoreDetailsResponse(BaseSchema):
    pass


class UpdateCartPaymentRequest(BaseSchema):
    pass


class CouponValidity(BaseSchema):
    pass


class PaymentCouponValidateSchema(BaseSchema):
    pass


class PaymentMetaSchema(BaseSchema):
    pass


class PaymentMethodSchema(BaseSchema):
    pass


class PlatformCartCheckoutDetailV2Request(BaseSchema):
    pass


class UpdateCartPaymentRequestV2(BaseSchema):
    pass





class IdentifierSchema(BaseSchema):
    # Cart swagger.json

    
    exclude_brand_id = fields.List(fields.Int(required=False), required=False)
    
    category_id = fields.List(fields.Int(required=False), required=False)
    
    item_id = fields.List(fields.Int(required=False), required=False)
    
    store_id = fields.List(fields.Int(required=False), required=False)
    
    article_id = fields.List(fields.Str(required=False), required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    collection_id = fields.List(fields.Str(required=False), required=False)
    
    brand_id = fields.List(fields.Int(required=False), required=False)
    
    company_id = fields.List(fields.Int(required=False), required=False)
    


class CouponDateMetaSchema(BaseSchema):
    # Cart swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class UsesRemainingSchema(BaseSchema):
    # Cart swagger.json

    
    app = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    user = fields.Int(required=False)
    


class UsesRestrictionSchema(BaseSchema):
    # Cart swagger.json

    
    maximum = fields.Nested(UsesRemainingSchema, required=False)
    
    remaining = fields.Nested(UsesRemainingSchema, required=False)
    


class PriceRangeSchema(BaseSchema):
    # Cart swagger.json

    
    max = fields.Int(required=False)
    
    min = fields.Int(required=False)
    


class PostOrderSchema(BaseSchema):
    # Cart swagger.json

    
    return_allowed = fields.Boolean(required=False)
    
    cancellation_allowed = fields.Boolean(required=False)
    


class BulkBundleRestriction(BaseSchema):
    # Cart swagger.json

    
    multi_store_allowed = fields.Boolean(required=False)
    


class PaymentAllowValueSchema(BaseSchema):
    # Cart swagger.json

    
    max = fields.Int(required=False)
    


class PaymentModesSchema(BaseSchema):
    # Cart swagger.json

    
    types = fields.List(fields.Str(required=False), required=False)
    
    codes = fields.List(fields.Str(required=False), required=False)
    
    uses = fields.Nested(PaymentAllowValueSchema, required=False)
    
    networks = fields.List(fields.Str(required=False), required=False)
    


class RestrictionsSchema(BaseSchema):
    # Cart swagger.json

    
    coupon_allowed = fields.Boolean(required=False)
    
    uses = fields.Nested(UsesRestrictionSchema, required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    price_range = fields.Nested(PriceRangeSchema, required=False)
    
    post_order = fields.Nested(PostOrderSchema, required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    user_type = fields.Str(required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    payments = fields.Dict(required=False)
    


class StateSchema(BaseSchema):
    # Cart swagger.json

    
    is_display = fields.Boolean(required=False)
    
    is_public = fields.Boolean(required=False)
    
    is_archived = fields.Boolean(required=False)
    


class RuleDefinitionSchema(BaseSchema):
    # Cart swagger.json

    
    is_exact = fields.Boolean(required=False)
    
    value_type = fields.Str(required=False)
    
    applicable_on = fields.Str(required=False)
    
    scope = fields.List(fields.Str(required=False), required=False)
    
    currency_code = fields.Str(required=False)
    
    calculate_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    auto_apply = fields.Boolean(required=False)
    


class RuleSchema(BaseSchema):
    # Cart swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    
    discount_qty = fields.Float(required=False)
    
    value = fields.Float(required=False)
    
    key = fields.Float(required=False)
    


class CouponScheduleSchema(BaseSchema):
    # Cart swagger.json

    
    end = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    cron = fields.Str(required=False)
    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    
    duration = fields.Int(required=False)
    


class CouponActionSchema(BaseSchema):
    # Cart swagger.json

    
    txn_mode = fields.Str(required=False)
    
    action_date = fields.Str(required=False)
    


class DisplayMetaDictSchema(BaseSchema):
    # Cart swagger.json

    
    title = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    


class DisplayMetaSchema(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    remove = fields.Nested(DisplayMetaDictSchema, required=False)
    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    apply = fields.Nested(DisplayMetaDictSchema, required=False)
    
    auto = fields.Nested(DisplayMetaDictSchema, required=False)
    


class OwnershipSchema(BaseSchema):
    # Cart swagger.json

    
    payable_by = fields.Str(required=False)
    
    payable_category = fields.Str(required=False)
    


class ValidationSchema(BaseSchema):
    # Cart swagger.json

    
    anonymous = fields.Boolean(required=False)
    
    app_id = fields.List(fields.Str(required=False), required=False)
    
    user_registered_after = fields.Str(required=False)
    


class CouponAuthorSchema(BaseSchema):
    # Cart swagger.json

    
    modified_by = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    


class ValiditySchema(BaseSchema):
    # Cart swagger.json

    
    priority = fields.Int(required=False)
    


class CouponAddSchema(BaseSchema):
    # Cart swagger.json

    
    identifiers = fields.Nested(IdentifierSchema, required=False)
    
    date_meta = fields.Nested(CouponDateMetaSchema, required=False)
    
    restrictions = fields.Nested(RestrictionsSchema, required=False)
    
    state = fields.Nested(StateSchema, required=False)
    
    rule_definition = fields.Nested(RuleDefinitionSchema, required=False)
    
    rule = fields.List(fields.Nested(RuleSchema, required=False), required=False)
    
    code = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponScheduleSchema, required=False)
    
    action = fields.Nested(CouponActionSchema, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMetaSchema, required=False)
    
    ownership = fields.Nested(OwnershipSchema, required=False)
    
    validation = fields.Nested(ValidationSchema, required=False)
    
    author = fields.Nested(CouponAuthorSchema, required=False)
    
    validity = fields.Nested(ValiditySchema, required=False)
    


class Page(BaseSchema):
    # Cart swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class CouponsResponse(BaseSchema):
    # Cart swagger.json

    
    items = fields.Nested(CouponAddSchema, required=False)
    
    page = fields.Nested(Page, required=False)
    


class SuccessMessage(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class OperationErrorResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class CouponUpdateSchema(BaseSchema):
    # Cart swagger.json

    
    identifiers = fields.Nested(IdentifierSchema, required=False)
    
    date_meta = fields.Nested(CouponDateMetaSchema, required=False)
    
    restrictions = fields.Nested(RestrictionsSchema, required=False)
    
    state = fields.Nested(StateSchema, required=False)
    
    rule_definition = fields.Nested(RuleDefinitionSchema, required=False)
    
    rule = fields.List(fields.Nested(RuleSchema, required=False), required=False)
    
    code = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponScheduleSchema, required=False)
    
    action = fields.Nested(CouponActionSchema, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMetaSchema, required=False)
    
    ownership = fields.Nested(OwnershipSchema, required=False)
    
    validation = fields.Nested(ValidationSchema, required=False)
    
    author = fields.Nested(CouponAuthorSchema, required=False)
    
    validity = fields.Nested(ValiditySchema, required=False)
    


class CouponPartialUpdate(BaseSchema):
    # Cart swagger.json

    
    archive = fields.Boolean(required=False)
    
    schedule = fields.Nested(CouponScheduleSchema, required=False)
    


class PromotionDateMetaSchema(BaseSchema):
    # Cart swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class PromotionScheduleSchema(BaseSchema):
    # Cart swagger.json

    
    end = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    cron = fields.Str(required=False)
    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    
    duration = fields.Int(required=False)
    
    published = fields.Boolean(required=False)
    


class CompareObjectSchema(BaseSchema):
    # Cart swagger.json

    
    less_than = fields.Float(required=False)
    
    less_than_equals = fields.Float(required=False)
    
    greater_than_equals = fields.Float(required=False)
    
    equals = fields.Float(required=False)
    
    greater_than = fields.Float(required=False)
    


class ItemCriteriaSchema(BaseSchema):
    # Cart swagger.json

    
    available_zones = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_company = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_category = fields.List(fields.Int(required=False), required=False)
    
    all_items = fields.Boolean(required=False)
    
    item_brand = fields.List(fields.Int(required=False), required=False)
    
    cart_unique_item_amount = fields.Nested(CompareObjectSchema, required=False)
    
    item_category = fields.List(fields.Int(required=False), required=False)
    
    product_tags = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_sku = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_store = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_brand = fields.List(fields.Int(required=False), required=False)
    
    item_store = fields.List(fields.Int(required=False), required=False)
    
    buy_rules = fields.List(fields.Str(required=False), required=False)
    
    cart_total = fields.Nested(CompareObjectSchema, required=False)
    
    item_sku = fields.List(fields.Str(required=False), required=False)
    
    item_company = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_id = fields.List(fields.Int(required=False), required=False)
    
    cart_quantity = fields.Nested(CompareObjectSchema, required=False)
    
    cart_unique_item_quantity = fields.Nested(CompareObjectSchema, required=False)
    
    item_size = fields.List(fields.Str(required=False), required=False)
    
    item_id = fields.List(fields.Int(required=False), required=False)
    


class DiscountOfferSchema(BaseSchema):
    # Cart swagger.json

    
    apportion_discount = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    min_offer_quantity = fields.Int(required=False)
    
    max_discount_amount = fields.Float(required=False)
    
    partial_can_ret = fields.Boolean(required=False)
    
    discount_amount = fields.Float(required=False)
    
    max_usage_per_transaction = fields.Int(required=False)
    
    discount_percentage = fields.Float(required=False)
    
    max_offer_quantity = fields.Int(required=False)
    
    discount_price = fields.Float(required=False)
    


class DiscountRuleSchema(BaseSchema):
    # Cart swagger.json

    
    discount_type = fields.Str(required=False)
    
    item_criteria = fields.Nested(ItemCriteriaSchema, required=False)
    
    buy_condition = fields.Str(required=False)
    
    offer = fields.Nested(DiscountOfferSchema, required=False)
    


class UsesRemainingSchema1(BaseSchema):
    # Cart swagger.json

    
    total = fields.Int(required=False)
    
    user = fields.Int(required=False)
    


class UsesRestrictionSchema1(BaseSchema):
    # Cart swagger.json

    
    maximum = fields.Nested(UsesRemainingSchema1, required=False)
    
    remaining = fields.Nested(UsesRemainingSchema1, required=False)
    


class PaymentAllowValueSchema1(BaseSchema):
    # Cart swagger.json

    
    max = fields.Int(required=False)
    


class PromotionPaymentModesSchema(BaseSchema):
    # Cart swagger.json

    
    type = fields.Str(required=False)
    
    codes = fields.List(fields.Str(required=False), required=False)
    
    uses = fields.Nested(PaymentAllowValueSchema1, required=False)
    


class PostOrderSchema1(BaseSchema):
    # Cart swagger.json

    
    return_allowed = fields.Boolean(required=False)
    
    cancellation_allowed = fields.Boolean(required=False)
    


class UserRegisteredSchema(BaseSchema):
    # Cart swagger.json

    
    end = fields.Str(required=False)
    
    start = fields.Str(required=False)
    


class RestrictionsSchema1(BaseSchema):
    # Cart swagger.json

    
    uses = fields.Nested(UsesRestrictionSchema1, required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    payments = fields.List(fields.Nested(PromotionPaymentModesSchema, required=False), required=False)
    
    post_order = fields.Nested(PostOrderSchema1, required=False)
    
    order_quantity = fields.Int(required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    anonymous_users = fields.Boolean(required=False)
    
    user_registered = fields.Nested(UserRegisteredSchema, required=False)
    


class PromotionAuthorSchema(BaseSchema):
    # Cart swagger.json

    
    modified_by = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    


class DisplayMetaSchema1(BaseSchema):
    # Cart swagger.json

    
    offer_text = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    offer_label = fields.Str(required=False)
    


class VisibilitySchema(BaseSchema):
    # Cart swagger.json

    
    pdp = fields.Boolean(required=False)
    
    coupon_list = fields.Boolean(required=False)
    


class OwnershipSchema1(BaseSchema):
    # Cart swagger.json

    
    payable_by = fields.Str(required=False)
    
    payable_category = fields.Str(required=False)
    


class PromotionActionSchema(BaseSchema):
    # Cart swagger.json

    
    action_date = fields.Str(required=False)
    
    action_type = fields.Str(required=False)
    


class PromotionListItem(BaseSchema):
    # Cart swagger.json

    
    date_meta = fields.Nested(PromotionDateMetaSchema, required=False)
    
    stackable = fields.Boolean(required=False)
    
    application_id = fields.Str(required=False)
    
    _schedule = fields.Nested(PromotionScheduleSchema, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRuleSchema, required=False), required=False)
    
    restrictions = fields.Nested(RestrictionsSchema1, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    author = fields.Nested(PromotionAuthorSchema, required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    display_meta = fields.Nested(DisplayMetaSchema1, required=False)
    
    mode = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    apply_priority = fields.Int(required=False)
    
    visiblility = fields.Nested(VisibilitySchema, required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    ownership = fields.Nested(OwnershipSchema1, required=False)
    
    promo_group = fields.Str(required=False)
    
    calculate_on = fields.Str(required=False)
    
    post_order_action = fields.Nested(PromotionActionSchema, required=False)
    


class PromotionsResponse(BaseSchema):
    # Cart swagger.json

    
    items = fields.Nested(PromotionListItem, required=False)
    
    page = fields.Nested(Page, required=False)
    


class PromotionAddSchema(BaseSchema):
    # Cart swagger.json

    
    date_meta = fields.Nested(PromotionDateMetaSchema, required=False)
    
    stackable = fields.Boolean(required=False)
    
    application_id = fields.Str(required=False)
    
    _schedule = fields.Nested(PromotionScheduleSchema, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRuleSchema, required=False), required=False)
    
    restrictions = fields.Nested(RestrictionsSchema1, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    author = fields.Nested(PromotionAuthorSchema, required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    display_meta = fields.Nested(DisplayMetaSchema1, required=False)
    
    mode = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    apply_priority = fields.Int(required=False)
    
    visiblility = fields.Nested(VisibilitySchema, required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    ownership = fields.Nested(OwnershipSchema1, required=False)
    
    promo_group = fields.Str(required=False)
    
    calculate_on = fields.Str(required=False)
    
    post_order_action = fields.Nested(PromotionActionSchema, required=False)
    


class PromotionUpdateSchema(BaseSchema):
    # Cart swagger.json

    
    date_meta = fields.Nested(PromotionDateMetaSchema, required=False)
    
    stackable = fields.Boolean(required=False)
    
    application_id = fields.Str(required=False)
    
    _schedule = fields.Nested(PromotionScheduleSchema, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRuleSchema, required=False), required=False)
    
    restrictions = fields.Nested(RestrictionsSchema1, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    author = fields.Nested(PromotionAuthorSchema, required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    display_meta = fields.Nested(DisplayMetaSchema1, required=False)
    
    mode = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    apply_priority = fields.Int(required=False)
    
    visiblility = fields.Nested(VisibilitySchema, required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    ownership = fields.Nested(OwnershipSchema1, required=False)
    
    promo_group = fields.Str(required=False)
    
    calculate_on = fields.Str(required=False)
    
    post_order_action = fields.Nested(PromotionActionSchema, required=False)
    


class PromotionPartialUpdate(BaseSchema):
    # Cart swagger.json

    
    archive = fields.Boolean(required=False)
    
    schedule = fields.Nested(PromotionScheduleSchema, required=False)
    


class ActivePromosResponse(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    is_hidden = fields.Boolean(required=False)
    
    entity_type = fields.Str(required=False)
    
    example = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    entity_slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class CartItemSchema(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    product_id = fields.Str(required=False)
    


class OpenapiCartDetailsRequest(BaseSchema):
    # Cart swagger.json

    
    cart_items = fields.List(fields.Nested(CartItemSchema, required=False), required=False)
    


class DisplayBreakupSchema(BaseSchema):
    # Cart swagger.json

    
    display = fields.Str(required=False)
    
    message = fields.List(fields.Str(required=False), required=False)
    
    value = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class LoyaltyPoints(BaseSchema):
    # Cart swagger.json

    
    applicable = fields.Float(required=False)
    
    description = fields.Str(required=False)
    
    total = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    


class RawBreakupSchema(BaseSchema):
    # Cart swagger.json

    
    you_saved = fields.Float(required=False)
    
    vog = fields.Float(required=False)
    
    fynd_cash = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    coupon = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    cod_charge = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    gst_charges = fields.Float(required=False)
    
    mrp_total = fields.Float(required=False)
    
    subtotal = fields.Float(required=False)
    
    convenience_fee = fields.Float(required=False)
    


class CouponBreakupSchema(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    uid = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    type = fields.Str(required=False)
    
    coupon_type = fields.Str(required=False)
    
    sub_title = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    


class CartBreakupSchema(BaseSchema):
    # Cart swagger.json

    
    display = fields.List(fields.Nested(DisplayBreakupSchema, required=False), required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    raw = fields.Nested(RawBreakupSchema, required=False)
    
    coupon = fields.Nested(CouponBreakupSchema, required=False)
    


class CartProductIdentifer(BaseSchema):
    # Cart swagger.json

    
    identifier = fields.Str(required=False)
    


class ProductAvailabilitySize(BaseSchema):
    # Cart swagger.json

    
    display = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    


class ProductAvailability(BaseSchema):
    # Cart swagger.json

    
    available_sizes = fields.List(fields.Nested(ProductAvailabilitySize, required=False), required=False)
    
    deliverable = fields.Boolean(required=False)
    
    other_store_quantity = fields.Int(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    


class FreeGiftItemSchema(BaseSchema):
    # Cart swagger.json

    
    item_brand_name = fields.Str(required=False)
    
    item_name = fields.Str(required=False)
    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    
    item_price_details = fields.Dict(required=False)
    
    item_slug = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    


class AppliedFreeArticlesSchema(BaseSchema):
    # Cart swagger.json

    
    free_gift_item_details = fields.Nested(FreeGiftItemSchema, required=False)
    
    quantity = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    


class BuyRulesSchema(BaseSchema):
    # Cart swagger.json

    
    item_criteria = fields.Dict(required=False)
    
    cart_conditions = fields.Dict(required=False)
    


class Ownership(BaseSchema):
    # Cart swagger.json

    
    payable_by = fields.Str(required=False)
    
    payable_category = fields.Str(required=False)
    


class DiscountRulesAppSchema(BaseSchema):
    # Cart swagger.json

    
    item_criteria = fields.Dict(required=False)
    
    raw_offer = fields.Dict(required=False)
    
    offer = fields.Dict(required=False)
    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    


class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    mrp_promotion = fields.Boolean(required=False)
    
    offer_text = fields.Str(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticlesSchema, required=False), required=False)
    
    article_quantity = fields.Int(required=False)
    
    promotion_group = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
    promo_id = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRulesSchema, required=False), required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesAppSchema, required=False), required=False)
    
    promotion_type = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    


class PromoMeta(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    


class ProductPrice(BaseSchema):
    # Cart swagger.json

    
    effective = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    selling = fields.Float(required=False)
    
    add_on = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    


class ProductPriceInfo(BaseSchema):
    # Cart swagger.json

    
    converted = fields.Nested(ProductPrice, required=False)
    
    base = fields.Nested(ProductPrice, required=False)
    


class PromiseTimestamp(BaseSchema):
    # Cart swagger.json

    
    max = fields.Float(required=False)
    
    min = fields.Float(required=False)
    


class PromiseFormatted(BaseSchema):
    # Cart swagger.json

    
    max = fields.Str(required=False)
    
    min = fields.Str(required=False)
    


class ShipmentPromise(BaseSchema):
    # Cart swagger.json

    
    timestamp = fields.Nested(PromiseTimestamp, required=False)
    
    formatted = fields.Nested(PromiseFormatted, required=False)
    


class BaseInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class ActionQuery(BaseSchema):
    # Cart swagger.json

    
    product_slug = fields.List(fields.Str(required=False), required=False)
    


class ProductAction(BaseSchema):
    # Cart swagger.json

    
    type = fields.Str(required=False)
    
    query = fields.Nested(ActionQuery, required=False)
    
    url = fields.Str(required=False)
    


class ProductImage(BaseSchema):
    # Cart swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class CategoryInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class NetQuantity(BaseSchema):
    # Cart swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class CartProduct(BaseSchema):
    # Cart swagger.json

    
    item_code = fields.Str(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class BasePriceSchema(BaseSchema):
    # Cart swagger.json

    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class ArticlePriceInfo(BaseSchema):
    # Cart swagger.json

    
    converted = fields.Nested(BasePriceSchema, required=False)
    
    base = fields.Nested(BasePriceSchema, required=False)
    


class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    size = fields.Str(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    type = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    custom_order = fields.Dict(required=False)
    
    coupon_message = fields.Str(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    key = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    message = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    moq = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    


class OpenapiCartDetailsResponse(BaseSchema):
    # Cart swagger.json

    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class OpenApiErrorResponse(BaseSchema):
    # Cart swagger.json

    
    errors = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class ShippingAddressSchema(BaseSchema):
    # Cart swagger.json

    
    phone = fields.Int(required=False)
    
    address_type = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country_phone_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    area = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class OpenApiCartServiceabilityRequest(BaseSchema):
    # Cart swagger.json

    
    cart_items = fields.List(fields.Nested(CartItemSchema, required=False), required=False)
    
    shipping_address = fields.Nested(ShippingAddressSchema, required=False)
    


class OpenApiCartServiceabilityResponse(BaseSchema):
    # Cart swagger.json

    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    message = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    


class MultiTenderPaymentMeta(BaseSchema):
    # Cart swagger.json

    
    current_status = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    


class MultiTenderPaymentMethod(BaseSchema):
    # Cart swagger.json

    
    meta = fields.Nested(MultiTenderPaymentMeta, required=False)
    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    


class OpenApiFilesSchema(BaseSchema):
    # Cart swagger.json

    
    values = fields.List(fields.Str(required=False), required=False)
    
    key = fields.Str(required=False)
    


class CartItemMeta(BaseSchema):
    # Cart swagger.json

    
    primary_item = fields.Boolean(required=False)
    
    group_id = fields.Str(required=False)
    


class OpenApiOrderItemSchema(BaseSchema):
    # Cart swagger.json

    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    price_effective = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    employee_discount = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    quantity = fields.Int(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    files = fields.List(fields.Nested(OpenApiFilesSchema, required=False), required=False)
    
    extra_meta = fields.Dict(required=False)
    
    meta = fields.Nested(CartItemMeta, required=False)
    
    size = fields.Str(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    product_id = fields.Int(required=False)
    


class OpenApiPlatformCheckoutReqSchema(BaseSchema):
    # Cart swagger.json

    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    billing_address = fields.Nested(ShippingAddressSchema, required=False)
    
    employee_discount = fields.Dict(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    files = fields.List(fields.Nested(OpenApiFilesSchema, required=False), required=False)
    
    cart_value = fields.Float(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    shipping_address = fields.Nested(ShippingAddressSchema, required=False)
    
    comment = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    
    cod_charges = fields.Float(required=False)
    
    coupon = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    cart_items = fields.List(fields.Nested(OpenApiOrderItemSchema, required=False), required=False)
    
    delivery_charges = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    


class OpenApiCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    order_ref_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class AbandonedCart(BaseSchema):
    # Cart swagger.json

    
    payment_methods = fields.List(fields.Dict(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    expire_at = fields.Str(required=False)
    
    cod_charges = fields.Dict(required=False)
    
    order_id = fields.Str(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    shipments = fields.List(fields.Dict(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    delivery_charges = fields.Dict(required=False)
    
    bulk_coupon_discount = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    gstin = fields.Str(required=False)
    
    cart_value = fields.Float(required=False)
    
    promotion = fields.Dict(required=False)
    
    is_archive = fields.Boolean(required=False)
    
    user_id = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    
    fc_index_map = fields.List(fields.Int(required=False), required=False)
    
    comment = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    coupon = fields.Dict(required=False)
    
    fynd_credits = fields.Dict(required=False)
    
    merge_qty = fields.Boolean(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    cashback = fields.Dict(required=False)
    
    payments = fields.Dict(required=False)
    


class AbandonedCartResponseSchema(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(AbandonedCart, required=False), required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    result = fields.Dict(required=False)
    
    page = fields.Nested(Page, required=False)
    


class PaymentSelectionLock(BaseSchema):
    # Cart swagger.json

    
    default_options = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    


class CartCurrencySchema(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    


class CartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    pan_config = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    pan_no = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    currency = fields.Nested(CartCurrencySchema, required=False)
    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    comment = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    buy_now = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    


class AddProductCart(BaseSchema):
    # Cart swagger.json

    
    display = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    article_assignment = fields.Dict(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    pos = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    seller_id = fields.Int(required=False)
    
    parent_item_identifiers = fields.List(fields.Dict(required=False), required=False)
    
    item_size = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    


class AddCartRequest(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    
    new_cart = fields.Boolean(required=False)
    


class AddCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    partial = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    


class UpdateProductCart(BaseSchema):
    # Cart swagger.json

    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    item_index = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    article_id = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    item_size = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    


class UpdateCartRequest(BaseSchema):
    # Cart swagger.json

    
    operation = fields.Str(required=False)
    
    items = fields.List(fields.Nested(UpdateProductCart, required=False), required=False)
    


class UpdateCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    


class GetShareCartLinkRequest(BaseSchema):
    # Cart swagger.json

    
    meta = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    


class GetShareCartLinkResponse(BaseSchema):
    # Cart swagger.json

    
    token = fields.Str(required=False)
    
    share_url = fields.Str(required=False)
    


class SharedCartDetails(BaseSchema):
    # Cart swagger.json

    
    token = fields.Str(required=False)
    
    source = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    


class SharedCart(BaseSchema):
    # Cart swagger.json

    
    delivery_charge_info = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    cart_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    
    coupon_text = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    currency = fields.Nested(CartCurrencySchema, required=False)
    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    comment = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    buy_now = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    


class SharedCartResponse(BaseSchema):
    # Cart swagger.json

    
    error = fields.Str(required=False)
    
    cart = fields.Nested(SharedCart, required=False)
    


class CartListSchema(BaseSchema):
    # Cart swagger.json

    
    item_counts = fields.Int(required=False)
    
    cart_value = fields.Float(required=False)
    
    cart_id = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    


class MultiCartResponseSchema(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(CartListSchema, required=False), required=False)
    


class UpdateUserCartMapping(BaseSchema):
    # Cart swagger.json

    
    user_id = fields.Str(required=False)
    


class UserInfoSchema(BaseSchema):
    # Cart swagger.json

    
    mobile = fields.Str(required=False)
    
    external_id = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    


class UserCartMappingResponse(BaseSchema):
    # Cart swagger.json

    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    user = fields.Nested(UserInfoSchema, required=False)
    
    pan_config = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    pan_no = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    currency = fields.Nested(CartCurrencySchema, required=False)
    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    comment = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    buy_now = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    


class DeleteCartRequest(BaseSchema):
    # Cart swagger.json

    
    cart_id_list = fields.List(fields.Str(required=False), required=False)
    


class DeleteCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class CartItemCountResponse(BaseSchema):
    # Cart swagger.json

    
    user_cart_items_count = fields.Int(required=False)
    


class Coupon(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    expires_on = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    is_applicable = fields.Boolean(required=False)
    
    sub_title = fields.Str(required=False)
    
    coupon_type = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    


class PageCouponSchema(BaseSchema):
    # Cart swagger.json

    
    has_previous = fields.Boolean(required=False)
    
    total_item_count = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class GetCouponResponse(BaseSchema):
    # Cart swagger.json

    
    available_coupon_list = fields.List(fields.Nested(Coupon, required=False), required=False)
    
    page = fields.Nested(PageCouponSchema, required=False)
    


class ApplyCouponRequest(BaseSchema):
    # Cart swagger.json

    
    coupon_code = fields.Str(required=False)
    


class GeoLocation(BaseSchema):
    # Cart swagger.json

    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    


class PlatformAddress(BaseSchema):
    # Cart swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    created_by_user_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    address_type = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    geo_location = fields.Nested(GeoLocation, required=False)
    
    meta = fields.Dict(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    google_map_point = fields.Dict(required=False)
    
    user_id = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class PlatformGetAddressesResponse(BaseSchema):
    # Cart swagger.json

    
    address = fields.List(fields.Nested(PlatformAddress, required=False), required=False)
    


class SaveAddressResponse(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


class UpdateAddressResponse(BaseSchema):
    # Cart swagger.json

    
    is_default_address = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    is_updated = fields.Boolean(required=False)
    


class DeleteAddressResponse(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    is_deleted = fields.Boolean(required=False)
    


class PlatformSelectCartAddressRequest(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class ShipmentResponse(BaseSchema):
    # Cart swagger.json

    
    shipment_type = fields.Str(required=False)
    
    dp_id = fields.Str(required=False)
    
    promise = fields.Nested(ShipmentPromise, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    dp_options = fields.Dict(required=False)
    
    box_type = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    shipments = fields.Int(required=False)
    
    fulfillment_id = fields.Int(required=False)
    


class CartShipmentsResponse(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    coupon_text = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    currency = fields.Nested(CartCurrencySchema, required=False)
    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    comment = fields.Str(required=False)
    
    error = fields.Boolean(required=False)
    
    cart_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    buy_now = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    


class UpdateCartShipmentItem(BaseSchema):
    # Cart swagger.json

    
    article_uid = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    shipment_type = fields.Str(required=False)
    


class UpdateCartShipmentRequest(BaseSchema):
    # Cart swagger.json

    
    shipments = fields.List(fields.Nested(UpdateCartShipmentItem, required=False), required=False)
    


class PlatformCartMetaRequest(BaseSchema):
    # Cart swagger.json

    
    comment = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    pan_no = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    


class CartMetaResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    


class CartMetaMissingResponse(BaseSchema):
    # Cart swagger.json

    
    errors = fields.List(fields.Str(required=False), required=False)
    


class FilesSchema(BaseSchema):
    # Cart swagger.json

    
    values = fields.List(fields.Str(required=False), required=False)
    
    key = fields.Str(required=False)
    


class StaffCheckoutSchema(BaseSchema):
    # Cart swagger.json

    
    user = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    employee_code = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    


class PlatformCartCheckoutDetailRequest(BaseSchema):
    # Cart swagger.json

    
    merchant_code = fields.Str(required=False)
    
    files = fields.List(fields.Nested(FilesSchema, required=False), required=False)
    
    callback_url = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    address_id = fields.Str(required=False)
    
    staff = fields.Nested(StaffCheckoutSchema, required=False)
    
    payment_params = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    billing_address = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    pick_at_store_uid = fields.Int(required=False)
    
    aggregator = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    pos = fields.Boolean(required=False)
    
    user_id = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    employee_code = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    ordering_store = fields.Int(required=False)
    
    device_id = fields.Str(required=False)
    


class CheckCartSchema(BaseSchema):
    # Cart swagger.json

    
    delivery_charge_info = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    error_message = fields.Str(required=False)
    
    cod_charges = fields.Int(required=False)
    
    cart_id = fields.Int(required=False)
    
    order_id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    delivery_charge_order_value = fields.Int(required=False)
    
    delivery_charges = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    store_emps = fields.List(fields.Dict(required=False), required=False)
    
    checkout_mode = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    store_code = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    currency = fields.Nested(CartCurrencySchema, required=False)
    
    cod_message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    comment = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    user_type = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    cod_available = fields.Boolean(required=False)
    


class CartCheckoutResponseSchema(BaseSchema):
    # Cart swagger.json

    
    data = fields.Dict(required=False)
    
    payment_confirm_url = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    app_intercept_url = fields.Str(required=False)
    
    cart = fields.Nested(CheckCartSchema, required=False)
    


class CartDeliveryModesResponse(BaseSchema):
    # Cart swagger.json

    
    available_modes = fields.List(fields.Str(required=False), required=False)
    
    pickup_stores = fields.List(fields.Int(required=False), required=False)
    


class PickupStoreDetail(BaseSchema):
    # Cart swagger.json

    
    store_code = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    state = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    area = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class StoreDetailsResponse(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(PickupStoreDetail, required=False), required=False)
    


class UpdateCartPaymentRequest(BaseSchema):
    # Cart swagger.json

    
    address_id = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    


class CouponValidity(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    display_message_en = fields.Str(required=False)
    
    valid = fields.Boolean(required=False)
    


class PaymentCouponValidateSchema(BaseSchema):
    # Cart swagger.json

    
    coupon_validity = fields.Nested(CouponValidity, required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class PaymentMetaSchema(BaseSchema):
    # Cart swagger.json

    
    merchant_code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    


class PaymentMethodSchema(BaseSchema):
    # Cart swagger.json

    
    amount = fields.Float(required=False)
    
    payment = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    payment_meta = fields.Nested(PaymentMetaSchema, required=False)
    


class PlatformCartCheckoutDetailV2Request(BaseSchema):
    # Cart swagger.json

    
    payment_methods = fields.List(fields.Nested(PaymentMethodSchema, required=False), required=False)
    
    merchant_code = fields.Str(required=False)
    
    files = fields.List(fields.Nested(FilesSchema, required=False), required=False)
    
    callback_url = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    address_id = fields.Str(required=False)
    
    staff = fields.Nested(StaffCheckoutSchema, required=False)
    
    payment_params = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    billing_address = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    pick_at_store_uid = fields.Int(required=False)
    
    aggregator = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    pos = fields.Boolean(required=False)
    
    user_id = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    employee_code = fields.Str(required=False)
    
    custom_meta = fields.Dict(required=False)
    
    order_type = fields.Str(required=False)
    
    ordering_store = fields.Int(required=False)
    
    device_id = fields.Str(required=False)
    


class UpdateCartPaymentRequestV2(BaseSchema):
    # Cart swagger.json

    
    payment_methods = fields.List(fields.Nested(PaymentMethodSchema, required=False), required=False)
    
    address_id = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    


