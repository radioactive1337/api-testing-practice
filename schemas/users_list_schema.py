schema = {
    "type": "object",
    "properties": {
        "meta": {
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer"
                },
                "offset": {
                    "type": "integer"
                },
                "total": {
                    "type": "integer"
                }
            },
            "required": ["limit", "offset", "total"]
        },
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "first_name": {
                        "type": ["string", "null"]
                    },
                    "last_name": {
                        "type": "string"
                    },
                    "company_id": {
                        "type": ["integer", "null"]
                    },
                    "user_id": {
                        "type": "integer"
                    }
                },
                "required": ["last_name", "user_id"]
            }
        }
    },
    "required": ["meta", "data"]
}
