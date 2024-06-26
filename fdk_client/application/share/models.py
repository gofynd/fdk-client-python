"""Share Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class QRCodeResp(BaseSchema):
    pass


class RedirectDevice(BaseSchema):
    pass


class WebRedirect(BaseSchema):
    pass


class Redirects(BaseSchema):
    pass


class CampaignShortLink(BaseSchema):
    pass


class Attribution(BaseSchema):
    pass


class SocialMediaTags(BaseSchema):
    pass


class ShortLinkReq(BaseSchema):
    pass


class UrlInfo(BaseSchema):
    pass


class ShortLinkRes(BaseSchema):
    pass


class ErrorRes(BaseSchema):
    pass





class QRCodeResp(BaseSchema):
    # Share swagger.json

    
    link = fields.Str(required=False)
    
    svg = fields.Str(required=False)
    


class RedirectDevice(BaseSchema):
    # Share swagger.json

    
    link = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class WebRedirect(BaseSchema):
    # Share swagger.json

    
    link = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class Redirects(BaseSchema):
    # Share swagger.json

    
    ios = fields.Nested(RedirectDevice, required=False)
    
    android = fields.Nested(RedirectDevice, required=False)
    
    web = fields.Nested(WebRedirect, required=False)
    
    force_web = fields.Boolean(required=False)
    


class CampaignShortLink(BaseSchema):
    # Share swagger.json

    
    source = fields.Str(required=False)
    
    medium = fields.Str(required=False)
    


class Attribution(BaseSchema):
    # Share swagger.json

    
    campaign_cookie_expiry = fields.Str(required=False)
    


class SocialMediaTags(BaseSchema):
    # Share swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    image = fields.Str(required=False)
    


class ShortLinkReq(BaseSchema):
    # Share swagger.json

    
    title = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    hash = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    expire_at = fields.Str(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    personalized = fields.Boolean(required=False)
    
    campaign = fields.Nested(CampaignShortLink, required=False)
    
    redirects = fields.Nested(Redirects, required=False)
    
    attribution = fields.Nested(Attribution, required=False)
    
    social_media_tags = fields.Nested(SocialMediaTags, required=False)
    
    count = fields.Int(required=False)
    


class UrlInfo(BaseSchema):
    # Share swagger.json

    
    original = fields.Str(required=False)
    
    hash = fields.Str(required=False)
    
    short_url = fields.Str(required=False)
    


class ShortLinkRes(BaseSchema):
    # Share swagger.json

    
    title = fields.Str(required=False)
    
    url = fields.Nested(UrlInfo, required=False)
    
    created_by = fields.Str(required=False)
    
    app_redirect = fields.Boolean(required=False)
    
    fallback = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    expire_at = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    updated_at = fields.Str(required=False)
    
    personalized = fields.Boolean(required=False)
    
    campaign = fields.Nested(CampaignShortLink, required=False)
    
    redirects = fields.Nested(Redirects, required=False)
    
    attribution = fields.Nested(Attribution, required=False)
    
    social_media_tags = fields.Nested(SocialMediaTags, required=False)
    
    count = fields.Int(required=False)
    


class ErrorRes(BaseSchema):
    # Share swagger.json

    
    message = fields.Str(required=False)
    


