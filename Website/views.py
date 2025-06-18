from flask import Blueprint, request, jsonify, render_template
from Website.Python_model import generate_sql_debug  # Import hàm từ Python_model.py

views = Blueprint('views', __name__)

@views.route('/')
def home():
    """
    Trang chính của ứng dụng.
    """
    return render_template('home.html')

@views.route('/generate_sql', methods=['POST'])
def generate_sql():
    """
    Xử lý yêu cầu POST để sinh câu SQL từ câu hỏi đầu vào.
    """
    try:
        # Lấy dữ liệu từ yêu cầu POST
        data = request.get_json()
        question = data.get("question", "")

        # Kiểm tra xem câu hỏi có hợp lệ không
        if not question:
            return jsonify({"error": "Câu hỏi không hợp lệ"}), 400

        # Sử dụng hàm generate_sql_debug để tạo câu SQL
        sql_query = generate_sql_debug(question, model_path=r"E:\Project_MachineLearning_NguyenMinhVu\Source\Basic-text-to-SQL-conversion\Python\t5_sql_model\checkpoint-28017")

        # Kiểm tra xem có lỗi khi sinh câu SQL không
        if sql_query is None:
            return jsonify({"error": "Không thể sinh câu SQL"}), 500

        # Trả về kết quả dưới dạng JSON
        return jsonify({"sql_query": sql_query})
    except Exception as e:
        return jsonify({"error": str(e)}), 500