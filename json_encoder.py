import json
import base64

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytearray):
            return base64.b64encode(obj).decode('utf-8')
        return super().default(obj)