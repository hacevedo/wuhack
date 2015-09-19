import SimpleHTTPServer
import SocketServer
import urlparse
import cgi

PORT = 8000

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_POST(self):
		# Extract and print the contents of the POST
		length = int(self.headers['Content-Length'])
		post_data = urlparse.parse_qs(self.rfile.read(length).decode('utf-8'))
		for key, value in post_data.iteritems():
			print "%s=%s" % (key, value)

		self.wfile.write('{"data":1}')
		form = cgi.FieldStorage()
		print form

httpd = SocketServer.TCPServer(("", PORT), ServerHandler)

print "serving at port", PORT
httpd.serve_forever()

