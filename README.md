# RMS MCP Server

An MCP (Model Context Protocol) server implementation for retrieving hotel inhouse reservation data. This server provides tools for fetching reservation information from hotel property management systems.

## Features

- Fetch inhouse reservations for specified hotels
- Date-based filtering of reservation data
- Standardized JSON response format

## Tools

### get-nepheli-inhouse

Retrieves inhouse reservations for a specified hotel and date.

**Parameters:**
- `hotel-name`: Name of the hotel
- `selected-date`: Date in YYYY-MM-DD format (valid range: 2019-2035)

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the MCP server:
```bash
python src/main.py
```

The server will start listening on stdin/stdout for MCP protocol messages.

## Development

This project uses the MCP SDK to implement a server that can be integrated with LLM systems. The server provides tools that can be discovered and called by MCP clients.

## License

MIT
