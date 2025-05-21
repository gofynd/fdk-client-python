"""Finance Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class CustomerCreditBalanceRequestSchema(BaseSchema):
    pass


class CustomerCreditBalanceReqData(BaseSchema):
    pass


class CustomerCreditBalanceResponseSchema(BaseSchema):
    pass


class CustomerCreditBalanceResData(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class ErrorMeta(BaseSchema):
    pass


class ErrorMetaItems(BaseSchema):
    pass


class LockUnlockRequestData(BaseSchema):
    pass


class LockUnlockRequestSchema(BaseSchema):
    pass


class LockUnlockResponseData(BaseSchema):
    pass


class LockUnlockResponseSchema(BaseSchema):
    pass





class CustomerCreditBalanceRequestSchema(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(CustomerCreditBalanceReqData, required=False)
    


class CustomerCreditBalanceReqData(BaseSchema):
    # Finance swagger.json

    
    seller_id = fields.Int(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    customer_mobile_number = fields.Str(required=False)
    
    customer_email = fields.Str(required=False)
    


class CustomerCreditBalanceResponseSchema(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(CustomerCreditBalanceResData, required=False)
    


class CustomerCreditBalanceResData(BaseSchema):
    # Finance swagger.json

    
    customer_mobile_number = fields.Str(required=False)
    
    customer_email = fields.Str(required=False)
    
    total_credited_balance = fields.Float(required=False)
    
    total_locked_amount = fields.Float(required=False)
    
    allowed_redemption_amount = fields.Float(required=False)
    


class Error(BaseSchema):
    # Finance swagger.json

    
    status = fields.Int(required=False)
    
    reason = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    code = fields.Str(required=False, allow_none=True)
    
    exception = fields.Str(required=False)
    
    info = fields.Str(required=False, allow_none=True)
    
    request_id = fields.Str(required=False, allow_none=True)
    
    stack_trace = fields.Str(required=False, allow_none=True)
    
    meta = fields.Nested(ErrorMeta, required=False)
    


class ErrorMeta(BaseSchema):
    # Finance swagger.json

    
    columns_errors = fields.List(fields.Nested(ErrorMetaItems, required=False), required=False)
    


class ErrorMetaItems(BaseSchema):
    # Finance swagger.json

    
    code = fields.Int(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    


class LockUnlockRequestData(BaseSchema):
    # Finance swagger.json

    
    seller_id = fields.Int(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    credit_note_number = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    request_type = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    


class LockUnlockRequestSchema(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(LockUnlockRequestData, required=False)
    


class LockUnlockResponseData(BaseSchema):
    # Finance swagger.json

    
    credit_note_number = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    


class LockUnlockResponseSchema(BaseSchema):
    # Finance swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(LockUnlockResponseData, required=False)
    


