from flask import Flask, request, make_response
import io
import qrcode

app = Flask(__name__)


@app.route('/qr-code', methods=['GET'])
def generate_qr_code():
    url = request.args.get('url')
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qrcode.make(url)

    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    response = make_response(img_io.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='qr_code.png')
    return response


if __name__ == '__main__':
    app.run(debug=True)
