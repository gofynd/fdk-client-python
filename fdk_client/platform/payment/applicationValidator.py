

"""Payment Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
        
    
    
        
        
    
    
        
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        

class PaymentValidator:
    
    
    class getBrandPaymentGatewayConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        aggregator = fields.Str(required=False)
        
        config_type = fields.Str(required=False)
         
        
    
    class saveBrandPaymentGatewayConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getPaymentModeRoutes(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
        
        request_type = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class getBankAccountDetailsOpenAPI(BaseSchema):
        
        
        order_id = fields.Str(required=False)
        
        request_hash = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class addRefundBankAccountUsingOTP(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getUserOrderBeneficiaries(BaseSchema):
        
        
        order_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getUserBeneficiaries(BaseSchema):
        
        
        order_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class confirmPayment(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getUserCODlimitRoutes(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        merchant_user_id = fields.Str(required=False)
        
        mobile_no = fields.Str(required=False)
         
        
    
    class setUserCODlimitRoutes(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class edcAggregatorsAndModelList(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class edcDeviceStats(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updateEdcDevice(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getEdcDevice(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        terminal_unique_identifier = fields.Str(required=False)
         
        
    
    class addEdcDevice(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        terminal_unique_identifier = fields.Str(required=False)
         
        
    
    class edcDeviceList(BaseSchema):
        
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        is_active = fields.Boolean(required=False)
        
        store_id = fields.Int(required=False)
        
        device_tag = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getPosPaymentModeRoutes(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        amount = fields.Int(required=False)
        
        cart_id = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
        
        order_id = fields.Str(required=False)
        
        card_reference = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
        
        user_details = fields.Str(required=False)
        
        display_split = fields.Boolean(required=False)
        
        advance_payment = fields.Boolean(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class initialisePayment(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class checkAndUpdatePaymentStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class resendOrCancelPayment(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class paymentStatusBulk(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class oauthGetUrl(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        aggregator = fields.Str(required=False)
        
        success_redirect_url = fields.Str(required=False)
        
        failure_redirect_url = fields.Str(required=False)
         
        
    
    class revokeOauthToken(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        aggregator = fields.Str(required=False)
         
        
    
    class repaymentDetails(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class merchantOnBoarding(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class verifyCustomerForPayment(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getPaymentLink(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        payment_link_id = fields.Str(required=False)
         
        
    
    class createPaymentLink(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class pollingPaymentLink(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        payment_link_id = fields.Str(required=False)
         
        
    
    class resendPaymentLink(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class cancelPaymentLink(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getPaymentModeControlRoutes(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        mode = fields.Str(required=False)
         
        
    
    class setMerchantModeControlRoutes(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        mode = fields.Str(required=False)
         
        
    
    class getPaymentModeCustomConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        mode = fields.Str(required=False)
         
        
    
    class setPaymentModeCustomConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        mode = fields.Str(required=False)
         
        
    
    class getPaymentCodeOption(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getPaymentSession(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        gid = fields.Str(required=False)
        
        line__item = fields.Boolean(required=False)
         
        
    
    class updatePaymentSession(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        gid = fields.Str(required=False)
         
        
    
    class updateRefundSession(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        gid = fields.Str(required=False)
        
        request_id = fields.Str(required=False)
         
        
    
    class getMerchantPaymentOption(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        payment_option_type = fields.Str(required=False)
         
        
    
    class patchMerchantPaymentOption(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getMerchantAggregatorPaymentModeDetails(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        aggregator_id = fields.Int(required=False)
        
        business_unit = fields.Str(required=False)
        
        device = fields.Str(required=False)
         
        
    
    class patchMerchantAggregatorPaymentModeDetails(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        aggregator_id = fields.Int(required=False)
         
        
    
    class getPGConfigAggregators(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getMerchantRefundPriority(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        config_type = fields.Str(required=False)
         
        
    
    class createMerchantRefundPriority(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        config_type = fields.Str(required=False)
         
        
    
    class updateMerchantRefundPriority(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        config_type = fields.Str(required=False)
         
        
    
    class createPaymentOrder(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getMerchantAggregatorAppVersion(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        aggregator_id = fields.Int(required=False)
        
        business_unit = fields.Str(required=False)
        
        device = fields.Str(required=False)
        
        payment_mode_id = fields.Int(required=False)
        
        sub_payment_mode = fields.Str(required=False)
         
        
    
    class patchMerchantPaymentOptionVersion(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        aggregator_id = fields.Int(required=False)
         
        
    
    class deleteBeneficiaryDetails(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        beneficiary_id = fields.Str(required=False)
         
        
    
    class getRefundOptions(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        configuration = fields.Str(required=False)
        
        product_type = fields.Str(required=False)
        
        amount = fields.Str(required=False)
         
        
    
    class setRefundOptionforShipment(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getSelectedRefundOption(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
         
        
    
    class getUserBeneficiariesDetailV2(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
        
        mop = fields.Str(required=False)
         
        
    
    class validateBeneficiaryAddress(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updateDefaultBeneficiary(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getPennyDropValidation(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updatePennyDropValidation(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    

