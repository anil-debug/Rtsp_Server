# RTSP Server with GStreamer in Python

This script sets up an RTSP server using GStreamer in Python. It takes an RTSP stream URI and a local port as inputs, then creates a server to stream the content.

## Prerequisites

- Python 3.x
- GStreamer
- GObject
- GLib

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/your/repository.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:

    ```bash
    python rtsp_server.py --rtsp_stream_uri [RTSP_STREAM_URI] --port [PORT] --stream_uri [STREAM_URI]
    ```

    Replace `[RTSP_STREAM_URI]` with the URI of the RTSP stream you want to serve, `[PORT]` with the desired port number for streaming images, and `[STREAM_URI]` with the URI of the stream.

4. Connect to the RTSP stream using a compatible client.

## Script Explanation

The script creates an RTSP server using GStreamer. It defines a custom `StreamFactory` class that extends `GstRtspServer.RTSPMediaFactory` to handle stream creation. The `StreamFactory` class creates a GStreamer pipeline to receive the RTSP stream, encode it, and then serve it via RTSP. The script also includes a `create_rtsp_server` function to set up the server with the specified parameters.

