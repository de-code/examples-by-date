from datetime import date
import logging
from typing import Annotated

from pydantic import Field
import requests

from fastmcp import FastMCP


mcp = FastMCP(name='eLife Search MCP')


@mcp.tool(
    description=(
        "Searches the eLife journal for articles matching the query."
    )
)
def search_elife(
    query: Annotated[str, Field(
        description=(
            "The search query to find relevant articles (avoid terms like 'preprints')."
        )
    )],
    start_date: Annotated[date | None, Field(
        description=(
            "Optional start date for filtering articles (YYYY-MM-DD)."
        )
    )] = None,
    end_date: Annotated[date | None, Field(
        description=(
            "Optional end date for filtering articles (YYYY-MM-DD)."
        )
    )] = None
) -> str:
    params = {
        'for': query
    }
    if start_date:
        params['start-date'] = start_date.isoformat()
    if end_date:
        params['end-date'] = end_date.isoformat()
    response = requests.get(
        'https://api.elifesciences.org/search',
        params=params
    )
    response.raise_for_status()
    return response.json()


def main():
    mcp.run(
        transport='streamable-http',
        port=8000
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
