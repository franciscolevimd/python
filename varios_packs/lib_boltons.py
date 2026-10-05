from boltons import urlutils


# Tratar una URL como un objeto con propiedades propias, no como un string.
mi_url = urlutils.URL(
    "https://www.example.com:8080/path/to/resource?query=param#fragment"
)
print("URL:", mi_url)
print("Host:", mi_url.host)
print("Port:", mi_url.port)
print("Scheme:", mi_url.scheme)
print("Path:", mi_url.path)
