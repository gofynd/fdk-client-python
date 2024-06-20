import ujson

async def create_curl(response, req_body=None):
    # Extract information from aiohttp response object
    method = response.request_info.method.upper()
    url = response.request_info.url
    headers = response.request_info.headers

    # Headers to exclude from the cURL command
    exclude_headers = [header.lower() for header in ['Content-Length', 'User-Agent', 'Accept', 'Host', 'Accept-Encoding']]

    # Construct cURL command
    curl_command = f"curl --request {method} '{url}'"

    # Add headers to cURL command
    for key, value in headers.items():
        if key.lower() not in exclude_headers:
            curl_command += f" --header '{key}: {value}'"

    # Determine content type
    content_type = headers.get('Content-Type', '')

    # Add data/body to cURL command based on content type
    if method != "GET" and req_body:
        if 'application/json' in content_type:
            curl_command += f" --data-raw '{ujson.dumps(req_body)}'"
        elif 'application/x-www-form-urlencoded' in content_type:
            form_data = '&'.join([f"{key}={value}" for key, value in req_body.items()])
            curl_command += f" --data '{form_data}'"
        else:
            # Fallback for any other types
            curl_command += f" --data-raw '{req_body}'"

    return curl_command