inhouse_schema = {
    "name": "get-nepheli-inhouse",
    "description": "Get inhouse reservations",
    "inputSchema": {
        "type": "object",
        "properties": {
            "hotel-name": {
                "type": "string",
                "description": "Hotel Name",
            },
            "selected-date": {
                "type": "date",
                "description": "Date to get inhouse guests [2035 > Year > 2019]. Format YYYY-MM-DD",
            }
        },
        "required": ["hotel-name", "selected-date"],
    }
}