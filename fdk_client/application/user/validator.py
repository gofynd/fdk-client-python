

"""User Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
    
        
    
    
        
    
    
    
    
    
    
        
    
    
    
    
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
    
    
        
    
    
        
    
    
        
    
    
        
        
        
        
        
        
    
    
    
        
    
    
        
    
    
        
        
        
        
        
    
    
    
        
    
    
        
    
    
    
    
        
    
    
    
        
    
    
        
    
    
        
    
    
        

class UserValidator:
    
    
    class loginWithFacebook(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class loginWithGoogle(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class loginWithGoogleAndroid(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class loginWithGoogleIOS(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class loginWithAppleIOS(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class loginWithOTP(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class loginWithEmailAndPassword(BaseSchema):
        
        pass 
        
    
    class sendResetPasswordEmail(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class sendResetPasswordMobile(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class sendResetToken(BaseSchema):
        
        pass 
        
    
    class forgotPassword(BaseSchema):
        
        pass 
        
    
    class resetForgotPassword(BaseSchema):
        
        pass 
        
    
    class loginWithToken(BaseSchema):
        
        pass 
        
    
    class registerWithForm(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class verifyEmail(BaseSchema):
        
        pass 
        
    
    class verifyMobile(BaseSchema):
        
        pass 
        
    
    class hasPassword(BaseSchema):
        
        pass 
        
    
    class updatePassword(BaseSchema):
        
        pass 
        
    
    class sendOTPOnMobile(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class sendForgotOTPOnMobile(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class verifyMobileOTP(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class verifyMobileForgotOTP(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class sendOTPOnEmail(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class sendForgotOTPOnEmail(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class verifyEmailOTP(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class verifyEmailForgotOTP(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class getLoggedInUser(BaseSchema):
        
        pass 
        
    
    class getListOfActiveSessions(BaseSchema):
        
        pass 
        
    
    class getPlatformConfig(BaseSchema):
        
        
        name = fields.Str(required=False)
         
        
    
    class updateProfile(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class addMobileNumber(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class deleteMobileNumber(BaseSchema):
        
        
        platform = fields.Str(required=False)
        
        active = fields.Boolean(required=False)
        
        primary = fields.Boolean(required=False)
        
        verified = fields.Boolean(required=False)
        
        country_code = fields.Str(required=False)
        
        phone = fields.Str(required=False)
         
        
    
    class setMobileNumberAsPrimary(BaseSchema):
        
        pass 
        
    
    class sendVerificationLinkToMobile(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class addEmail(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class deleteEmail(BaseSchema):
        
        
        platform = fields.Str(required=False)
        
        active = fields.Boolean(required=False)
        
        primary = fields.Boolean(required=False)
        
        verified = fields.Boolean(required=False)
        
        email = fields.Str(required=False)
         
        
    
    class setEmailAsPrimary(BaseSchema):
        
        pass 
        
    
    class sendVerificationLinkToEmail(BaseSchema):
        
        
        platform = fields.Str(required=False)
         
        
    
    class userExists(BaseSchema):
        
        
        q = fields.Str(required=False)
         
        
    
    class deleteUser(BaseSchema):
        
        pass 
        
    
    class logout(BaseSchema):
        
        pass 
        
    
    class getUserAttributes(BaseSchema):
        
        
        slug = fields.Str(required=False)
         
        
    
    class updateUserAttributes(BaseSchema):
        
        pass 
        
    
    class sendOTPOnPrimary(BaseSchema):
        
        
        entity = fields.Str(required=False)
         
        
    
    class verifyOTPonPrimary(BaseSchema):
        
        
        entity = fields.Str(required=False)
         
        
    
    class sendOTPForUpdate(BaseSchema):
        
        
        entity = fields.Str(required=False)
         
        
    
    class verifyOTPForUpdate(BaseSchema):
        
        
        entity = fields.Str(required=False)
         
        
    
    


