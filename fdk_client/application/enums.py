"""Application Enums."""

from enum import Enum









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
    
    PRODUCT_REVIEWS = "product-reviews"
    
    ADD_PRODUCT_REVIEW = "add-product-review"
    
    PRODUCT_REQUEST = "product-request"
    
    PRODUCTS = "products"
    
    PROFILE = "profile"
    
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
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid PageType type")











