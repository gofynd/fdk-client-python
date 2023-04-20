"""PosCart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ..ApplicationModel import BaseSchema





class PromiseFormatted(BaseSchema):
    pass


class PromiseTimestamp(BaseSchema):
    pass


class ShipmentPromise(BaseSchema):
    pass


class DisplayBreakup(BaseSchema):
    pass


class LoyaltyPoints(BaseSchema):
    pass


class RawBreakup(BaseSchema):
    pass


class CouponBreakup(BaseSchema):
    pass


class CartBreakup(BaseSchema):
    pass


class PaymentSelectionLock(BaseSchema):
    pass


class CartCurrency(BaseSchema):
    pass


class ProductPrice(BaseSchema):
    pass


class ProductPriceInfo(BaseSchema):
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


class BaseInfo(BaseSchema):
    pass


class ProductImage(BaseSchema):
    pass


class CategoryInfo(BaseSchema):
    pass


class ActionQuery(BaseSchema):
    pass


class ProductAction(BaseSchema):
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


class ShipmentResponse(BaseSchema):
    pass


class CartShipmentsResponse(BaseSchema):
    pass


class UpdateCartShipmentItem(BaseSchema):
    pass


class UpdateCartShipmentRequest(BaseSchema):
    pass


class CartCheckoutCustomMeta(BaseSchema):
    pass


class StaffCheckout(BaseSchema):
    pass


class Files(BaseSchema):
    pass


class CartPosCheckoutDetailRequest(BaseSchema):
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


class CartDeliveryModesResponse(BaseSchema):
    pass


class PickupStoreDetail(BaseSchema):
    pass


class StoreDetailsResponse(BaseSchema):
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





class PromiseFormatted(BaseSchema):
    # PosCart swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class PromiseTimestamp(BaseSchema):
    # PosCart swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    


class ShipmentPromise(BaseSchema):
    # PosCart swagger.json

    
    formatted = fields.Nested(PromiseFormatted, required=False)
    
    timestamp = fields.Nested(PromiseTimestamp, required=False)
    


class DisplayBreakup(BaseSchema):
    # PosCart swagger.json

    
    message = fields.List(fields.Str(required=False), required=False)
    
    display = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    key = fields.Str(required=False)
    


class LoyaltyPoints(BaseSchema):
    # PosCart swagger.json

    
    total = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    applicable = fields.Float(required=False)
    
    description = fields.Str(required=False)
    


class RawBreakup(BaseSchema):
    # PosCart swagger.json

    
    discount = fields.Float(required=False)
    
    cod_charge = fields.Float(required=False)
    
    coupon = fields.Float(required=False)
    
    mrp_total = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    fynd_cash = fields.Float(required=False)
    
    you_saved = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    convenience_fee = fields.Float(required=False)
    
    vog = fields.Float(required=False)
    
    gst_charges = fields.Float(required=False)
    
    subtotal = fields.Float(required=False)
    


class CouponBreakup(BaseSchema):
    # PosCart swagger.json

    
    uid = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    value = fields.Float(required=False)
    
    type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class CartBreakup(BaseSchema):
    # PosCart swagger.json

    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    


class PaymentSelectionLock(BaseSchema):
    # PosCart swagger.json

    
    payment_identifier = fields.Str(required=False)
    
    default_options = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    


class CartCurrency(BaseSchema):
    # PosCart swagger.json

    
    symbol = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class ProductPrice(BaseSchema):
    # PosCart swagger.json

    
    add_on = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    selling = fields.Float(required=False)
    


class ProductPriceInfo(BaseSchema):
    # PosCart swagger.json

    
    converted = fields.Nested(ProductPrice, required=False)
    
    base = fields.Nested(ProductPrice, required=False)
    


class DiscountRulesApp(BaseSchema):
    # PosCart swagger.json

    
    item_criteria = fields.Dict(required=False)
    
    offer = fields.Dict(required=False)
    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    
    raw_offer = fields.Dict(required=False)
    


class BuyRules(BaseSchema):
    # PosCart swagger.json

    
    item_criteria = fields.Dict(required=False)
    
    cart_conditions = fields.Dict(required=False)
    


class FreeGiftItem(BaseSchema):
    # PosCart swagger.json

    
    item_brand_name = fields.Str(required=False)
    
    item_slug = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    item_name = fields.Str(required=False)
    
    item_price_details = fields.Dict(required=False)
    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    


class AppliedFreeArticles(BaseSchema):
    # PosCart swagger.json

    
    article_id = fields.Str(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
    free_gift_item_details = fields.Nested(FreeGiftItem, required=False)
    
    quantity = fields.Int(required=False)
    


class AppliedPromotion(BaseSchema):
    # PosCart swagger.json

    
    promo_id = fields.Str(required=False)
    
    promotion_group = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesApp, required=False), required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRules, required=False), required=False)
    
    offer_text = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    article_quantity = fields.Int(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    


class ProductAvailability(BaseSchema):
    # PosCart swagger.json

    
    other_store_quantity = fields.Int(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    deliverable = fields.Boolean(required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    is_valid = fields.Boolean(required=False)
    


class BaseInfo(BaseSchema):
    # PosCart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class ProductImage(BaseSchema):
    # PosCart swagger.json

    
    url = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    


class CategoryInfo(BaseSchema):
    # PosCart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class ActionQuery(BaseSchema):
    # PosCart swagger.json

    
    product_slug = fields.List(fields.Str(required=False), required=False)
    


class ProductAction(BaseSchema):
    # PosCart swagger.json

    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    query = fields.Nested(ActionQuery, required=False)
    


class CartProduct(BaseSchema):
    # PosCart swagger.json

    
    uid = fields.Int(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    name = fields.Str(required=False)
    


class PromoMeta(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    


class CartProductIdentifer(BaseSchema):
    # PosCart swagger.json

    
    identifier = fields.Str(required=False)
    


class BasePrice(BaseSchema):
    # PosCart swagger.json

    
    marked = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class ArticlePriceInfo(BaseSchema):
    # PosCart swagger.json

    
    converted = fields.Nested(BasePrice, required=False)
    
    base = fields.Nested(BasePrice, required=False)
    


class ProductArticle(BaseSchema):
    # PosCart swagger.json

    
    uid = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class CartProductInfo(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    discount = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    coupon_message = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    key = fields.Str(required=False)
    


class CartDetailResponse(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    comment = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    id = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    


class AddProductCart(BaseSchema):
    # PosCart swagger.json

    
    store_id = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    seller_id = fields.Int(required=False)
    
    display = fields.Str(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    item_id = fields.Int(required=False)
    
    article_assignment = fields.Dict(required=False)
    
    article_id = fields.Str(required=False)
    
    pos = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    


class AddCartRequest(BaseSchema):
    # PosCart swagger.json

    
    new_cart = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    


class AddCartDetailResponse(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    success = fields.Boolean(required=False)
    
    partial = fields.Boolean(required=False)
    


class UpdateProductCart(BaseSchema):
    # PosCart swagger.json

    
    extra_meta = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    item_size = fields.Str(required=False)
    
    item_index = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    article_id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class UpdateCartRequest(BaseSchema):
    # PosCart swagger.json

    
    items = fields.List(fields.Nested(UpdateProductCart, required=False), required=False)
    
    operation = fields.Str(required=False)
    


class UpdateCartDetailResponse(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    success = fields.Boolean(required=False)
    


class CartItemCountResponse(BaseSchema):
    # PosCart swagger.json

    
    user_cart_items_count = fields.Int(required=False)
    


class Coupon(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    title = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    is_applicable = fields.Boolean(required=False)
    
    expires_on = fields.Str(required=False)
    
    sub_title = fields.Str(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    coupon_code = fields.Str(required=False)
    


class PageCoupon(BaseSchema):
    # PosCart swagger.json

    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    total_item_count = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class GetCouponResponse(BaseSchema):
    # PosCart swagger.json

    
    available_coupon_list = fields.List(fields.Nested(Coupon, required=False), required=False)
    
    page = fields.Nested(PageCoupon, required=False)
    


class ApplyCouponRequest(BaseSchema):
    # PosCart swagger.json

    
    coupon_code = fields.Str(required=False)
    


class OfferPrice(BaseSchema):
    # PosCart swagger.json

    
    marked = fields.Int(required=False)
    
    effective = fields.Int(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    bulk_effective = fields.Float(required=False)
    


class OfferItem(BaseSchema):
    # PosCart swagger.json

    
    margin = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    total = fields.Float(required=False)
    
    best = fields.Boolean(required=False)
    
    auto_applied = fields.Boolean(required=False)
    
    price = fields.Nested(OfferPrice, required=False)
    
    quantity = fields.Int(required=False)
    


class OfferSeller(BaseSchema):
    # PosCart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class BulkPriceOffer(BaseSchema):
    # PosCart swagger.json

    
    offers = fields.List(fields.Nested(OfferItem, required=False), required=False)
    
    seller = fields.Nested(OfferSeller, required=False)
    


class BulkPriceResponse(BaseSchema):
    # PosCart swagger.json

    
    data = fields.List(fields.Nested(BulkPriceOffer, required=False), required=False)
    


class RewardPointRequest(BaseSchema):
    # PosCart swagger.json

    
    points = fields.Boolean(required=False)
    


class GeoLocation(BaseSchema):
    # PosCart swagger.json

    
    longitude = fields.Float(required=False)
    
    latitude = fields.Float(required=False)
    


class Address(BaseSchema):
    # PosCart swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    country_code = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    geo_location = fields.Nested(GeoLocation, required=False)
    
    meta = fields.Dict(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    country = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    city = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    landmark = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    google_map_point = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    


class GetAddressesResponse(BaseSchema):
    # PosCart swagger.json

    
    address = fields.List(fields.Nested(Address, required=False), required=False)
    


class SaveAddressResponse(BaseSchema):
    # PosCart swagger.json

    
    is_default_address = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    


class UpdateAddressResponse(BaseSchema):
    # PosCart swagger.json

    
    is_updated = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    


class DeleteAddressResponse(BaseSchema):
    # PosCart swagger.json

    
    is_deleted = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    


class SelectCartAddressRequest(BaseSchema):
    # PosCart swagger.json

    
    billing_address_id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class UpdateCartPaymentRequest(BaseSchema):
    # PosCart swagger.json

    
    address_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    


class CouponValidity(BaseSchema):
    # PosCart swagger.json

    
    valid = fields.Boolean(required=False)
    
    discount = fields.Float(required=False)
    
    title = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    display_message_en = fields.Str(required=False)
    


class PaymentCouponValidate(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    coupon_validity = fields.Nested(CouponValidity, required=False)
    


class ShipmentResponse(BaseSchema):
    # PosCart swagger.json

    
    box_type = fields.Str(required=False)
    
    dp_id = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    shipments = fields.Int(required=False)
    
    dp_options = fields.Dict(required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    promise = fields.Nested(ShipmentPromise, required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    shipment_type = fields.Str(required=False)
    


class CartShipmentsResponse(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    comment = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    error = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    


class UpdateCartShipmentItem(BaseSchema):
    # PosCart swagger.json

    
    article_uid = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    shipment_type = fields.Str(required=False)
    


class UpdateCartShipmentRequest(BaseSchema):
    # PosCart swagger.json

    
    shipments = fields.List(fields.Nested(UpdateCartShipmentItem, required=False), required=False)
    


class CartCheckoutCustomMeta(BaseSchema):
    # PosCart swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class StaffCheckout(BaseSchema):
    # PosCart swagger.json

    
    _id = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    user = fields.Str(required=False)
    


class Files(BaseSchema):
    # PosCart swagger.json

    
    values = fields.List(fields.Str(required=False), required=False)
    
    key = fields.Str(required=False)
    


class CartPosCheckoutDetailRequest(BaseSchema):
    # PosCart swagger.json

    
    custom_meta = fields.List(fields.Nested(CartCheckoutCustomMeta, required=False), required=False)
    
    payment_mode = fields.Str(required=False)
    
    payment_params = fields.Dict(required=False)
    
    address_id = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    billing_address = fields.Dict(required=False)
    
    staff = fields.Nested(StaffCheckout, required=False)
    
    merchant_code = fields.Str(required=False)
    
    pos = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    callback_url = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    pick_at_store_uid = fields.Int(required=False)
    
    ordering_store = fields.Int(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    aggregator = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    order_type = fields.Str(required=False)
    
    files = fields.List(fields.Nested(Files, required=False), required=False)
    
    delivery_address = fields.Dict(required=False)
    


class CheckCart(BaseSchema):
    # PosCart swagger.json

    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    cod_available = fields.Boolean(required=False)
    
    store_emps = fields.List(fields.Dict(required=False), required=False)
    
    gstin = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    delivery_charge_order_value = fields.Int(required=False)
    
    error_message = fields.Str(required=False)
    
    user_type = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    comment = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    delivery_charges = fields.Int(required=False)
    
    cod_charges = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    store_code = fields.Str(required=False)
    
    cod_message = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class CartCheckoutResponse(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    
    cart = fields.Nested(CheckCart, required=False)
    
    callback_url = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    app_intercept_url = fields.Str(required=False)
    
    payment_confirm_url = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    


class CartMetaRequest(BaseSchema):
    # PosCart swagger.json

    
    pick_up_customer_details = fields.Dict(required=False)
    
    comment = fields.Str(required=False)
    
    delivery_slots = fields.Dict(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    


class CartMetaResponse(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    


class CartMetaMissingResponse(BaseSchema):
    # PosCart swagger.json

    
    errors = fields.List(fields.Str(required=False), required=False)
    


class CartDeliveryModesResponse(BaseSchema):
    # PosCart swagger.json

    
    available_modes = fields.List(fields.Str(required=False), required=False)
    
    pickup_stores = fields.List(fields.Int(required=False), required=False)
    


class PickupStoreDetail(BaseSchema):
    # PosCart swagger.json

    
    uid = fields.Int(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    area_code = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class StoreDetailsResponse(BaseSchema):
    # PosCart swagger.json

    
    items = fields.List(fields.Nested(PickupStoreDetail, required=False), required=False)
    


class GetShareCartLinkRequest(BaseSchema):
    # PosCart swagger.json

    
    meta = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    


class GetShareCartLinkResponse(BaseSchema):
    # PosCart swagger.json

    
    share_url = fields.Str(required=False)
    
    token = fields.Str(required=False)
    


class SharedCartDetails(BaseSchema):
    # PosCart swagger.json

    
    source = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    token = fields.Str(required=False)
    


class SharedCart(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    comment = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    last_modified = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    
    id = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    


class SharedCartResponse(BaseSchema):
    # PosCart swagger.json

    
    cart = fields.Nested(SharedCart, required=False)
    
    error = fields.Str(required=False)
    


