"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class Page(BaseSchema):
    pass


class Rule(BaseSchema):
    pass


class CouponAction(BaseSchema):
    pass


class Validity(BaseSchema):
    pass


class CouponAuthor(BaseSchema):
    pass


class State(BaseSchema):
    pass


class Ownership(BaseSchema):
    pass


class CouponSchedule(BaseSchema):
    pass


class Identifier(BaseSchema):
    pass


class DisplayMetaDict(BaseSchema):
    pass


class DisplayMeta(BaseSchema):
    pass


class RuleDefinition(BaseSchema):
    pass


class CouponDateMeta(BaseSchema):
    pass


class Validation(BaseSchema):
    pass


class BulkBundleRestriction(BaseSchema):
    pass


class PriceRange(BaseSchema):
    pass


class PaymentAllowValue(BaseSchema):
    pass


class PaymentModes(BaseSchema):
    pass


class UsesRemaining(BaseSchema):
    pass


class UsesRestriction(BaseSchema):
    pass


class PostOrder(BaseSchema):
    pass


class Restrictions(BaseSchema):
    pass


class CouponAdd(BaseSchema):
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


class DisplayMeta1(BaseSchema):
    pass


class PaymentAllowValue1(BaseSchema):
    pass


class PromotionPaymentModes(BaseSchema):
    pass


class UsesRemaining1(BaseSchema):
    pass


class UsesRestriction1(BaseSchema):
    pass


class PostOrder1(BaseSchema):
    pass


class UserRegistered(BaseSchema):
    pass


class Restrictions1(BaseSchema):
    pass


class Visibility(BaseSchema):
    pass


class PromotionSchedule(BaseSchema):
    pass


class PromotionAuthor(BaseSchema):
    pass


class PromotionDateMeta(BaseSchema):
    pass


class PromotionAction(BaseSchema):
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


class CartItem(BaseSchema):
    pass


class OpenapiCartDetailsRequest(BaseSchema):
    pass


class ProductImage(BaseSchema):
    pass


class ActionQuery(BaseSchema):
    pass


class ProductAction(BaseSchema):
    pass


class CategoryInfo(BaseSchema):
    pass


class NetQuantity(BaseSchema):
    pass


class BaseInfo(BaseSchema):
    pass


class CartProduct(BaseSchema):
    pass


class ProductPrice(BaseSchema):
    pass


class ProductPriceInfo(BaseSchema):
    pass


class BasePrice(BaseSchema):
    pass


class ArticlePriceInfo(BaseSchema):
    pass


class ProductArticle(BaseSchema):
    pass


class ProductAvailabilitySize(BaseSchema):
    pass


class ProductAvailability(BaseSchema):
    pass


class PromoMeta(BaseSchema):
    pass


class CartProductIdentifer(BaseSchema):
    pass


class FreeGiftItem(BaseSchema):
    pass


class AppliedFreeArticles(BaseSchema):
    pass


class BuyRules(BaseSchema):
    pass


class Ownership2(BaseSchema):
    pass


class DiscountRulesApp(BaseSchema):
    pass


class AppliedPromotion(BaseSchema):
    pass


class PromiseTimestamp(BaseSchema):
    pass


class PromiseFormatted(BaseSchema):
    pass


class ShipmentPromise(BaseSchema):
    pass


class CartProductInfo(BaseSchema):
    pass


class DisplayBreakup(BaseSchema):
    pass


class CouponBreakup(BaseSchema):
    pass


class RawBreakup(BaseSchema):
    pass


class LoyaltyPoints(BaseSchema):
    pass


class CartBreakup(BaseSchema):
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


class MultiTenderPaymentMeta(BaseSchema):
    pass


class MultiTenderPaymentMethod(BaseSchema):
    pass


class OpenApiFiles(BaseSchema):
    pass


class CartItemMeta(BaseSchema):
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


class CartCurrency(BaseSchema):
    pass


class PaymentSelectionLock(BaseSchema):
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


class StaffCheckout(BaseSchema):
    pass


class Files(BaseSchema):
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





class Page(BaseSchema):
    # Cart swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class Rule(BaseSchema):
    # Cart swagger.json

    
    key = fields.Float(required=False)
    
    discount_qty = fields.Float(required=False)
    
    value = fields.Float(required=False)
    
    max = fields.Float(required=False)
    
    min = fields.Float(required=False)
    


class CouponAction(BaseSchema):
    # Cart swagger.json

    
    txn_mode = fields.Str(required=False)
    
    action_date = fields.Str(required=False)
    


class Validity(BaseSchema):
    # Cart swagger.json

    
    priority = fields.Int(required=False)
    


class CouponAuthor(BaseSchema):
    # Cart swagger.json

    
    modified_by = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    


class State(BaseSchema):
    # Cart swagger.json

    
    is_display = fields.Boolean(required=False)
    
    is_public = fields.Boolean(required=False)
    
    is_archived = fields.Boolean(required=False)
    


class Ownership(BaseSchema):
    # Cart swagger.json

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    


class CouponSchedule(BaseSchema):
    # Cart swagger.json

    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    
    end = fields.Str(required=False)
    
    cron = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    


class Identifier(BaseSchema):
    # Cart swagger.json

    
    brand_id = fields.List(fields.Int(required=False), required=False)
    
    item_id = fields.List(fields.Int(required=False), required=False)
    
    exclude_brand_id = fields.List(fields.Int(required=False), required=False)
    
    collection_id = fields.List(fields.Str(required=False), required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    store_id = fields.List(fields.Int(required=False), required=False)
    
    company_id = fields.List(fields.Int(required=False), required=False)
    
    article_id = fields.List(fields.Str(required=False), required=False)
    
    category_id = fields.List(fields.Int(required=False), required=False)
    


class DisplayMetaDict(BaseSchema):
    # Cart swagger.json

    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class DisplayMeta(BaseSchema):
    # Cart swagger.json

    
    title = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    apply = fields.Nested(DisplayMetaDict, required=False)
    
    auto = fields.Nested(DisplayMetaDict, required=False)
    
    remove = fields.Nested(DisplayMetaDict, required=False)
    
    description = fields.Str(required=False)
    


class RuleDefinition(BaseSchema):
    # Cart swagger.json

    
    is_exact = fields.Boolean(required=False)
    
    scope = fields.List(fields.Str(required=False), required=False)
    
    value_type = fields.Str(required=False)
    
    applicable_on = fields.Str(required=False)
    
    calculate_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    auto_apply = fields.Boolean(required=False)
    
    currency_code = fields.Str(required=False)
    


class CouponDateMeta(BaseSchema):
    # Cart swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class Validation(BaseSchema):
    # Cart swagger.json

    
    user_registered_after = fields.Str(required=False)
    
    app_id = fields.List(fields.Str(required=False), required=False)
    
    anonymous = fields.Boolean(required=False)
    


class BulkBundleRestriction(BaseSchema):
    # Cart swagger.json

    
    multi_store_allowed = fields.Boolean(required=False)
    


class PriceRange(BaseSchema):
    # Cart swagger.json

    
    max = fields.Int(required=False)
    
    min = fields.Int(required=False)
    


class PaymentAllowValue(BaseSchema):
    # Cart swagger.json

    
    max = fields.Int(required=False)
    


class PaymentModes(BaseSchema):
    # Cart swagger.json

    
    types = fields.List(fields.Str(required=False), required=False)
    
    uses = fields.Nested(PaymentAllowValue, required=False)
    
    codes = fields.List(fields.Str(required=False), required=False)
    
    networks = fields.List(fields.Str(required=False), required=False)
    


class UsesRemaining(BaseSchema):
    # Cart swagger.json

    
    total = fields.Int(required=False)
    
    app = fields.Int(required=False)
    
    user = fields.Int(required=False)
    


class UsesRestriction(BaseSchema):
    # Cart swagger.json

    
    remaining = fields.Nested(UsesRemaining, required=False)
    
    maximum = fields.Nested(UsesRemaining, required=False)
    


class PostOrder(BaseSchema):
    # Cart swagger.json

    
    return_allowed = fields.Boolean(required=False)
    
    cancellation_allowed = fields.Boolean(required=False)
    


class Restrictions(BaseSchema):
    # Cart swagger.json

    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    payments = fields.Dict(required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    user_type = fields.Str(required=False)
    
    post_order = fields.Nested(PostOrder, required=False)
    
    coupon_allowed = fields.Boolean(required=False)
    


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    type_slug = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    code = fields.Str(required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    


class CouponsResponse(BaseSchema):
    # Cart swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.Nested(CouponAdd, required=False)
    


class SuccessMessage(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class OperationErrorResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    type_slug = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    code = fields.Str(required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    


class CouponPartialUpdate(BaseSchema):
    # Cart swagger.json

    
    schedule = fields.Nested(CouponSchedule, required=False)
    
    archive = fields.Boolean(required=False)
    


class Ownership1(BaseSchema):
    # Cart swagger.json

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    


class CompareObject(BaseSchema):
    # Cart swagger.json

    
    equals = fields.Float(required=False)
    
    less_than_equals = fields.Float(required=False)
    
    less_than = fields.Float(required=False)
    
    greater_than_equals = fields.Float(required=False)
    
    greater_than = fields.Float(required=False)
    


class ItemCriteria(BaseSchema):
    # Cart swagger.json

    
    item_size = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_id = fields.List(fields.Int(required=False), required=False)
    
    available_zones = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_brand = fields.List(fields.Int(required=False), required=False)
    
    item_company = fields.List(fields.Int(required=False), required=False)
    
    item_sku = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_store = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_sku = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_category = fields.List(fields.Int(required=False), required=False)
    
    cart_unique_item_amount = fields.Nested(CompareObject, required=False)
    
    item_exclude_company = fields.List(fields.Int(required=False), required=False)
    
    cart_unique_item_quantity = fields.Nested(CompareObject, required=False)
    
    all_items = fields.Boolean(required=False)
    
    item_brand = fields.List(fields.Int(required=False), required=False)
    
    item_category = fields.List(fields.Int(required=False), required=False)
    
    cart_quantity = fields.Nested(CompareObject, required=False)
    
    item_id = fields.List(fields.Int(required=False), required=False)
    
    buy_rules = fields.List(fields.Str(required=False), required=False)
    
    cart_total = fields.Nested(CompareObject, required=False)
    
    product_tags = fields.List(fields.Str(required=False), required=False)
    
    item_store = fields.List(fields.Int(required=False), required=False)
    


class DiscountOffer(BaseSchema):
    # Cart swagger.json

    
    apportion_discount = fields.Boolean(required=False)
    
    discount_percentage = fields.Float(required=False)
    
    max_discount_amount = fields.Float(required=False)
    
    max_usage_per_transaction = fields.Int(required=False)
    
    partial_can_ret = fields.Boolean(required=False)
    
    min_offer_quantity = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    discount_amount = fields.Float(required=False)
    
    discount_price = fields.Float(required=False)
    
    max_offer_quantity = fields.Int(required=False)
    


class DiscountRule(BaseSchema):
    # Cart swagger.json

    
    buy_condition = fields.Str(required=False)
    
    item_criteria = fields.Nested(ItemCriteria, required=False)
    
    offer = fields.Nested(DiscountOffer, required=False)
    
    discount_type = fields.Str(required=False)
    


class DisplayMeta1(BaseSchema):
    # Cart swagger.json

    
    offer_text = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    offer_label = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class PaymentAllowValue1(BaseSchema):
    # Cart swagger.json

    
    max = fields.Int(required=False)
    


class PromotionPaymentModes(BaseSchema):
    # Cart swagger.json

    
    uses = fields.Nested(PaymentAllowValue1, required=False)
    
    type = fields.Str(required=False)
    
    codes = fields.List(fields.Str(required=False), required=False)
    


class UsesRemaining1(BaseSchema):
    # Cart swagger.json

    
    total = fields.Int(required=False)
    
    user = fields.Int(required=False)
    


class UsesRestriction1(BaseSchema):
    # Cart swagger.json

    
    remaining = fields.Nested(UsesRemaining1, required=False)
    
    maximum = fields.Nested(UsesRemaining1, required=False)
    


class PostOrder1(BaseSchema):
    # Cart swagger.json

    
    return_allowed = fields.Boolean(required=False)
    
    cancellation_allowed = fields.Boolean(required=False)
    


class UserRegistered(BaseSchema):
    # Cart swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class Restrictions1(BaseSchema):
    # Cart swagger.json

    
    order_quantity = fields.Int(required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    payments = fields.List(fields.Nested(PromotionPaymentModes, required=False), required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    uses = fields.Nested(UsesRestriction1, required=False)
    
    anonymous_users = fields.Boolean(required=False)
    
    post_order = fields.Nested(PostOrder1, required=False)
    
    user_registered = fields.Nested(UserRegistered, required=False)
    


class Visibility(BaseSchema):
    # Cart swagger.json

    
    pdp = fields.Boolean(required=False)
    
    coupon_list = fields.Boolean(required=False)
    


class PromotionSchedule(BaseSchema):
    # Cart swagger.json

    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    
    end = fields.Str(required=False)
    
    cron = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    start = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    


class PromotionAuthor(BaseSchema):
    # Cart swagger.json

    
    modified_by = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    


class PromotionDateMeta(BaseSchema):
    # Cart swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class PromotionAction(BaseSchema):
    # Cart swagger.json

    
    action_date = fields.Str(required=False)
    
    action_type = fields.Str(required=False)
    


class PromotionListItem(BaseSchema):
    # Cart swagger.json

    
    mode = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    promo_group = fields.Str(required=False)
    
    apply_priority = fields.Int(required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    calculate_on = fields.Str(required=False)
    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    code = fields.Str(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    buy_rules = fields.Dict(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    stackable = fields.Boolean(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    


class PromotionsResponse(BaseSchema):
    # Cart swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.Nested(PromotionListItem, required=False)
    


class PromotionAdd(BaseSchema):
    # Cart swagger.json

    
    mode = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    promo_group = fields.Str(required=False)
    
    apply_priority = fields.Int(required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    calculate_on = fields.Str(required=False)
    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    code = fields.Str(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    buy_rules = fields.Dict(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    stackable = fields.Boolean(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    


class PromotionUpdate(BaseSchema):
    # Cart swagger.json

    
    mode = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    promo_group = fields.Str(required=False)
    
    apply_priority = fields.Int(required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    calculate_on = fields.Str(required=False)
    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    code = fields.Str(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    buy_rules = fields.Dict(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    stackable = fields.Boolean(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    


class PromotionPartialUpdate(BaseSchema):
    # Cart swagger.json

    
    schedule = fields.Nested(PromotionSchedule, required=False)
    
    archive = fields.Boolean(required=False)
    


class ActivePromosResponse(BaseSchema):
    # Cart swagger.json

    
    example = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    is_hidden = fields.Boolean(required=False)
    
    subtitle = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    entity_slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class CartItem(BaseSchema):
    # Cart swagger.json

    
    size = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    product_id = fields.Str(required=False)
    


class OpenapiCartDetailsRequest(BaseSchema):
    # Cart swagger.json

    
    cart_items = fields.Nested(CartItem, required=False)
    


class ProductImage(BaseSchema):
    # Cart swagger.json

    
    url = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    


class ActionQuery(BaseSchema):
    # Cart swagger.json

    
    product_slug = fields.List(fields.Str(required=False), required=False)
    


class ProductAction(BaseSchema):
    # Cart swagger.json

    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    query = fields.Nested(ActionQuery, required=False)
    


class CategoryInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class NetQuantity(BaseSchema):
    # Cart swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class BaseInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class CartProduct(BaseSchema):
    # Cart swagger.json

    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    name = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    type = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    


class ProductPrice(BaseSchema):
    # Cart swagger.json

    
    marked = fields.Float(required=False)
    
    add_on = fields.Float(required=False)
    
    selling = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class ProductPriceInfo(BaseSchema):
    # Cart swagger.json

    
    base = fields.Nested(ProductPrice, required=False)
    
    converted = fields.Nested(ProductPrice, required=False)
    


class BasePrice(BaseSchema):
    # Cart swagger.json

    
    currency_code = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class ArticlePriceInfo(BaseSchema):
    # Cart swagger.json

    
    base = fields.Nested(BasePrice, required=False)
    
    converted = fields.Nested(BasePrice, required=False)
    


class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    size = fields.Str(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    


class ProductAvailabilitySize(BaseSchema):
    # Cart swagger.json

    
    value = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    


class ProductAvailability(BaseSchema):
    # Cart swagger.json

    
    available_sizes = fields.List(fields.Nested(ProductAvailabilitySize, required=False), required=False)
    
    deliverable = fields.Boolean(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    other_store_quantity = fields.Int(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    out_of_stock = fields.Boolean(required=False)
    


class PromoMeta(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    


class CartProductIdentifer(BaseSchema):
    # Cart swagger.json

    
    identifier = fields.Str(required=False)
    


class FreeGiftItem(BaseSchema):
    # Cart swagger.json

    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    
    item_name = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    item_brand_name = fields.Str(required=False)
    
    item_slug = fields.Str(required=False)
    
    item_price_details = fields.Dict(required=False)
    


class AppliedFreeArticles(BaseSchema):
    # Cart swagger.json

    
    free_gift_item_details = fields.Nested(FreeGiftItem, required=False)
    
    quantity = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    


class BuyRules(BaseSchema):
    # Cart swagger.json

    
    cart_conditions = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    


class Ownership2(BaseSchema):
    # Cart swagger.json

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    


class DiscountRulesApp(BaseSchema):
    # Cart swagger.json

    
    raw_offer = fields.Dict(required=False)
    
    offer = fields.Dict(required=False)
    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    
    item_criteria = fields.Dict(required=False)
    


class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    
    promo_id = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    offer_text = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership2, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesApp, required=False), required=False)
    
    article_quantity = fields.Int(required=False)
    
    promotion_group = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    


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
    


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    is_set = fields.Boolean(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    coupon_message = fields.Str(required=False)
    
    moq = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    message = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class DisplayBreakup(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    message = fields.List(fields.Str(required=False), required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class CouponBreakup(BaseSchema):
    # Cart swagger.json

    
    max_discount_value = fields.Float(required=False)
    
    title = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    coupon_type = fields.Str(required=False)
    
    sub_title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class RawBreakup(BaseSchema):
    # Cart swagger.json

    
    mrp_total = fields.Float(required=False)
    
    gst_charges = fields.Float(required=False)
    
    coupon = fields.Float(required=False)
    
    cod_charge = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    fynd_cash = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    subtotal = fields.Float(required=False)
    
    vog = fields.Float(required=False)
    
    convenience_fee = fields.Float(required=False)
    
    you_saved = fields.Float(required=False)
    
    total = fields.Float(required=False)
    


class LoyaltyPoints(BaseSchema):
    # Cart swagger.json

    
    total = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    applicable = fields.Float(required=False)
    
    description = fields.Str(required=False)
    


class CartBreakup(BaseSchema):
    # Cart swagger.json

    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    


class OpenapiCartDetailsResponse(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    


class OpenApiErrorResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    errors = fields.Dict(required=False)
    


class ShippingAddress(BaseSchema):
    # Cart swagger.json

    
    country_phone_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    phone = fields.Int(required=False)
    
    address_type = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    landmark = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    address = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class OpenApiCartServiceabilityRequest(BaseSchema):
    # Cart swagger.json

    
    cart_items = fields.Nested(CartItem, required=False)
    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    


class OpenApiCartServiceabilityResponse(BaseSchema):
    # Cart swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    message = fields.Str(required=False)
    


class MultiTenderPaymentMeta(BaseSchema):
    # Cart swagger.json

    
    current_status = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    


class MultiTenderPaymentMethod(BaseSchema):
    # Cart swagger.json

    
    mode = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Nested(MultiTenderPaymentMeta, required=False)
    


class OpenApiFiles(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    values = fields.List(fields.Str(required=False), required=False)
    


class CartItemMeta(BaseSchema):
    # Cart swagger.json

    
    primary_item = fields.Boolean(required=False)
    
    group_id = fields.Str(required=False)
    


class OpenApiOrderItem(BaseSchema):
    # Cart swagger.json

    
    coupon_effective_discount = fields.Float(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    price_marked = fields.Float(required=False)
    
    employee_discount = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    product_id = fields.Int(required=False)
    
    amount_paid = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    meta = fields.Nested(CartItemMeta, required=False)
    
    extra_meta = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    


class OpenApiPlatformCheckoutReq(BaseSchema):
    # Cart swagger.json

    
    cart_value = fields.Float(required=False)
    
    comment = fields.Str(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    payment_mode = fields.Str(required=False)
    
    employee_discount = fields.Dict(required=False)
    
    cod_charges = fields.Float(required=False)
    
    cart_items = fields.List(fields.Nested(OpenApiOrderItem, required=False), required=False)
    
    gstin = fields.Str(required=False)
    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    
    order_id = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    coupon = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    
    billing_address = fields.Nested(ShippingAddress, required=False)
    
    coupon_value = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    


class OpenApiCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    order_ref_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    


class AbandonedCart(BaseSchema):
    # Cart swagger.json

    
    cart_value = fields.Float(required=False)
    
    comment = fields.Str(required=False)
    
    expire_at = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    bulk_coupon_discount = fields.Float(required=False)
    
    uid = fields.Int(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    order_id = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    
    shipments = fields.List(fields.Dict(required=False), required=False)
    
    is_default = fields.Boolean(required=False)
    
    promotion = fields.Dict(required=False)
    
    coupon = fields.Dict(required=False)
    
    merge_qty = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    is_archive = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    cashback = fields.Dict(required=False)
    
    payment_methods = fields.List(fields.Dict(required=False), required=False)
    
    cod_charges = fields.Dict(required=False)
    
    user_id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    fc_index_map = fields.List(fields.Int(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    discount = fields.Float(required=False)
    
    last_modified = fields.Str(required=False)
    
    payments = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    fynd_credits = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    delivery_charges = fields.Dict(required=False)
    


class AbandonedCartResponse(BaseSchema):
    # Cart swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(AbandonedCart, required=False), required=False)
    
    message = fields.Str(required=False)
    
    result = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    


class CartCurrency(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    


class PaymentSelectionLock(BaseSchema):
    # Cart swagger.json

    
    enabled = fields.Boolean(required=False)
    
    default_options = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    


class CartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    comment = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    pan_no = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    coupon_text = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    pan_config = fields.Dict(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    message = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    last_modified = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    buy_now = fields.Boolean(required=False)
    


class AddProductCart(BaseSchema):
    # Cart swagger.json

    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    item_size = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    seller_id = fields.Int(required=False)
    
    display = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    store_id = fields.Int(required=False)
    
    pos = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    article_assignment = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    


class AddCartRequest(BaseSchema):
    # Cart swagger.json

    
    new_cart = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    


class AddCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    partial = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class UpdateProductCart(BaseSchema):
    # Cart swagger.json

    
    item_size = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    item_index = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    


class UpdateCartRequest(BaseSchema):
    # Cart swagger.json

    
    operation = fields.Str(required=False)
    
    items = fields.List(fields.Nested(UpdateProductCart, required=False), required=False)
    


class UpdateCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class GetShareCartLinkRequest(BaseSchema):
    # Cart swagger.json

    
    meta = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    


class GetShareCartLinkResponse(BaseSchema):
    # Cart swagger.json

    
    share_url = fields.Str(required=False)
    
    token = fields.Str(required=False)
    


class SharedCartDetails(BaseSchema):
    # Cart swagger.json

    
    user = fields.Dict(required=False)
    
    token = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    source = fields.Dict(required=False)
    


class SharedCart(BaseSchema):
    # Cart swagger.json

    
    comment = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    uid = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    coupon_text = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    
    id = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    message = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    last_modified = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    buy_now = fields.Boolean(required=False)
    
    cart_id = fields.Int(required=False)
    


class SharedCartResponse(BaseSchema):
    # Cart swagger.json

    
    cart = fields.Nested(SharedCart, required=False)
    
    error = fields.Str(required=False)
    


class CartList(BaseSchema):
    # Cart swagger.json

    
    cart_value = fields.Float(required=False)
    
    item_counts = fields.Int(required=False)
    
    user_id = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    


class MultiCartResponse(BaseSchema):
    # Cart swagger.json

    
    data = fields.List(fields.Nested(CartList, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class UpdateUserCartMapping(BaseSchema):
    # Cart swagger.json

    
    user_id = fields.Str(required=False)
    


class UserInfo(BaseSchema):
    # Cart swagger.json

    
    mobile = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    external_id = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class UserCartMappingResponse(BaseSchema):
    # Cart swagger.json

    
    comment = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    pan_no = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    coupon_text = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    user = fields.Nested(UserInfo, required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    pan_config = fields.Dict(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    message = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    last_modified = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    buy_now = fields.Boolean(required=False)
    


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

    
    max_discount_value = fields.Float(required=False)
    
    title = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    
    expires_on = fields.Str(required=False)
    
    is_applicable = fields.Boolean(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    coupon_type = fields.Str(required=False)
    
    sub_title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class PageCoupon(BaseSchema):
    # Cart swagger.json

    
    current = fields.Int(required=False)
    
    total_item_count = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    total = fields.Int(required=False)
    
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

    
    name = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    google_map_point = fields.Dict(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    address_type = fields.Str(required=False)
    
    geo_location = fields.Nested(GeoLocation, required=False)
    
    landmark = fields.Str(required=False)
    
    created_by_user_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    country_code = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    cart_id = fields.Str(required=False)
    
    address = fields.Str(required=False)
    


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
    
    billing_address_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    


class ShipmentResponse(BaseSchema):
    # Cart swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    promise = fields.Nested(ShipmentPromise, required=False)
    
    dp_options = fields.Dict(required=False)
    
    dp_id = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    box_type = fields.Str(required=False)
    
    shipments = fields.Int(required=False)
    
    fulfillment_type = fields.Str(required=False)
    


class CartShipmentsResponse(BaseSchema):
    # Cart swagger.json

    
    comment = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    error = fields.Boolean(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    message = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    last_modified = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    


class UpdateCartShipmentItem(BaseSchema):
    # Cart swagger.json

    
    shipment_type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    article_uid = fields.Str(required=False)
    


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
    


class StaffCheckout(BaseSchema):
    # Cart swagger.json

    
    user = fields.Str(required=False)
    
    employee_code = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    


class Files(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    values = fields.List(fields.Str(required=False), required=False)
    


class PlatformCartCheckoutDetailRequest(BaseSchema):
    # Cart swagger.json

    
    payment_mode = fields.Str(required=False)
    
    employee_code = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    staff = fields.Nested(StaffCheckout, required=False)
    
    address_id = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    callback_url = fields.Str(required=False)
    
    payment_params = fields.Dict(required=False)
    
    pos = fields.Boolean(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    ordering_store = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    device_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    files = fields.List(fields.Nested(Files, required=False), required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    merchant_code = fields.Str(required=False)
    
    billing_address = fields.Dict(required=False)
    
    pick_at_store_uid = fields.Int(required=False)
    


class CheckCart(BaseSchema):
    # Cart swagger.json

    
    comment = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    delivery_charge_order_value = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    coupon_text = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    error_message = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    cod_available = fields.Boolean(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    store_emps = fields.List(fields.Dict(required=False), required=False)
    
    id = fields.Str(required=False)
    
    cod_charges = fields.Int(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    cod_message = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    user_type = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    buy_now = fields.Boolean(required=False)
    
    cart_id = fields.Int(required=False)
    
    delivery_charges = fields.Int(required=False)
    


class CartCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    cart = fields.Nested(CheckCart, required=False)
    
    callback_url = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    payment_confirm_url = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    app_intercept_url = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class CartDeliveryModesResponse(BaseSchema):
    # Cart swagger.json

    
    pickup_stores = fields.List(fields.Int(required=False), required=False)
    
    available_modes = fields.List(fields.Str(required=False), required=False)
    


class PickupStoreDetail(BaseSchema):
    # Cart swagger.json

    
    store_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    email = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    address_type = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    landmark = fields.Str(required=False)
    
    address = fields.Str(required=False)
    


class StoreDetailsResponse(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(PickupStoreDetail, required=False), required=False)
    


class UpdateCartPaymentRequest(BaseSchema):
    # Cart swagger.json

    
    payment_mode = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    address_id = fields.Str(required=False)
    


class CouponValidity(BaseSchema):
    # Cart swagger.json

    
    display_message_en = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    valid = fields.Boolean(required=False)
    


class PaymentCouponValidate(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    coupon_validity = fields.Nested(CouponValidity, required=False)
    


