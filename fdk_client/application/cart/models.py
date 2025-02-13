"""Cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class PromoBuyRuleCartConditions(BaseSchema):
    pass


class PromoBuyRuleCompareFieldsTypes(BaseSchema):
    pass


class BuyRules(BaseSchema):
    pass


class PromoDiscountRuleOffer(BaseSchema):
    pass


class PromoDiscountRuleRawOffer(BaseSchema):
    pass


class PromoDiscountRuleItemCriteria(BaseSchema):
    pass


class DiscountRulesApp(BaseSchema):
    pass


class Ownership(BaseSchema):
    pass


class AppliedFreeArticles(BaseSchema):
    pass


class AppliedPromotion(BaseSchema):
    pass


class PaymentSelectionLock(BaseSchema):
    pass


class PromiseFormatted(BaseSchema):
    pass


class PromiseISOFormat(BaseSchema):
    pass


class PromiseTimestamp(BaseSchema):
    pass


class ShipmentPromise(BaseSchema):
    pass


class BasePrice(BaseSchema):
    pass


class ArticleAppliedPriceAdjustment(BaseSchema):
    pass


class ArticlePriceInfo(BaseSchema):
    pass


class BaseInfo(BaseSchema):
    pass


class StoreInfo(BaseSchema):
    pass


class ArticleGiftCard(BaseSchema):
    pass


class ProductArticle(BaseSchema):
    pass


class CartProductIdentifer(BaseSchema):
    pass


class PromoMeta(BaseSchema):
    pass


class BaseChargeCurrency(BaseSchema):
    pass


class ChargesAmount(BaseSchema):
    pass


class Charges(BaseSchema):
    pass


class ProductPrice(BaseSchema):
    pass


class ProductPriceInfo(BaseSchema):
    pass


class ProductPricePerUnit(BaseSchema):
    pass


class ProductPricePerUnitInfo(BaseSchema):
    pass


class ProductAvailabilitySize(BaseSchema):
    pass


class ProductAvailability(BaseSchema):
    pass


class ActionQuery(BaseSchema):
    pass


class ProductAction(BaseSchema):
    pass


class Tags(BaseSchema):
    pass


class ProductImage(BaseSchema):
    pass


class CategoryInfo(BaseSchema):
    pass


class CartProduct(BaseSchema):
    pass


class CouponDetails(BaseSchema):
    pass


class ParentItemIdentifiers(BaseSchema):
    pass


class CartItemMOQ(BaseSchema):
    pass


class CartItemCustomOrder(BaseSchema):
    pass


class CartProductInfo(BaseSchema):
    pass


class DiscountMeta(BaseSchema):
    pass


class PriceAdjustmentApplied(BaseSchema):
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


class CartCurrency(BaseSchema):
    pass


class CartCouponMedias(BaseSchema):
    pass


class CartDetailCoupon(BaseSchema):
    pass


class ChargesThreshold(BaseSchema):
    pass


class DeliveryChargesConfig(BaseSchema):
    pass


class CartCommonConfig(BaseSchema):
    pass


class CartAppliedPriceAdjustment(BaseSchema):
    pass


class CustomCart(BaseSchema):
    pass


class CartDetailResponse(BaseSchema):
    pass


class ArticleAssignment(BaseSchema):
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


class DeleteCartDetailResponse(BaseSchema):
    pass


class CartItemCountResponse(BaseSchema):
    pass


class CartItemCountResponseV2(BaseSchema):
    pass


class Coupon(BaseSchema):
    pass


class PageCoupon(BaseSchema):
    pass


class GetCouponResponse(BaseSchema):
    pass


class ApplyCouponRequest(BaseSchema):
    pass


class OfferPrice(BaseSchema):
    pass


class OfferItem(BaseSchema):
    pass


class OfferSeller(BaseSchema):
    pass


class BulkPriceOffer(BaseSchema):
    pass


class BulkPriceResponse(BaseSchema):
    pass


class RewardPointRequest(BaseSchema):
    pass


class GeoLocation(BaseSchema):
    pass


class Address(BaseSchema):
    pass


class GetAddressesResponse(BaseSchema):
    pass


class SaveAddressResponse(BaseSchema):
    pass


class UpdateAddressResponse(BaseSchema):
    pass


class DeleteAddressResponse(BaseSchema):
    pass


class SelectCartAddressRequest(BaseSchema):
    pass


class UpdateCartPaymentRequest(BaseSchema):
    pass


class CouponValidity(BaseSchema):
    pass


class PaymentCouponValidate(BaseSchema):
    pass


class ShipmentError(BaseSchema):
    pass


class ShipmentResponse(BaseSchema):
    pass


class ShipmentMeta(BaseSchema):
    pass


class ShipmentMetaDimension(BaseSchema):
    pass


class ShipmentLogisticsMeta(BaseSchema):
    pass


class ShipmentLogisticsMetaAccount(BaseSchema):
    pass


class ShipmentLogisticsMetaAccountAreaCode(BaseSchema):
    pass


class ShipmentLogisticsMetaAccountDpTat(BaseSchema):
    pass


class CartShipmentsResponse(BaseSchema):
    pass


class CartCheckoutCustomMeta(BaseSchema):
    pass


class CustomerDetails(BaseSchema):
    pass


class StaffCheckout(BaseSchema):
    pass


class CartCheckoutDetailRequest(BaseSchema):
    pass


class CheckCart(BaseSchema):
    pass


class CartCheckoutResponse(BaseSchema):
    pass


class GiftDetail(BaseSchema):
    pass


class ArticleGiftDetail(BaseSchema):
    pass


class CartMetaRequest(BaseSchema):
    pass


class CartMetaResponse(BaseSchema):
    pass


class CartMetaMissingResponse(BaseSchema):
    pass


class CartMetaFieldsValidation(BaseSchema):
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


class OperationErrorResponse(BaseSchema):
    pass


class StandardError(BaseSchema):
    pass


class LadderPrice(BaseSchema):
    pass


class LadderOfferItem(BaseSchema):
    pass


class LadderPriceOffer(BaseSchema):
    pass


class CurrencyInfo(BaseSchema):
    pass


class LadderPriceOffers(BaseSchema):
    pass


class PaymentMeta(BaseSchema):
    pass


class PaymentMethod(BaseSchema):
    pass


class CartCheckoutDetailV2Request(BaseSchema):
    pass


class CartMetaConfigListResponse(BaseSchema):
    pass


class CartMetaConfigListObject(BaseSchema):
    pass


class OrderPlacing(BaseSchema):
    pass


class PanCard(BaseSchema):
    pass


class CartConfigDetailObj(BaseSchema):
    pass


class CartConfigDetailResponse(BaseSchema):
    pass


class SelectAddressResponseError(BaseSchema):
    pass


class AllAddressForSelectAddress(BaseSchema):
    pass


class DeleteCartRequest(BaseSchema):
    pass





class PromoBuyRuleCartConditions(BaseSchema):
    # Cart swagger.json

    
    cart_quantity = fields.Nested(PromoBuyRuleCompareFieldsTypes, required=False)
    
    cart_total = fields.Nested(PromoBuyRuleCompareFieldsTypes, required=False)
    
    item_id = fields.List(fields.Float(required=False), required=False)
    
    item_store = fields.List(fields.Float(required=False), required=False)
    
    item_company = fields.List(fields.Float(required=False), required=False)
    
    item_brand = fields.List(fields.Float(required=False), required=False)
    
    item_exclude_brand = fields.List(fields.Float(required=False), required=False)
    
    item_category = fields.List(fields.Float(required=False), required=False)
    
    item_exclude_category = fields.List(fields.Float(required=False), required=False)
    
    item_l1_category = fields.List(fields.Float(required=False), required=False)
    
    item_exclude_l1_category = fields.List(fields.Float(required=False), required=False)
    
    item_l2_category = fields.List(fields.Float(required=False), required=False)
    
    item_exclude_l2_category = fields.List(fields.Float(required=False), required=False)
    
    item_department = fields.List(fields.Float(required=False), required=False)
    
    item_exclude_id = fields.List(fields.Float(required=False), required=False)
    
    available_zones = fields.List(fields.Float(required=False), required=False)
    
    product_tags = fields.List(fields.Str(required=False), required=False)
    


class PromoBuyRuleCompareFieldsTypes(BaseSchema):
    # Cart swagger.json

    
    greater_than_equals = fields.Float(required=False)
    
    greater_than = fields.Float(required=False)
    
    equals = fields.Float(required=False)
    
    less_than = fields.Float(required=False)
    
    less_than_equals = fields.Float(required=False)
    


class BuyRules(BaseSchema):
    # Cart swagger.json

    
    cart_conditions = fields.Nested(PromoBuyRuleCartConditions, required=False)
    
    item_criteria = fields.Dict(required=False)
    
    all_items = fields.Boolean(required=False, allow_none=True)
    
    mrp_promo = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    


class PromoDiscountRuleOffer(BaseSchema):
    # Cart swagger.json

    
    max_offer_quantity = fields.Float(required=False, allow_none=True)
    
    discount_percentage = fields.Float(required=False, allow_none=True)
    
    discount_amount = fields.Float(required=False, allow_none=True)
    


class PromoDiscountRuleRawOffer(BaseSchema):
    # Cart swagger.json

    
    buy_condition = fields.Str(required=False)
    
    discount_type = fields.Str(required=False)
    
    offer = fields.Nested(PromoDiscountRuleOffer, required=False)
    
    item_criteria = fields.Nested(PromoDiscountRuleItemCriteria, required=False)
    


class PromoDiscountRuleItemCriteria(BaseSchema):
    # Cart swagger.json

    
    item_id = fields.List(fields.Float(required=False), required=False)
    
    buy_rules = fields.List(fields.Str(required=False), required=False)
    
    all_items = fields.Boolean(required=False)
    


class DiscountRulesApp(BaseSchema):
    # Cart swagger.json

    
    offer = fields.Nested(PromoDiscountRuleOffer, required=False)
    
    raw_offer = fields.Nested(PromoDiscountRuleRawOffer, required=False)
    
    item_criteria = fields.Nested(PromoDiscountRuleItemCriteria, required=False)
    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    


class Ownership(BaseSchema):
    # Cart swagger.json

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    


class AppliedFreeArticles(BaseSchema):
    # Cart swagger.json

    
    parent_item_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    
    free_gift_item_details = fields.Nested(FreeGiftItems, required=False)
    


class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    article_quantity = fields.Int(required=False)
    
    original_article_quantity = fields.Int(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesApp, required=False), required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    
    promotion_name = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    offer_text = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    promotion_type = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    promotion_group = fields.Str(required=False)
    
    promo_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    code = fields.Str(required=False, allow_none=True)
    
    offer_label = fields.Str(required=False, allow_none=True)
    
    return_allowed = fields.Boolean(required=False, allow_none=True)
    
    cancellation_allowed = fields.Boolean(required=False, allow_none=True)
    
    promo_code = fields.Str(required=False, allow_none=True)
    
    free_quantity = fields.Int(required=False, allow_none=True)
    
    offer_description = fields.Str(required=False, allow_none=True)
    


class PaymentSelectionLock(BaseSchema):
    # Cart swagger.json

    
    enabled = fields.Boolean(required=False)
    
    default_options = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    


class PromiseFormatted(BaseSchema):
    # Cart swagger.json

    
    max = fields.Str(required=False, allow_none=True)
    
    min = fields.Str(required=False, allow_none=True)
    


class PromiseISOFormat(BaseSchema):
    # Cart swagger.json

    
    max = fields.Str(required=False, allow_none=True)
    
    min = fields.Str(required=False, allow_none=True)
    


class PromiseTimestamp(BaseSchema):
    # Cart swagger.json

    
    max = fields.Float(required=False, allow_none=True)
    
    min = fields.Float(required=False, allow_none=True)
    


class ShipmentPromise(BaseSchema):
    # Cart swagger.json

    
    formatted = fields.Nested(PromiseFormatted, required=False)
    
    timestamp = fields.Nested(PromiseTimestamp, required=False)
    
    iso = fields.Nested(PromiseISOFormat, required=False)
    


class BasePrice(BaseSchema):
    # Cart swagger.json

    
    effective = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    marked = fields.Float(required=False)
    
    selling = fields.Float(required=False)
    


class ArticleAppliedPriceAdjustment(BaseSchema):
    # Cart swagger.json

    
    adjusted_value = fields.Dict(required=False)
    
    article_level_distribution = fields.Boolean(required=False)
    
    article_id = fields.Str(required=False)
    
    applied_quantity = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    


class ArticlePriceInfo(BaseSchema):
    # Cart swagger.json

    
    base = fields.Nested(BasePrice, required=False)
    
    converted = fields.Nested(BasePrice, required=False)
    


class BaseInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False, allow_none=True)
    


class StoreInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False, allow_none=True)
    
    store_code = fields.Str(required=False, allow_none=True)
    


class ArticleGiftCard(BaseSchema):
    # Cart swagger.json

    
    gift_price = fields.Float(required=False)
    
    display_text = fields.Str(required=False, allow_none=True)
    
    is_gift_applied = fields.Boolean(required=False)
    


class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    seller_identifier = fields.Str(required=False, allow_none=True)
    
    quantity = fields.Int(required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    cart_item_meta = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    is_gift_visible = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    gift_card = fields.Nested(ArticleGiftCard, required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    identifier = fields.Dict(required=False, allow_none=True)
    
    mto_quantity = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    meta = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    store = fields.Nested(StoreInfo, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    variants = fields.Dict(required=False)
    


class CartProductIdentifer(BaseSchema):
    # Cart swagger.json

    
    identifier = fields.Str(required=False)
    


class PromoMeta(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    


class BaseChargeCurrency(BaseSchema):
    # Cart swagger.json

    
    value = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    


class ChargesAmount(BaseSchema):
    # Cart swagger.json

    
    ordering_currency = fields.Dict(required=False)
    
    base_currency = fields.Dict(required=False)
    


class Charges(BaseSchema):
    # Cart swagger.json

    
    meta = fields.Dict(required=False)
    
    amount = fields.Nested(ChargesAmount, required=False)
    
    name = fields.Str(required=False)
    
    allow_refund = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class ProductPrice(BaseSchema):
    # Cart swagger.json

    
    marked = fields.Float(required=False)
    
    add_on = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    
    selling = fields.Float(required=False)
    
    selling_price = fields.Float(required=False)
    


class ProductPriceInfo(BaseSchema):
    # Cart swagger.json

    
    base = fields.Nested(ProductPrice, required=False)
    
    converted = fields.Nested(ProductPrice, required=False)
    


class ProductPricePerUnit(BaseSchema):
    # Cart swagger.json

    
    currency_symbol = fields.Str(required=False)
    
    selling_price = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    add_on = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    


class ProductPricePerUnitInfo(BaseSchema):
    # Cart swagger.json

    
    base = fields.Nested(ProductPricePerUnit, required=False)
    
    converted = fields.Nested(ProductPricePerUnit, required=False)
    


class ProductAvailabilitySize(BaseSchema):
    # Cart swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    


class ProductAvailability(BaseSchema):
    # Cart swagger.json

    
    out_of_stock = fields.Boolean(required=False)
    
    deliverable = fields.Boolean(required=False)
    
    available_sizes = fields.List(fields.Nested(ProductAvailabilitySize, required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    
    other_store_quantity = fields.Int(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    


class ActionQuery(BaseSchema):
    # Cart swagger.json

    
    product_slug = fields.List(fields.Str(required=False), required=False)
    


class ProductAction(BaseSchema):
    # Cart swagger.json

    
    query = fields.Nested(ActionQuery, required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class Tags(BaseSchema):
    # Cart swagger.json

    
    tags = fields.Dict(required=False)
    


class ProductImage(BaseSchema):
    # Cart swagger.json

    
    secure_url = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class CategoryInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class CartProduct(BaseSchema):
    # Cart swagger.json

    
    slug = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    teaser_tag = fields.Dict(required=False, allow_none=True)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    uid = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    type = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    
    item_code = fields.Str(required=False, allow_none=True)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    attributes = fields.Dict(required=False, allow_none=True)
    


class CouponDetails(BaseSchema):
    # Cart swagger.json

    
    discount_total_quantity = fields.Float(required=False)
    
    discount_single_quantity = fields.Float(required=False)
    
    code = fields.Str(required=False)
    


class ParentItemIdentifiers(BaseSchema):
    # Cart swagger.json

    
    identifier = fields.Str(required=False, allow_none=True)
    
    parent_item_size = fields.Str(required=False, allow_none=True)
    
    parent_item_id = fields.Str(required=False, allow_none=True)
    


class CartItemMOQ(BaseSchema):
    # Cart swagger.json

    
    increment_unit = fields.Float(required=False, allow_none=True)
    
    maximum = fields.Float(required=False, allow_none=True)
    
    minimum = fields.Float(required=False, allow_none=True)
    


class CartItemCustomOrder(BaseSchema):
    # Cart swagger.json

    
    is_custom_order = fields.Boolean(required=False)
    
    manufacturing_time = fields.Float(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    product_ean_id = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False, allow_none=True)
    
    article = fields.Nested(ProductArticle, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    key = fields.Str(required=False)
    
    coupon = fields.Nested(CouponDetails, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    price_adjustment_applied = fields.List(fields.Nested(ArticleAppliedPriceAdjustment, required=False), required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    coupon_message = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    message = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    moq = fields.Nested(CartItemMOQ, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    custom_order = fields.Nested(CartItemCustomOrder, required=False)
    
    charges = fields.List(fields.Float(required=False), required=False)
    
    seller_count = fields.Float(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    discount_meta = fields.Nested(DiscountMeta, required=False)
    


class DiscountMeta(BaseSchema):
    # Cart swagger.json

    
    timer = fields.Boolean(required=False)
    
    start_timer_in_minutes = fields.Float(required=False)
    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class PriceAdjustmentApplied(BaseSchema):
    # Cart swagger.json

    
    article_id = fields.Str(required=False)
    
    adjusted_value = fields.Dict(required=False)
    
    applied_quantity = fields.Float(required=False)
    
    meta = fields.Dict(required=False)
    
    article_level_distribution = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class CouponBreakup(BaseSchema):
    # Cart swagger.json

    
    title = fields.Str(required=False, allow_none=True)
    
    max_discount_value = fields.Float(required=False)
    
    value = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    uid = fields.Str(required=False, allow_none=True)
    
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
    
    original = fields.Float(required=False)
    
    attr = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    preset = fields.Float(required=False)
    


class LoyaltyPoints(BaseSchema):
    # Cart swagger.json

    
    is_applied = fields.Boolean(required=False, allow_none=True)
    
    total = fields.Float(required=False, allow_none=True)
    
    applicable = fields.Float(required=False, allow_none=True)
    
    description = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    


class RawBreakup(BaseSchema):
    # Cart swagger.json

    
    promotion = fields.Float(required=False)
    
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
    
    sub_total = fields.Float(required=False)
    
    convenience_fee = fields.Float(required=False)
    
    total_charge = fields.Float(required=False)
    
    mop_total = fields.Float(required=False)
    


class CartBreakup(BaseSchema):
    # Cart swagger.json

    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    


class CartCurrency(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    


class CartCouponMedias(BaseSchema):
    # Cart swagger.json

    
    alt = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    key = fields.Str(required=False)
    


class CartDetailCoupon(BaseSchema):
    # Cart swagger.json

    
    cashback_amount = fields.Float(required=False)
    
    cashback_message_primary = fields.Str(required=False)
    
    cashback_message_secondary = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    
    coupon_description = fields.Str(required=False)
    
    coupon_id = fields.Str(required=False, allow_none=True)
    
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
    
    medias = fields.List(fields.Nested(CartCouponMedias, required=False), required=False)
    


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
    


class CartAppliedPriceAdjustment(BaseSchema):
    # Cart swagger.json

    
    remove_articles = fields.Boolean(required=False)
    
    adjusted_value = fields.Dict(required=False)
    
    article_level_distribution = fields.Boolean(required=False)
    
    auto_remove = fields.Boolean(required=False)
    
    applied_articles_ids = fields.List(fields.Str(required=False), required=False)
    
    message = fields.Str(required=False)
    
    _type = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    restrictions = fields.Dict(required=False)
    
    _id = fields.Str(required=False)
    


class CustomCart(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    cart_name = fields.Str(required=False)
    
    cart_type = fields.Str(required=False)
    
    is_universal = fields.Boolean(required=False)
    


class CartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    cart_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
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
    
    price_adjustment_applied = fields.List(fields.Nested(CartAppliedPriceAdjustment, required=False), required=False)
    
    buy_now = fields.Boolean(required=False)
    
    gstin = fields.Str(required=False, allow_none=True)
    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    pan_no = fields.Str(required=False, allow_none=True)
    
    custom_cart = fields.Nested(CustomCart, required=False)
    
    is_pan_received = fields.Boolean(required=False)
    
    pan_config = fields.Dict(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class ArticleAssignment(BaseSchema):
    # Cart swagger.json

    
    level = fields.Str(required=False)
    
    strategy = fields.Str(required=False)
    


class AddProductCart(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    price_factory_type_id = fields.Str(required=False)
    
    parent_item_identifiers = fields.List(fields.Dict(required=False), required=False)
    
    product_group_tags = fields.List(fields.Str(required=False, allow_none=True), required=False)
    
    article_id = fields.Str(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    store_id = fields.Int(required=False)
    
    display = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    pos = fields.Boolean(required=False)
    
    seller_identifier = fields.Str(required=False)
    


class AddCartRequest(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    
    new_cart = fields.Boolean(required=False)
    


class AddCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    partial = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    result = fields.Dict(required=False)
    


class UpdateProductCart(BaseSchema):
    # Cart swagger.json

    
    extra_meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    item_index = fields.Int(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    article_id = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    price_factory_type_id = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    


class UpdateCartRequest(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(UpdateProductCart, required=False), required=False)
    
    operation = fields.Str(required=False)
    


class UpdateCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    result = fields.Dict(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    success = fields.Boolean(required=False)
    


class DeleteCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class CartItemCountResponse(BaseSchema):
    # Cart swagger.json

    
    user_cart_items_count = fields.Int(required=False)
    


class CartItemCountResponseV2(BaseSchema):
    # Cart swagger.json

    
    user_all_cart_articles_quantity_count = fields.Int(required=False)
    
    user_all_cart_article_count = fields.Int(required=False)
    
    custom_cart_count = fields.Dict(required=False)
    
    custom_cart_ordered_count = fields.List(fields.Dict(required=False, allow_none=True), required=False)
    


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
    
    is_bank_offer = fields.Boolean(required=False)
    
    offer_text = fields.Str(required=False)
    
    coupon_amount = fields.Float(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    medias = fields.List(fields.Nested(CartCouponMedias, required=False), required=False)
    


class PageCoupon(BaseSchema):
    # Cart swagger.json

    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    total_item_count = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    


class GetCouponResponse(BaseSchema):
    # Cart swagger.json

    
    page = fields.Nested(PageCoupon, required=False)
    
    available_coupon_list = fields.List(fields.Nested(Coupon, required=False), required=False)
    


class ApplyCouponRequest(BaseSchema):
    # Cart swagger.json

    
    coupon_code = fields.Str(required=False)
    


class OfferPrice(BaseSchema):
    # Cart swagger.json

    
    currency_symbol = fields.Str(required=False)
    
    bulk_effective = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    effective = fields.Int(required=False)
    
    marked = fields.Int(required=False)
    


class OfferItem(BaseSchema):
    # Cart swagger.json

    
    price = fields.Nested(OfferPrice, required=False)
    
    margin = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    best = fields.Boolean(required=False)
    
    total = fields.Float(required=False)
    
    auto_applied = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class OfferSeller(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class BulkPriceOffer(BaseSchema):
    # Cart swagger.json

    
    offers = fields.List(fields.Nested(OfferItem, required=False), required=False)
    
    seller = fields.Nested(OfferSeller, required=False)
    


class BulkPriceResponse(BaseSchema):
    # Cart swagger.json

    
    data = fields.List(fields.Nested(BulkPriceOffer, required=False), required=False)
    


class RewardPointRequest(BaseSchema):
    # Cart swagger.json

    
    points = fields.Boolean(required=False)
    


class GeoLocation(BaseSchema):
    # Cart swagger.json

    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    


class Address(BaseSchema):
    # Cart swagger.json

    
    pincode = fields.Float(required=False)
    
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
    
    email = fields.Str(required=False, allow_none=True)
    
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
    
    uid = fields.Float(required=False)
    
    is_anonymous = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    expire_at = fields.Str(required=False, allow_none=True)
    
    address_id = fields.Str(required=False, allow_none=True)
    
    store_name = fields.Str(required=False, allow_none=True)
    


class GetAddressesResponse(BaseSchema):
    # Cart swagger.json

    
    pii_masking = fields.Boolean(required=False)
    
    address = fields.List(fields.Nested(Address, required=False), required=False)
    


class SaveAddressResponse(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    address_id = fields.Raw(required=False)
    


class UpdateAddressResponse(BaseSchema):
    # Cart swagger.json

    
    is_updated = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    address_id = fields.Str(required=False, allow_none=True)
    


class DeleteAddressResponse(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    is_deleted = fields.Boolean(required=False)
    
    address_id = fields.Str(required=False)
    


class SelectCartAddressRequest(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    


class UpdateCartPaymentRequest(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False, allow_none=True)
    
    address_id = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    


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
    


class ShipmentError(BaseSchema):
    # Cart swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    value = fields.List(fields.Str(required=False), required=False)
    
    message = fields.Str(required=False, allow_none=True)
    


class ShipmentResponse(BaseSchema):
    # Cart swagger.json

    
    shipments = fields.Int(required=False)
    
    promise = fields.Nested(ShipmentPromise, required=False)
    
    order_type = fields.Str(required=False)
    
    box_type = fields.Str(required=False, allow_none=True)
    
    shipment_type = fields.Str(required=False)
    
    dp_options = fields.Dict(required=False, allow_none=True)
    
    dp_id = fields.Str(required=False, allow_none=True)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    meta = fields.Nested(ShipmentMeta, required=False)
    
    logistics_meta = fields.Nested(ShipmentLogisticsMeta, required=False)
    
    error = fields.Nested(ShipmentError, required=False)
    


class ShipmentMeta(BaseSchema):
    # Cart swagger.json

    
    packaging_name = fields.Str(required=False, allow_none=True)
    
    dimension = fields.Nested(ShipmentMetaDimension, required=False)
    
    assign_dp_from_sb = fields.Str(required=False, allow_none=True)
    
    dp_sort_key = fields.Str(required=False, allow_none=True)
    
    shipment_weight = fields.Float(required=False, allow_none=True)
    
    shipment_volumetric_weight = fields.Float(required=False, allow_none=True)
    
    shipment_chargeable_weight = fields.Float(required=False, allow_none=True)
    
    shipping_zone = fields.Str(required=False, allow_none=True)
    


class ShipmentMetaDimension(BaseSchema):
    # Cart swagger.json

    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    width = fields.Float(required=False)
    


class ShipmentLogisticsMeta(BaseSchema):
    # Cart swagger.json

    
    account_options = fields.List(fields.Nested(ShipmentLogisticsMetaAccount, required=False), required=False)
    
    account_info = fields.Dict(required=False)
    
    dp_sort_key = fields.Str(required=False, allow_none=True)
    
    assign_dp_from_sb = fields.Str(required=False, allow_none=True)
    


class ShipmentLogisticsMetaAccount(BaseSchema):
    # Cart swagger.json

    
    name = fields.Str(required=False, allow_none=True)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    fm_priority = fields.Float(required=False, allow_none=True)
    
    lm_priority = fields.Float(required=False, allow_none=True)
    
    rvp_priority = fields.Float(required=False, allow_none=True)
    
    type = fields.Str(required=False, allow_none=True)
    
    sub_type = fields.Str(required=False, allow_none=True)
    
    parent_id = fields.Str(required=False, allow_none=True)
    
    is_active = fields.Boolean(required=False, allow_none=True)
    
    payment_mode = fields.Str(required=False, allow_none=True)
    
    assign_dp_from_sb = fields.Str(required=False, allow_none=True)
    
    internal_account_id = fields.Str(required=False, allow_none=True)
    
    external_account_id = fields.Str(required=False, allow_none=True)
    
    f_priority = fields.Float(required=False, allow_none=True)
    
    r_priority = fields.Float(required=False, allow_none=True)
    
    dp_shipping_charges = fields.Float(required=False, allow_none=True)
    
    qc_enabled = fields.Boolean(required=False, allow_none=True)
    
    area_code = fields.Nested(ShipmentLogisticsMetaAccountAreaCode, required=False)
    
    operations = fields.List(fields.Str(required=False), required=False)
    
    dp_tat = fields.Nested(ShipmentLogisticsMetaAccountDpTat, required=False)
    


class ShipmentLogisticsMetaAccountAreaCode(BaseSchema):
    # Cart swagger.json

    
    from_pincode = fields.Str(required=False, allow_none=True)
    
    to_pincode = fields.Str(required=False, allow_none=True)
    
    source = fields.Str(required=False, allow_none=True)
    
    destination = fields.Str(required=False, allow_none=True)
    


class ShipmentLogisticsMetaAccountDpTat(BaseSchema):
    # Cart swagger.json

    
    min = fields.Float(required=False, allow_none=True)
    
    max = fields.Float(required=False, allow_none=True)
    


class CartShipmentsResponse(BaseSchema):
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
    
    staff_user_id = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    gstin = fields.Str(required=False, allow_none=True)
    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    pan_no = fields.Str(required=False, allow_none=True)
    
    custom_cart = fields.Nested(CustomCart, required=False)
    
    price_adjustment_applied = fields.List(fields.Nested(CartAppliedPriceAdjustment, required=False), required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    error = fields.Boolean(required=False)
    
    is_pan_received = fields.Boolean(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class CartCheckoutCustomMeta(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class CustomerDetails(BaseSchema):
    # Cart swagger.json

    
    email = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class StaffCheckout(BaseSchema):
    # Cart swagger.json

    
    employee_code = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class CartCheckoutDetailRequest(BaseSchema):
    # Cart swagger.json

    
    custom_meta = fields.List(fields.Nested(CartCheckoutCustomMeta, required=False), required=False)
    
    customer_details = fields.Dict(required=False)
    
    merchant_code = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    payment_mode = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    address_id = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    staff = fields.Nested(StaffCheckout, required=False)
    
    order_type = fields.Str(required=False)
    
    ordering_store = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    billing_address = fields.Dict(required=False)
    
    payment_params = fields.Dict(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    payment_extra_identifiers = fields.Dict(required=False)
    
    iin = fields.Str(required=False)
    
    network = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    


class CheckCart(BaseSchema):
    # Cart swagger.json

    
    user_type = fields.Str(required=False)
    
    cod_message = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
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
    
    gstin = fields.Str(required=False, allow_none=True)
    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    pan_no = fields.Str(required=False, allow_none=True)
    
    custom_cart = fields.Nested(CustomCart, required=False)
    
    price_adjustment_applied = fields.List(fields.Nested(PriceAdjustmentApplied, required=False), required=False)
    
    is_pan_received = fields.Boolean(required=False)
    
    pan_config = fields.Dict(required=False)
    
    order_id = fields.Str(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class CartCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    payment_confirm_url = fields.Str(required=False, allow_none=True)
    
    app_intercept_url = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    callback_url = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    order_id = fields.Str(required=False)
    
    cart = fields.Nested(CheckCart, required=False)
    


class GiftDetail(BaseSchema):
    # Cart swagger.json

    
    is_gift_applied = fields.Boolean(required=False)
    
    gift_message = fields.Str(required=False)
    


class ArticleGiftDetail(BaseSchema):
    # Cart swagger.json

    
    article_id = fields.Nested(GiftDetail, required=False)
    


class CartMetaRequest(BaseSchema):
    # Cart swagger.json

    
    gstin = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gift_details = fields.Dict(required=False, allow_none=True)
    
    pan_no = fields.Str(required=False, allow_none=True)
    
    comment = fields.Str(required=False)
    
    staff_user_id = fields.Str(required=False, allow_none=True)
    
    delivery_slots = fields.Dict(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class CartMetaResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    


class CartMetaMissingResponse(BaseSchema):
    # Cart swagger.json

    
    errors = fields.Nested(CartMetaFieldsValidation, required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    meta = fields.Nested(CartMetaFieldsValidation, required=False)
    


class CartMetaFieldsValidation(BaseSchema):
    # Cart swagger.json

    
    pan_no = fields.List(fields.Str(required=False), required=False)
    
    gstin = fields.List(fields.Str(required=False), required=False)
    
    checkout_mode = fields.List(fields.Str(required=False), required=False)
    
    comment = fields.List(fields.Str(required=False), required=False)
    
    pick_up_customer_details = fields.List(fields.Str(required=False), required=False)
    
    gift_details = fields.List(fields.Str(required=False), required=False)
    
    staff_user_id = fields.List(fields.Str(required=False), required=False)
    
    delivery_slots = fields.List(fields.Str(required=False), required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


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

    
    token = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    source = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    


class SharedCart(BaseSchema):
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
    
    gstin = fields.Str(required=False, allow_none=True)
    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    pan_no = fields.Str(required=False, allow_none=True)
    
    custom_cart = fields.Nested(CustomCart, required=False)
    
    price_adjustment_applied = fields.List(fields.Nested(CartAppliedPriceAdjustment, required=False), required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    
    is_pan_received = fields.Boolean(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class SharedCartResponse(BaseSchema):
    # Cart swagger.json

    
    error = fields.Str(required=False)
    
    cart = fields.Nested(SharedCart, required=False)
    


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
    
    tags = fields.List(fields.Str(required=False), required=False)
    


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
    
    valid_till = fields.Str(required=False)
    


class PromotionPaymentOffersResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    promotions = fields.List(fields.Nested(PromotionPaymentOffer, required=False), required=False)
    


class OperationErrorResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class StandardError(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    


class LadderPrice(BaseSchema):
    # Cart swagger.json

    
    currency_symbol = fields.Str(required=False)
    
    offer_price = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    effective = fields.Int(required=False)
    
    marked = fields.Int(required=False)
    


class LadderOfferItem(BaseSchema):
    # Cart swagger.json

    
    price = fields.Nested(LadderPrice, required=False)
    
    margin = fields.Int(required=False)
    
    max_quantity = fields.Int(required=False)
    
    min_quantity = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class LadderPriceOffer(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    calculate_on = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    promotion_group = fields.Str(required=False)
    
    valid_till = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Dict(required=False), required=False)
    
    offer_prices = fields.List(fields.Nested(LadderOfferItem, required=False), required=False)
    
    free_gift_items = fields.List(fields.Nested(FreeGiftItems, required=False), required=False)
    
    description = fields.Str(required=False)
    


class CurrencyInfo(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    


class LadderPriceOffers(BaseSchema):
    # Cart swagger.json

    
    available_offers = fields.List(fields.Nested(LadderPriceOffer, required=False), required=False)
    
    currency = fields.Nested(CurrencyInfo, required=False)
    
    store_id = fields.List(fields.Float(required=False), required=False)
    


class PaymentMeta(BaseSchema):
    # Cart swagger.json

    
    merchant_code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False, allow_none=True)
    


class PaymentMethod(BaseSchema):
    # Cart swagger.json

    
    payment_meta = fields.Nested(PaymentMeta, required=False)
    
    mode = fields.Str(required=False)
    
    payment = fields.Str(required=False)
    
    amount = fields.Float(required=False, allow_none=True)
    
    payment_identifier = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    
    payment_extra_identifiers = fields.Dict(required=False)
    


class CartCheckoutDetailV2Request(BaseSchema):
    # Cart swagger.json

    
    custom_meta = fields.Dict(required=False)
    
    customer_details = fields.Dict(required=False, allow_none=True)
    
    merchant_code = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    id = fields.Str(required=False, allow_none=True)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMethod, required=False), required=False)
    
    payment_mode = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    address_id = fields.Str(required=False)
    
    callback_url = fields.Str(required=False, allow_none=True)
    
    delivery_address = fields.Dict(required=False)
    
    staff = fields.Nested(StaffCheckout, required=False)
    
    order_type = fields.Str(required=False)
    
    ordering_store = fields.Int(required=False, allow_none=True)
    
    extra_meta = fields.Dict(required=False)
    
    payment_identifier = fields.Str(required=False, allow_none=True)
    
    billing_address = fields.Dict(required=False)
    
    payment_params = fields.Dict(required=False, allow_none=True)
    
    billing_address_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    iin = fields.Str(required=False)
    
    network = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    


class CartMetaConfigListResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(CartMetaConfigListObject, required=False), required=False)
    


class CartMetaConfigListObject(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    article_tags = fields.List(fields.Str(required=False), required=False)
    


class OrderPlacing(BaseSchema):
    # Cart swagger.json

    
    enabled = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class PanCard(BaseSchema):
    # Cart swagger.json

    
    enabled = fields.Boolean(required=False)
    
    cod_threshold_amount = fields.Int(required=False)
    
    online_threshold_amount = fields.Int(required=False)
    


class CartConfigDetailObj(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    
    last_modified_by = fields.Str(required=False)
    
    min_cart_value = fields.Int(required=False)
    
    max_cart_value = fields.Int(required=False)
    
    bulk_coupons = fields.Boolean(required=False)
    
    max_cart_items = fields.Int(required=False)
    
    gift_display_text = fields.Str(required=False)
    
    delivery_charges = fields.Nested(DeliveryChargesConfig, required=False)
    
    revenue_engine_coupon = fields.Boolean(required=False)
    
    gift_pricing = fields.Float(required=False)
    
    enabled = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    order_placing = fields.Nested(OrderPlacing, required=False)
    
    name = fields.Str(required=False)
    
    article_tags = fields.List(fields.Str(required=False), required=False)
    
    allow_coupon_with_rewards = fields.Boolean(required=False)
    
    gst_input = fields.Boolean(required=False)
    
    staff_selection = fields.Boolean(required=False)
    
    placing_for_customer = fields.Boolean(required=False)
    
    hide_on_storefront = fields.Boolean(required=False)
    
    pan_card = fields.Nested(PanCard, required=False)
    
    slug = fields.Str(required=False)
    
    is_universal = fields.Boolean(required=False)
    
    international_delivery_charges = fields.Nested(DeliveryChargesConfig, required=False)
    


class CartConfigDetailResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(CartConfigDetailObj, required=False)
    


class SelectAddressResponseError(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    cart_id = fields.Float(required=False)
    
    id = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    address = fields.Nested(AllAddressForSelectAddress, required=False)
    


class AllAddressForSelectAddress(BaseSchema):
    # Cart swagger.json

    
    address = fields.List(fields.Nested(Address, required=False), required=False)
    
    pii_masking = fields.Boolean(required=False)
    


class DeleteCartRequest(BaseSchema):
    # Cart swagger.json

    
    cart_id_list = fields.List(fields.Str(required=False), required=False)
    


