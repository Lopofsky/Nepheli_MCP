from httpx import AsyncClient
from typing import Any, List, Dict
from mcp.types import TextContent

# App Modules:
from constants import BASE_URL
from utils import _text, make_request

async def get_inhouse(hotel_name, selected_date) -> List[TextContent]:
    async with AsyncClient() as client:
        inhouse_reservations_url = f"{
            BASE_URL}/api?hotel_name={hotel_name}&selected_date={selected_date}"
        inhouse_response = await make_request(client, inhouse_reservations_url)

        if inhouse_response is None:
            return _text(f"(1) Failed to retrieve inhouse reservation data: {inhouse_response=}")

        response_status = inhouse_response.get('status')

        if response_status not in ('success', 'fail',):
            return _text(f"Unknown response status {response_status}")

        if response_status == 'fail':
            reason = inhouse_response['reason']
            return _text(f"Failed to retrieve inhouse reservation data: {reason}")

        data = inhouse_response['data']

        if data is None:
            return _text("No inhouse reservations!")

        # Format the reservations into a readable format
        inhouse_reservations = f"Inhouse reservations for {
            hotel_name}:\n\n" + "\n".join(format_inhouse(data))

        return _text(inhouse_reservations)


def format_inhouse(reservations: List[Dict[str, Any]]) -> List[str]:
    """Format reservation data into readable strings, agnostic of the data structure."""
    result: List[str] = []
    for reservation in reservations:
        fields = []
        for key, value in sorted(reservation.items()):
            field_name = key.replace('_', ' ').title()
            fields.append(f"{field_name}: {value}")
        formatted = '\n'.join(fields) + '\n---'
        result.append(formatted)
    return result
