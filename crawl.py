import tkinter as tk
from tkinter import ttk, scrolledtext
import requests
from bs4 import BeautifulSoup

class DCInsideCrawler:
    def __init__(self, master):
        self.master = master
        master.title("DC Inside Crawler")
        master.geometry("600x500")  # 높이를 조금 늘렸습니다

        # 입력 프레임
        input_frame = ttk.Frame(master, padding="10")
        input_frame.pack(fill=tk.X)

        # 갤러리 입력창
        ttk.Label(input_frame, text="갤러리 이름:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.gall_entry = ttk.Entry(input_frame)
        self.gall_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        # 사이트 입력창
        ttk.Label(input_frame, text="사이트:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.site_entry = ttk.Entry(input_frame)
        self.site_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)  # row를 1로 수정

        # 게시판 입력창
        ttk.Label(input_frame, text="게시판:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.gall_name_entry = ttk.Entry(input_frame)
        self.gall_name_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

        # 페이지 범위 선택
        ttk.Label(input_frame, text="페이지 범위:").grid(row=3, column=0, sticky=tk.W, pady=5)
        page_frame = ttk.Frame(input_frame)
        page_frame.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)  # row를 3으로 수정
        
        self.start_page = ttk.Spinbox(page_frame, from_=1, to=100, width=5)
        self.start_page.pack(side=tk.LEFT, padx=(0, 5))
        ttk.Label(page_frame, text="부터").pack(side=tk.LEFT, padx=(0, 5))
        self.end_page = ttk.Spinbox(page_frame, from_=1, to=100, width=5)
        self.end_page.pack(side=tk.LEFT, padx=(0, 5))
        ttk.Label(page_frame, text="까지").pack(side=tk.LEFT)

        # 개념글만 옮기기 토글
        self.best_only = tk.BooleanVar()
        ttk.Checkbutton(input_frame, text="개념글만 옮기기", variable=self.best_only).grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=5)

        ttk.Button(input_frame, text="크롤링 시작", command=self.start_crawling).grid(row=5, column=0, columnspan=2, pady=10)

        # 결과 표시 영역
        self.result_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=70, height=20)
        self.result_text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    def start_crawling(self):
        gall_entry = self.gall_entry.get()
        gall_name = self.gall_name_entry.get()
        start_page = int(self.start_page.get())
        end_page = int(self.end_page.get())
        best_only = self.best_only.get()
        
        self.result_text.delete(1.0, tk.END)  # 이전 결과 지우기
        
        gall_size = ["", "mgallery/", "mini/"]
        url_check = False

        for j in range(start_page, end_page):
            url_check = False
            
            for g in gall_size:
                url = f"https://gall.dcinside.com/{g}board/lists/"
                params = {'id' : gall_entry, 'page' : j}
                headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
                print(best_only)
                if best_only:
                    print("개념글만 옮기기")
                    params['exception_mode'] = 'recommend'
                webpage = requests.get(url, params=params, headers=headers)
                soup = BeautifulSoup(webpage.content, "html.parser")
                article = soup.select(".us-post")
                if article:
                    url_check = True
                    break
                print(soup)
            if url_check:
                for i in article:
                    link = "https://gall.dcinside.com/" + i.select("a")[0]['href'].strip() #웹사이트 링크

                    ###########
                    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

                    webpage = requests.get(link, headers=headers)
                    soup = BeautifulSoup(webpage.content, "html.parser")
                    title = soup.select('.title_subject')[0].text.strip()
                    
                    self.result_text.insert(tk.END, f"제목: {title}\n")
                    # 본문 내용 추출
                    content = soup.select('div.write_div')

                    self.result_text.insert(tk.END, f"제목: {content}\n")

                    self.result_text.see(tk.END)
                    self.master.update()
            else:
                self.result_text.insert(tk.END, "데이터가 없습니다.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = DCInsideCrawler(root)
    root.mainloop()