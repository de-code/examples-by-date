import logging
import os

import requests

from smolagents import (  # type: ignore[import-untyped]
    GradioUI,
    Model,
    OpenAIServerModel,
    tool,
    ToolCallingAgent
)


@tool
def search_elife(
    query: str,
    start_date: str | None = None,
    end_date: str | None = None
) -> str:
    """
    Searches the eLife journal for articles matching the query.

    Args:
        query (str): The search query to find relevant articles (avoid terms like "preprints").
        start_date (str): Optional start date for filtering articles (YYYY-MM-DD).
        end_date (str): Optional end date for filtering articles (YYYY-MM-DD).
    """

    params = {
        'for': query
    }
    if start_date:
        params['start-date'] = start_date
    if end_date:
        params['end-date'] = end_date
    response = requests.get(
        'https://api.elifesciences.org/search',
        params=params
    )
    response.raise_for_status()
    return response.json()


def get_model() -> Model:
    return OpenAIServerModel(
        model_id=os.getenv(
            'OPENAI_MODEL_ID',
            'gpt-4o-mini'
        ),
        api_base=os.getenv(
            'OPENAI_BASE_URL',
            'https://api.openai.com/v1'
        ),
        api_key=os.environ['OPENAI_API_KEY']
    )


def main():
    model = get_model()

    agent = ToolCallingAgent(
        tools=[search_elife],
        add_base_tools=False,
        model=model,
        max_steps=3
    )

    GradioUI(agent).launch(share=False)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
