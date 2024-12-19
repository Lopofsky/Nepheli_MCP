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
                "type": "string",  # Changed from "date" to "string"
                "description": "Date to get inhouse guests [2035 > Year > 2019]. Format YYYY-MM-DD",
                "pattern": "^\\d{4}-\\d{2}-\\d{2}$"  # Added pattern to validate date format
            }
        },
        "required": ["hotel-name", "selected-date"],
    }
}