import SimpleHTTPServer
import SocketServer
import urlparse
import cgi
import json
import formatIO
import route

PORT = 8000
INPUT_START_FIELD = "start"
INPUT_DESTINATION_FIELD = "destinations"

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def end_headers(self):
			self.send_my_headers()
			SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

	def send_my_headers(self):
		self.send_header("Access-Control-Allow-Origin", "*")
		self.send_header("Access-Control-Allow-Methods",'GET,PUT,POST,DELETE,OPTIONS')

	def do_POST(self):
		content_len = int(self.headers.getheader('content-length', 0))
		post_body = self.rfile.read(content_len)
		post_data = json.loads(post_body)

		rawStart = post_data.get(INPUT_START_FIELD)
		rawDests = post_data.get(INPUT_DESTINATION_FIELD)
		start = (float(rawStart.get("lat")), float(rawStart.get("long")))
		destinations = [formatIO.Destination(dest.get("lat"), dest.get("long"), dest.get("id")) for dest in rawDests]

		order = route.route(start, destinations)
		out = [destination.id for destination in order]
		self.wfile.write(json.dumps(out))


httpd = SocketServer.TCPServer(("", PORT), ServerHandler)

print "serving at port", PORT
httpd.serve_forever()

