"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



class Page(BaseSchema):
    pass


class UsesRemaining(BaseSchema):
    pass


class UsesRestriction(BaseSchema):
    pass


class PostOrder(BaseSchema):
    pass


class PriceRange(BaseSchema):
    pass


class BulkBundleRestriction(BaseSchema):
    pass


class PaymentAllowValue(BaseSchema):
    pass


class PaymentModes(BaseSchema):
    pass


class Restrictions(BaseSchema):
    pass


class Rule(BaseSchema):
    pass


class DisplayMetaDict(BaseSchema):
    pass


class DisplayMeta(BaseSchema):
    pass


class Validity(BaseSchema):
    pass


class CouponAuthor(BaseSchema):
    pass


class CouponAction(BaseSchema):
    pass


class Identifier(BaseSchema):
    pass


class RuleDefinition(BaseSchema):
    pass


class CouponDateMeta(BaseSchema):
    pass


class CouponSchedule(BaseSchema):
    pass


class State(BaseSchema):
    pass


class Ownership(BaseSchema):
    pass


class Validation(BaseSchema):
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


class DisplayMeta1(BaseSchema):
    pass


class PromotionAction(BaseSchema):
    pass


class PromotionSchedule(BaseSchema):
    pass


class Visibility(BaseSchema):
    pass


class UsesRemaining1(BaseSchema):
    pass


class UsesRestriction1(BaseSchema):
    pass


class PostOrder1(BaseSchema):
    pass


class UserRegistered(BaseSchema):
    pass


class PaymentAllowValue1(BaseSchema):
    pass


class PromotionPaymentModes(BaseSchema):
    pass


class Restrictions1(BaseSchema):
    pass


class CompareObject(BaseSchema):
    pass


class ItemCriteria(BaseSchema):
    pass


class PromotionAuthor(BaseSchema):
    pass


class PromotionDateMeta(BaseSchema):
    pass


class DiscountOffer(BaseSchema):
    pass


class DiscountRule(BaseSchema):
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


class ProductAvailability(BaseSchema):
    pass


class PromoMeta(BaseSchema):
    pass


class ProductPrice(BaseSchema):
    pass


class ProductPriceInfo(BaseSchema):
    pass


class CartProductIdentifer(BaseSchema):
    pass


class BuyRules(BaseSchema):
    pass


class DiscountRulesApp(BaseSchema):
    pass


class FreeGiftItem(BaseSchema):
    pass


class AppliedFreeArticles(BaseSchema):
    pass


class AppliedPromotion(BaseSchema):
    pass


class BaseInfo(BaseSchema):
    pass


class BasePrice(BaseSchema):
    pass


class ArticlePriceInfo(BaseSchema):
    pass


class ProductArticle(BaseSchema):
    pass


class ProductImage(BaseSchema):
    pass


class CategoryInfo(BaseSchema):
    pass


class ActionQuery(BaseSchema):
    pass


class ProductAction(BaseSchema):
    pass


class NetQuantity(BaseSchema):
    pass


class CartProduct(BaseSchema):
    pass


class CartProductInfo(BaseSchema):
    pass


class CouponBreakup(BaseSchema):
    pass


class RawBreakup(BaseSchema):
    pass


class DisplayBreakup(BaseSchema):
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


class PromiseTimestamp(BaseSchema):
    pass


class PromiseFormatted(BaseSchema):
    pass


class ShipmentPromise(BaseSchema):
    pass


class OpenApiCartServiceabilityResponse(BaseSchema):
    pass


class MultiTenderPaymentMeta(BaseSchema):
    pass


class MultiTenderPaymentMethod(BaseSchema):
    pass


class CartItemMeta(BaseSchema):
    pass


class OpenApiFiles(BaseSchema):
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



class Page(BaseSchema):
    # Cart swagger.json

    
    last_id = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    page = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    


class UsesRemaining(BaseSchema):
    # Cart swagger.json

    
    total = fields.Int(required=False)
    
    user = fields.Int(required=False)
    
    app = fields.Int(required=False)
    


class UsesRestriction(BaseSchema):
    # Cart swagger.json

    
    maximum = fields.Nested(UsesRemaining, required=False)
    
    remaining = fields.Nested(UsesRemaining, required=False)
    


class PostOrder(BaseSchema):
    # Cart swagger.json

    
    cancellation_allowed = fields.Boolean(required=False)
    
    return_allowed = fields.Boolean(required=False)
    


class PriceRange(BaseSchema):
    # Cart swagger.json

    
    max = fields.Int(required=False)
    
    min = fields.Int(required=False)
    


class BulkBundleRestriction(BaseSchema):
    # Cart swagger.json

    
    multi_store_allowed = fields.Boolean(required=False)
    


class PaymentAllowValue(BaseSchema):
    # Cart swagger.json

    
    max = fields.Int(required=False)
    


class PaymentModes(BaseSchema):
    # Cart swagger.json

    
    networks = fields.List(fields.Str(required=False), required=False)
    
    types = fields.List(fields.Str(required=False), required=False)
    
    uses = fields.Nested(PaymentAllowValue, required=False)
    
    codes = fields.List(fields.Str(required=False), required=False)
    


class Restrictions(BaseSchema):
    # Cart swagger.json

    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    coupon_allowed = fields.Boolean(required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
    post_order = fields.Nested(PostOrder, required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    user_type = fields.Str(required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    payments = fields.Dict(required=False)
    


class Rule(BaseSchema):
    # Cart swagger.json

    
    key = fields.Float(required=False)
    
    min = fields.Float(required=False)
    
    discount_qty = fields.Float(required=False)
    
    max = fields.Float(required=False)
    
    value = fields.Float(required=False)
    


class DisplayMetaDict(BaseSchema):
    # Cart swagger.json

    
    title = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    


class DisplayMeta(BaseSchema):
    # Cart swagger.json

    
    remove = fields.Nested(DisplayMetaDict, required=False)
    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    apply = fields.Nested(DisplayMetaDict, required=False)
    
    description = fields.Str(required=False)
    
    auto = fields.Nested(DisplayMetaDict, required=False)
    


class Validity(BaseSchema):
    # Cart swagger.json

    
    priority = fields.Int(required=False)
    


class CouponAuthor(BaseSchema):
    # Cart swagger.json

    
    modified_by = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    


class CouponAction(BaseSchema):
    # Cart swagger.json

    
    txn_mode = fields.Str(required=False)
    
    action_date = fields.Str(required=False)
    


class Identifier(BaseSchema):
    # Cart swagger.json

    
    company_id = fields.List(fields.Int(required=False), required=False)
    
    brand_id = fields.List(fields.Int(required=False), required=False)
    
    exclude_brand_id = fields.List(fields.Int(required=False), required=False)
    
    store_id = fields.List(fields.Int(required=False), required=False)
    
    category_id = fields.List(fields.Int(required=False), required=False)
    
    article_id = fields.List(fields.Str(required=False), required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    item_id = fields.List(fields.Int(required=False), required=False)
    
    collection_id = fields.List(fields.Str(required=False), required=False)
    


class RuleDefinition(BaseSchema):
    # Cart swagger.json

    
    currency_code = fields.Str(required=False)
    
    scope = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    auto_apply = fields.Boolean(required=False)
    
    value_type = fields.Str(required=False)
    
    applicable_on = fields.Str(required=False)
    
    is_exact = fields.Boolean(required=False)
    
    calculate_on = fields.Str(required=False)
    


class CouponDateMeta(BaseSchema):
    # Cart swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class CouponSchedule(BaseSchema):
    # Cart swagger.json

    
    cron = fields.Str(required=False)
    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    
    start = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    
    end = fields.Str(required=False)
    


class State(BaseSchema):
    # Cart swagger.json

    
    is_archived = fields.Boolean(required=False)
    
    is_display = fields.Boolean(required=False)
    
    is_public = fields.Boolean(required=False)
    


class Ownership(BaseSchema):
    # Cart swagger.json

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    


class Validation(BaseSchema):
    # Cart swagger.json

    
    app_id = fields.List(fields.Str(required=False), required=False)
    
    user_registered_after = fields.Str(required=False)
    
    anonymous = fields.Boolean(required=False)
    


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    code = fields.Str(required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    state = fields.Nested(State, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    type_slug = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    


class CouponsResponse(BaseSchema):
    # Cart swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.Nested(CouponAdd, required=False)
    


class SuccessMessage(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class OperationErrorResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    code = fields.Str(required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    state = fields.Nested(State, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    type_slug = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    


class CouponPartialUpdate(BaseSchema):
    # Cart swagger.json

    
    archive = fields.Boolean(required=False)
    
    schedule = fields.Nested(CouponSchedule, required=False)
    


class Ownership1(BaseSchema):
    # Cart swagger.json

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    


class DisplayMeta1(BaseSchema):
    # Cart swagger.json

    
    offer_label = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    


class PromotionAction(BaseSchema):
    # Cart swagger.json

    
    action_type = fields.Str(required=False)
    
    action_date = fields.Str(required=False)
    


class PromotionSchedule(BaseSchema):
    # Cart swagger.json

    
    cron = fields.Str(required=False)
    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    
    start = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    
    end = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    


class Visibility(BaseSchema):
    # Cart swagger.json

    
    pdp = fields.Boolean(required=False)
    
    coupon_list = fields.Boolean(required=False)
    


class UsesRemaining1(BaseSchema):
    # Cart swagger.json

    
    total = fields.Int(required=False)
    
    user = fields.Int(required=False)
    


class UsesRestriction1(BaseSchema):
    # Cart swagger.json

    
    maximum = fields.Nested(UsesRemaining1, required=False)
    
    remaining = fields.Nested(UsesRemaining1, required=False)
    


class PostOrder1(BaseSchema):
    # Cart swagger.json

    
    cancellation_allowed = fields.Boolean(required=False)
    
    return_allowed = fields.Boolean(required=False)
    


class UserRegistered(BaseSchema):
    # Cart swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class PaymentAllowValue1(BaseSchema):
    # Cart swagger.json

    
    max = fields.Int(required=False)
    


class PromotionPaymentModes(BaseSchema):
    # Cart swagger.json

    
    type = fields.Str(required=False)
    
    uses = fields.Nested(PaymentAllowValue1, required=False)
    
    codes = fields.List(fields.Str(required=False), required=False)
    


class Restrictions1(BaseSchema):
    # Cart swagger.json

    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    uses = fields.Nested(UsesRestriction1, required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    order_quantity = fields.Int(required=False)
    
    post_order = fields.Nested(PostOrder1, required=False)
    
    user_registered = fields.Nested(UserRegistered, required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    anonymous_users = fields.Boolean(required=False)
    
    payments = fields.List(fields.Nested(PromotionPaymentModes, required=False), required=False)
    


class CompareObject(BaseSchema):
    # Cart swagger.json

    
    greater_than_equals = fields.Float(required=False)
    
    less_than_equals = fields.Float(required=False)
    
    greater_than = fields.Float(required=False)
    
    less_than = fields.Float(required=False)
    
    equals = fields.Float(required=False)
    


class ItemCriteria(BaseSchema):
    # Cart swagger.json

    
    item_exclude_sku = fields.List(fields.Str(required=False), required=False)
    
    all_items = fields.Boolean(required=False)
    
    item_category = fields.List(fields.Int(required=False), required=False)
    
    item_store = fields.List(fields.Int(required=False), required=False)
    
    cart_quantity = fields.Nested(CompareObject, required=False)
    
    item_exclude_id = fields.List(fields.Int(required=False), required=False)
    
    item_id = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_category = fields.List(fields.Int(required=False), required=False)
    
    item_company = fields.List(fields.Int(required=False), required=False)
    
    item_brand = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_store = fields.List(fields.Int(required=False), required=False)
    
    buy_rules = fields.List(fields.Str(required=False), required=False)
    
    item_size = fields.List(fields.Str(required=False), required=False)
    
    product_tags = fields.List(fields.Str(required=False), required=False)
    
    item_sku = fields.List(fields.Str(required=False), required=False)
    
    cart_unique_item_quantity = fields.Nested(CompareObject, required=False)
    
    item_exclude_brand = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_company = fields.List(fields.Int(required=False), required=False)
    
    available_zones = fields.List(fields.Str(required=False), required=False)
    
    cart_unique_item_amount = fields.Nested(CompareObject, required=False)
    
    cart_total = fields.Nested(CompareObject, required=False)
    


class PromotionAuthor(BaseSchema):
    # Cart swagger.json

    
    modified_by = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    


class PromotionDateMeta(BaseSchema):
    # Cart swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class DiscountOffer(BaseSchema):
    # Cart swagger.json

    
    discount_price = fields.Float(required=False)
    
    discount_amount = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    partial_can_ret = fields.Boolean(required=False)
    
    min_offer_quantity = fields.Int(required=False)
    
    discount_percentage = fields.Float(required=False)
    
    max_discount_amount = fields.Float(required=False)
    
    max_offer_quantity = fields.Int(required=False)
    
    max_usage_per_transaction = fields.Int(required=False)
    
    apportion_discount = fields.Boolean(required=False)
    


class DiscountRule(BaseSchema):
    # Cart swagger.json

    
    buy_condition = fields.Str(required=False)
    
    offer = fields.Nested(DiscountOffer, required=False)
    
    item_criteria = fields.Nested(ItemCriteria, required=False)
    
    discount_type = fields.Str(required=False)
    


class PromotionListItem(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    application_id = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    promotion_type = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    promo_group = fields.Str(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    apply_priority = fields.Int(required=False)
    
    calculate_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    stackable = fields.Boolean(required=False)
    
    mode = fields.Str(required=False)
    


class PromotionsResponse(BaseSchema):
    # Cart swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.Nested(PromotionListItem, required=False)
    


class PromotionAdd(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    application_id = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    promotion_type = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    promo_group = fields.Str(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    apply_priority = fields.Int(required=False)
    
    calculate_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    stackable = fields.Boolean(required=False)
    
    mode = fields.Str(required=False)
    


class PromotionUpdate(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    application_id = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    promotion_type = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    promo_group = fields.Str(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    apply_priority = fields.Int(required=False)
    
    calculate_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    stackable = fields.Boolean(required=False)
    
    mode = fields.Str(required=False)
    


class PromotionPartialUpdate(BaseSchema):
    # Cart swagger.json

    
    archive = fields.Boolean(required=False)
    
    schedule = fields.Nested(PromotionSchedule, required=False)
    


class ActivePromosResponse(BaseSchema):
    # Cart swagger.json

    
    subtitle = fields.Str(required=False)
    
    example = fields.Str(required=False)
    
    entity_slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    is_hidden = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class CartItem(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    product_id = fields.Str(required=False)
    


class OpenapiCartDetailsRequest(BaseSchema):
    # Cart swagger.json

    
    cart_items = fields.Nested(CartItem, required=False)
    


class ProductAvailability(BaseSchema):
    # Cart swagger.json

    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    deliverable = fields.Boolean(required=False)
    
    other_store_quantity = fields.Int(required=False)
    


class PromoMeta(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    


class ProductPrice(BaseSchema):
    # Cart swagger.json

    
    currency_code = fields.Str(required=False)
    
    add_on = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    selling = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    


class ProductPriceInfo(BaseSchema):
    # Cart swagger.json

    
    converted = fields.Nested(ProductPrice, required=False)
    
    base = fields.Nested(ProductPrice, required=False)
    


class CartProductIdentifer(BaseSchema):
    # Cart swagger.json

    
    identifier = fields.Str(required=False)
    


class BuyRules(BaseSchema):
    # Cart swagger.json

    
    cart_conditions = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    


class DiscountRulesApp(BaseSchema):
    # Cart swagger.json

    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    
    raw_offer = fields.Dict(required=False)
    
    offer = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    


class FreeGiftItem(BaseSchema):
    # Cart swagger.json

    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    
    item_price_details = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    item_brand_name = fields.Str(required=False)
    
    item_name = fields.Str(required=False)
    
    item_slug = fields.Str(required=False)
    


class AppliedFreeArticles(BaseSchema):
    # Cart swagger.json

    
    parent_item_identifier = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    
    free_gift_item_details = fields.Nested(FreeGiftItem, required=False)
    
    quantity = fields.Int(required=False)
    


class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    mrp_promotion = fields.Boolean(required=False)
    
    promotion_type = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesApp, required=False), required=False)
    
    promotion_group = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    article_quantity = fields.Int(required=False)
    
    promo_id = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    


class BaseInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class BasePrice(BaseSchema):
    # Cart swagger.json

    
    marked = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class ArticlePriceInfo(BaseSchema):
    # Cart swagger.json

    
    converted = fields.Nested(BasePrice, required=False)
    
    base = fields.Nested(BasePrice, required=False)
    


class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    extra_meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    size = fields.Str(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    


class ProductImage(BaseSchema):
    # Cart swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class CategoryInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class ActionQuery(BaseSchema):
    # Cart swagger.json

    
    product_slug = fields.List(fields.Str(required=False), required=False)
    


class ProductAction(BaseSchema):
    # Cart swagger.json

    
    query = fields.Nested(ActionQuery, required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class NetQuantity(BaseSchema):
    # Cart swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class CartProduct(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    name = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    slug = fields.Str(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    availability = fields.Nested(ProductAvailability, required=False)
    
    key = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    coupon_message = fields.Str(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    message = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    is_set = fields.Boolean(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    


class CouponBreakup(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    coupon_type = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    sub_title = fields.Str(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    value = fields.Float(required=False)
    


class RawBreakup(BaseSchema):
    # Cart swagger.json

    
    mrp_total = fields.Float(required=False)
    
    convenience_fee = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    gst_charges = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    cod_charge = fields.Float(required=False)
    
    vog = fields.Float(required=False)
    
    fynd_cash = fields.Float(required=False)
    
    you_saved = fields.Float(required=False)
    
    coupon = fields.Float(required=False)
    
    subtotal = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    


class DisplayBreakup(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    message = fields.List(fields.Str(required=False), required=False)
    
    value = fields.Float(required=False)
    


class LoyaltyPoints(BaseSchema):
    # Cart swagger.json

    
    total = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    applicable = fields.Float(required=False)
    
    description = fields.Str(required=False)
    


class CartBreakup(BaseSchema):
    # Cart swagger.json

    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    


class OpenapiCartDetailsResponse(BaseSchema):
    # Cart swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    message = fields.Str(required=False)
    


class OpenApiErrorResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    errors = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    


class ShippingAddress(BaseSchema):
    # Cart swagger.json

    
    country_code = fields.Str(required=False)
    
    phone = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    city = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class OpenApiCartServiceabilityRequest(BaseSchema):
    # Cart swagger.json

    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    
    cart_items = fields.Nested(CartItem, required=False)
    


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
    


class OpenApiCartServiceabilityResponse(BaseSchema):
    # Cart swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    


class MultiTenderPaymentMeta(BaseSchema):
    # Cart swagger.json

    
    extra_meta = fields.Dict(required=False)
    
    current_status = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    


class MultiTenderPaymentMethod(BaseSchema):
    # Cart swagger.json

    
    meta = fields.Nested(MultiTenderPaymentMeta, required=False)
    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    


class CartItemMeta(BaseSchema):
    # Cart swagger.json

    
    group_id = fields.Str(required=False)
    
    primary_item = fields.Boolean(required=False)
    


class OpenApiFiles(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    values = fields.List(fields.Str(required=False), required=False)
    


class OpenApiOrderItem(BaseSchema):
    # Cart swagger.json

    
    extra_meta = fields.Dict(required=False)
    
    cod_charges = fields.Float(required=False)
    
    employee_discount = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    meta = fields.Nested(CartItemMeta, required=False)
    
    quantity = fields.Int(required=False)
    
    price_effective = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    product_id = fields.Int(required=False)
    
    amount_paid = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    price_marked = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    loyalty_discount = fields.Float(required=False)
    


class OpenApiPlatformCheckoutReq(BaseSchema):
    # Cart swagger.json

    
    cod_charges = fields.Float(required=False)
    
    employee_discount = fields.Dict(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    
    payment_mode = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    order_id = fields.Str(required=False)
    
    cart_items = fields.List(fields.Nested(OpenApiOrderItem, required=False), required=False)
    
    delivery_charges = fields.Float(required=False)
    
    coupon = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    comment = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    billing_address = fields.Nested(ShippingAddress, required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    gstin = fields.Str(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    cart_value = fields.Float(required=False)
    


class OpenApiCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    order_ref_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class AbandonedCart(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    merge_qty = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    is_archive = fields.Boolean(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    
    expire_at = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Dict(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    promotion = fields.Dict(required=False)
    
    gstin = fields.Str(required=False)
    
    shipments = fields.List(fields.Dict(required=False), required=False)
    
    coupon = fields.Dict(required=False)
    
    delivery_charges = fields.Dict(required=False)
    
    cart_value = fields.Float(required=False)
    
    _id = fields.Str(required=False)
    
    fc_index_map = fields.List(fields.Int(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    cod_charges = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    discount = fields.Float(required=False)
    
    user_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    bulk_coupon_discount = fields.Float(required=False)
    
    payments = fields.Dict(required=False)
    
    order_id = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    fynd_credits = fields.Dict(required=False)
    
    cashback = fields.Dict(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    


class AbandonedCartResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    result = fields.Dict(required=False)
    
    page = fields.Nested(Page, required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(AbandonedCart, required=False), required=False)
    


class PaymentSelectionLock(BaseSchema):
    # Cart swagger.json

    
    payment_identifier = fields.Str(required=False)
    
    default_options = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    


class CartCurrency(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    


class CartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    comment = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    


class AddProductCart(BaseSchema):
    # Cart swagger.json

    
    extra_meta = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    pos = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    seller_id = fields.Int(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    item_size = fields.Str(required=False)
    
    article_assignment = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    


class AddCartRequest(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    


class AddCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    partial = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class UpdateProductCart(BaseSchema):
    # Cart swagger.json

    
    extra_meta = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    
    item_index = fields.Int(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    item_id = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    


class UpdateCartRequest(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(UpdateProductCart, required=False), required=False)
    
    operation = fields.Str(required=False)
    


class UpdateCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    message = fields.Str(required=False)
    

