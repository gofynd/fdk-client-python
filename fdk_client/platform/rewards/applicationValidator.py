

"""Rewards Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        

class RewardsValidator:
    
    
    class showGiveaways(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class saveGiveAway(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getGiveawayById(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateGiveAway(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getGiveawayAudienceStatus(BaseSchema):
        
        
        audience_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class showOffers(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getOfferByName(BaseSchema):
        
        
        name = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        cookie = fields.Str(required=False)
         
        
    
    class updateOfferByName(BaseSchema):
        
        
        name = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updateUserStatus(BaseSchema):
        
        
        user_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class user(BaseSchema):
        
        
        user_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getPointsHistory(BaseSchema):
        
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        user_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    
