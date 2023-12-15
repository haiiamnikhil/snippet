class Response:
    code: int = 200
    status: bool = True
    success: bool = True
    message: str = ''
    result: list = []
    error: str = ''

    @classmethod
    def to_dict(cls):
        values = {}
        values.update({
            'code': cls.code,
            'status': cls.status,
            'success': cls.success,
            'message': cls.message,
            'result': cls.result,
            'error': cls.error
        })
        return values
