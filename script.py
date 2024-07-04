import qrcode

# Datos que quieres codificar (URL)
data = "https://www.example.com"

# Crear una instancia del objeto QRCode
qr = qrcode.QRCode(
    version=1,  # controla el tamaño del QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controla el nivel de corrección de errores
    box_size=10,  # controla el tamaño de cada caja del código QR
    border=4,  # controla el tamaño del borde (el número de cajas)
)

# Agregar datos al objeto QRCode
qr.add_data(data)
qr.make(fit=True)

# Crear una imagen del código QR
img = qr.make_image(fill="black", back_color="white")

# Guardar la imagen del código QR
img.save("codigo_qr.png")
