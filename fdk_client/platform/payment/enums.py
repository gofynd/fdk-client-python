"""Payment Platform Enum."""

from enum import Enum


class OrderingSource(Enum):
    
    STOREFRONT = "storefront"
    
    STORE_OS_POS = "store_os_pos"
    
    KIOSK = "kiosk"
    
    SCAN_GO = "scan_go"
    
    SMART_TROLLEY = "smart_trolley"
    
    GOFYND = "gofynd"
    
    UNIKET = "uniket"
    
    MARKETPLACE = "marketplace"
    
    SOCIAL_COMMERCE = "social_commerce"
    
    ONDC = "ondc"
    
    NEXUS = "nexus"
    
    NYKAA_FASHION = "nykaa_fashion"
    
    ETSY = "etsy"
    
    VUIVUI = "vuivui"
    
    ZILINGO = "zilingo"
    
    FIRSTCRY = "firstcry"
    
    BUKALAPAK = "bukalapak"
    
    MYNTRA_PPMP = "myntra_ppmp"
    
    LAZADA = "lazada"
    
    TIKTOK = "tiktok"
    
    SFCC = "sfcc"
    
    DEBENHAMS = "debenhams"
    
    PRESTOMALL = "prestomall"
    
    MEESHO = "meesho"
    
    AMAZON_VDF = "amazon_vdf"
    
    BIGCOMMERCE = "bigcommerce"
    
    SENDO = "sendo"
    
    STOREHIPPO = "storehippo"
    
    CDISCOUNT = "cdiscount"
    
    NYKAA = "nykaa"
    
    TRENDYOL = "trendyol"
    
    WELOVESHOPPING = "weloveshopping"
    
    JOLLEE = "jollee"
    
    WISH = "wish"
    
    TIKI = "tiki"
    
    CENTRAL_ONLINE = "central_online"
    
    Q10 = "q10"
    
    CRED = "cred"
    
    WALMART = "walmart"
    
    SNAPDEAL = "snapdeal"
    
    FLIPKART = "flipkart"
    
    BLIBLI = "blibli"
    
    AJIO_JIT = "ajio_jit"
    
    PHARMEASY = "pharmeasy"
    
    EZMALL = "ezmall"
    
    ADOBE_COMMERCE = "adobe_commerce"
    
    KARTMAX = "kartmax"
    
    SHOPEE = "shopee"
    
    ZALORA = "zalora"
    
    PRESTASHOP = "prestashop"
    
    SMYTTEN = "smytten"
    
    AMAZON_SC = "amazon_sc"
    
    URBANPIPER = "urbanpiper"
    
    FLIPKART_QUICK = "flipkart_quick"
    
    WOOCOMMERCE = "woocommerce"
    
    ZIVAME = "zivame"
    
    LELONG = "lelong"
    
    FACEBOOK = "facebook"
    
    JIOMART = "jiomart"
    
    GMC = "gmc"
    
    ROBINS = "robins"
    
    AKULAKU = "akulaku"
    
    NOON = "noon"
    
    TATACLIQ = "tatacliq"
    
    KARTROCKET = "kartrocket"
    
    INORBIT = "inorbit"
    
    AJIO_BUSINESS = "ajio_business"
    
    SWIGGY = "swiggy"
    
    ASOS = "asos"
    
    TOKOPEDIA = "tokopedia"
    
    LIMEROAD = "limeroad"
    
    MYNTRA_OMNI = "myntra_omni"
    
    SPOYL = "spoyl"
    
    AMAZON_MLF = "amazon_mlf"
    
    FULFILLED_BY_LAZADA = "fulfilled_by_lazada"
    
    EBAY = "ebay"
    
    JD = "jd"
    
    AMAZON_PHARMACY = "amazon_pharmacy"
    
    AJIO_VMS = "ajio_vms"
    
    DARAZ = "daraz"
    
    OKER = "oker"
    
    FLIPKART_B2B = "flipkart_b2b"
    
    AMAZON_MLF_SS = "amazon_mlf_ss"
    
    WOOVLY = "woovly"
    
    TATA1MG = "tata1mg"
    
    ZOMATO = "zomato"
    
    SHOPIFY = "shopify"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid OrderingSource type")

