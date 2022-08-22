"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Rule import Rule

from .RuleDefinition import RuleDefinition



from .State import State

from .CouponDateMeta import CouponDateMeta

from .Identifier import Identifier

from .CouponAuthor import CouponAuthor

from .Ownership import Ownership

from .CouponAction import CouponAction

from .DisplayMeta import DisplayMeta

from .Restrictions import Restrictions

from .CouponSchedule import CouponSchedule

from .Validation import Validation



from .Validity import Validity


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    type_slug = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    code = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    validity = fields.Nested(Validity, required=False)
    

