# Video Extraction Engine

This script extracts videos from web pages using BeautifulSoup and yt-dlp. It supports:

- HTML5 video tags
- Iframes
- JavaScript video URLs
- M3U8 streams

## Requirements
- `BeautifulSoup4`
- `yt-dlp`

## Usage
1. Install the required packages:
   ```bash
   pip install beautifulsoup4 yt-dlp
   ```
2. Use the script to extract videos from a provided URL.

## Example Code
```python
import requests
from bs4 import BeautifulSoup
import yt_dlp

def extract_video(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    video_urls = []

    # Extract video tags
    for video in soup.find_all('video'):
        video_urls.append(video['src'])

    # Extract iframe sources
    for iframe in soup.find_all('iframe'):
        iframe_src = iframe['src']
        if iframe_src:
            video_urls.append(iframe_src)

    # ... (Handle JavaScript video URLs and M3U8 streams)

    return video_urls

# Example usage
url = 'https://example.com'
videos = extract_video(url)
for video in videos:
    print(video)
```