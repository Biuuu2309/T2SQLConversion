import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Kiểm tra thiết bị (GPU/CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def generate_sql_debug(question, model_path=r"E:\Project_MachineLearning_NguyenMinhVu\Source\Basic-text-to-SQL-conversion\Python\t5_sql_model\checkpoint-28017"):
    """
    Hàm sinh câu SQL từ câu hỏi đầu vào sử dụng mô hình T5 đã được huấn luyện.
    
    Args:
        question (str): Câu hỏi đầu vào.
        model_path (str): Đường dẫn đến mô hình đã được huấn luyện.
    
    Returns:
        str: Câu SQL được sinh ra.
    """
    try:
        # Tải tokenizer và mô hình từ đường dẫn đã huấn luyện
        tokenizer = T5Tokenizer.from_pretrained(model_path)
        model = T5ForConditionalGeneration.from_pretrained(model_path).to(device)
        
        # Tiền xử lý câu hỏi đầu vào
        input_text = f"{question}"
        inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        inputs = {key: val.to(device) for key, val in inputs.items()}
        
        # Sinh câu SQL
        outputs = model.generate(**inputs, max_length=512)
        sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return sql_query
    except Exception as e:
        print(f"Lỗi khi sinh câu SQL: {e}")
        return None