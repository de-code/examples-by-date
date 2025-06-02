# 2025-06-02 AI Agents using Smolagents

## Prerequisites

- [make](https://en.wikipedia.org/wiki/Make_(software))
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Environment Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| OPENAI_BASE_URL | The base URL for the OpenAI compatible API | `https://api.openai.com/v1` |
| OPENAI_API_KEY | The API key for the above API | |
| OPENAI_MODEL_ID | The model to use | gpt-4o-mini |

## Create Virtual Environment and Install Dependencies

```bash
make dev-venv
```

## Sync Dependencies to Virtual Environment

```bash
make dev-install
```

## Examples

### 1 Smolagents Gradio Chat

```bash
uv run 1_smolagents_gradio_chat.py
```

URL: `http://127.0.0.1:7860`

This uses:

- `smolagents` as the AI Agents framework
- smolagents' `ToolCallingAgent` for simple tool execution (as opposted to `CodeAgent`)
- `Gradio` for a chat interface
- `DuckDuckGoSearchTool` for web search

| Example questions | Comment |
| ----------------- | ------- |
| What are five accepted definitions of AI Agent? | Should search the web and bring back a reasonable response |
| What life science Neuroscience preprints were posted in May 2025? | Will do a web search for `Neuroscience preprints May 2025` and bring back reasonable results |
| What Neuroscience preprints were evaluated by eLife in May 2025? | Will do a web search for `Neuroscience eLife reviewed preprints May 2024` and bring back reasonable responses. |
| What five Neuroscience preprints were evaluated by eLife in January 2024? | Will do a web search for `Neuroscience eLife reviewed preprints January 2024`. It sort of works but retrieves results where one of the versions was matched with January 2024. It is struggling to find five examples. |
| What five articles on covid were evaluated by eLife in January 2024? | May do a web search for `Protection afforded by post-infection SARS-CoV-2 vaccine doses eLife January 2024`.That limits the search. Results may also not actually be evaluated in January 2024. |

### 2 eLife Search Tool

```bash
uv run 1_elife_search.py
```

URL: `http://127.0.0.1:7860`

Same as previous example but uses eLife Search API instead of web search.

| Example questions | Comment |
| ----------------- | ------- |
| What five articles on covid were evaluated by eLife in January 2024? | It should use the `search_elife` tool with the parameters `{'query': 'covid', 'start_date': '2024-01-01', 'end_date': '2024-01-31'}`. It responds with the papers from the search results. |

### 3 eLife Search as MCP Tool

#### 3a eLife Search MCP Server

```bash
uv run 3a_elife_search_mcp_server.py
```

MCP URL: `http://127.0.0.1:8000/mcp`

You can inspect it using the [inspector](https://github.com/modelcontextprotocol/inspector):

```bash
npx @modelcontextprotocol/inspector
```

Then open: `http://localhost:6274/?transport=streamable-http&serverUrl=http://127.0.0.1:8000/mcp`

#### 3b Agent using MCP Server

```bash
uv run 3b_agent_using_elife_search_mcp_server.py
```

URL: `http://127.0.0.1:7860`

Same as previous example but now uses eLife Search via MCP Server.

| Example questions | Comment |
| ----------------- | ------- |
| What five articles on covid were evaluated by eLife in January 2024? | It should use the `search_elife` tool with the parameters `{'query': 'covid', 'start_date': '2024-01-01', 'end_date': '2024-01-31'}`. It responds with the papers from the search results. |
