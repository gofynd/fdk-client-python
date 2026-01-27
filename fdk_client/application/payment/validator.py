

"""Payment Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
        
    
    
    
        
    
    
        
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
        
        
    
    
    
    
        
    
    
        
    
    
        
    
    
    
    
    
    
    
        
    
    
    
    
    
        
    
    
        
    
    
    
    
    
        
    
    
        
        
    
    
        
    
    
    
        
    
    
    
    
        
        
    
    
    
        
    
    
        
        
        
    

class PaymentValidator:
    
    
    class getAggregatorsConfig(BaseSchema):
        
        
        refresh = fields.Boolean(required=False)
         
        
    
    class attachCardToCustomer(BaseSchema):
        
        pass 
        
    
    class getActiveCardAggregator(BaseSchema):
        
        
        refresh = fields.Boolean(required=False)
         
        
    
    class getActiveUserCards(BaseSchema):
        
        
        force_refresh = fields.Boolean(required=False)
         
        
    
    class deleteUserCard(BaseSchema):
        
        pass 
        
    
    class verifyCustomerForPayment(BaseSchema):
        
        pass 
        
    
    class verifyAndChargePayment(BaseSchema):
        
        pass 
        
    
    class initialisePayment(BaseSchema):
        
        pass 
        
    
    class checkAndUpdatePaymentStatus(BaseSchema):
        
        pass 
        
    
    class getPaymentModeRoutes(BaseSchema):
        
        
        amount = fields.Int(required=False)
        
        cart_id = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
        
        order_id = fields.Str(required=False)
        
        card_reference = fields.Str(required=False)
        
        user_details = fields.Str(required=False)
        
        display_split = fields.Boolean(required=False)
        
        advance_payment = fields.Boolean(required=False)
        
        shipment_id = fields.Str(required=False)
        
        fulfillment_option = fields.List(fields.Str(required=False), required=False)
         
        
    
    class getPosPaymentModeRoutes(BaseSchema):
        
        
        amount = fields.Int(required=False)
        
        cart_id = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        refresh = fields.Boolean(required=False)
        
        card_reference = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
        
        user_details = fields.Str(required=False)
         
        
    
    class walletLinkInitiate(BaseSchema):
        
        pass 
        
    
    class linkWallet(BaseSchema):
        
        pass 
        
    
    class delinkWallet(BaseSchema):
        
        pass 
        
    
    class resendOrCancelPayment(BaseSchema):
        
        pass 
        
    
    class renderHTML(BaseSchema):
        
        pass 
        
    
    class validateVPA(BaseSchema):
        
        pass 
        
    
    class cardDetails(BaseSchema):
        
        
        card_info = fields.Str(required=False)
        
        aggregator = fields.Str(required=False)
         
        
    
    class getActiveRefundTransferModes(BaseSchema):
        
        pass 
        
    
    class enableOrDisableRefundTransferMode(BaseSchema):
        
        pass 
        
    
    class getUserBeneficiariesDetail(BaseSchema):
        
        
        order_id = fields.Str(required=False)
         
        
    
    class verifyIfscCode(BaseSchema):
        
        
        ifsc_code = fields.Str(required=False)
         
        
    
    class getOrderBeneficiariesDetail(BaseSchema):
        
        
        order_id = fields.Str(required=False)
         
        
    
    class verifyOtpAndAddBeneficiaryForBank(BaseSchema):
        
        pass 
        
    
    class addBeneficiaryDetails(BaseSchema):
        
        pass 
        
    
    class addRefundBankAccountUsingOTP(BaseSchema):
        
        pass 
        
    
    class verifyOtpAndAddBeneficiaryForWallet(BaseSchema):
        
        pass 
        
    
    class updateDefaultBeneficiary(BaseSchema):
        
        pass 
        
    
    class getPaymentLink(BaseSchema):
        
        
        payment_link_id = fields.Str(required=False)
         
        
    
    class createPaymentLink(BaseSchema):
        
        pass 
        
    
    class resendPaymentLink(BaseSchema):
        
        pass 
        
    
    class cancelPaymentLink(BaseSchema):
        
        pass 
        
    
    class getPaymentModeRoutesPaymentLink(BaseSchema):
        
        
        payment_link_id = fields.Str(required=False)
         
        
    
    class pollingPaymentLink(BaseSchema):
        
        
        payment_link_id = fields.Str(required=False)
         
        
    
    class createOrderHandlerPaymentLink(BaseSchema):
        
        pass 
        
    
    class initialisePaymentPaymentLink(BaseSchema):
        
        pass 
        
    
    class checkAndUpdatePaymentStatusPaymentLink(BaseSchema):
        
        pass 
        
    
    class customerCreditSummary(BaseSchema):
        
        
        aggregator = fields.Str(required=False)
         
        
    
    class redirectToAggregator(BaseSchema):
        
        
        source = fields.Str(required=False)
        
        aggregator = fields.Str(required=False)
         
        
    
    class checkCredit(BaseSchema):
        
        
        aggregator = fields.Str(required=False)
         
        
    
    class customerOnboard(BaseSchema):
        
        pass 
        
    
    class paidOrderDetails(BaseSchema):
        
        
        aggregator = fields.Str(required=False)
         
        
    
    class createPaymentOrder(BaseSchema):
        
        pass 
        
    
    class validateCustomerAndCreditSummary(BaseSchema):
        
        pass 
        
    
    class getRefundBeneficiaries(BaseSchema):
        
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class addBeneficiary(BaseSchema):
        
        pass 
        
    
    class deleteBeneficiary(BaseSchema):
        
        
        id = fields.Str(required=False)
         
        
    
    class getRefundBeneficiariesUsingOTPSession(BaseSchema):
        
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
        
        filter_by = fields.Str(required=False)
         
        
    
    class addRefundBeneficiaryUsingOTPSession(BaseSchema):
        
        pass 
        
    
    


