import http.server
import socketserver
import os

# Укажите порт, на котором будет работать сервер
PORT = 8000

class FileListingHandler(http.server.SimpleHTTPRequestHandler):
    def list_directory(self, path):
        """Переопределяем метод для кастомного отображения списка файлов."""
        try:
            file_list = os.listdir(path)
            file_list.sort()
            response = f"<html><head><title>Directory listing</title></head><body>"
            response += f"<h1>Directory listing for {os.path.abspath(path)}</h1><ul>"

            # Добавляем список файлов
            for name in file_list:
                response += f"<li>{name}</li>"
            
            response += "</ul>"

            # Добавляем изображение после списка файлов
            response += '<div style="margin-top:20px;">'
            response += '<img src="obito.jpg" alt="Special Image" style="max-width:1000px; max-height:1000px;">'
            response += '</div>'

            response += "</body></html>"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(response.encode("utf-8"))
        except Exception as e:
            self.send_error(404, f"Error: {e}")

# Создаем HTTP-сервер
with socketserver.TCPServer(("", PORT), FileListingHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
