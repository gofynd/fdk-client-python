"""Catalog Platform Enum."""

from enum import Enum


class order(Enum):
    
    BROWNTAPE_V2 = "browntape_v2"
    
    EASYOPS = "easyops"
    
    HOLISOL = "holisol"
    
    LOGIC = "logic"
    
    TCNSS = "tcnss"
    
    INCREFF = "increff"
    
    LIBERTY = "liberty"
    
    BROWNTAPE = "browntape"
    
    EASYECOM = "easyecom"
    
    MAJOR_BRANDS = "major_brands"
    
    JIOPOS = "jiopos"
    
    JOCKEY = "jockey"
    
    OMSGURU = "omsguru"
    
    PULSE = "pulse"
    
    SELLERWARE = "sellerware"
    
    UNICOMMERCE = "unicommerce"
    
    ETHOS = "ethos"
    
    SARASUOLE = "sarasuole"
    
    VAJOR = "vajor"
    
    VINCULUM = "vinculum"
    
    JIOMART_POS = "jiomart_pos"
    
    RBL_SAP = "rbl_sap"
    
    GINESYS_POS = "ginesys-pos"
    
    FYNDPOS = "fyndpos"
    
    JIOPOS_OPENAPI = "jiopos_openapi"
    
    JIOPOS_HAMLEYS = "jiopos_hamleys"
    
    WESTELM = "westelm"
    
    RBL_SAP_FURNITURE = "rbl_sap_furniture"
    
    VINCULUM_V2 = "vinculum_v2"
    
    WIZAPP = "wizapp"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid order type")


class PageType(Enum):
    
    ABOUT_US = "about-us"
    
    ADDRESSES = "addresses"
    
    BLOG = "blog"
    
    BRANDS = "brands"
    
    CARDS = "cards"
    
    CART = "cart"
    
    CATEGORIES = "categories"
    
    BRAND = "brand"
    
    CATEGORY = "category"
    
    COLLECTION = "collection"
    
    COLLECTIONS = "collections"
    
    CUSTOM = "custom"
    
    CONTACT_US = "contact-us"
    
    EXTERNAL = "external"
    
    FAQ = "faq"
    
    FRESHCHAT = "freshchat"
    
    HOME = "home"
    
    NOTIFICATION_SETTINGS = "notification-settings"
    
    ORDERS = "orders"
    
    PAGE = "page"
    
    POLICY = "policy"
    
    PRODUCT = "product"
    
    PRODUCT_REQUEST = "product-request"
    
    PRODUCTS = "products"
    
    PROFILE = "profile"
    
    PROFILE_ORDER_SHIPMENT = "profile-order-shipment"
    
    PROFILE_BASIC = "profile-basic"
    
    PROFILE_COMPANY = "profile-company"
    
    PROFILE_EMAILS = "profile-emails"
    
    PROFILE_PHONES = "profile-phones"
    
    RATE_US = "rate-us"
    
    REFER_EARN = "refer-earn"
    
    SETTINGS = "settings"
    
    SHARED_CART = "shared-cart"
    
    TNC = "tnc"
    
    TRACK_ORDER = "track-order"
    
    WISHLIST = "wishlist"
    
    SECTIONS = "sections"
    
    FORM = "form"
    
    CART_DELIVERY = "cart-delivery"
    
    CART_PAYMENT = "cart-payment"
    
    CART_REVIEW = "cart-review"
    
    LOGIN = "login"
    
    REGISTER = "register"
    
    SHIPPING_POLICY = "shipping-policy"
    
    RETURN_POLICY = "return-policy"
    
    ORDER_STATUS = "order-status"
    
    LOCATE_US = "locate-us"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid PageType type")


class CurrencyCodeEnum(Enum):
    
    INR = "INR"
    
    USD = "USD"
    
    EUR = "EUR"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid CurrencyCodeEnum type")

