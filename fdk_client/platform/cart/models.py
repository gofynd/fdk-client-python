"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class CouponDateMeta(BaseSchema):
    pass


class Ownership(BaseSchema):
    pass


class CouponAuthor(BaseSchema):
    pass


class State(BaseSchema):
    pass


class PaymentAllowValue(BaseSchema):
    pass


class PaymentModes(BaseSchema):
    pass


class PriceRange(BaseSchema):
    pass


class PostOrder(BaseSchema):
    pass


class BulkBundleRestriction(BaseSchema):
    pass


class UsesRemaining(BaseSchema):
    pass


class UsesRestriction(BaseSchema):
    pass


class Restrictions(BaseSchema):
    pass


class Validation(BaseSchema):
    pass


class CouponAction(BaseSchema):
    pass


class CouponSchedule(BaseSchema):
    pass


class Rule(BaseSchema):
    pass


class DisplayMetaDict(BaseSchema):
    pass


class DisplayMeta(BaseSchema):
    pass


class Identifier(BaseSchema):
    pass


class Validity(BaseSchema):
    pass


class RuleDefinition(BaseSchema):
    pass


class CouponAdd(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class CouponsResponse(BaseSchema):
    pass


class SuccessMessage(BaseSchema):
    pass


class OperationErrorResponse(BaseSchema):
    pass


class CouponUpdate(BaseSchema):
    pass


class CouponPartialUpdate(BaseSchema):
    pass


class DisplayMeta1(BaseSchema):
    pass


class Ownership1(BaseSchema):
    pass


class CompareObject(BaseSchema):
    pass


class ItemCriteria(BaseSchema):
    pass


class DiscountOffer(BaseSchema):
    pass


class DiscountRule(BaseSchema):
    pass


class PaymentAllowValue1(BaseSchema):
    pass


class PromotionPaymentModes(BaseSchema):
    pass


class UserRegistered(BaseSchema):
    pass


class PostOrder1(BaseSchema):
    pass


class UsesRemaining1(BaseSchema):
    pass


class UsesRestriction1(BaseSchema):
    pass


class Restrictions1(BaseSchema):
    pass


class PromotionSchedule(BaseSchema):
    pass


class PromotionAction(BaseSchema):
    pass


class PromotionAuthor(BaseSchema):
    pass


class Visibility(BaseSchema):
    pass


class PromotionDateMeta(BaseSchema):
    pass


class PromotionListItem(BaseSchema):
    pass


class PromotionsResponse(BaseSchema):
    pass


class PromotionAdd(BaseSchema):
    pass


class PromotionUpdate(BaseSchema):
    pass


class PromotionPartialUpdate(BaseSchema):
    pass


class ActivePromosResponse(BaseSchema):
    pass


class Charges(BaseSchema):
    pass


class DeliveryCharges(BaseSchema):
    pass


class CartMetaConfigUpdate(BaseSchema):
    pass


class CartMetaConfigAdd(BaseSchema):
    pass


class Article(BaseSchema):
    pass


class PriceAdjustmentRestrictions(BaseSchema):
    pass


class Collection(BaseSchema):
    pass


class PriceAdjustmentUpdate(BaseSchema):
    pass


class BulkPriceAdjustmentUpdate(BaseSchema):
    pass


class PriceAdjustment(BaseSchema):
    pass


class PriceAdjustmentResponse(BaseSchema):
    pass


class GetPriceAdjustmentResponse(BaseSchema):
    pass


class PriceAdjustmentAdd(BaseSchema):
    pass


class BulkPriceAdjustmentAdd(BaseSchema):
    pass


class CartItem(BaseSchema):
    pass


class OpenapiCartDetailsRequest(BaseSchema):
    pass


class CouponBreakup(BaseSchema):
    pass


class DisplayBreakup(BaseSchema):
    pass


class LoyaltyPoints(BaseSchema):
    pass


class RawBreakup(BaseSchema):
    pass


class CartBreakup(BaseSchema):
    pass


class ProductImage(BaseSchema):
    pass


class Tags(BaseSchema):
    pass


class BaseInfo(BaseSchema):
    pass


class ActionQuery(BaseSchema):
    pass


class ProductAction(BaseSchema):
    pass


class CategoryInfo(BaseSchema):
    pass


class CartProduct(BaseSchema):
    pass


class BasePrice(BaseSchema):
    pass


class ArticlePriceInfo(BaseSchema):
    pass


class StoreInfo(BaseSchema):
    pass


class ProductArticle(BaseSchema):
    pass


class Ownership2(BaseSchema):
    pass


class DiscountRulesApp(BaseSchema):
    pass


class AppliedFreeArticles(BaseSchema):
    pass


class BuyRules(BaseSchema):
    pass


class AppliedPromotion(BaseSchema):
    pass


class PromiseFormatted(BaseSchema):
    pass


class PromiseISOFormat(BaseSchema):
    pass


class PromiseTimestamp(BaseSchema):
    pass


class ShipmentPromise(BaseSchema):
    pass


class CouponDetails(BaseSchema):
    pass


class ProductPrice(BaseSchema):
    pass


class ProductPriceInfo(BaseSchema):
    pass


class CartProductIdentifer(BaseSchema):
    pass


class ProductAvailabilitySize(BaseSchema):
    pass


class ProductAvailability(BaseSchema):
    pass


class PromoMeta(BaseSchema):
    pass


class CartProductInfo(BaseSchema):
    pass


class OpenapiCartDetailsResponse(BaseSchema):
    pass


class OpenApiErrorResponse(BaseSchema):
    pass


class ShippingAddress(BaseSchema):
    pass


class OpenApiCartServiceabilityRequest(BaseSchema):
    pass


class OpenApiCartServiceabilityResponse(BaseSchema):
    pass


class OpenApiFiles(BaseSchema):
    pass


class CartItemMeta(BaseSchema):
    pass


class MultiTenderPaymentMeta(BaseSchema):
    pass


class MultiTenderPaymentMethod(BaseSchema):
    pass


class OpenApiOrderItem(BaseSchema):
    pass


class OpenApiPlatformCheckoutReq(BaseSchema):
    pass


class OpenApiCheckoutResponse(BaseSchema):
    pass


class AbandonedCart(BaseSchema):
    pass


class AbandonedCartResponse(BaseSchema):
    pass


class PaymentSelectionLock(BaseSchema):
    pass


class CartCurrency(BaseSchema):
    pass


class CartDetailCoupon(BaseSchema):
    pass


class ChargesThreshold(BaseSchema):
    pass


class DeliveryChargesConfig(BaseSchema):
    pass


class CartCommonConfig(BaseSchema):
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


class OverrideCartItemPromo(BaseSchema):
    pass


class OverrideCartItem(BaseSchema):
    pass


class OverrideCheckoutReq(BaseSchema):
    pass


class OverrideCheckoutResponse(BaseSchema):
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


class CartList(BaseSchema):
    pass


class MultiCartResponse(BaseSchema):
    pass


class UpdateUserCartMapping(BaseSchema):
    pass


class UserInfo(BaseSchema):
    pass


class UserCartMappingResponse(BaseSchema):
    pass


class PlatformAddCartRequest(BaseSchema):
    pass


class PlatformUpdateCartRequest(BaseSchema):
    pass


class DeleteCartRequest(BaseSchema):
    pass


class DeleteCartDetailResponse(BaseSchema):
    pass


class CartItemCountResponse(BaseSchema):
    pass


class Coupon(BaseSchema):
    pass


class PageCoupon(BaseSchema):
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


class ShipmentArticle(BaseSchema):
    pass


class PlatformShipmentResponse(BaseSchema):
    pass


class PlatformCartShipmentsResponse(BaseSchema):
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


class StaffCheckout(BaseSchema):
    pass


class CustomerDetails(BaseSchema):
    pass


class Files(BaseSchema):
    pass


class CartCheckoutCustomMeta(BaseSchema):
    pass


class PlatformCartCheckoutDetailRequest(BaseSchema):
    pass


class CheckCart(BaseSchema):
    pass


class CartCheckoutResponse(BaseSchema):
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


class PaymentCouponValidate(BaseSchema):
    pass


class PaymentMeta(BaseSchema):
    pass


class PaymentMethod(BaseSchema):
    pass


class PlatformCartCheckoutDetailV2Request(BaseSchema):
    pass


class UpdateCartPaymentRequestV2(BaseSchema):
    pass


class PriceMinMax(BaseSchema):
    pass


class ItemPriceDetails(BaseSchema):
    pass


class FreeGiftItems(BaseSchema):
    pass


class PromotionOffer(BaseSchema):
    pass


class PromotionOffersResponse(BaseSchema):
    pass


class PromotionPaymentOffer(BaseSchema):
    pass


class PromotionPaymentOffersResponse(BaseSchema):
    pass


class BulkPriceAdjustmentUpdateRequest(BaseSchema):
    pass


class BulkPriceAdjustmentResponse(BaseSchema):
    pass


class BulkPriceAdjustmentAddRequest(BaseSchema):
    pass





class CouponDateMeta(BaseSchema):
    # Cart swagger.json

    
    modified_on = fields.Str(required=False, allow_none=True)
    
    created_on = fields.Str(required=False, allow_none=True)
    


class Ownership(BaseSchema):
    # Cart swagger.json

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    


class CouponAuthor(BaseSchema):
    # Cart swagger.json

    
    created_by = fields.Str(required=False, allow_none=True)
    
    modified_by = fields.Str(required=False, allow_none=True)
    


class State(BaseSchema):
    # Cart swagger.json

    
    is_archived = fields.Boolean(required=False)
    
    is_display = fields.Boolean(required=False)
    
    is_public = fields.Boolean(required=False)
    


class PaymentAllowValue(BaseSchema):
    # Cart swagger.json

    
    max = fields.Int(required=False)
    


class PaymentModes(BaseSchema):
    # Cart swagger.json

    
    codes = fields.List(fields.Str(required=False), required=False)
    
    iins = fields.List(fields.Str(required=False), required=False)
    
    types = fields.List(fields.Str(required=False), required=False)
    
    networks = fields.List(fields.Str(required=False), required=False)
    
    uses = fields.Nested(PaymentAllowValue, required=False)
    


class PriceRange(BaseSchema):
    # Cart swagger.json

    
    max = fields.Int(required=False)
    
    min = fields.Int(required=False)
    


class PostOrder(BaseSchema):
    # Cart swagger.json

    
    cancellation_allowed = fields.Boolean(required=False)
    
    return_allowed = fields.Boolean(required=False)
    


class BulkBundleRestriction(BaseSchema):
    # Cart swagger.json

    
    multi_store_allowed = fields.Boolean(required=False)
    


class UsesRemaining(BaseSchema):
    # Cart swagger.json

    
    user = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    app = fields.Int(required=False)
    


class UsesRestriction(BaseSchema):
    # Cart swagger.json

    
    maximum = fields.Nested(UsesRemaining, required=False)
    
    remaining = fields.Nested(UsesRemaining, required=False)
    


class Restrictions(BaseSchema):
    # Cart swagger.json

    
    payments = fields.Dict(required=False)
    
    user_type = fields.Str(required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    post_order = fields.Nested(PostOrder, required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    coupon_allowed = fields.Boolean(required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    


class Validation(BaseSchema):
    # Cart swagger.json

    
    app_id = fields.List(fields.Str(required=False), required=False)
    
    anonymous = fields.Boolean(required=False)
    
    user_registered_after = fields.Str(required=False, allow_none=True)
    


class CouponAction(BaseSchema):
    # Cart swagger.json

    
    action_date = fields.Str(required=False, allow_none=True)
    
    txn_mode = fields.Str(required=False)
    


class CouponSchedule(BaseSchema):
    # Cart swagger.json

    
    end = fields.Str(required=False, allow_none=True)
    
    start = fields.Str(required=False)
    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    
    cron = fields.Str(required=False, allow_none=True)
    
    duration = fields.Int(required=False, allow_none=True)
    


class Rule(BaseSchema):
    # Cart swagger.json

    
    key = fields.Float(required=False)
    
    value = fields.Float(required=False)
    
    max = fields.Float(required=False)
    
    discount_qty = fields.Float(required=False)
    
    min = fields.Float(required=False)
    


class DisplayMetaDict(BaseSchema):
    # Cart swagger.json

    
    title = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    


class DisplayMeta(BaseSchema):
    # Cart swagger.json

    
    title = fields.Str(required=False)
    
    auto = fields.Nested(DisplayMetaDict, required=False)
    
    apply = fields.Nested(DisplayMetaDict, required=False)
    
    remove = fields.Nested(DisplayMetaDict, required=False)
    
    subtitle = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class Identifier(BaseSchema):
    # Cart swagger.json

    
    brand_id = fields.List(fields.Int(required=False), required=False)
    
    email_domain = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.List(fields.Int(required=False), required=False)
    
    store_id = fields.List(fields.Int(required=False), required=False)
    
    collection_id = fields.List(fields.Str(required=False), required=False)
    
    item_id = fields.List(fields.Int(required=False), required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    category_id = fields.List(fields.Int(required=False), required=False)
    
    article_id = fields.List(fields.Str(required=False), required=False)
    
    exclude_brand_id = fields.List(fields.Int(required=False), required=False)
    


class Validity(BaseSchema):
    # Cart swagger.json

    
    priority = fields.Int(required=False)
    


class RuleDefinition(BaseSchema):
    # Cart swagger.json

    
    currency_code = fields.Str(required=False)
    
    auto_apply = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    is_exact = fields.Boolean(required=False)
    
    applicable_on = fields.Str(required=False)
    
    calculate_on = fields.Str(required=False)
    
    value_type = fields.Str(required=False)
    
    scope = fields.List(fields.Str(required=False), required=False)
    


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    state = fields.Nested(State, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    code = fields.Str(required=False)
    
    type_slug = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    _id = fields.Str(required=False)
    


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

    
    items = fields.List(fields.Nested(CouponAdd, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class SuccessMessage(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class OperationErrorResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    error = fields.Str(required=False)
    


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    state = fields.Nested(State, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    code = fields.Str(required=False)
    
    type_slug = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    


class CouponPartialUpdate(BaseSchema):
    # Cart swagger.json

    
    archive = fields.Boolean(required=False)
    
    schedule = fields.Nested(CouponSchedule, required=False)
    


class DisplayMeta1(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    offer_label = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    


class Ownership1(BaseSchema):
    # Cart swagger.json

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    


class CompareObject(BaseSchema):
    # Cart swagger.json

    
    equals = fields.Float(required=False)
    
    greater_than = fields.Float(required=False)
    
    less_than_equals = fields.Float(required=False)
    
    less_than = fields.Float(required=False)
    
    greater_than_equals = fields.Float(required=False)
    


class ItemCriteria(BaseSchema):
    # Cart swagger.json

    
    cart_quantity = fields.Nested(CompareObject, required=False)
    
    available_zones = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_company = fields.List(fields.Int(required=False), required=False)
    
    item_id = fields.List(fields.Int(required=False), required=False)
    
    item_l1_category = fields.List(fields.Int(required=False), required=False)
    
    cart_total = fields.Nested(CompareObject, required=False)
    
    cart_unique_item_quantity = fields.Nested(CompareObject, required=False)
    
    cart_unique_item_amount = fields.Nested(CompareObject, required=False)
    
    item_exclude_id = fields.List(fields.Int(required=False), required=False)
    
    all_items = fields.Boolean(required=False)
    
    item_exclude_l1_category = fields.List(fields.Int(required=False), required=False)
    
    item_size = fields.List(fields.Str(required=False), required=False)
    
    item_store = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_sku = fields.List(fields.Str(required=False), required=False)
    
    item_department = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_store = fields.List(fields.Int(required=False), required=False)
    
    item_brand = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_department = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_category = fields.List(fields.Int(required=False), required=False)
    
    item_category = fields.List(fields.Int(required=False), required=False)
    
    buy_rules = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_brand = fields.List(fields.Int(required=False), required=False)
    
    item_l2_category = fields.List(fields.Int(required=False), required=False)
    
    item_company = fields.List(fields.Int(required=False), required=False)
    
    item_tags = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_l2_category = fields.List(fields.Int(required=False), required=False)
    
    item_sku = fields.List(fields.Str(required=False), required=False)
    


class DiscountOffer(BaseSchema):
    # Cart swagger.json

    
    max_discount_amount = fields.Float(required=False)
    
    discount_price = fields.Float(required=False)
    
    apportion_discount = fields.Boolean(required=False)
    
    partial_can_ret = fields.Boolean(required=False)
    
    max_usage_per_transaction = fields.Int(required=False)
    
    min_offer_quantity = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    discount_amount = fields.Float(required=False)
    
    discount_percentage = fields.Float(required=False)
    
    max_offer_quantity = fields.Int(required=False)
    


class DiscountRule(BaseSchema):
    # Cart swagger.json

    
    discount_type = fields.Str(required=False)
    
    buy_condition = fields.Str(required=False)
    
    item_criteria = fields.Nested(ItemCriteria, required=False)
    
    offer = fields.Nested(DiscountOffer, required=False)
    


class PaymentAllowValue1(BaseSchema):
    # Cart swagger.json

    
    max = fields.Int(required=False)
    


class PromotionPaymentModes(BaseSchema):
    # Cart swagger.json

    
    type = fields.Str(required=False)
    
    uses = fields.Nested(PaymentAllowValue1, required=False)
    
    codes = fields.List(fields.Str(required=False), required=False)
    


class UserRegistered(BaseSchema):
    # Cart swagger.json

    
    end = fields.Str(required=False, allow_none=True)
    
    start = fields.Str(required=False, allow_none=True)
    


class PostOrder1(BaseSchema):
    # Cart swagger.json

    
    cancellation_allowed = fields.Boolean(required=False)
    
    return_allowed = fields.Boolean(required=False)
    


class UsesRemaining1(BaseSchema):
    # Cart swagger.json

    
    user = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class UsesRestriction1(BaseSchema):
    # Cart swagger.json

    
    maximum = fields.Nested(UsesRemaining1, required=False)
    
    remaining = fields.Nested(UsesRemaining1, required=False)
    


class Restrictions1(BaseSchema):
    # Cart swagger.json

    
    payments = fields.Dict(required=False)
    
    user_registered = fields.Nested(UserRegistered, required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    post_order = fields.Nested(PostOrder1, required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    order_quantity = fields.Int(required=False)
    
    anonymous_users = fields.Boolean(required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    uses = fields.Nested(UsesRestriction1, required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    


class PromotionSchedule(BaseSchema):
    # Cart swagger.json

    
    end = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    
    cron = fields.Str(required=False, allow_none=True)
    
    duration = fields.Int(required=False, allow_none=True)
    


class PromotionAction(BaseSchema):
    # Cart swagger.json

    
    action_date = fields.Str(required=False, allow_none=True)
    
    action_type = fields.Str(required=False)
    


class PromotionAuthor(BaseSchema):
    # Cart swagger.json

    
    created_by = fields.Str(required=False, allow_none=True)
    
    modified_by = fields.Str(required=False, allow_none=True)
    


class Visibility(BaseSchema):
    # Cart swagger.json

    
    coupon_list = fields.Boolean(required=False)
    
    pdp = fields.Boolean(required=False)
    


class PromotionDateMeta(BaseSchema):
    # Cart swagger.json

    
    modified_on = fields.Str(required=False, allow_none=True)
    
    created_on = fields.Str(required=False, allow_none=True)
    


class PromotionListItem(BaseSchema):
    # Cart swagger.json

    
    stackable = fields.Boolean(required=False)
    
    calculate_on = fields.Str(required=False)
    
    apply_exclusive = fields.Str(required=False, allow_none=True)
    
    promo_group = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    promotion_type = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    currency = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    
    apply_priority = fields.Int(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    application_id = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    _id = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class PromotionsResponse(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(PromotionListItem, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class PromotionAdd(BaseSchema):
    # Cart swagger.json

    
    stackable = fields.Boolean(required=False)
    
    calculate_on = fields.Str(required=False)
    
    apply_exclusive = fields.Str(required=False, allow_none=True)
    
    promo_group = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    promotion_type = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    currency = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    
    apply_priority = fields.Int(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    application_id = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class PromotionUpdate(BaseSchema):
    # Cart swagger.json

    
    stackable = fields.Boolean(required=False)
    
    calculate_on = fields.Str(required=False)
    
    apply_exclusive = fields.Str(required=False, allow_none=True)
    
    promo_group = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    promotion_type = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    currency = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    
    apply_priority = fields.Int(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    application_id = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class PromotionPartialUpdate(BaseSchema):
    # Cart swagger.json

    
    archive = fields.Boolean(required=False)
    
    schedule = fields.Nested(PromotionSchedule, required=False)
    


class ActivePromosResponse(BaseSchema):
    # Cart swagger.json

    
    entity_slug = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    example = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    is_hidden = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class Charges(BaseSchema):
    # Cart swagger.json

    
    charges = fields.Int(required=False)
    
    threshold = fields.Int(required=False)
    


class DeliveryCharges(BaseSchema):
    # Cart swagger.json

    
    charges = fields.List(fields.Nested(Charges, required=False), required=False)
    
    enabled = fields.Boolean(required=False)
    


class CartMetaConfigUpdate(BaseSchema):
    # Cart swagger.json

    
    min_cart_value = fields.Int(required=False)
    
    max_cart_value = fields.Int(required=False)
    
    bulk_coupons = fields.Boolean(required=False)
    
    max_cart_items = fields.Int(required=False)
    
    gift_display_text = fields.Str(required=False)
    
    delivery_charges = fields.Nested(DeliveryCharges, required=False)
    
    revenue_engine_coupon = fields.Boolean(required=False)
    
    gift_pricing = fields.Float(required=False)
    
    enabled = fields.Boolean(required=False)
    


class CartMetaConfigAdd(BaseSchema):
    # Cart swagger.json

    
    min_cart_value = fields.Int(required=False)
    
    max_cart_value = fields.Int(required=False)
    
    bulk_coupons = fields.Boolean(required=False)
    
    max_cart_items = fields.Int(required=False)
    
    gift_display_text = fields.Str(required=False)
    
    delivery_charges = fields.Nested(DeliveryCharges, required=False)
    
    revenue_engine_coupon = fields.Boolean(required=False)
    
    gift_pricing = fields.Float(required=False)
    
    enabled = fields.Boolean(required=False)
    


class Article(BaseSchema):
    # Cart swagger.json

    
    value = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    


class PriceAdjustmentRestrictions(BaseSchema):
    # Cart swagger.json

    
    post_order = fields.Dict(required=False)
    


class Collection(BaseSchema):
    # Cart swagger.json

    
    refund_by = fields.Str(required=False)
    
    collected_by = fields.Str(required=False)
    


class PriceAdjustmentUpdate(BaseSchema):
    # Cart swagger.json

    
    modified_by = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    apply_expiry = fields.Str(required=False)
    
    restrictions = fields.Nested(PriceAdjustmentRestrictions, required=False)
    
    article_level_distribution = fields.Boolean(required=False)
    
    collection = fields.Nested(Collection, required=False)
    
    type = fields.Str(required=False)
    
    allowed_refund = fields.Boolean(required=False)
    
    is_authenticated = fields.Boolean(required=False)
    
    article_ids = fields.List(fields.Nested(Article, required=False), required=False)
    
    auto_remove = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    cart_id = fields.Str(required=False)
    


class BulkPriceAdjustmentUpdate(BaseSchema):
    # Cart swagger.json

    
    modified_by = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    apply_expiry = fields.Str(required=False)
    
    restrictions = fields.Nested(PriceAdjustmentRestrictions, required=False)
    
    article_level_distribution = fields.Boolean(required=False)
    
    collection = fields.Nested(Collection, required=False)
    
    type = fields.Str(required=False)
    
    allowed_refund = fields.Boolean(required=False)
    
    article_ids = fields.List(fields.Nested(Article, required=False), required=False)
    
    meta = fields.Dict(required=False)
    


class PriceAdjustment(BaseSchema):
    # Cart swagger.json

    
    value = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    apply_expiry = fields.Str(required=False)
    
    restrictions = fields.Nested(PriceAdjustmentRestrictions, required=False)
    
    article_level_distribution = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    collection = fields.Nested(Collection, required=False)
    
    type = fields.Str(required=False)
    
    allowed_refund = fields.Boolean(required=False)
    
    is_authenticated = fields.Boolean(required=False)
    
    article_ids = fields.List(fields.Nested(Article, required=False), required=False)
    
    auto_remove = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    cart_id = fields.Str(required=False)
    


class PriceAdjustmentResponse(BaseSchema):
    # Cart swagger.json

    
    data = fields.Nested(PriceAdjustment, required=False)
    


class GetPriceAdjustmentResponse(BaseSchema):
    # Cart swagger.json

    
    data = fields.List(fields.Nested(PriceAdjustment, required=False), required=False)
    


class PriceAdjustmentAdd(BaseSchema):
    # Cart swagger.json

    
    value = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    apply_expiry = fields.Str(required=False)
    
    restrictions = fields.Nested(PriceAdjustmentRestrictions, required=False)
    
    created_by = fields.Str(required=False)
    
    article_level_distribution = fields.Boolean(required=False)
    
    collection = fields.Nested(Collection, required=False)
    
    type = fields.Str(required=False)
    
    allowed_refund = fields.Boolean(required=False)
    
    is_authenticated = fields.Boolean(required=False)
    
    article_ids = fields.List(fields.Nested(Article, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    cart_id = fields.Str(required=False)
    
    auto_remove = fields.Boolean(required=False)
    


class BulkPriceAdjustmentAdd(BaseSchema):
    # Cart swagger.json

    
    value = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    apply_expiry = fields.Str(required=False)
    
    restrictions = fields.Nested(PriceAdjustmentRestrictions, required=False)
    
    created_by = fields.Str(required=False)
    
    article_level_distribution = fields.Boolean(required=False)
    
    collection = fields.Nested(Collection, required=False)
    
    type = fields.Str(required=False)
    
    allowed_refund = fields.Boolean(required=False)
    
    article_ids = fields.List(fields.Nested(Article, required=False), required=False)
    
    meta = fields.Dict(required=False)
    


class CartItem(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    product_id = fields.Str(required=False)
    
    size = fields.Str(required=False)
    


class OpenapiCartDetailsRequest(BaseSchema):
    # Cart swagger.json

    
    cart_items = fields.List(fields.Nested(CartItem, required=False), required=False)
    


class CouponBreakup(BaseSchema):
    # Cart swagger.json

    
    title = fields.Str(required=False, allow_none=True)
    
    max_discount_value = fields.Float(required=False)
    
    value = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    coupon_type = fields.Str(required=False, allow_none=True)
    
    sub_title = fields.Str(required=False, allow_none=True)
    
    coupon_value = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    description = fields.Str(required=False, allow_none=True)
    


class DisplayBreakup(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    message = fields.List(fields.Str(required=False), required=False)
    


class LoyaltyPoints(BaseSchema):
    # Cart swagger.json

    
    is_applied = fields.Boolean(required=False)
    
    total = fields.Float(required=False)
    
    applicable = fields.Float(required=False)
    
    description = fields.Str(required=False)
    


class RawBreakup(BaseSchema):
    # Cart swagger.json

    
    coupon = fields.Float(required=False)
    
    gst_charges = fields.Float(required=False)
    
    mrp_total = fields.Float(required=False)
    
    fynd_cash = fields.Float(required=False)
    
    vog = fields.Float(required=False)
    
    gift_card = fields.Float(required=False)
    
    cod_charge = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    you_saved = fields.Float(required=False)
    
    subtotal = fields.Float(required=False)
    
    convenience_fee = fields.Float(required=False)
    


class CartBreakup(BaseSchema):
    # Cart swagger.json

    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    


class ProductImage(BaseSchema):
    # Cart swagger.json

    
    secure_url = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    


class Tags(BaseSchema):
    # Cart swagger.json

    
    tags = fields.Dict(required=False)
    


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
    
    url = fields.Str(required=False)
    
    query = fields.Nested(ActionQuery, required=False)
    


class CategoryInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class CartProduct(BaseSchema):
    # Cart swagger.json

    
    slug = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    teaser_tag = fields.Nested(Tags, required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    uid = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    item_code = fields.Str(required=False, allow_none=True)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    attributes = fields.Dict(required=False)
    


class BasePrice(BaseSchema):
    # Cart swagger.json

    
    effective = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    marked = fields.Float(required=False)
    


class ArticlePriceInfo(BaseSchema):
    # Cart swagger.json

    
    converted = fields.Nested(BasePrice, required=False)
    
    base = fields.Nested(BasePrice, required=False)
    


class StoreInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    


class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    seller_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    cart_item_meta = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    is_gift_visible = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    gift_card = fields.Dict(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    identifier = fields.Dict(required=False)
    
    mto_quantity = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    meta = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    store = fields.Nested(StoreInfo, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class Ownership2(BaseSchema):
    # Cart swagger.json

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    


class DiscountRulesApp(BaseSchema):
    # Cart swagger.json

    
    offer = fields.Dict(required=False)
    
    raw_offer = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    


class AppliedFreeArticles(BaseSchema):
    # Cart swagger.json

    
    parent_item_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    
    free_gift_item_details = fields.Nested(FreeGiftItems, required=False)
    


class BuyRules(BaseSchema):
    # Cart swagger.json

    
    cart_conditions = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    


class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    article_quantity = fields.Int(required=False)
    
    ownership = fields.Nested(Ownership2, required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesApp, required=False), required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    
    promotion_name = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    offer_text = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    float_amount = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    promotion_group = fields.Str(required=False)
    
    promo_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    code = fields.Str(required=False, allow_none=True)
    


class PromiseFormatted(BaseSchema):
    # Cart swagger.json

    
    max = fields.Str(required=False)
    
    min = fields.Str(required=False)
    


class PromiseISOFormat(BaseSchema):
    # Cart swagger.json

    
    max = fields.Str(required=False)
    
    min = fields.Str(required=False)
    


class PromiseTimestamp(BaseSchema):
    # Cart swagger.json

    
    max = fields.Float(required=False)
    
    min = fields.Float(required=False)
    


class ShipmentPromise(BaseSchema):
    # Cart swagger.json

    
    formatted = fields.Nested(PromiseFormatted, required=False)
    
    timestamp = fields.Nested(PromiseTimestamp, required=False)
    
    iso = fields.Nested(PromiseISOFormat, required=False)
    


class CouponDetails(BaseSchema):
    # Cart swagger.json

    
    discount_total_quantity = fields.Float(required=False)
    
    discount_single_quantity = fields.Float(required=False)
    
    code = fields.Str(required=False)
    


class ProductPrice(BaseSchema):
    # Cart swagger.json

    
    marked = fields.Float(required=False)
    
    add_on = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    
    selling = fields.Float(required=False)
    


class ProductPriceInfo(BaseSchema):
    # Cart swagger.json

    
    converted = fields.Nested(ProductPrice, required=False)
    
    base = fields.Nested(ProductPrice, required=False)
    


class CartProductIdentifer(BaseSchema):
    # Cart swagger.json

    
    identifier = fields.Str(required=False)
    


class ProductAvailabilitySize(BaseSchema):
    # Cart swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    


class ProductAvailability(BaseSchema):
    # Cart swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    other_store_quantity = fields.Int(required=False)
    
    deliverable = fields.Boolean(required=False)
    
    available_sizes = fields.List(fields.Nested(ProductAvailabilitySize, required=False), required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    


class PromoMeta(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    product_ean_id = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    key = fields.Str(required=False)
    
    coupon = fields.Nested(CouponDetails, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    coupon_message = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    message = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    moq = fields.Dict(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    custom_order = fields.Dict(required=False)
    


class OpenapiCartDetailsResponse(BaseSchema):
    # Cart swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    


class OpenApiErrorResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    


class ShippingAddress(BaseSchema):
    # Cart swagger.json

    
    country = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False, allow_none=True)
    
    city = fields.Str(required=False, allow_none=True)
    
    phone = fields.Int(required=False)
    
    area_code = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    
    country_phone_code = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    address_type = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    address = fields.Str(required=False)
    


class OpenApiCartServiceabilityRequest(BaseSchema):
    # Cart swagger.json

    
    cart_items = fields.List(fields.Nested(CartItem, required=False), required=False)
    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    


class OpenApiCartServiceabilityResponse(BaseSchema):
    # Cart swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    


class OpenApiFiles(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    values = fields.List(fields.Str(required=False), required=False)
    


class CartItemMeta(BaseSchema):
    # Cart swagger.json

    
    primary_item = fields.Boolean(required=False)
    
    group_id = fields.Str(required=False)
    


class MultiTenderPaymentMeta(BaseSchema):
    # Cart swagger.json

    
    payment_id = fields.Str(required=False, allow_none=True)
    
    payment_gateway = fields.Str(required=False, allow_none=True)
    
    extra_meta = fields.Dict(required=False, allow_none=True)
    
    current_status = fields.Str(required=False, allow_none=True)
    
    order_id = fields.Str(required=False, allow_none=True)
    


class MultiTenderPaymentMethod(BaseSchema):
    # Cart swagger.json

    
    mode = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    meta = fields.Nested(MultiTenderPaymentMeta, required=False)
    
    name = fields.Str(required=False)
    


class OpenApiOrderItem(BaseSchema):
    # Cart swagger.json

    
    cashback_applied = fields.Float(required=False)
    
    quantity = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    meta = fields.Nested(CartItemMeta, required=False)
    
    extra_meta = fields.Dict(required=False)
    
    product_id = fields.Int(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    employee_discount = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    


class OpenApiPlatformCheckoutReq(BaseSchema):
    # Cart swagger.json

    
    payment_mode = fields.Str(required=False)
    
    cart_value = fields.Float(required=False)
    
    cart_items = fields.List(fields.Nested(OpenApiOrderItem, required=False), required=False)
    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    comment = fields.Str(required=False, allow_none=True)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    employee_discount = fields.Dict(required=False)
    
    coupon = fields.Str(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    gstin = fields.Str(required=False, allow_none=True)
    
    billing_address = fields.Nested(ShippingAddress, required=False)
    
    coupon_code = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    cod_charges = fields.Float(required=False)
    


class OpenApiCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    order_ref_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    


class AbandonedCart(BaseSchema):
    # Cart swagger.json

    
    expire_at = fields.Str(required=False)
    
    promotion = fields.Dict(required=False)
    
    is_default = fields.Boolean(required=False)
    
    comment = fields.Str(required=False, allow_none=True)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    coupon = fields.Dict(required=False, allow_none=True)
    
    bulk_coupon_discount = fields.Float(required=False, allow_none=True)
    
    _id = fields.Str(required=False)
    
    fynd_credits = fields.Dict(required=False)
    
    fc_index_map = fields.List(fields.Int(required=False), required=False)
    
    order_id = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    cod_charges = fields.Dict(required=False)
    
    payments = fields.Dict(required=False, allow_none=True)
    
    payment_mode = fields.Str(required=False, allow_none=True)
    
    shipments = fields.List(fields.Dict(required=False), required=False)
    
    pick_up_customer_details = fields.Dict(required=False, allow_none=True)
    
    uid = fields.Int(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    cart_value = fields.Float(required=False)
    
    is_archive = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    buy_now = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    cashback = fields.Dict(required=False)
    
    payment_methods = fields.List(fields.Dict(required=False), required=False)
    
    gstin = fields.Str(required=False, allow_none=True)
    
    delivery_charges = fields.Dict(required=False)
    
    merge_qty = fields.Boolean(required=False, allow_none=True)
    
    user_id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    


class AbandonedCartResponse(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(AbandonedCart, required=False), required=False)
    
    result = fields.Dict(required=False)
    
    page = fields.Nested(Page, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class PaymentSelectionLock(BaseSchema):
    # Cart swagger.json

    
    payment_identifier = fields.Str(required=False)
    
    default_options = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    


class CartCurrency(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    


class CartDetailCoupon(BaseSchema):
    # Cart swagger.json

    
    cashback_amount = fields.Float(required=False)
    
    cashback_message_primary = fields.Str(required=False)
    
    cashback_message_secondary = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    
    coupon_description = fields.Str(required=False)
    
    coupon_id = fields.Str(required=False)
    
    coupon_subtitle = fields.Str(required=False)
    
    coupon_title = fields.Str(required=False)
    
    coupon_type = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    maximum_discount_value = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    


class ChargesThreshold(BaseSchema):
    # Cart swagger.json

    
    charges = fields.Float(required=False)
    
    threshold = fields.Float(required=False)
    


class DeliveryChargesConfig(BaseSchema):
    # Cart swagger.json

    
    enabled = fields.Boolean(required=False)
    
    charges = fields.List(fields.Nested(ChargesThreshold, required=False), required=False)
    


class CartCommonConfig(BaseSchema):
    # Cart swagger.json

    
    delivery_charges_config = fields.Nested(DeliveryChargesConfig, required=False)
    


class CartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    cart_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    pan_config = fields.Dict(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    comment = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    common_config = fields.Nested(CartCommonConfig, required=False)
    
    coupon = fields.Nested(CartDetailCoupon, required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    notification = fields.Dict(required=False)
    
    staff_user_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    gstin = fields.Str(required=False)
    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    pan_no = fields.Str(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class AddProductCart(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    parent_item_identifiers = fields.List(fields.Dict(required=False), required=False)
    
    product_group_tags = fields.List(fields.Str(required=False, allow_none=True), required=False)
    
    article_id = fields.Str(required=False)
    
    article_assignment = fields.Dict(required=False)
    
    store_id = fields.Int(required=False)
    
    display = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    pos = fields.Boolean(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    


class AddCartRequest(BaseSchema):
    # Cart swagger.json

    
    new_cart = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    


class AddCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    partial = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class UpdateProductCart(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    item_index = fields.Int(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    article_id = fields.Str(required=False)
    


class UpdateCartRequest(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(UpdateProductCart, required=False), required=False)
    
    operation = fields.Str(required=False)
    


class UpdateCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    message = fields.Str(required=False)
    


class OverrideCartItemPromo(BaseSchema):
    # Cart swagger.json

    
    promo_id = fields.Str(required=False)
    
    promo_amount = fields.Str(required=False)
    
    promo_desc = fields.Str(required=False)
    
    rwrd_tndr = fields.Str(required=False)
    
    item_list = fields.List(fields.Dict(required=False, allow_none=True), required=False)
    
    parent_promo_id = fields.Str(required=False)
    


class OverrideCartItem(BaseSchema):
    # Cart swagger.json

    
    seller_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    price_marked = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    promo_list = fields.List(fields.Nested(OverrideCartItemPromo, required=False), required=False)
    
    extra_meta = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    discount = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    


class OverrideCheckoutReq(BaseSchema):
    # Cart swagger.json

    
    cart_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    billing_address = fields.Dict(required=False)
    
    merchant_code = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False, allow_none=True)
    
    currency_code = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    cart_items = fields.List(fields.Nested(OverrideCartItem, required=False), required=False)
    
    ordering_store = fields.Int(required=False, allow_none=True)
    
    shipping_address = fields.Dict(required=False)
    


class OverrideCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    data = fields.Dict(required=False)
    
    cart = fields.Dict(required=False)
    
    success = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class GetShareCartLinkRequest(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class GetShareCartLinkResponse(BaseSchema):
    # Cart swagger.json

    
    token = fields.Str(required=False)
    
    share_url = fields.Str(required=False)
    


class SharedCartDetails(BaseSchema):
    # Cart swagger.json

    
    source = fields.Dict(required=False)
    
    user = fields.Dict(required=False)
    
    token = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class SharedCart(BaseSchema):
    # Cart swagger.json

    
    coupon_text = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    comment = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    last_modified = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    cart_id = fields.Int(required=False)
    
    gstin = fields.Str(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class SharedCartResponse(BaseSchema):
    # Cart swagger.json

    
    cart = fields.Nested(SharedCart, required=False)
    
    error = fields.Str(required=False)
    


class CartList(BaseSchema):
    # Cart swagger.json

    
    cart_id = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    
    cart_value = fields.Float(required=False)
    
    created_on = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    item_counts = fields.Int(required=False)
    


class MultiCartResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(CartList, required=False), required=False)
    


class UpdateUserCartMapping(BaseSchema):
    # Cart swagger.json

    
    user_id = fields.Str(required=False)
    


class UserInfo(BaseSchema):
    # Cart swagger.json

    
    gender = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    external_id = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    


class UserCartMappingResponse(BaseSchema):
    # Cart swagger.json

    
    coupon_text = fields.Str(required=False)
    
    user = fields.Nested(UserInfo, required=False)
    
    id = fields.Str(required=False)
    
    pan_config = fields.Dict(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    comment = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    gstin = fields.Str(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    pan_no = fields.Str(required=False)
    


class PlatformAddCartRequest(BaseSchema):
    # Cart swagger.json

    
    user_id = fields.Str(required=False)
    
    new_cart = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    


class PlatformUpdateCartRequest(BaseSchema):
    # Cart swagger.json

    
    user_id = fields.Str(required=False)
    
    items = fields.List(fields.Nested(UpdateProductCart, required=False), required=False)
    
    operation = fields.Str(required=False)
    


class DeleteCartRequest(BaseSchema):
    # Cart swagger.json

    
    cart_id_list = fields.List(fields.Str(required=False), required=False)
    


class DeleteCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class CartItemCountResponse(BaseSchema):
    # Cart swagger.json

    
    user_cart_items_count = fields.Int(required=False)
    
    user_cart_article_count = fields.Int(required=False)
    


class Coupon(BaseSchema):
    # Cart swagger.json

    
    title = fields.Str(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    coupon_code = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    coupon_type = fields.Str(required=False, allow_none=True)
    
    expires_on = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    sub_title = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    is_applicable = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    description = fields.Str(required=False, allow_none=True)
    
    start_date = fields.Str(required=False, allow_none=True)
    
    end_date = fields.Str(required=False, allow_none=True)
    
    coupon_applicable_message = fields.Str(required=False)
    


class PageCoupon(BaseSchema):
    # Cart swagger.json

    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    total_item_count = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    


class GetCouponResponse(BaseSchema):
    # Cart swagger.json

    
    available_coupon_list = fields.List(fields.Nested(Coupon, required=False), required=False)
    
    page = fields.Nested(PageCoupon, required=False)
    


class ApplyCouponRequest(BaseSchema):
    # Cart swagger.json

    
    coupon_code = fields.Str(required=False)
    


class GeoLocation(BaseSchema):
    # Cart swagger.json

    
    longitude = fields.Float(required=False)
    
    latitude = fields.Float(required=False)
    


class PlatformAddress(BaseSchema):
    # Cart swagger.json

    
    phone = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    geo_location = fields.Nested(GeoLocation, required=False)
    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    created_by_user_id = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    google_map_point = fields.Dict(required=False)
    
    cart_id = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    country_phone_code = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    


class PlatformGetAddressesResponse(BaseSchema):
    # Cart swagger.json

    
    address = fields.List(fields.Nested(PlatformAddress, required=False), required=False)
    


class SaveAddressResponse(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    is_default_address = fields.Boolean(required=False)
    


class UpdateAddressResponse(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    is_updated = fields.Boolean(required=False)
    


class DeleteAddressResponse(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    is_deleted = fields.Boolean(required=False)
    


class PlatformSelectCartAddressRequest(BaseSchema):
    # Cart swagger.json

    
    cart_id = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class ShipmentArticle(BaseSchema):
    # Cart swagger.json

    
    meta = fields.Str(required=False)
    
    quantity = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    


class PlatformShipmentResponse(BaseSchema):
    # Cart swagger.json

    
    shipments = fields.Int(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    dp_options = fields.Dict(required=False, allow_none=True)
    
    shipment_type = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    box_type = fields.Str(required=False, allow_none=True)
    
    promise = fields.Nested(ShipmentPromise, required=False)
    
    dp_id = fields.Str(required=False, allow_none=True)
    
    fulfillment_type = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(ShipmentArticle, required=False), required=False)
    


class PlatformCartShipmentsResponse(BaseSchema):
    # Cart swagger.json

    
    coupon_text = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    pan_config = fields.Dict(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    comment = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    staff_user_id = fields.Str(required=False, allow_none=True)
    
    is_valid = fields.Boolean(required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipmentResponse, required=False), required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    gstin = fields.Str(required=False)
    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    error = fields.Boolean(required=False)
    
    pan_no = fields.Str(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class UpdateCartShipmentItem(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    shipment_type = fields.Str(required=False)
    
    article_uid = fields.Str(required=False)
    


class UpdateCartShipmentRequest(BaseSchema):
    # Cart swagger.json

    
    shipments = fields.List(fields.Nested(UpdateCartShipmentItem, required=False), required=False)
    


class PlatformCartMetaRequest(BaseSchema):
    # Cart swagger.json

    
    gstin = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gift_details = fields.Dict(required=False, allow_none=True)
    
    pan_no = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    staff_user_id = fields.Str(required=False, allow_none=True)
    


class CartMetaResponse(BaseSchema):
    # Cart swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class CartMetaMissingResponse(BaseSchema):
    # Cart swagger.json

    
    errors = fields.List(fields.Str(required=False), required=False)
    


class StaffCheckout(BaseSchema):
    # Cart swagger.json

    
    employee_code = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    


class CustomerDetails(BaseSchema):
    # Cart swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False, allow_none=True)
    
    mobile = fields.Str(required=False)
    


class Files(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    values = fields.List(fields.Str(required=False), required=False)
    


class CartCheckoutCustomMeta(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class PlatformCartCheckoutDetailRequest(BaseSchema):
    # Cart swagger.json

    
    custom_meta = fields.List(fields.Nested(CartCheckoutCustomMeta, required=False), required=False)
    
    address_id = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False, allow_none=True)
    
    payment_params = fields.Dict(required=False, allow_none=True)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    pos = fields.Boolean(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    pick_at_store_uid = fields.Int(required=False, allow_none=True)
    
    device_id = fields.Str(required=False, allow_none=True)
    
    delivery_address = fields.Dict(required=False)
    
    payment_mode = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    customer_details = fields.Nested(CustomerDetails, required=False)
    
    meta = fields.Dict(required=False)
    
    staff = fields.Nested(StaffCheckout, required=False)
    
    employee_code = fields.Str(required=False, allow_none=True)
    
    billing_address = fields.Dict(required=False)
    
    callback_url = fields.Str(required=False, allow_none=True)
    
    user_id = fields.Str(required=False, allow_none=True)
    
    extra_meta = fields.Dict(required=False)
    
    order_type = fields.Str(required=False)
    
    files = fields.List(fields.Nested(Files, required=False), required=False)
    
    ordering_store = fields.Int(required=False, allow_none=True)
    
    payment_extra_identifiers = fields.Dict(required=False)
    
    iin = fields.Str(required=False)
    
    network = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    


class CheckCart(BaseSchema):
    # Cart swagger.json

    
    coupon_text = fields.Str(required=False)
    
    cod_message = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    comment = fields.Str(required=False)
    
    user_type = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    error_message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    cod_charges = fields.Float(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    last_modified = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    delivery_charge_order_value = fields.Int(required=False)
    
    cart_id = fields.Int(required=False)
    
    store_emps = fields.List(fields.Dict(required=False), required=False)
    
    gstin = fields.Str(required=False)
    
    cod_available = fields.Boolean(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class CartCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    app_intercept_url = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    cart = fields.Nested(CheckCart, required=False)
    
    success = fields.Boolean(required=False)
    
    callback_url = fields.Str(required=False)
    
    payment_confirm_url = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class CartDeliveryModesResponse(BaseSchema):
    # Cart swagger.json

    
    pickup_stores = fields.List(fields.Int(required=False), required=False)
    
    available_modes = fields.List(fields.Str(required=False), required=False)
    


class PickupStoreDetail(BaseSchema):
    # Cart swagger.json

    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    store_manager_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    address = fields.Str(required=False)
    


class StoreDetailsResponse(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(PickupStoreDetail, required=False), required=False)
    


class UpdateCartPaymentRequest(BaseSchema):
    # Cart swagger.json

    
    address_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False, allow_none=True)
    
    id = fields.Str(required=False)
    


class CouponValidity(BaseSchema):
    # Cart swagger.json

    
    title = fields.Str(required=False)
    
    next_validation_required = fields.Boolean(required=False, allow_none=True)
    
    valid = fields.Boolean(required=False)
    
    display_message_en = fields.Str(required=False, allow_none=True)
    
    code = fields.Str(required=False, allow_none=True)
    
    discount = fields.Float(required=False)
    


class PaymentCouponValidate(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    coupon_validity = fields.Nested(CouponValidity, required=False)
    


class PaymentMeta(BaseSchema):
    # Cart swagger.json

    
    payment_gateway = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False, allow_none=True)
    
    merchant_code = fields.Str(required=False)
    


class PaymentMethod(BaseSchema):
    # Cart swagger.json

    
    mode = fields.Str(required=False)
    
    payment = fields.Str(required=False)
    
    payment_meta = fields.Nested(PaymentMeta, required=False)
    
    amount = fields.Float(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    
    payment_extra_identifiers = fields.Dict(required=False)
    


class PlatformCartCheckoutDetailV2Request(BaseSchema):
    # Cart swagger.json

    
    address_id = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False, allow_none=True)
    
    payment_params = fields.Dict(required=False, allow_none=True)
    
    custom_meta = fields.Dict(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    pos = fields.Boolean(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    pick_at_store_uid = fields.Int(required=False, allow_none=True)
    
    device_id = fields.Str(required=False, allow_none=True)
    
    delivery_address = fields.Dict(required=False)
    
    payment_mode = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    customer_details = fields.Dict(required=False, allow_none=True)
    
    meta = fields.Dict(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMethod, required=False), required=False)
    
    staff = fields.Nested(StaffCheckout, required=False)
    
    employee_code = fields.Str(required=False, allow_none=True)
    
    billing_address = fields.Dict(required=False)
    
    callback_url = fields.Str(required=False, allow_none=True)
    
    user_id = fields.Str(required=False, allow_none=True)
    
    extra_meta = fields.Dict(required=False)
    
    order_type = fields.Str(required=False)
    
    files = fields.List(fields.Nested(Files, required=False), required=False)
    
    ordering_store = fields.Int(required=False, allow_none=True)
    
    iin = fields.Str(required=False)
    
    network = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    


class UpdateCartPaymentRequestV2(BaseSchema):
    # Cart swagger.json

    
    address_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False, allow_none=True)
    
    id = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMethod, required=False), required=False)
    


class PriceMinMax(BaseSchema):
    # Cart swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    


class ItemPriceDetails(BaseSchema):
    # Cart swagger.json

    
    marked = fields.Nested(PriceMinMax, required=False)
    
    effective = fields.Nested(PriceMinMax, required=False)
    
    currency = fields.Str(required=False)
    


class FreeGiftItems(BaseSchema):
    # Cart swagger.json

    
    item_slug = fields.Str(required=False)
    
    item_name = fields.Str(required=False)
    
    item_price_details = fields.Nested(ItemPriceDetails, required=False)
    
    item_brand_name = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    


class PromotionOffer(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    offer_text = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
    promotion_group = fields.Str(required=False)
    
    valid_till = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Dict(required=False), required=False)
    
    free_gift_items = fields.List(fields.Nested(FreeGiftItems, required=False), required=False)
    
    description = fields.Str(required=False)
    


class PromotionOffersResponse(BaseSchema):
    # Cart swagger.json

    
    available_promotions = fields.List(fields.Nested(PromotionOffer, required=False), required=False)
    


class PromotionPaymentOffer(BaseSchema):
    # Cart swagger.json

    
    application_id = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Dict(required=False), required=False)
    
    calculate_on = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Dict(required=False), required=False)
    
    id = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    promotion_group = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    


class PromotionPaymentOffersResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    promotions = fields.List(fields.Nested(PromotionPaymentOffer, required=False), required=False)
    


class BulkPriceAdjustmentUpdateRequest(BaseSchema):
    # Cart swagger.json

    
    cart_id = fields.Str(required=False)
    
    is_authenticated = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(BulkPriceAdjustmentUpdate, required=False), required=False)
    


class BulkPriceAdjustmentResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(PriceAdjustmentResponse, required=False), required=False)
    


class BulkPriceAdjustmentAddRequest(BaseSchema):
    # Cart swagger.json

    
    cart_id = fields.Str(required=False)
    
    is_authenticated = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(BulkPriceAdjustmentAdd, required=False), required=False)
    


