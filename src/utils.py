from httpx import AsyncClient
from typing import Any, List
from mcp.types import TextContent
import sys

# App Modules:
# from constants import USER_AGENT


def _text(text: str) -> List[TextContent]:
    return [TextContent(type="text", text=text)]

async def make_request(client: AsyncClient, url: str) -> dict[str, Any] | None:
    """Make a request to the API with proper error handling."""
    try:
        response = await client.get(
            url,
            headers={"Accept": "application/json"},
            follow_redirects=True
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Debug: Error occurred: {type(e).__name__} - {str(e)}", file=sys.stderr)
        return None

