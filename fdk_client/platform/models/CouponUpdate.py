"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponDateMeta import CouponDateMeta

from .CouponSchedule import CouponSchedule

from .RuleDefinition import RuleDefinition

from .Ownership import Ownership

from .State import State

from .Identifier import Identifier



from .Validity import Validity



from .Rule import Rule

from .CouponAuthor import CouponAuthor

from .Validation import Validation

from .Restrictions import Restrictions

from .DisplayMeta import DisplayMeta

from .CouponAction import CouponAction




class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    state = fields.Nested(State, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    type_slug = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    code = fields.Str(required=False)
    

