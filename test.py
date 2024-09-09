from deepface import DeepFace
import pandas as pd
import os

dfs = DeepFace.find(img_path=r"D:\FaceRecognition\Dataset\Johnny Depp\019_3eb26944.jpg", db_path=r"D:\FaceRecognition\Dataset2", model_name='Facenet', enforce_detection=False)

# Kiểm tra nếu danh sách kết quả không rỗng
if len(dfs) > 0 and isinstance(dfs, list):
    # Lấy DataFrame đầu tiên từ danh sách dfs
    df = dfs[0]
    
    if len(df) > 0:
        # Chọn ảnh có khoảng cách nhỏ nhất (kết quả khớp tốt nhất)
        best_match = df.iloc[0]  # Dòng đầu tiên trong DataFrame có khoảng cách nhỏ nhất

        # Lấy đường dẫn tới ảnh khớp tốt nhất
        best_match_path = best_match['identity']

        # Trích xuất tên thư mục chứa ảnh khớp tốt nhất
        best_match_folder = os.path.basename(os.path.dirname(best_match_path))
        
        # In tên folder
        print("Tên folder có kết quả nhận diện cao nhất là:", best_match_folder)
    else:
        print("Không có kết quả khớp nào trong DataFrame.")
else:
    print("Không tìm thấy kết quả nào.")