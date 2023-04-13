"""Cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class RawBreakup(BaseSchema):
    pass


class DisplayBreakup(BaseSchema):
    pass


class CouponBreakup(BaseSchema):
    pass


class LoyaltyPoints(BaseSchema):
    pass


class CartBreakup(BaseSchema):
    pass


class PromiseFormatted(BaseSchema):
    pass


class PromiseTimestamp(BaseSchema):
    pass


class ShipmentPromise(BaseSchema):
    pass


class CartCurrency(BaseSchema):
    pass


class Ownership(BaseSchema):
    pass


class BuyRules(BaseSchema):
    pass


class FreeGiftItem(BaseSchema):
    pass


class AppliedFreeArticles(BaseSchema):
    pass


class DiscountRulesApp(BaseSchema):
    pass


class AppliedPromotion(BaseSchema):
    pass


class ProductAvailabilitySize(BaseSchema):
    pass


class ProductAvailability(BaseSchema):
    pass


class ProductPrice(BaseSchema):
    pass


class ProductPriceInfo(BaseSchema):
    pass


class PromoMeta(BaseSchema):
    pass


class CartProductIdentifer(BaseSchema):
    pass


class NetQuantity(BaseSchema):
    pass


class CategoryInfo(BaseSchema):
    pass


class ProductImage(BaseSchema):
    pass


class ActionQuery(BaseSchema):
    pass


class ProductAction(BaseSchema):
    pass


class BaseInfo(BaseSchema):
    pass


class CartProduct(BaseSchema):
    pass


class BasePrice(BaseSchema):
    pass


class ArticlePriceInfo(BaseSchema):
    pass


class ProductArticle(BaseSchema):
    pass


class CartProductInfo(BaseSchema):
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


class OfferSeller(BaseSchema):
    pass


class OfferPrice(BaseSchema):
    pass


class OfferItem(BaseSchema):
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


class ShipmentResponse(BaseSchema):
    pass


class CartShipmentsResponse(BaseSchema):
    pass


class StaffCheckout(BaseSchema):
    pass


class CartCheckoutCustomMeta(BaseSchema):
    pass


class CartCheckoutDetailRequest(BaseSchema):
    pass


class CheckCart(BaseSchema):
    pass


class CartCheckoutResponse(BaseSchema):
    pass


class CartMetaRequest(BaseSchema):
    pass


class CartMetaResponse(BaseSchema):
    pass


class CartMetaMissingResponse(BaseSchema):
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


class FreeGiftItems(BaseSchema):
    pass


class PromotionOffer(BaseSchema):
    pass


class PromotionOffersResponse(BaseSchema):
    pass


class OperationErrorResponse(BaseSchema):
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





class RawBreakup(BaseSchema):
    # Cart swagger.json

    
    convenience_fee = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    fynd_cash = fields.Float(required=False)
    
    coupon = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    vog = fields.Float(required=False)
    
    you_saved = fields.Float(required=False)
    
    cod_charge = fields.Float(required=False)
    
    subtotal = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    mrp_total = fields.Float(required=False)
    
    gst_charges = fields.Float(required=False)
    


class DisplayBreakup(BaseSchema):
    # Cart swagger.json

    
    value = fields.Float(required=False)
    
    key = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    message = fields.List(fields.Str(required=False), required=False)
    
    currency_symbol = fields.Str(required=False)
    


class CouponBreakup(BaseSchema):
    # Cart swagger.json

    
    title = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    sub_title = fields.Str(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    coupon_type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class LoyaltyPoints(BaseSchema):
    # Cart swagger.json

    
    total = fields.Float(required=False)
    
    description = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    applicable = fields.Float(required=False)
    


class CartBreakup(BaseSchema):
    # Cart swagger.json

    
    raw = fields.Nested(RawBreakup, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    


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
    


class CartCurrency(BaseSchema):
    # Cart swagger.json

    
    symbol = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class Ownership(BaseSchema):
    # Cart swagger.json

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    


class BuyRules(BaseSchema):
    # Cart swagger.json

    
    cart_conditions = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    


class FreeGiftItem(BaseSchema):
    # Cart swagger.json

    
    item_slug = fields.Str(required=False)
    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    
    item_id = fields.Int(required=False)
    
    item_name = fields.Str(required=False)
    
    item_brand_name = fields.Str(required=False)
    
    item_price_details = fields.Dict(required=False)
    


class AppliedFreeArticles(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
    free_gift_item_details = fields.Nested(FreeGiftItem, required=False)
    


class DiscountRulesApp(BaseSchema):
    # Cart swagger.json

    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    
    offer = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    
    raw_offer = fields.Dict(required=False)
    


class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    amount = fields.Float(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    offer_text = fields.Str(required=False)
    
    promotion_group = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    promo_id = fields.Str(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    
    article_quantity = fields.Int(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesApp, required=False), required=False)
    
    promotion_name = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    


class ProductAvailabilitySize(BaseSchema):
    # Cart swagger.json

    
    display = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    


class ProductAvailability(BaseSchema):
    # Cart swagger.json

    
    deliverable = fields.Boolean(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    available_sizes = fields.List(fields.Nested(ProductAvailabilitySize, required=False), required=False)
    
    other_store_quantity = fields.Int(required=False)
    


class ProductPrice(BaseSchema):
    # Cart swagger.json

    
    selling = fields.Float(required=False)
    
    add_on = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    marked = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    


class ProductPriceInfo(BaseSchema):
    # Cart swagger.json

    
    base = fields.Nested(ProductPrice, required=False)
    
    converted = fields.Nested(ProductPrice, required=False)
    


class PromoMeta(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    


class CartProductIdentifer(BaseSchema):
    # Cart swagger.json

    
    identifier = fields.Str(required=False)
    


class NetQuantity(BaseSchema):
    # Cart swagger.json

    
    value = fields.Str(required=False)
    
    unit = fields.Str(required=False)
    


class CategoryInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class ProductImage(BaseSchema):
    # Cart swagger.json

    
    url = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    


class ActionQuery(BaseSchema):
    # Cart swagger.json

    
    product_slug = fields.List(fields.Str(required=False), required=False)
    


class ProductAction(BaseSchema):
    # Cart swagger.json

    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    query = fields.Nested(ActionQuery, required=False)
    


class BaseInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class CartProduct(BaseSchema):
    # Cart swagger.json

    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    uid = fields.Int(required=False)
    
    item_code = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    type = fields.Str(required=False)
    


class BasePrice(BaseSchema):
    # Cart swagger.json

    
    currency_symbol = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    marked = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    


class ArticlePriceInfo(BaseSchema):
    # Cart swagger.json

    
    base = fields.Nested(BasePrice, required=False)
    
    converted = fields.Nested(BasePrice, required=False)
    


class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    parent_item_identifiers = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    parent_item_identifiers = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    key = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    is_set = fields.Boolean(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    coupon_message = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    moq = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    


class PaymentSelectionLock(BaseSchema):
    # Cart swagger.json

    
    payment_identifier = fields.Str(required=False)
    
    default_options = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    


class CartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    buy_now = fields.Boolean(required=False)
    
    comment = fields.Str(required=False)
    
    pan_config = fields.Dict(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    pan_no = fields.Str(required=False)
    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    coupon_text = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class AddProductCart(BaseSchema):
    # Cart swagger.json

    
    parent_item_identifiers = fields.Dict(required=False)
    
    item_size = fields.Str(required=False)
    
    pos = fields.Boolean(required=False)
    
    article_id = fields.Str(required=False)
    
    article_assignment = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    store_id = fields.Int(required=False)
    
    seller_id = fields.Int(required=False)
    
    display = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    


class AddCartRequest(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    
    new_cart = fields.Boolean(required=False)
    


class AddCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    partial = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


class UpdateProductCart(BaseSchema):
    # Cart swagger.json

    
    parent_item_identifiers = fields.Dict(required=False)
    
    item_size = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    
    item_index = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    item_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    


class UpdateCartRequest(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(UpdateProductCart, required=False), required=False)
    
    operation = fields.Str(required=False)
    


class UpdateCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    success = fields.Boolean(required=False)
    


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
    
    message = fields.Str(required=False)
    
    expires_on = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    sub_title = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    coupon_type = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    is_applicable = fields.Boolean(required=False)
    


class PageCoupon(BaseSchema):
    # Cart swagger.json

    
    total_item_count = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    


class GetCouponResponse(BaseSchema):
    # Cart swagger.json

    
    available_coupon_list = fields.List(fields.Nested(Coupon, required=False), required=False)
    
    page = fields.Nested(PageCoupon, required=False)
    


class ApplyCouponRequest(BaseSchema):
    # Cart swagger.json

    
    coupon_code = fields.Str(required=False)
    


class OfferSeller(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class OfferPrice(BaseSchema):
    # Cart swagger.json

    
    currency_code = fields.Str(required=False)
    
    bulk_effective = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    marked = fields.Int(required=False)
    
    effective = fields.Int(required=False)
    


class OfferItem(BaseSchema):
    # Cart swagger.json

    
    best = fields.Boolean(required=False)
    
    auto_applied = fields.Boolean(required=False)
    
    margin = fields.Int(required=False)
    
    total = fields.Float(required=False)
    
    quantity = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    price = fields.Nested(OfferPrice, required=False)
    


class BulkPriceOffer(BaseSchema):
    # Cart swagger.json

    
    seller = fields.Nested(OfferSeller, required=False)
    
    offers = fields.List(fields.Nested(OfferItem, required=False), required=False)
    


class BulkPriceResponse(BaseSchema):
    # Cart swagger.json

    
    data = fields.List(fields.Nested(BulkPriceOffer, required=False), required=False)
    


class RewardPointRequest(BaseSchema):
    # Cart swagger.json

    
    points = fields.Boolean(required=False)
    


class GeoLocation(BaseSchema):
    # Cart swagger.json

    
    longitude = fields.Float(required=False)
    
    latitude = fields.Float(required=False)
    


class Address(BaseSchema):
    # Cart swagger.json

    
    address = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country_phone_code = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    geo_location = fields.Nested(GeoLocation, required=False)
    
    google_map_point = fields.Dict(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    landmark = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    created_by_user_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    country_code = fields.Str(required=False)
    


class GetAddressesResponse(BaseSchema):
    # Cart swagger.json

    
    address = fields.List(fields.Nested(Address, required=False), required=False)
    
    pii_masking = fields.Boolean(required=False)
    


class SaveAddressResponse(BaseSchema):
    # Cart swagger.json

    
    is_default_address = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class UpdateAddressResponse(BaseSchema):
    # Cart swagger.json

    
    is_default_address = fields.Boolean(required=False)
    
    is_updated = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class DeleteAddressResponse(BaseSchema):
    # Cart swagger.json

    
    is_deleted = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    


class SelectCartAddressRequest(BaseSchema):
    # Cart swagger.json

    
    billing_address_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    


class UpdateCartPaymentRequest(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    address_id = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    


class CouponValidity(BaseSchema):
    # Cart swagger.json

    
    discount = fields.Float(required=False)
    
    display_message_en = fields.Str(required=False)
    
    valid = fields.Boolean(required=False)
    
    title = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class PaymentCouponValidate(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    coupon_validity = fields.Nested(CouponValidity, required=False)
    
    success = fields.Boolean(required=False)
    


class ShipmentResponse(BaseSchema):
    # Cart swagger.json

    
    promise = fields.Nested(ShipmentPromise, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    order_type = fields.Str(required=False)
    
    dp_id = fields.Str(required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    box_type = fields.Str(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    dp_options = fields.Dict(required=False)
    
    shipments = fields.Int(required=False)
    


class CartShipmentsResponse(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    buy_now = fields.Boolean(required=False)
    
    comment = fields.Str(required=False)
    
    error = fields.Boolean(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    last_modified = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    coupon_text = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class StaffCheckout(BaseSchema):
    # Cart swagger.json

    
    _id = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    employee_code = fields.Str(required=False)
    


class CartCheckoutCustomMeta(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class CartCheckoutDetailRequest(BaseSchema):
    # Cart swagger.json

    
    staff = fields.Nested(StaffCheckout, required=False)
    
    payment_params = fields.Dict(required=False)
    
    callback_url = fields.Str(required=False)
    
    ordering_store = fields.Int(required=False)
    
    payment_mode = fields.Str(required=False)
    
    custom_meta = fields.List(fields.Nested(CartCheckoutCustomMeta, required=False), required=False)
    
    extra_meta = fields.Dict(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    billing_address = fields.Dict(required=False)
    
    address_id = fields.Str(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    merchant_code = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    


class CheckCart(BaseSchema):
    # Cart swagger.json

    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    buy_now = fields.Boolean(required=False)
    
    comment = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    delivery_charge_order_value = fields.Int(required=False)
    
    delivery_charges = fields.Int(required=False)
    
    cod_available = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    store_emps = fields.List(fields.Dict(required=False), required=False)
    
    id = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    cod_charges = fields.Int(required=False)
    
    cod_message = fields.Str(required=False)
    
    error_message = fields.Str(required=False)
    
    user_type = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    success = fields.Boolean(required=False)
    
    coupon_text = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class CartCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    callback_url = fields.Str(required=False)
    
    app_intercept_url = fields.Str(required=False)
    
    payment_confirm_url = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    
    cart = fields.Nested(CheckCart, required=False)
    
    message = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    


class CartMetaRequest(BaseSchema):
    # Cart swagger.json

    
    gstin = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    


class CartMetaResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    


class CartMetaMissingResponse(BaseSchema):
    # Cart swagger.json

    
    errors = fields.List(fields.Str(required=False), required=False)
    


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

    
    source = fields.Dict(required=False)
    
    user = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    token = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    


class SharedCart(BaseSchema):
    # Cart swagger.json

    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    buy_now = fields.Boolean(required=False)
    
    comment = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    last_modified = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    uid = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    coupon_text = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class SharedCartResponse(BaseSchema):
    # Cart swagger.json

    
    error = fields.Str(required=False)
    
    cart = fields.Nested(SharedCart, required=False)
    


class FreeGiftItems(BaseSchema):
    # Cart swagger.json

    
    item_slug = fields.Str(required=False)
    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    
    item_id = fields.Int(required=False)
    
    item_name = fields.Str(required=False)
    
    item_brand_name = fields.Str(required=False)
    
    item_price_details = fields.Dict(required=False)
    


class PromotionOffer(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    valid_till = fields.Str(required=False)
    
    promotion_group = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    free_gift_items = fields.List(fields.Nested(FreeGiftItems, required=False), required=False)
    
    discount_rules = fields.List(fields.Dict(required=False), required=False)
    
    offer_text = fields.Str(required=False)
    


class PromotionOffersResponse(BaseSchema):
    # Cart swagger.json

    
    available_promotions = fields.List(fields.Nested(PromotionOffer, required=False), required=False)
    


class OperationErrorResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class LadderPrice(BaseSchema):
    # Cart swagger.json

    
    currency_code = fields.Str(required=False)
    
    offer_price = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    marked = fields.Int(required=False)
    
    effective = fields.Int(required=False)
    


class LadderOfferItem(BaseSchema):
    # Cart swagger.json

    
    min_quantity = fields.Int(required=False)
    
    margin = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    max_quantity = fields.Int(required=False)
    
    price = fields.Nested(LadderPrice, required=False)
    


class LadderPriceOffer(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    valid_till = fields.Str(required=False)
    
    promotion_group = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    calculate_on = fields.Str(required=False)
    
    free_gift_items = fields.List(fields.Nested(FreeGiftItems, required=False), required=False)
    
    offer_prices = fields.List(fields.Nested(LadderOfferItem, required=False), required=False)
    
    discount_rules = fields.List(fields.Dict(required=False), required=False)
    
    offer_text = fields.Str(required=False)
    


class CurrencyInfo(BaseSchema):
    # Cart swagger.json

    
    symbol = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class LadderPriceOffers(BaseSchema):
    # Cart swagger.json

    
    available_offers = fields.List(fields.Nested(LadderPriceOffer, required=False), required=False)
    
    currency = fields.Nested(CurrencyInfo, required=False)
    


