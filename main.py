import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import time

class DCInsideCrawler:
    def __init__(self, master):
        self.master = master
        master.title("DC Inside Crawler")
        master.geometry("800x600")

        self.setup_ui()

    def setup_ui(self):
        # 갤러리 URL 입력
        self.url_label = ttk.Label(self.master, text="갤러리 URL:")
        self.url_label.pack()
        self.url_entry = ttk.Entry(self.master, width=50)
        self.url_entry.pack()

        # 크롤링 시작 버튼
        self.start_button = ttk.Button(self.master, text="크롤링 시작", command=self.start_crawling)
        self.start_button.pack()

        # 로그 표시 영역
        self.log_text = tk.Text(self.master, height=20, width=80)
        self.log_text.pack()

    def start_crawling(self):
        url = self.url_entry.get()
        self.log_text.insert(tk.END, f"크롤링 시작: {url}\n")
        
        # 여기에 실제 크롤링 로직을 구현합니다
        self.crawl_gallery(url)

    def crawl_gallery(self, url):
        # 일반게시판 크롤링
        self.crawl_board(url, "일반게시판")
        
        # 개념글게시판 크롤링
        concept_url = url + "/concept"
        self.crawl_board(concept_url, "개념글게시판")

    def crawl_board(self, url, board_type):
        # 여기에 실제 크롤링 및 게시 로직을 구현합니다
        self.log_text.insert(tk.END, f"{board_type} 크롤링 중...\n")
        # 크롤링 로직 구현
        # 게시 로직 구현
        self.log_text.insert(tk.END, f"{board_type} 크롤링 완료\n")

root = tk.Tk()
crawler = DCInsideCrawler(root)
root.mainloop()