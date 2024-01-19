class _BaseException(Exception):
    code: str
    status_code: int 

    def __init__(self, desc: str) -> None:
        self.desc = desc
        super().__init__(desc)

class NotFoundError(_BaseException):
    code = 'NOT_FOUND'
    status_code = 404

class LimitError(_BaseException):
    code = 'LIMIT_ERROR'
    status_code = 400

class InsufficientFundsError(_BaseException):
    code = 'INSUFFISIENT_FUNDS'
    status_code = 400

class ValueIsLessThanMiminumError(_BaseException):
    code = 'VALUE_IS_LESS_THAN_MIMIMUM'
    status_code = 400

class ValueIsMoreThanMaximumError(_BaseException):
    code = 'VALUE_IS_MORE_THAN_MAXIMUM'
    status_code = 400

class ValueIsTooLongError(_BaseException):
    code = 'VALUE_IS_TOO_LONG'
    status_code = 400

class UserError(_BaseException):
    code = 'USER_ERROR'
    status_code = 400