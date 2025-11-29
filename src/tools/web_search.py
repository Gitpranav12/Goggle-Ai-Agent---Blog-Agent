from typing import List, Dict
from tavily import TavilyClient


class WebSearchTool:
    """
    Wraps Tavily search for simple 'query -> list of results'.
    """

    def __init__(self, api_key: str):
        self.client = TavilyClient(api_key=api_key)

    def search(self, query: str, max_results: int = 4) -> List[Dict]:
        """
        Returns a list of {title, content, url} dicts.
        """
        response = self.client.search(
            query=query,
            max_results=max_results,
            include_answer=False,
        )

        results: List[Dict] = []
        for item in response.get("results", []):
            results.append(
                {
                    "title": item.get("title", ""),
                    "content": item.get("content", ""),
                    "url": item.get("url", ""),
                }
            )
        return results
