def load_questions(file_path):
    """
    Membaca soal dan jawaban dari file.
    Format soal: "soal || jawaban"
    """
    questions = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if '||' in line:
                    question, answer = line.strip().split('||')
                    questions.append((question.strip(), answer.strip()))
    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan.")
        return None
    return questions


def ask_questions(questions):
    """
    Menampilkan soal, menerima jawaban pengguna, dan menghitung skor.
    """
    print("\n===== Selamat Datang di Aplikasi Kuis =====\n")
    score = 0
    total_questions = len(questions)

    for i, (question, answer) in enumerate(questions, start=1):
        print(f"Soal {i}: {question}")
        user_answer = input("Jawaban Anda: ").strip()

        if user_answer.lower() == answer.lower():
            print("✔️ Benar!\n")
            score += 1
        else:
            print(f"❌ Salah! Jawaban yang benar adalah: {answer}\n")

    print("===== Kuis Selesai =====")
    print(f"Skor Anda: {score} / {total_questions}")
    print("========================")


def main():
    file_path = "tantangan.txt"  # Nama file soal
    questions = load_questions(file_path)

    if questions is not None and len(questions) > 0:
        ask_questions(questions)
    else:
        print("Tidak ada soal yang dapat ditampilkan.")


# Menjalankan aplikasi
if __name__ == "__main__":
    main()
