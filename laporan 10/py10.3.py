def baca_log_email(file_nama):
   
    email_histogram = {}

    try:
        with open(file_nama, 'r') as file:
            for line in file:
                if line.startswith("From "):
                    kata = line.split()
                    email = kata[1]

                    if email in email_histogram:
                        email_histogram[email] += 1
                    else:
                        email_histogram[email] = 1
    except FileNotFoundError:
        print(f"File '{file_nama}' tidak ditemukan.")
    
    return email_histogram


def tampilkan_histogram(email_histogram):
    """
    Menampilkan histogram email dalam bentuk dictionary.
    
    Args:
        email_histogram (dict): Dictionary dengan email sebagai key dan jumlah pesan sebagai value.
    """
    print("Histogram email:")
    for email, jumlah in email_histogram.items():
        print(f"{email}: {jumlah} pesan")


# Nama file
file_nama = "data-short.txt"

# Membaca log email dan menghitung histogram
email_histogram = baca_log_email(file_nama)

# Menampilkan hasil histogram
tampilkan_histogram(email_histogram)
