# # from fastapi import FastAPI
# # import yt_dlp
# # import requests
# # from fastapi.responses import StreamingResponse
# # app = FastAPI()

# # # Function to extract the video URL using yt-dlp
# # def get_youtube_url(video_id):
# #     ydl_opts = {
# #         'format': 'best',
# #         'quiet': True,  # Suppress output
# #     }
# #     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #         info_dict = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
# #         video_url = info_dict.get("url", None)
# #     return video_url

# # # Streaming generator function to pipe video content
# # def stream_video(url):
# #     response = requests.get(url, stream=True)
# #     for chunk in response.iter_content(chunk_size=1024):
# #         if chunk:
# #             yield chunk

# # # FastAPI route to stream the video
# # @app.get("/stream/{video_id}")
# # async def stream(video_id: str):
# #     video_url = get_youtube_url(video_id)
# #     if video_url:
# #         return StreamingResponse(stream_video(video_url), media_type="video/mp4")
# #     return {"error": "Video not found"}

# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run(app, host="0.0.0.0", port=8000)

# ##################################################################################################


# from fastapi import FastAPI
# from fastapi.responses import StreamingResponse
# import yt_dlp
# import requests
# import random

# app = FastAPI()

# # List of proxies to rotate
# proxies_list = [
#     "20.111.54.16:8123",
#     "157.254.53.50:80",
#     "41.196.0.163:8081",
#     "43.200.77.128:3128",
#     "47.178.24.220:80",
#     "103.237.144.232:1311",
#     "143.42.66.91:80",
#     "160.86.242.23:8080",
#     "198.49.68.80:80",
#     "41.169.69.91:3128",
#     "87.98.148.98:80",
#     "47.251.43.115:33333",
#     "178.128.113.118:23128",
#     "162.223.90.130:80",
#     "187.94.100.254:8080",
#     "51.210.54.186:80",
#     "23.247.136.245:80",
#     "87.248.129.26:80",
#     "47.237.2.245:1311",
#     "114.129.2.82:8081",
#     "190.103.177.131:80",
#     "51.89.255.67:80",
#     "20.206.106.192:8123",
#     "20.210.113.32:8123",
#     "47.237.107.41:9080",
#     "47.237.92.86:86",
#     "47.91.120.190:1025",
#     "154.236.177.105:1976",
#     "165.232.129.150:80",
#     "192.73.244.36:80",
#     "82.102.10.253:80",
#     "47.88.31.196:8080",
#     "8.219.97.248:80",
#     "23.88.51.178:8888",
#     "103.190.179.27:80",
#     "162.55.61.160:9001",
#     "86.104.75.109:1080"
# ]

# # Function to extract the video URL using yt-dlp
# def get_youtube_url(video_id):
#     ydl_opts = {
#         'format': 'best',
#         'quiet': True,  # Suppress output
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info_dict = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
#         video_url = info_dict.get("url", None)
#     return video_url

# # Streaming generator function to pipe video content with proxy support
# def stream_video(url):
#     # Select a random proxy from the list
#     proxy = random.choice(proxies_list)
#     proxies = {
#         "http": f"http://{proxy}"
#     }

#     # Print the selected proxy to the console
#     print(f"Using proxy: {proxy}")

#     response = requests.get(url, stream=True, proxies=proxies)
#     for chunk in response.iter_content(chunk_size=1024):
#         if chunk:
#             yield chunk

# # FastAPI route to stream the video
# @app.get("/stream/{video_id}")
# async def stream(video_id: str):
#     video_url = get_youtube_url(video_id)
#     if video_url:
#         return StreamingResponse(stream_video(video_url), media_type="video/mp4")
#     return {"error": "Video not found"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


#################################################################################################

# from fastapi import FastAPI
# from fastapi.responses import StreamingResponse
# import yt_dlp
# import requests
# import random

# app = FastAPI()

# # Tor proxy settings
# TOR_PROXY = {
#     'http': 'socks5h://127.0.0.1:9050'
# }

# # Function to extract the video URL using yt-dlp
# def get_youtube_url(video_id):
#     ydl_opts = {
#         'format': 'best',
#         'quiet': True,  # Suppress output
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info_dict = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
#         video_url = info_dict.get("url", None)
#     return video_url

# # Streaming generator function to pipe video content with Tor proxy support
# def stream_video(url):
#     # Print the Tor proxy being used
#     print(f"Using Tor proxy: {TOR_PROXY}")

#     # Use the Tor proxy to route requests through Tor
#     response = requests.get(url, stream=True, proxies=TOR_PROXY)
#     for chunk in response.iter_content(chunk_size=1024):
#         if chunk:
#             yield chunk

# # FastAPI route to stream the video
# @app.get("/stream/{video_id}")
# async def stream(video_id: str):
#     video_url = get_youtube_url(video_id)
#     if video_url:
#         return StreamingResponse(stream_video(video_url), media_type="video/mp4")
#     return {"error": "Video not found"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

#############################################################################################

# from fastapi import FastAPI, Header, Response, HTTPException
# from fastapi.responses import StreamingResponse
# import yt_dlp
# import requests

# app = FastAPI()

# TOR_PROXY = {
#     'http': 'socks5h://127.0.0.1:9050'
# }

# def get_youtube_url(video_id):
#     ydl_opts = {
#         'format': 'best',
#         'quiet': True,  # Suppress output
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info_dict = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
#         video_url = info_dict.get("url", None)
#         return video_url

# def stream_video(url, start_byte=None):
#     headers = {}
#     if start_byte:
#         headers['Range'] = f'bytes={start_byte}-'

#     response = requests.get(url, stream=True, proxies=TOR_PROXY, headers=headers)
    
#     if response.status_code == 200 or response.status_code == 206:
#         content_length = response.headers.get('Content-Length')
#         content_range = response.headers.get('Content-Range')

#         return response.iter_content(chunk_size=1024), content_length, content_range
#     else:
#         raise HTTPException(status_code=404, detail="Unable to stream the video with range request")

# @app.get("/stream/{video_id}")
# async def stream(video_id: str, range: str = Header(None)):
#     video_url = get_youtube_url(video_id)
#     if not video_url:
#         return {"error": "Video not found"}

#     start_byte = 0
#     if range:
#         start_byte = int(range.replace("bytes=", "").split("-")[0])

#     video_stream, content_length, content_range = stream_video(video_url, start_byte)

#     headers = {
#         "Content-Type": "video/mp4",
#         "Accept-Ranges": "bytes",
#         "Content-Length": str(content_length),
#         "Content-Range": content_range if content_range else f"bytes {start_byte}-{content_length}/{content_length}",
#     }

#     return StreamingResponse(video_stream, headers=headers)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


#############################################################################################

# from fastapi import FastAPI, Header, Response, HTTPException
# from fastapi.responses import StreamingResponse
# import yt_dlp
# import requests

# app = FastAPI()

# # Tor proxy settings
# TOR_PROXY = {
#     'http': 'socks5h://127.0.0.1:9050'
# }

# # Function to extract the video URL using yt-dlp
# def get_youtube_url(video_id):
#     ydl_opts = {
#         'format': 'best',
#         'quiet': True,  # Suppress output
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info_dict = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
#         video_url = info_dict.get("url", None)
#         return video_url

# # Streaming generator function to pipe video content with range support
# def stream_video(url, start_byte=None):
#     headers = {}
#     if start_byte is not None:
#         headers['Range'] = f'bytes={start_byte}-'

#     response = requests.get(url, stream=True, proxies=TOR_PROXY, headers=headers)
    
#     # Check if the response supports range requests (206 Partial Content)
#     if response.status_code == 200 or response.status_code == 206:
#         content_length = response.headers.get('Content-Length')
#         content_range = response.headers.get('Content-Range')
        
#         # Stream the video content chunk by chunk (1KB at a time)
#         return response.iter_content(chunk_size=1024), content_length, content_range
#     else:
#         raise HTTPException(status_code=404, detail="Unable to stream the video with range request")

# # FastAPI route to stream the video with support for range requests
# @app.get("/stream/{video_id}")
# async def stream(video_id: str, range: str = Header(None)):
#     video_url = get_youtube_url(video_id)
#     if not video_url:
#         return {"error": "Video not found"}

#     # Extract the starting byte from the range header, if present
#     start_byte = 0
#     if range:
#         start_byte = int(range.replace("bytes=", "").split("-")[0])

#     # Get the video stream, content length, and range
#     video_stream, content_length, content_range = stream_video(video_url, start_byte)

#     # If no content range is returned from the upstream server, calculate it
#     if content_range is None:
#         end_byte = int(content_length) - 1
#         content_range = f"bytes {start_byte}-{end_byte}/{content_length}"

#     # Prepare the headers for the response
#     headers = {
#         "Content-Type": "video/mp4",
#         "Accept-Ranges": "bytes",
#         "Content-Length": str(content_length),
#         "Content-Range": content_range,
#     }

#     # Return the streaming response with appropriate headers
#     return StreamingResponse(video_stream, headers=headers, status_code=206 if start_byte > 0 else 200)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

#############################################################################################

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import StreamingResponse
import yt_dlp
import requests
import random

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to restrict origins as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# List of proxies to rotate
proxies_list = [
    "20.111.54.16:8123",
    "157.254.53.50:80",
    "41.196.0.163:8081",
    "43.200.77.128:3128",
    "47.178.24.220:80",
    "103.237.144.232:1311",
    "143.42.66.91:80",
    "160.86.242.23:8080",
    "198.49.68.80:80",
    "41.169.69.91:3128",
    "87.98.148.98:80",
    "47.251.43.115:33333",
    "178.128.113.118:23128",
    "162.223.90.130:80",
    "187.94.100.254:8080",
    "51.210.54.186:80",
    "23.247.136.245:80",
    "87.248.129.26:80",
    "47.237.2.245:1311",
    "114.129.2.82:8081",
    "190.103.177.131:80",
    "51.89.255.67:80",
    "20.206.106.192:8123",
    "20.210.113.32:8123",
    "47.237.107.41:9080",
    "47.237.92.86:86",
    "47.91.120.190:1025",
    "154.236.177.105:1976",
    "165.232.129.150:80",
    "192.73.244.36:80",
    "82.102.10.253:80",
    "47.88.31.196:8080",
    "8.219.97.248:80",
    "23.88.51.178:8888",
    "103.190.179.27:80",
    "162.55.61.160:9001",
    "86.104.75.109:1080"
]


# Function to extract the video URL using yt-dlp
def get_youtube_url(video_id):
    ydl_opts = {
        'format': 'best',
        'quiet': True,  # Suppress output
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
        video_url = info_dict.get("url", None)
    return video_url

# Streaming generator function to pipe video content with proxy and range support
def stream_video(url, start_byte=None):
    # Select a random proxy from the list
    proxy = random.choice(proxies_list)
    proxies = {
        "http": f"http://{proxy}"
    }

    # Print the selected proxy to the console
    print(f"Using proxy: {proxy}")

    headers = {}
    if start_byte:
        headers['Range'] = f'bytes={start_byte}-'

    response = requests.get(url, stream=True, proxies=proxies, headers=headers)

    # Check if the response is valid (200 OK or 206 Partial Content)
    if response.status_code == 200 or response.status_code == 206:
        content_length = response.headers.get('Content-Length')
        content_range = response.headers.get('Content-Range')
        return response.iter_content(chunk_size=1024), content_length, content_range
    else:
        raise HTTPException(status_code=404, detail="Unable to stream the video")

# FastAPI route to stream the video with range request support
@app.get("/stream/{video_id}")
async def stream(video_id: str, range: str = Header(None)):
    video_url = get_youtube_url(video_id)
    if not video_url:
        return {"error": "Video not found"}

    # Extract the starting byte from the range header, if present
    start_byte = 0
    if range:
        start_byte = int(range.replace("bytes=", "").split("-")[0])

    # Stream the video from the start byte
    video_stream, content_length, content_range = stream_video(video_url, start_byte)

    # Calculate content range if it's not returned by the upstream server
    if content_range is None:
        end_byte = int(content_length) - 1
        content_range = f"bytes {start_byte}-{end_byte}/{content_length}"

    # Set the headers for the response
    headers = {
        "Content-Type": "video/mp4",
        "Accept-Ranges": "bytes",
        "Content-Length": str(content_length),
        "Content-Range": content_range,
    }

    # Return the StreamingResponse with range support
    return StreamingResponse(video_stream, headers=headers, status_code=206 if start_byte > 0 else 200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
