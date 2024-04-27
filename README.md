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

2. **Install GStreamer**: Ensure that GStreamer is installed on your system. Depending on your operating system, you can install GStreamer using the following commands:

   - For Ubuntu/Debian:

     ```bash
     sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
     ```

3. Run the script:

    ```bash
    python rtsp_server.py --rtsp_stream_uri [RTSP_STREAM_URI] --port [PORT] --stream_uri [STREAM_URI]
    ```

    Replace `[RTSP_STREAM_URI]` with the URI of the RTSP stream you want to serve, `[PORT]` with the desired port number for streaming images, and `[STREAM_URI]` with the URI of the stream.

4. Connect to the RTSP stream using a compatible client.

## Script Explanation

The script creates an RTSP server using GStreamer. It defines a custom `StreamFactory` class that extends `GstRtspServer.RTSPMediaFactory` to handle stream creation. The `StreamFactory` class creates a GStreamer pipeline to receive the RTSP stream, encode it, and then serve it via RTSP. The script also includes a `create_rtsp_server` function to set up the server with the specified parameters.
