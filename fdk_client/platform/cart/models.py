"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ..PlatformModel import BaseSchema





class BulkBundleRestriction(BaseSchema):
    pass


class PriceRange(BaseSchema):
    pass


class PaymentAllowValue(BaseSchema):
    pass


class PaymentModes(BaseSchema):
    pass


class PostOrder(BaseSchema):
    pass


class UsesRemaining(BaseSchema):
    pass


class UsesRestriction(BaseSchema):
    pass


class Restrictions(BaseSchema):
    pass


class Validity(BaseSchema):
    pass


class Rule(BaseSchema):
    pass


class CouponAction(BaseSchema):
    pass


class CouponSchedule(BaseSchema):
    pass


class State(BaseSchema):
    pass


class DisplayMetaDict(BaseSchema):
    pass


class DisplayMeta(BaseSchema):
    pass


class RuleDefinition(BaseSchema):
    pass


class CouponDateMeta(BaseSchema):
    pass


class CouponAuthor(BaseSchema):
    pass


class Identifier(BaseSchema):
    pass


class Ownership(BaseSchema):
    pass


class Validation(BaseSchema):
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


class PromotionSchedule(BaseSchema):
    pass


class PromotionDateMeta(BaseSchema):
    pass


class Ownership1(BaseSchema):
    pass


class DisplayMeta1(BaseSchema):
    pass


class UserRegistered(BaseSchema):
    pass


class PaymentAllowValue1(BaseSchema):
    pass


class PromotionPaymentModes(BaseSchema):
    pass


class PostOrder1(BaseSchema):
    pass


class UsesRemaining1(BaseSchema):
    pass


class UsesRestriction1(BaseSchema):
    pass


class Restrictions1(BaseSchema):
    pass


class CompareObject(BaseSchema):
    pass


class ItemCriteria(BaseSchema):
    pass


class PromotionAuthor(BaseSchema):
    pass


class DiscountOffer(BaseSchema):
    pass


class DiscountRule(BaseSchema):
    pass


class Visibility(BaseSchema):
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


class DiscountRulesApp(BaseSchema):
    pass


class BuyRules(BaseSchema):
    pass


class FreeGiftItem(BaseSchema):
    pass


class AppliedFreeArticles(BaseSchema):
    pass


class AppliedPromotion(BaseSchema):
    pass


class ProductAvailability(BaseSchema):
    pass


class ProductPrice(BaseSchema):
    pass


class ProductPriceInfo(BaseSchema):
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


class CartProduct(BaseSchema):
    pass


class PromoMeta(BaseSchema):
    pass


class CartProductIdentifer(BaseSchema):
    pass


class BasePrice(BaseSchema):
    pass


class ArticlePriceInfo(BaseSchema):
    pass


class ProductArticle(BaseSchema):
    pass


class CartProductInfo(BaseSchema):
    pass


class RawBreakup(BaseSchema):
    pass


class CouponBreakup(BaseSchema):
    pass


class LoyaltyPoints(BaseSchema):
    pass


class DisplayBreakup(BaseSchema):
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


class PromiseFormatted(BaseSchema):
    pass


class PromiseTimestamp(BaseSchema):
    pass


class ShipmentPromise(BaseSchema):
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

    
    codes = fields.List(fields.Str(required=False), required=False)
    
    networks = fields.List(fields.Str(required=False), required=False)
    
    types = fields.List(fields.Str(required=False), required=False)
    
    uses = fields.Nested(PaymentAllowValue, required=False)
    


class PostOrder(BaseSchema):
    # Cart swagger.json

    
    return_allowed = fields.Boolean(required=False)
    
    cancellation_allowed = fields.Boolean(required=False)
    


class UsesRemaining(BaseSchema):
    # Cart swagger.json

    
    app = fields.Int(required=False)
    
    user = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class UsesRestriction(BaseSchema):
    # Cart swagger.json

    
    maximum = fields.Nested(UsesRemaining, required=False)
    
    remaining = fields.Nested(UsesRemaining, required=False)
    


class Restrictions(BaseSchema):
    # Cart swagger.json

    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    
    payments = fields.Dict(required=False)
    
    post_order = fields.Nested(PostOrder, required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    coupon_allowed = fields.Boolean(required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    


class Validity(BaseSchema):
    # Cart swagger.json

    
    priority = fields.Int(required=False)
    


class Rule(BaseSchema):
    # Cart swagger.json

    
    max = fields.Float(required=False)
    
    key = fields.Float(required=False)
    
    value = fields.Float(required=False)
    
    discount_qty = fields.Float(required=False)
    
    min = fields.Float(required=False)
    


class CouponAction(BaseSchema):
    # Cart swagger.json

    
    txn_mode = fields.Str(required=False)
    
    action_date = fields.Str(required=False)
    


class CouponSchedule(BaseSchema):
    # Cart swagger.json

    
    cron = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    
    duration = fields.Int(required=False)
    
    end = fields.Str(required=False)
    


class State(BaseSchema):
    # Cart swagger.json

    
    is_display = fields.Boolean(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    is_public = fields.Boolean(required=False)
    


class DisplayMetaDict(BaseSchema):
    # Cart swagger.json

    
    title = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    


class DisplayMeta(BaseSchema):
    # Cart swagger.json

    
    remove = fields.Nested(DisplayMetaDict, required=False)
    
    auto = fields.Nested(DisplayMetaDict, required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    apply = fields.Nested(DisplayMetaDict, required=False)
    
    subtitle = fields.Str(required=False)
    


class RuleDefinition(BaseSchema):
    # Cart swagger.json

    
    auto_apply = fields.Boolean(required=False)
    
    applicable_on = fields.Str(required=False)
    
    scope = fields.List(fields.Str(required=False), required=False)
    
    currency_code = fields.Str(required=False)
    
    value_type = fields.Str(required=False)
    
    calculate_on = fields.Str(required=False)
    
    is_exact = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class CouponDateMeta(BaseSchema):
    # Cart swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class CouponAuthor(BaseSchema):
    # Cart swagger.json

    
    modified_by = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    


class Identifier(BaseSchema):
    # Cart swagger.json

    
    company_id = fields.List(fields.Int(required=False), required=False)
    
    article_id = fields.List(fields.Str(required=False), required=False)
    
    collection_id = fields.List(fields.Str(required=False), required=False)
    
    category_id = fields.List(fields.Int(required=False), required=False)
    
    brand_id = fields.List(fields.Int(required=False), required=False)
    
    item_id = fields.List(fields.Int(required=False), required=False)
    
    store_id = fields.List(fields.Int(required=False), required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    


class Ownership(BaseSchema):
    # Cart swagger.json

    
    payable_by = fields.Str(required=False)
    
    payable_category = fields.Str(required=False)
    


class Validation(BaseSchema):
    # Cart swagger.json

    
    user_registered_after = fields.Str(required=False)
    
    anonymous = fields.Boolean(required=False)
    
    app_id = fields.List(fields.Str(required=False), required=False)
    


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    state = fields.Nested(State, required=False)
    
    type_slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    


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

    
    items = fields.Nested(CouponAdd, required=False)
    
    page = fields.Nested(Page, required=False)
    


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
    
    validity = fields.Nested(Validity, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    state = fields.Nested(State, required=False)
    
    type_slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    


class CouponPartialUpdate(BaseSchema):
    # Cart swagger.json

    
    archive = fields.Boolean(required=False)
    
    schedule = fields.Nested(CouponSchedule, required=False)
    


class PromotionSchedule(BaseSchema):
    # Cart swagger.json

    
    cron = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    
    duration = fields.Int(required=False)
    
    end = fields.Str(required=False)
    


class PromotionDateMeta(BaseSchema):
    # Cart swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class Ownership1(BaseSchema):
    # Cart swagger.json

    
    payable_by = fields.Str(required=False)
    
    payable_category = fields.Str(required=False)
    


class DisplayMeta1(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    offer_label = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class UserRegistered(BaseSchema):
    # Cart swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class PaymentAllowValue1(BaseSchema):
    # Cart swagger.json

    
    max = fields.Int(required=False)
    


class PromotionPaymentModes(BaseSchema):
    # Cart swagger.json

    
    codes = fields.List(fields.Str(required=False), required=False)
    
    uses = fields.Nested(PaymentAllowValue1, required=False)
    
    type = fields.Str(required=False)
    


class PostOrder1(BaseSchema):
    # Cart swagger.json

    
    return_allowed = fields.Boolean(required=False)
    
    cancellation_allowed = fields.Boolean(required=False)
    


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

    
    order_quantity = fields.Int(required=False)
    
    user_registered = fields.Nested(UserRegistered, required=False)
    
    anonymous_users = fields.Boolean(required=False)
    
    payments = fields.List(fields.Nested(PromotionPaymentModes, required=False), required=False)
    
    post_order = fields.Nested(PostOrder1, required=False)
    
    uses = fields.Nested(UsesRestriction1, required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    


class CompareObject(BaseSchema):
    # Cart swagger.json

    
    equals = fields.Float(required=False)
    
    greater_than_equals = fields.Float(required=False)
    
    less_than = fields.Float(required=False)
    
    less_than_equals = fields.Float(required=False)
    
    greater_than = fields.Float(required=False)
    


class ItemCriteria(BaseSchema):
    # Cart swagger.json

    
    cart_unique_item_quantity = fields.Nested(CompareObject, required=False)
    
    item_exclude_l2_category = fields.List(fields.Int(required=False), required=False)
    
    item_brand = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_store = fields.List(fields.Int(required=False), required=False)
    
    cart_quantity = fields.Nested(CompareObject, required=False)
    
    item_exclude_l1_category = fields.List(fields.Int(required=False), required=False)
    
    cart_unique_item_amount = fields.Nested(CompareObject, required=False)
    
    item_company = fields.List(fields.Int(required=False), required=False)
    
    item_l1_category = fields.List(fields.Int(required=False), required=False)
    
    item_l2_category = fields.List(fields.Int(required=False), required=False)
    
    all_items = fields.Boolean(required=False)
    
    cart_total = fields.Nested(CompareObject, required=False)
    
    item_sku = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_sku = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_company = fields.List(fields.Int(required=False), required=False)
    
    item_category = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_id = fields.List(fields.Int(required=False), required=False)
    
    available_zones = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_brand = fields.List(fields.Int(required=False), required=False)
    
    buy_rules = fields.List(fields.Str(required=False), required=False)
    
    item_id = fields.List(fields.Int(required=False), required=False)
    
    item_store = fields.List(fields.Int(required=False), required=False)
    
    item_exclude_department = fields.List(fields.Int(required=False), required=False)
    
    item_department = fields.List(fields.Int(required=False), required=False)
    
    item_size = fields.List(fields.Str(required=False), required=False)
    
    item_tags = fields.List(fields.Str(required=False), required=False)
    
    item_exclude_category = fields.List(fields.Int(required=False), required=False)
    


class PromotionAuthor(BaseSchema):
    # Cart swagger.json

    
    modified_by = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    


class DiscountOffer(BaseSchema):
    # Cart swagger.json

    
    min_offer_quantity = fields.Int(required=False)
    
    discount_price = fields.Float(required=False)
    
    max_offer_quantity = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    apportion_discount = fields.Boolean(required=False)
    
    max_discount_amount = fields.Float(required=False)
    
    partial_can_ret = fields.Boolean(required=False)
    
    discount_percentage = fields.Float(required=False)
    
    max_usage_per_transaction = fields.Int(required=False)
    
    discount_amount = fields.Float(required=False)
    


class DiscountRule(BaseSchema):
    # Cart swagger.json

    
    buy_condition = fields.Str(required=False)
    
    item_criteria = fields.Nested(ItemCriteria, required=False)
    
    discount_type = fields.Str(required=False)
    
    offer = fields.Nested(DiscountOffer, required=False)
    


class Visibility(BaseSchema):
    # Cart swagger.json

    
    coupon_list = fields.Boolean(required=False)
    
    pdp = fields.Boolean(required=False)
    


class PromotionAction(BaseSchema):
    # Cart swagger.json

    
    action_type = fields.Str(required=False)
    
    action_date = fields.Str(required=False)
    


class PromotionListItem(BaseSchema):
    # Cart swagger.json

    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    apply_priority = fields.Int(required=False)
    
    promo_group = fields.Str(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    currency = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    code = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    promotion_type = fields.Str(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    stackable = fields.Boolean(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    calculate_on = fields.Str(required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    


class PromotionsResponse(BaseSchema):
    # Cart swagger.json

    
    items = fields.Nested(PromotionListItem, required=False)
    
    page = fields.Nested(Page, required=False)
    


class PromotionAdd(BaseSchema):
    # Cart swagger.json

    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    apply_priority = fields.Int(required=False)
    
    promo_group = fields.Str(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    currency = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    code = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    promotion_type = fields.Str(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    stackable = fields.Boolean(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    calculate_on = fields.Str(required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    


class PromotionUpdate(BaseSchema):
    # Cart swagger.json

    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    apply_priority = fields.Int(required=False)
    
    promo_group = fields.Str(required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    currency = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    code = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    promotion_type = fields.Str(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    stackable = fields.Boolean(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    calculate_on = fields.Str(required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    


class PromotionPartialUpdate(BaseSchema):
    # Cart swagger.json

    
    archive = fields.Boolean(required=False)
    
    schedule = fields.Nested(PromotionSchedule, required=False)
    


class ActivePromosResponse(BaseSchema):
    # Cart swagger.json

    
    is_hidden = fields.Boolean(required=False)
    
    entity_slug = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    example = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class CartItem(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    product_id = fields.Str(required=False)
    


class OpenapiCartDetailsRequest(BaseSchema):
    # Cart swagger.json

    
    cart_items = fields.Nested(CartItem, required=False)
    


class DiscountRulesApp(BaseSchema):
    # Cart swagger.json

    
    item_criteria = fields.Dict(required=False)
    
    offer = fields.Dict(required=False)
    
    raw_offer = fields.Dict(required=False)
    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    


class BuyRules(BaseSchema):
    # Cart swagger.json

    
    item_criteria = fields.Dict(required=False)
    
    cart_conditions = fields.Dict(required=False)
    


class FreeGiftItem(BaseSchema):
    # Cart swagger.json

    
    item_name = fields.Str(required=False)
    
    item_slug = fields.Str(required=False)
    
    item_price_details = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    
    item_brand_name = fields.Str(required=False)
    


class AppliedFreeArticles(BaseSchema):
    # Cart swagger.json

    
    article_id = fields.Str(required=False)
    
    free_gift_item_details = fields.Nested(FreeGiftItem, required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    article_quantity = fields.Int(required=False)
    
    promotion_type = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesApp, required=False), required=False)
    
    promotion_name = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    promo_id = fields.Str(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    
    offer_text = fields.Str(required=False)
    
    promotion_group = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    


class ProductAvailability(BaseSchema):
    # Cart swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    deliverable = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    other_store_quantity = fields.Int(required=False)
    


class ProductPrice(BaseSchema):
    # Cart swagger.json

    
    add_on = fields.Float(required=False)
    
    selling = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class ProductPriceInfo(BaseSchema):
    # Cart swagger.json

    
    converted = fields.Nested(ProductPrice, required=False)
    
    base = fields.Nested(ProductPrice, required=False)
    


class BaseInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class ActionQuery(BaseSchema):
    # Cart swagger.json

    
    product_slug = fields.List(fields.Str(required=False), required=False)
    


class ProductAction(BaseSchema):
    # Cart swagger.json

    
    url = fields.Str(required=False)
    
    query = fields.Nested(ActionQuery, required=False)
    
    type = fields.Str(required=False)
    


class ProductImage(BaseSchema):
    # Cart swagger.json

    
    url = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    


class CategoryInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class CartProduct(BaseSchema):
    # Cart swagger.json

    
    brand = fields.Nested(BaseInfo, required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    name = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class PromoMeta(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    


class CartProductIdentifer(BaseSchema):
    # Cart swagger.json

    
    identifier = fields.Str(required=False)
    


class BasePrice(BaseSchema):
    # Cart swagger.json

    
    marked = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class ArticlePriceInfo(BaseSchema):
    # Cart swagger.json

    
    converted = fields.Nested(BasePrice, required=False)
    
    base = fields.Nested(BasePrice, required=False)
    


class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    store = fields.Nested(BaseInfo, required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    size = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    uid = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    coupon_message = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    discount = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    bulk_offer = fields.Dict(required=False)
    


class RawBreakup(BaseSchema):
    # Cart swagger.json

    
    cod_charge = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    you_saved = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    gst_charges = fields.Float(required=False)
    
    mrp_total = fields.Float(required=False)
    
    coupon = fields.Float(required=False)
    
    convenience_fee = fields.Float(required=False)
    
    subtotal = fields.Float(required=False)
    
    fynd_cash = fields.Float(required=False)
    
    vog = fields.Float(required=False)
    


class CouponBreakup(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class LoyaltyPoints(BaseSchema):
    # Cart swagger.json

    
    is_applied = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    total = fields.Float(required=False)
    
    applicable = fields.Float(required=False)
    


class DisplayBreakup(BaseSchema):
    # Cart swagger.json

    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    message = fields.List(fields.Str(required=False), required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class CartBreakup(BaseSchema):
    # Cart swagger.json

    
    raw = fields.Nested(RawBreakup, required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    


class OpenapiCartDetailsResponse(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class OpenApiErrorResponse(BaseSchema):
    # Cart swagger.json

    
    errors = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ShippingAddress(BaseSchema):
    # Cart swagger.json

    
    area = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Int(required=False)
    
    pincode = fields.Int(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class OpenApiCartServiceabilityRequest(BaseSchema):
    # Cart swagger.json

    
    cart_items = fields.Nested(CartItem, required=False)
    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    


class PromiseFormatted(BaseSchema):
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
    


class OpenApiCartServiceabilityResponse(BaseSchema):
    # Cart swagger.json

    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    


class MultiTenderPaymentMeta(BaseSchema):
    # Cart swagger.json

    
    order_id = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    current_status = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    


class MultiTenderPaymentMethod(BaseSchema):
    # Cart swagger.json

    
    meta = fields.Nested(MultiTenderPaymentMeta, required=False)
    
    amount = fields.Float(required=False)
    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class OpenApiFiles(BaseSchema):
    # Cart swagger.json

    
    values = fields.List(fields.Str(required=False), required=False)
    
    key = fields.Str(required=False)
    


class CartItemMeta(BaseSchema):
    # Cart swagger.json

    
    primary_item = fields.Boolean(required=False)
    
    group_id = fields.Str(required=False)
    


class OpenApiOrderItem(BaseSchema):
    # Cart swagger.json

    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    cod_charges = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    discount = fields.Float(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    quantity = fields.Int(required=False)
    
    price_effective = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    product_id = fields.Int(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    employee_discount = fields.Float(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    meta = fields.Nested(CartItemMeta, required=False)
    


class OpenApiPlatformCheckoutReq(BaseSchema):
    # Cart swagger.json

    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    cod_charges = fields.Float(required=False)
    
    payment_mode = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    cart_items = fields.List(fields.Nested(OpenApiOrderItem, required=False), required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    cart_value = fields.Float(required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    coupon_code = fields.Str(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    coupon = fields.Str(required=False)
    
    billing_address = fields.Nested(ShippingAddress, required=False)
    
    employee_discount = fields.Dict(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    


class OpenApiCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    order_ref_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


