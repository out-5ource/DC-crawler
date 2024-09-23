import tkinter as tk
from tkinter import filedialog
import json
import traceback

# 샘플 dict 데이터
data = {
    "이름": "홍길동",
    "나이": 30,
    "직업": "개발자",
    "취미": ["독서", "등산", "코딩"]
}

def save_json():
    try:
        # 파일 저장 대화상자 열기
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON 파일", "*.json")])
        
        if file_path:
            # JSON 파일로 저장
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            result_label.config(text="파일이 성공적으로 저장되었습니다!")
    except Exception as e:
        result_label.config(text=f"오류 발생: {str(e)}")
        print(f"오류 발생: {str(e)}")
        print(traceback.format_exc())

try:
    # 메인 윈도우 생성
    root = tk.Tk()
    root.title("JSON 파일 다운로더")
    root.geometry("300x150")

    # 버튼 생성
    save_button = tk.Button(root, text="JSON 파일로 저장", command=save_json)
    save_button.pack(pady=20)

    # 결과 표시 레이블
    result_label = tk.Label(root, text="")
    result_label.pack()

    print("GUI가 생성되었습니다. 창이 보이지 않으면 작업 표시줄을 확인해 주세요.")

    # 메인 루프 실행
    root.mainloop()
except Exception as e:
    print(f"GUI 생성 중 오류 발생: {str(e)}")
    print(traceback.format_exc())