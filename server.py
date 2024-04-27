import gi
import argparse

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GObject, GLib

class StreamFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self, stream_uri, rtsp_stream_uri, **properties):
        super(StreamFactory, self).__init__(**properties)
        self.rtsp_stream_uri = rtsp_stream_uri
        self.stream_uri = stream_uri

    def do_create_element(self, url):
        # Use uridecodebin to receive the RTSP stream
        return Gst.parse_launch(f'uridecodebin uri={self.rtsp_stream_uri} ! videoconvert ! video/x-raw,format=I420 ! x264enc tune=zerolatency ! rtph264pay name=pay0 pt=96')

def create_rtsp_server(stream_uri, rtsp_stream_uri, port):
    GObject.threads_init()
    Gst.init(None)

    server = GstRtspServer.RTSPServer()

    factory = StreamFactory(
        stream_uri=stream_uri,
        rtsp_stream_uri=rtsp_stream_uri
    )
    factory.set_shared(True)
    server.get_mount_points().add_factory(stream_uri, factory)

    server.set_service(str(port))
    server.attach(None)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--rtsp_stream_uri", required=True, help="RTSP stream URI")
    parser.add_argument("--port", default=8554, help="port to stream images", type=int)
    parser.add_argument("--stream_uri", required=True, help="Stream URI")
    opt = parser.parse_args()

    create_rtsp_server(opt.stream_uri, opt.rtsp_stream_uri, opt.port)

    # Run the main loop
    loop = GLib.MainLoop()
    try:
        loop.run()
    except KeyboardInterrupt:
        pass