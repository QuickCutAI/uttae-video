import os

from flask import jsonify, url_for


def save_file(file, folder):
    # 파일이 선택되지 않은 경우 처리
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # 파일 저장 경로 설정
    filename = os.path.join(folder, file.filename)

    # 파일 저장
    file.save(filename)

    # 파일 URL 반환
    file_url = url_for('uploaded_file', filename=file.filename)
    return jsonify({'file_url': file_url})

def file_delete(path):
    if not path:
        return jsonify({"error": "파일 경로를 제공해야 합니다."}), 400
    if os.path.exists(path):
        os.remove(path)
        return jsonify({"message": "파일이 성공적으로 삭제되었습니다."})
    else:
        return jsonify({"error": "해당 파일을 찾을 수 없습니다."}), 404

def get_filename(path):
    filenames = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    return filenames[0]

def get_file_directory(path):
    return os.path.dirname(path)

def new_filename(path):
    directory = get_file_directory(path)
    filename = get_filename(path)
    name, extend = filename.split(".")
    return directory + "/" + name + "new." + extend

