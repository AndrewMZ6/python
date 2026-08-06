from concurrent.futures import ThreadPoolExecutor, as_completed
import requests


urls: list[str] = [
    "https://example.com",
    "https://claude.ai/",
    "https://deepseek.com/",
    "https://opencode.ai/",
    "https://openai.com/",
    "http://open8493ai.com/",
]


def do_request(url: str) -> int:
    print(f"making a requests to {url}")
    response = requests.get(url)
    print(f"end requests for {url}")
    return response.status_code


with ThreadPoolExecutor(max_workers=len(urls)) as executor:
    future_to_url = {executor.submit(do_request, url): url for url in urls}

    for future in as_completed(future_to_url):
        url = future_to_url[future]
        try:
            status_code = future.result()
            print(f"{url} -> {status_code}")
        except requests.RequestException as e:
            print(f"Err => {url} raised an exception {e}")


print("end of the program")
