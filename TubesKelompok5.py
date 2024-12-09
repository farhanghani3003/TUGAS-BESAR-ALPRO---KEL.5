import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring

# Data Soal
questions = {}

# Fungsi login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "KELOMPOK5" and password == "12345678":
        login_frame.pack_forget()
        admin_frame.pack()
    else:
        messagebox.showerror("Login Gagal", "Username atau Password salah!")

# Fungsi Tambah Soal
def add_question():
    question = askstring("Tambah Soal", "Masukkan soal:")
    answer = askstring("Tambah Jawaban", "Masukkan jawaban:")
    if question and answer:
        questions[question] = answer
        update_question_list()
    else:
        messagebox.showerror("Error", "Soal atau jawaban tidak boleh kosong!")

# Fungsi Edit Soal
def edit_question():
    selected_question = question_listbox.get(tk.ACTIVE)
    if selected_question:
        new_question = askstring("Edit Soal", "Edit soal:", initialvalue=selected_question)
        new_answer = askstring("Edit Jawaban", "Edit jawaban:", initialvalue=questions[selected_question])
        if new_question and new_answer:
            del questions[selected_question]
            questions[new_question] = new_answer
            update_question_list()
        else:
            messagebox.showerror("Error", "Soal atau jawaban tidak boleh kosong!")
    else:
        messagebox.showerror("Error", "Pilih soal yang ingin diedit!")

# Fungsi Hapus Soal
def delete_question():
    selected_question = question_listbox.get(tk.ACTIVE)
    if selected_question:
        del questions[selected_question]
        update_question_list()
    else:
        messagebox.showerror("Error", "Pilih soal yang ingin dihapus!")

# Fungsi Update List Soal
def update_question_list():
    question_listbox.delete(0, tk.END)
    for q in questions:
        question_listbox.insert(tk.END, q)

# Fungsi Mulai Kuis
def start_quiz():
    if not questions:
        messagebox.showinfo("Info", "Belum ada soal ditambahkan!")
        return
    admin_frame.pack_forget()
    quiz_frame.pack()
    recursive_quiz(0, list(questions.keys()), 0)

# Fungsi Rekursif untuk Quiz
def recursive_quiz(index, keys, score):
    if index < len(keys):
        question = keys[index]
        user_answer = askstring("Quiz", question)
        if user_answer:
            if user_answer.lower() == questions[question].lower():
                score += 1
        recursive_quiz(index + 1, keys, score)
    else:
        messagebox.showinfo("Skor", f"Kuis selesai! Skor Anda: {score}/{len(keys)}")
        quiz_frame.pack_forget()
        admin_frame.pack()

# GUI Utama
root = tk.Tk()
root.title("Aplikasi Kuis")
root.geometry("600x600")

# Frame Login
login_frame = tk.Frame(root)
login_frame.pack()

tk.Label(login_frame, text="Username:").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text="Password:").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

tk.Button(login_frame, text="Login", command=login).pack()

# Frame Admin
admin_frame = tk.Frame(root)

tk.Label(admin_frame, text="Soal Tersedia").pack()
question_listbox = tk.Listbox(admin_frame)
question_listbox.pack()

tk.Button(admin_frame, text="Tambah Soal", command=add_question).pack()
tk.Button(admin_frame, text="Edit Soal", command=edit_question).pack()
tk.Button(admin_frame, text="Hapus Soal", command=delete_question).pack()
tk.Button(admin_frame, text="Mulai Kuis", command=start_quiz).pack()

# Frame Kuis
quiz_frame = tk.Frame(root)

root.mainloop()
