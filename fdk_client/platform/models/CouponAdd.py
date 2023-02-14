"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Rule import Rule

from .Identifier import Identifier

from .RuleDefinition import RuleDefinition

from .Validation import Validation



from .CouponSchedule import CouponSchedule

from .State import State

from .CouponDateMeta import CouponDateMeta

from .CouponAction import CouponAction

from .CouponAuthor import CouponAuthor

from .Validity import Validity

from .Ownership import Ownership



from .DisplayMeta import DisplayMeta

from .Restrictions import Restrictions




class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    type_slug = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    state = fields.Nested(State, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    code = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    

