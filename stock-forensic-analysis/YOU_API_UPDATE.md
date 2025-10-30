# You.com API Integration Update

## Summary

Updated the You.com API integration to use the correct `/news` endpoint for news retrieval, following the official You.com API documentation.

## Changes Made

### 1. Configuration Updates (`config.py`)

Added the dedicated news endpoint configuration:

```python
YOU_API_NEWS_ENDPOINT = "/news"
```

### 2. Data Fetcher Updates (`src/data_fetcher.py`)

Updated the `YouComNewsDataFetcher.search_news()` method with the following changes:

#### Endpoint Change
- **Old**: `/search` endpoint
- **New**: `/news` endpoint (dedicated news endpoint)

#### Parameter Change
- **Old**: `num_web_results` parameter
- **New**: `count` parameter (as per You.com API documentation)

#### Response Handling
Updated to correctly parse the news endpoint response structure:

```json
{
  "news": {
    "results": [
      {
        "title": "Article title",
        "description": "Article description",
        "url": "https://...",
        "age": "6h",
        "source_name": "Source Name",
        "meta_url": {
          "hostname": "domain.com"
        }
      }
    ]
  }
}
```

Key response field mappings:
- `title` → Article title
- `description` → Article description/snippet
- `url` → Article URL
- `age` or `page_age` → Publication date/age
- `source_name` → News source name
- `meta_url.hostname` → Fallback source identifier

#### Error Handling Improvements

Added specific error messages for common API issues:
- **401 Unauthorized**: Invalid API key
- **403 Forbidden**: Access denied to news endpoint
- **Other errors**: Display HTTP status code and partial response

### 3. Backward Compatibility

Maintained fallback support for the old response format (`hits` structure) to ensure compatibility if the search endpoint is used instead of the news endpoint.

## Testing

A new test script has been created: `test_you_api.py`

Run the test with:

```bash
python test_you_api.py
```

The test script verifies:
1. API key configuration
2. General news search functionality
3. Stock-specific news search functionality
4. Response parsing and data extraction

## API Documentation Reference

- Official Documentation: https://documentation.you.com/api-reference/news
- News Endpoint: `https://api.ydc-index.io/news`
- Authentication: `X-API-Key` header
- Parameters:
  - `query` (required): Search query string
  - `count` (optional): Number of results to return

## Migration Notes

### No Breaking Changes
This update is backward compatible with existing code. The `YouComNewsDataFetcher` API remains the same:

```python
fetcher = YouComNewsDataFetcher(api_key)
news = fetcher.search_news("query", num_results=10)
stock_news = fetcher.get_stock_news("AAPL", "Apple Inc.", num_results=10)
```

### Benefits
- ✓ Uses the correct dedicated news endpoint
- ✓ Follows You.com API best practices
- ✓ More reliable news retrieval
- ✓ Better error handling and debugging
- ✓ Proper response structure parsing

## Configuration Required

Ensure your `.env` file contains a valid You.com API key:

```bash
YOU_API_KEY=your_api_key_here
```

Get your API key from: https://api.you.com/

## Troubleshooting

### Error: "Invalid You.com API key"
- Verify your API key is correct in the `.env` file
- Check that the API key has not expired
- Ensure there are no extra spaces or characters in the key

### Error: "Access forbidden"
- Verify your API key has access to the news endpoint
- Check your API plan includes news search capabilities
- Contact You.com support if issues persist

### No Results Returned
- Verify your internet connection
- Check if the query is too specific or restrictive
- Try with a broader search query
- Run `test_you_api.py` to verify API connectivity

## Additional Resources

- You.com API Quickstart: https://documentation.you.com/quickstart
- You.com API Reference: https://documentation.you.com/api-reference/search
- Get API Access: https://api.you.com/
