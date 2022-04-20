"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Validation import Validation

from .Validity import Validity

from .Identifier import Identifier

from .Restrictions import Restrictions

from .State import State



from .CouponAuthor import CouponAuthor

from .CouponSchedule import CouponSchedule



from .CouponAction import CouponAction

from .RuleDefinition import RuleDefinition

from .Ownership import Ownership

from .Rule import Rule

from .DisplayMeta import DisplayMeta

from .CouponDateMeta import CouponDateMeta




class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    validation = fields.Nested(Validation, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    code = fields.Str(required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    type_slug = fields.Str(required=False)
    

