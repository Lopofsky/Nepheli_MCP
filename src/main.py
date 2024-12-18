from typing import List, Optional, Sequence
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
) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    """
    Handle tool execution requests.
    Tools can fetch hotel inhouse reservation data.
    """
    if not arguments:
        raise ValueError("Missing arguments")

    if name == "get-nepheli-inhouse":
        hotel_name: Optional[str] = arguments.get("hotel-name")
        selected_date: Optional[str] = arguments.get("selected-date")

        if not hotel_name:
            raise ValueError("Missing hotel name")
        if not selected_date:
            raise ValueError("Missing selected date")
        
        payload: List[TextContent] = await get_inhouse(hotel_name, selected_date)
        return payload

    return _text(f"Unknown service {name=}")

async def main():
    # await handle_call_tool(name="get-nepheli-inhouse", arguments={
    #     'hotel-name': 'castellum',
    #     'selected-date': '2022-05-16',
    # })
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
