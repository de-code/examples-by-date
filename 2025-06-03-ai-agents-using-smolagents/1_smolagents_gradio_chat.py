import logging
import os

from smolagents import (  # type: ignore[import-untyped]
    DuckDuckGoSearchTool,
    GradioUI,
    Model,
    OpenAIServerModel,
    ToolCallingAgent
)


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
        tools=[DuckDuckGoSearchTool()],
        add_base_tools=False,
        model=model,
        max_steps=3
    )

    GradioUI(agent).launch(share=False)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
