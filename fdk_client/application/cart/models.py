"""Cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class BuyRules(BaseSchema):
    pass


class DiscountRulesApp(BaseSchema):
    pass


class Ownership(BaseSchema):
    pass


class FreeGiftItem(BaseSchema):
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


class ArticlePriceInfo(BaseSchema):
    pass


class BaseInfo(BaseSchema):
    pass


class StoreInfo(BaseSchema):
    pass


class ProductArticle(BaseSchema):
    pass


class CartProductIdentifer(BaseSchema):
    pass


class PromoMeta(BaseSchema):
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


class ProductActionParams(BaseSchema):
    pass


class ProductActionPage(BaseSchema):
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


class CartProductInfo(BaseSchema):
    pass


class DisplayBreakup(BaseSchema):
    pass


class RawBreakup(BaseSchema):
    pass


class CouponBreakup(BaseSchema):
    pass


class LoyaltyPoints(BaseSchema):
    pass


class CartBreakup(BaseSchema):
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


class CartDetailResult(BaseSchema):
    pass


class AddProductCart(BaseSchema):
    pass


class AddCartCreation(BaseSchema):
    pass


class AddCartDetailResult(BaseSchema):
    pass


class UpdateProductCart(BaseSchema):
    pass


class FreeGiftItemCreation(BaseSchema):
    pass


class UpdateCartCreation(BaseSchema):
    pass


class UpdateCartDetailResult(BaseSchema):
    pass


class DeleteCartDetailResult(BaseSchema):
    pass


class CartItemCountResult(BaseSchema):
    pass


class PageCoupon(BaseSchema):
    pass


class Coupon(BaseSchema):
    pass


class GetCouponResult(BaseSchema):
    pass


class ApplyCoupon(BaseSchema):
    pass


class OfferPrice(BaseSchema):
    pass


class OfferItem(BaseSchema):
    pass


class OfferSeller(BaseSchema):
    pass


class BulkPriceOffer(BaseSchema):
    pass


class BulkPriceResult(BaseSchema):
    pass


class RewardPointCreation(BaseSchema):
    pass


class GeoLocation(BaseSchema):
    pass


class Address(BaseSchema):
    pass


class ValidationConfig(BaseSchema):
    pass


class GetAddressesResult(BaseSchema):
    pass


class SaveAddressResult(BaseSchema):
    pass


class UpdateAddressResult(BaseSchema):
    pass


class DeleteAddressResult(BaseSchema):
    pass


class SelectCartAddressCreation(BaseSchema):
    pass


class UpdateCartPaymentCreation(BaseSchema):
    pass


class CouponValidity(BaseSchema):
    pass


class PaymentCouponValidate(BaseSchema):
    pass


class ShipmentResult(BaseSchema):
    pass


class CartShipmentsResult(BaseSchema):
    pass


class CartCheckoutCustomMeta(BaseSchema):
    pass


class CustomerDetails(BaseSchema):
    pass


class StaffCheckout(BaseSchema):
    pass


class CartCheckoutDetailCreation(BaseSchema):
    pass


class CheckCart(BaseSchema):
    pass


class CartCheckoutResult(BaseSchema):
    pass


class GiftDetail(BaseSchema):
    pass


class ArticleGiftDetail(BaseSchema):
    pass


class CartMetaCreation(BaseSchema):
    pass


class CartMetaResult(BaseSchema):
    pass


class CartMetaMissingResult(BaseSchema):
    pass


class GetShareCartLinkCreation(BaseSchema):
    pass


class GetShareCartLinkResult(BaseSchema):
    pass


class SharedCartDetails(BaseSchema):
    pass


class SharedCart(BaseSchema):
    pass


class SharedCartResult(BaseSchema):
    pass


class PriceMinMax(BaseSchema):
    pass


class ItemPriceDetails(BaseSchema):
    pass


class ArticlePriceDetails(BaseSchema):
    pass


class FreeGiftItems(BaseSchema):
    pass


class PromotionOffer(BaseSchema):
    pass


class PromotionOffersResult(BaseSchema):
    pass


class PromotionPaymentOffer(BaseSchema):
    pass


class PromotionPaymentOffersResult(BaseSchema):
    pass


class OperationErrorResult(BaseSchema):
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


class CartCheckoutDetailV2Creation(BaseSchema):
    pass


class ValidationError(BaseSchema):
    pass





class BuyRules(BaseSchema):
    # Cart swagger.json

    
    item_criteria = fields.Dict(required=False)
    
    cart_conditions = fields.Dict(required=False)
    


class DiscountRulesApp(BaseSchema):
    # Cart swagger.json

    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    
    raw_offer = fields.Dict(required=False)
    
    offer = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    


class Ownership(BaseSchema):
    # Cart swagger.json

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    


class FreeGiftItem(BaseSchema):
    # Cart swagger.json

    
    item_slug = fields.Str(required=False)
    
    item_name = fields.Str(required=False)
    
    item_price_details = fields.Dict(required=False)
    
    item_brand_name = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    


class AppliedFreeArticles(BaseSchema):
    # Cart swagger.json

    
    free_gift_item_details = fields.Nested(FreeGiftItems, required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    


class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    promo_id = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    offer_text = fields.Str(required=False)
    
    promotion_group = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    promotion_name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesApp, required=False), required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    article_quantity = fields.Int(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    
    promotion_type = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    code = fields.Str(required=False, allow_none=True)
    


class PaymentSelectionLock(BaseSchema):
    # Cart swagger.json

    
    enabled = fields.Boolean(required=False)
    
    default_options = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    


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
    


class BasePrice(BaseSchema):
    # Cart swagger.json

    
    effective = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    marked = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    


class ArticlePriceInfo(BaseSchema):
    # Cart swagger.json

    
    base = fields.Nested(BasePrice, required=False)
    
    converted = fields.Nested(BasePrice, required=False)
    


class BaseInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class StoreInfo(BaseSchema):
    # Cart swagger.json

    
    store_code = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    extra_meta = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    mto_quantity = fields.Int(required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    identifier = fields.Dict(required=False)
    
    store = fields.Nested(StoreInfo, required=False)
    
    cart_item_meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    gift_card = fields.Dict(required=False)
    
    is_gift_visible = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class CartProductIdentifer(BaseSchema):
    # Cart swagger.json

    
    identifier = fields.Str(required=False)
    


class PromoMeta(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    


class ChargesAmount(BaseSchema):
    # Cart swagger.json

    
    value = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    


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

    
    currency_symbol = fields.Str(required=False)
    
    selling = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    add_on = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    


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
    


class ProductActionParams(BaseSchema):
    # Cart swagger.json

    
    slug = fields.List(fields.Str(required=False), required=False)
    


class ProductActionPage(BaseSchema):
    # Cart swagger.json

    
    type = fields.Str(required=False)
    
    params = fields.Nested(ProductActionParams, required=False)
    


class ProductAction(BaseSchema):
    # Cart swagger.json

    
    query = fields.Nested(ActionQuery, required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    page = fields.Nested(ProductActionPage, required=False)
    


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

    
    _custom_json = fields.Dict(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    teaser_tag = fields.Nested(Tags, required=False)
    
    slug = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    item_code = fields.Str(required=False, allow_none=True)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    


class CouponDetails(BaseSchema):
    # Cart swagger.json

    
    discount_single_quantity = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    discount_total_quantity = fields.Float(required=False)
    


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    article = fields.Nested(ProductArticle, required=False)
    
    moq = fields.Dict(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    charges = fields.List(fields.Nested(Charges, required=False), required=False)
    
    discount = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    product_ean_id = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    coupon = fields.Nested(CouponDetails, required=False)
    
    custom_order = fields.Dict(required=False)
    
    coupon_message = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    price_per_unit = fields.Nested(ProductPricePerUnitInfo, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    


class DisplayBreakup(BaseSchema):
    # Cart swagger.json

    
    currency_symbol = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    message = fields.List(fields.Str(required=False), required=False)
    
    currency_code = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    preset = fields.Float(required=False)
    


class RawBreakup(BaseSchema):
    # Cart swagger.json

    
    vog = fields.Float(required=False)
    
    subtotal = fields.Float(required=False)
    
    fynd_cash = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    convenience_fee = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    gst_charges = fields.Float(required=False)
    
    mrp_total = fields.Float(required=False)
    
    mop_total = fields.Float(required=False)
    
    total_charge = fields.Float(required=False)
    
    coupon = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    gift_card = fields.Float(required=False)
    
    you_saved = fields.Float(required=False)
    
    cod_charge = fields.Float(required=False)
    


class CouponBreakup(BaseSchema):
    # Cart swagger.json

    
    coupon_value = fields.Float(required=False)
    
    title = fields.Str(required=False, allow_none=True)
    
    sub_title = fields.Str(required=False, allow_none=True)
    
    minimum_cart_value = fields.Float(required=False)
    
    message = fields.Str(required=False)
    
    coupon_type = fields.Str(required=False, allow_none=True)
    
    uid = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    description = fields.Str(required=False, allow_none=True)
    
    code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class LoyaltyPoints(BaseSchema):
    # Cart swagger.json

    
    total = fields.Float(required=False)
    
    description = fields.Str(required=False)
    
    applicable = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    


class CartBreakup(BaseSchema):
    # Cart swagger.json

    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    


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
    


class CartDetailResult(BaseSchema):
    # Cart swagger.json

    
    cart_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    checkout_mode = fields.Str(required=False)
    
    pan_no = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    comment = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    common_config = fields.Nested(CartCommonConfig, required=False)
    
    coupon = fields.Nested(CartDetailCoupon, required=False)
    
    message = fields.Str(required=False)
    
    notification = fields.Dict(required=False)
    
    staff_user_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    gstin = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    coupon_text = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    pan_config = fields.Dict(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class AddProductCart(BaseSchema):
    # Cart swagger.json

    
    article_assignment = fields.Dict(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False, allow_none=True), required=False)
    
    extra_meta = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    item_size = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    display = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    
    parent_item_identifiers = fields.List(fields.Dict(required=False), required=False)
    
    seller_id = fields.Int(required=False)
    
    pos = fields.Boolean(required=False)
    
    item_id = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    


class AddCartCreation(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    
    new_cart = fields.Boolean(required=False)
    


class AddCartDetailResult(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    partial = fields.Boolean(required=False)
    
    cart = fields.Nested(CartDetailResult, required=False)
    
    success = fields.Boolean(required=False)
    


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
    
    item_id = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    


class FreeGiftItemCreation(BaseSchema):
    # Cart swagger.json

    
    promotion_id = fields.Str(required=False)
    
    item_id = fields.Str(required=False)
    
    item_size = fields.Str(required=False)
    


class UpdateCartCreation(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(UpdateProductCart, required=False), required=False)
    
    free_gift_items = fields.List(fields.Nested(FreeGiftItemCreation, required=False), required=False)
    
    operation = fields.Str(required=False)
    


class UpdateCartDetailResult(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    cart = fields.Nested(CartDetailResult, required=False)
    
    success = fields.Boolean(required=False)
    


class DeleteCartDetailResult(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class CartItemCountResult(BaseSchema):
    # Cart swagger.json

    
    user_cart_items_count = fields.Int(required=False)
    


class PageCoupon(BaseSchema):
    # Cart swagger.json

    
    total_item_count = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    total = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    


class Coupon(BaseSchema):
    # Cart swagger.json

    
    coupon_amount = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    title = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    sub_title = fields.Str(required=False)
    
    expires_on = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    coupon_type = fields.Str(required=False, allow_none=True)
    
    max_discount_value = fields.Float(required=False)
    
    coupon_code = fields.Str(required=False)
    
    is_applicable = fields.Boolean(required=False)
    
    description = fields.Str(required=False, allow_none=True)
    
    is_applied = fields.Boolean(required=False)
    
    start_date = fields.Str(required=False, allow_none=True)
    
    end_date = fields.Str(required=False, allow_none=True)
    
    coupon_applicable_message = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    is_bank_offer = fields.Boolean(required=False)
    


class GetCouponResult(BaseSchema):
    # Cart swagger.json

    
    page = fields.Nested(PageCoupon, required=False)
    
    available_coupon_list = fields.List(fields.Nested(Coupon, required=False), required=False)
    


class ApplyCoupon(BaseSchema):
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
    


class BulkPriceResult(BaseSchema):
    # Cart swagger.json

    
    data = fields.List(fields.Nested(BulkPriceOffer, required=False), required=False)
    


class RewardPointCreation(BaseSchema):
    # Cart swagger.json

    
    points = fields.Boolean(required=False)
    


class GeoLocation(BaseSchema):
    # Cart swagger.json

    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    


class Address(BaseSchema):
    # Cart swagger.json

    
    country_iso_code = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    country_phone_code = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    geo_location = fields.Nested(GeoLocation, required=False)
    
    id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    city = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    created_by_user_id = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    google_map_point = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    country_code = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    area_code = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class ValidationConfig(BaseSchema):
    # Cart swagger.json

    
    address_max_limit = fields.Int(required=False)
    
    user_address_count = fields.Int(required=False)
    


class GetAddressesResult(BaseSchema):
    # Cart swagger.json

    
    pii_masking = fields.Boolean(required=False)
    
    address = fields.List(fields.Nested(Address, required=False), required=False)
    
    validation_config = fields.Nested(ValidationConfig, required=False)
    


class SaveAddressResult(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    is_default_address = fields.Boolean(required=False)
    


class UpdateAddressResult(BaseSchema):
    # Cart swagger.json

    
    is_updated = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    is_default_address = fields.Boolean(required=False)
    


class DeleteAddressResult(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    is_deleted = fields.Boolean(required=False)
    


class SelectCartAddressCreation(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    


class UpdateCartPaymentCreation(BaseSchema):
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
    
    discount = fields.Float(required=False)
    
    next_validation_required = fields.Boolean(required=False, allow_none=True)
    
    valid = fields.Boolean(required=False)
    
    display_message_en = fields.Str(required=False, allow_none=True)
    
    code = fields.Str(required=False, allow_none=True)
    
    error_en = fields.Str(required=False, allow_none=True)
    


class PaymentCouponValidate(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    coupon_validity = fields.Nested(CouponValidity, required=False)
    
    success = fields.Boolean(required=False)
    


class ShipmentResult(BaseSchema):
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
    


class CartShipmentsResult(BaseSchema):
    # Cart swagger.json

    
    delivery_charge_info = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    id = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResult, required=False), required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    coupon_text = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    error = fields.Boolean(required=False)
    
    comment = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
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
    


class CartCheckoutDetailCreation(BaseSchema):
    # Cart swagger.json

    
    custom_meta = fields.List(fields.Nested(CartCheckoutCustomMeta, required=False), required=False)
    
    customer_details = fields.Nested(CustomerDetails, required=False)
    
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

    
    checkout_mode = fields.Str(required=False)
    
    user_type = fields.Str(required=False)
    
    cod_message = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    id = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    error_message = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    comment = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    uid = fields.Str(required=False)
    
    delivery_charge_order_value = fields.Int(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    cod_available = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    store_code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    store_emps = fields.List(fields.Dict(required=False), required=False)
    
    coupon_text = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    cod_charges = fields.Float(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class CartCheckoutResult(BaseSchema):
    # Cart swagger.json

    
    payment_confirm_url = fields.Str(required=False)
    
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
    


class CartMetaCreation(BaseSchema):
    # Cart swagger.json

    
    delivery_slots = fields.Dict(required=False)
    
    gift_details = fields.Nested(ArticleGiftDetail, required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class CartMetaResult(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    


class CartMetaMissingResult(BaseSchema):
    # Cart swagger.json

    
    errors = fields.List(fields.Str(required=False), required=False)
    


class GetShareCartLinkCreation(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class GetShareCartLinkResult(BaseSchema):
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

    
    checkout_mode = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    comment = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    uid = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    coupon_text = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class SharedCartResult(BaseSchema):
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
    


class ArticlePriceDetails(BaseSchema):
    # Cart swagger.json

    
    marked = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    


class FreeGiftItems(BaseSchema):
    # Cart swagger.json

    
    item_slug = fields.Str(required=False)
    
    item_name = fields.Str(required=False)
    
    item_price_details = fields.Nested(ItemPriceDetails, required=False)
    
    article_price = fields.Nested(ArticlePriceDetails, required=False)
    
    item_brand_name = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    available_sizes = fields.List(fields.Str(required=False), required=False)
    
    size = fields.Str(required=False)
    
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
    


class PromotionOffersResult(BaseSchema):
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
    


class PromotionPaymentOffersResult(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    promotions = fields.List(fields.Nested(PromotionPaymentOffer, required=False), required=False)
    


class OperationErrorResult(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


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
    
    name = fields.Str(required=False)
    
    payment_extra_identifiers = fields.Dict(required=False)
    


class CartCheckoutDetailV2Creation(BaseSchema):
    # Cart swagger.json

    
    custom_meta = fields.List(fields.Nested(CartCheckoutCustomMeta, required=False), required=False)
    
    customer_details = fields.Nested(CustomerDetails, required=False)
    
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
    


class ValidationError(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    field = fields.Str(required=False)
    


