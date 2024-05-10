import tkinter as tk
from tkinter import scrolledtext, messagebox

class NotepadApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pink Notepad")
        self.master.geometry("600x400")
        self.master.config(bg="pink")

        self.text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, font=("Calibri", 12))
        self.text_area.pack(expand=True, fill="both", padx=5, pady=5)

        self.highlight_button = tk.Button(self.master, text="Highlight", command=self.highlight_text)
        self.highlight_button.pack(side=tk.LEFT, padx=(10, 0), pady=10)

        self.save_button = tk.Button(self.master, text="Save", command=self.save_text)
        self.save_button.pack(side=tk.RIGHT, padx=(0, 10), pady=10)

    def highlight_text(self):
        try:
            start_index = self.text_area.index(tk.SEL_FIRST)
            end_index = self.text_area.index(tk.SEL_LAST)
            self.text_area.tag_add("highlight", start_index, end_index)
            self.text_area.tag_config("highlight", background="pink")
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select text to highlight.")

    def save_text(self):
        text_content = self.text_area.get("1.0", tk.END)
        with open("notepad_text.txt", "w") as file:
            file.write(text_content)
        messagebox.showinfo("Info", "Text saved successfully.")

def main():
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
