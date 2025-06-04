
from flask import Blueprint, request, jsonify
import os
from utils.resume_parser import parse_resume

resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    file_path = os.path.join('/tmp', file.filename)
    file.save(file_path)
    text = parse_resume(file_path)
    return jsonify({"parsed_text": text})
