from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/download/<platform>/<media_type>/<url>', methods=['GET'])
def download_media(platform, media_type, url):
    try:
        # TikTok
        if platform.lower() == 'tiktok':
            if media_type.lower() == 'video':
                download_url = f"https://tiktok.com/{url}/download"
            elif media_type.lower() == 'photo':
                download_url = f"https://tiktok.com/{url}/photo"
            elif media_type.lower() == 'audio':
                download_url = f"https://tiktok.com/{url}/audio"
        
        # Facebook
        elif platform.lower() == 'facebook' and media_type.lower() == 'video':
            download_url = f"https://facebook.com/{url}/video/download"

        # YouTube
        elif platform.lower() == 'youtube' and media_type.lower() == 'video':
            download_url = f"https://youtube.com/{url}/video/download"
        
        # Instagram
        elif platform.lower() == 'instagram':
            if media_type.lower() == 'video':
                download_url = f"https://instagram.com/{url}/video/download"
            elif media_type.lower() == 'photo':
                download_url = f"https://instagram.com/{url}/photo/download"

        # If platform or media type is invalid
        else:
            return jsonify({"error": "Invalid platform or media type"}), 400
        
        # Return the response in the required format
        response = {
            "download_url": download_url,
            "developer": "Pasindu",
            "contact": "For support, contact: https://t.me/Pasindu_21"
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
