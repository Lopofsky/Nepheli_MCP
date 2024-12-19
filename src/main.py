from typing import List, Optional, Sequence, Union
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.types import TextContent, Tool, ImageContent, EmbeddedResource
from mcp.server.stdio import stdio_server
from asyncio import run as async_run

# App Modules:
from app_utils import get_inhouse
from utils import _text
from constants import SERVER_NAME, SERVER_VERSION
import tools as tools_module

server = Server(SERVER_NAME)

@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """
    List available tools.
    Each tool specifies its arguments using JSON Schema validation.
    """
    # Get all module variables that are dicts and don't start with _
    tool_schemas = {
        name: value for name, value in vars(tools_module).items()
        if isinstance(value, dict) and not name.startswith('_')
    }
    
    # Create Tool instances using each schema dict as kwargs
    return [Tool(**schema) for schema in tool_schemas.values()]


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> Union[List[TextContent], List[ImageContent], List[EmbeddedResource]]:
    if not arguments:
        return _text("Missing arguments")

    if name == "get-nepheli-inhouse":
        hotel_name = arguments.get("hotel-name")
        selected_date = arguments.get("selected-date")

        if not hotel_name:
            return _text("Missing hotel name")
        if not selected_date:
            return _text("Missing selected date")
        
        return await get_inhouse(hotel_name, selected_date)

    return _text(f"Unknown service {name}")


async def main():
    # Run the server using stdin/stdout streams
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=SERVER_NAME,
                server_version=SERVER_VERSION,
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    async_run(main())