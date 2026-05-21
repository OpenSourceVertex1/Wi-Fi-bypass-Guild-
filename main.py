"""
██████╗ ██╗███████╗██╗    ██╗██╗███████╗██╗
██╔══██╗██║██╔════╝██║    ██║██║██╔════╝██║
██████╔╝██║█████╗  ██║ █╗ ██║██║█████╗  ██║
██╔══██╗██║██╔══╝  ██║███╗██║██║██╔══╝  ██║
██████╔╝██║███████╗╚███╔███╔╝██║██║     ██║
╚═════╝ ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝
"""

from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Wi-Fi Bypass Guide</title>

    <style>
        body{
            background:#0d1117;
            color:white;
            font-family:Arial;
            padding:40px;
        }

        h1{
            color:#58a6ff;
        }

        .box{
            background:#161b22;
            padding:20px;
            margin-top:20px;
            border-radius:10px;
        }
    </style>
</head>

<body>

    <h1>📶 Wi-Fi Bypass Guide</h1>

    <div class="box">
        <h2>VPN Bypass</h2>
        <p>
            VPNs encrypt your internet traffic and help bypass restrictions.
        </p>
    </div>

    <div class="box">
        <h2>DNS Tunneling</h2>
        <p>
            DNS tunneling encapsulates internet traffic within DNS requests.
        </p>
    </div>

    <div class="box">
        <h2>Proxy Servers</h2>
        <p>
            Proxy servers route traffic through external systems.
        </p>
    </div>

    <div class="box">
        <h2>Captive Portal Bypass</h2>
        <p>
            Public Wi-Fi portals may sometimes be bypassed using
            DNS manipulation or MAC spoofing.
        </p>
    </div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(debug=True)
