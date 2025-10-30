"""
Test script for You.com API integration
This script tests the updated You.com API implementation
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(__file__))

from src.data_fetcher import YouComNewsDataFetcher
from config import Config

def test_you_api():
    """Test the You.com API integration"""

    print("=" * 70)
    print("Testing You.com API Integration")
    print("=" * 70)
    print()

    # Check if API key is configured
    api_key = Config.YOU_API_KEY
    if not api_key:
        print("❌ ERROR: YOU_API_KEY not configured")
        print("Please set YOUR_API_KEY in .env file or environment variables")
        return False

    print(f"✓ API Key configured: {api_key[:10]}...")
    print(f"✓ Base URL: {Config.YOU_API_BASE_URL}")
    print(f"✓ News Endpoint: {Config.YOU_API_NEWS_ENDPOINT}")
    print()

    # Initialize the news fetcher
    fetcher = YouComNewsDataFetcher(api_key)

    # Test 1: Search for general news
    print("-" * 70)
    print("TEST 1: Searching for general tech news")
    print("-" * 70)

    try:
        results = fetcher.search_news("technology news", num_results=3)

        if results:
            print(f"✓ Successfully retrieved {len(results)} news articles")
            print()

            for i, article in enumerate(results, 1):
                print(f"Article {i}:")
                print(f"  Title: {article.get('title', 'N/A')[:80]}...")
                print(f"  Source: {article.get('source', 'N/A')}")
                print(f"  Date: {article.get('published_date', 'N/A')}")
                print(f"  URL: {article.get('url', 'N/A')[:60]}...")
                print()
        else:
            print("❌ No results returned")
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

    # Test 2: Search for stock-specific news
    print("-" * 70)
    print("TEST 2: Searching for stock news (AAPL)")
    print("-" * 70)

    try:
        results = fetcher.get_stock_news("AAPL", "Apple Inc.", num_results=3)

        if results:
            print(f"✓ Successfully retrieved {len(results)} stock news articles")
            print()

            for i, article in enumerate(results, 1):
                print(f"Article {i}:")
                print(f"  Title: {article.get('title', 'N/A')[:80]}...")
                print(f"  Source: {article.get('source', 'N/A')}")
                print(f"  Date: {article.get('published_date', 'N/A')}")
                print()
        else:
            print("⚠ No stock-specific results returned")

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

    print("=" * 70)
    print("✓ All tests completed successfully!")
    print("=" * 70)

    return True

if __name__ == "__main__":
    success = test_you_api()
    sys.exit(0 if success else 1)
