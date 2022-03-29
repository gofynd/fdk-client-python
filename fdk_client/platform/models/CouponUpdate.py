"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Validation import Validation

from .CouponDateMeta import CouponDateMeta

from .Ownership import Ownership



from .Validity import Validity

from .State import State

from .CouponAuthor import CouponAuthor



from .RuleDefinition import RuleDefinition

from .DisplayMeta import DisplayMeta

from .Restrictions import Restrictions

from .Identifier import Identifier

from .Rule import Rule

from .CouponAction import CouponAction

from .CouponSchedule import CouponSchedule




class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    validation = fields.Nested(Validation, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    code = fields.Str(required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    state = fields.Nested(State, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    type_slug = fields.Str(required=False)
    

