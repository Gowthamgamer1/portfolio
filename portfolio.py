import tkinter as tk
from tkinter import ttk
import webbrowser

# ---------------------
# Constants and Styling
# ---------------------
BG_COLOR = "#f7f9fc"
HEADER_COLOR = "#002b5c"
NAV_COLOR = "#00509e"
TEXT_COLOR = "#ffffff"
BUTTON_COLOR = "#0074d9"
HOVER_COLOR = "#005fbf"
FONT_HEADER = ("Segoe UI", 24, "bold")
FONT_TEXT = ("Segoe UI", 11)
FONT_BUTTON = ("Segoe UI", 10, "bold")

# ---------------------
# Open website function
# ---------------------
def open_website(url):
    webbrowser.open_new_tab(url)

# ---------------------
# Hover effect
# ---------------------
def on_enter(e):
    e.widget['background'] = HOVER_COLOR

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR

# ---------------------
# Main Window
# ---------------------
root = tk.Tk()
root.title("Interactive Portfolio Desktop GUI")
root.geometry("900x650")
root.config(bg=BG_COLOR)

# ---------------------
# Header
# ---------------------
header = tk.Frame(root, bg=HEADER_COLOR, height=100)
header.pack(fill='x')

title = tk.Label(header, text=" My Developer Portfolio", font=FONT_HEADER, fg=TEXT_COLOR, bg=HEADER_COLOR)
title.pack(pady=30)

# ---------------------
# Navigation Bar
# ---------------------
nav = tk.Frame(root, bg=NAV_COLOR, height=50)
nav.pack(fill='x')

nav_links = [
    ("Home", lambda: content_label.config(text="Welcome to my portfolio.\nExplore my work and connect with me.")),
    ("GitHub", lambda: open_website("https://github.com")),
    ("LinkedIn", lambda: open_website("https://www.linkedin.com")),
    ("YouTube", lambda: open_website("https://www.youtube.com")),
    ("Contact", lambda: content_label.config(text=" Email me at: gouthamvadduru@email.com")),
]

for text, cmd in nav_links:
    btn = tk.Button(nav, text=text, bg=BUTTON_COLOR, fg="white", font=FONT_BUTTON, relief="flat", padx=15, pady=8, command=cmd)
    btn.pack(side="left", padx=5, pady=5)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# ---------------------
# Content Section
# ---------------------
content_frame = tk.Frame(root, bg=BG_COLOR)
content_frame.pack(fill='both', expand=True, pady=30)

content_label = tk.Label(content_frame, text="Welcome to my portfolio.\nExplore my work and connect with me.",
                         font=("Segoe UI", 14), bg=BG_COLOR, justify="left")
content_label.pack(pady=10)

# ---------------------
# Project Showcase
# ---------------------
project_title = tk.Label(content_frame, text=" Featured Projects", font=("Segoe UI", 16, "bold"), bg=BG_COLOR)
project_title.pack(pady=10)

projects = [
    ("Flappy Bird Game", "https://github.com/Gowthamgamer1/flappy-bird.git"),
    ("linkedin Profile", "https://www.linkedin.com/in/gowtham-gamer1-75804030b/"),
    ("Portfolio Website", "https://github.com/Gowthamgamer1"),
]

for name, link in projects:
    link_btn = tk.Button(content_frame, text=name, font=FONT_TEXT, fg="white", bg=BUTTON_COLOR, relief="groove", command=lambda l=link: open_website(l))
    link_btn.pack(pady=4)
    link_btn.bind("<Enter>", on_enter)
    link_btn.bind("<Leave>", on_leave)

# ---------------------
# Footer
# ---------------------
footer = tk.Frame(root, bg=HEADER_COLOR, height=40)
footer.pack(fill='x', side='bottom')

footer_label = tk.Label(footer, text="© 2025 My Portfolio • Designed with  in Tkinter", fg=TEXT_COLOR, bg=HEADER_COLOR, font=("Segoe UI", 9))
footer_label.pack(pady=10)

root.mainloop()
