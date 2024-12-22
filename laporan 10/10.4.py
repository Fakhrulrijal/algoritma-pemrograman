def baca_domain_email(file_nama):
    """
    Membaca file log email untuk mencatat dan menghitung jumlah pesan berdasarkan domain.

    Args:
        file_nama (str): Nama file yang berisi log email.

    Returns:
        dict: Dictionary dengan domain sebagai key dan jumlah pesan sebagai value.
    """
    domain_histogram = {}

    try:
        with open(file_nama, 'r') as file:
            for line in file:
                # Memproses hanya baris yang diawali dengan "From"
                if line.startswith("From "):
                    # Memisahkan baris menjadi kata-kata
                    kata = line.split()

                    # Email biasanya ada di posisi kedua
                    email = kata[1]

                    # Memisahkan domain dari email (setelah '@')
                    domain = email.split('@')[-1]

                    # Tambahkan domain ke histogram
                    if domain in domain_histogram:
                        domain_histogram[domain] += 1
                    else:
                        domain_histogram[domain] = 1
    except FileNotFoundError:
        print(f"File '{file_nama}' tidak ditemukan.")
    
    return domain_histogram


def tampilkan_histogram_domain(domain_histogram):
    """
    Menampilkan histogram domain dalam bentuk dictionary.

    Args:
        domain_histogram (dict): Dictionary dengan domain sebagai key dan jumlah pesan sebagai value.
    """
    print("Histogram domain pengirim:")
    for domain, jumlah in domain_histogram.items():
        print(f"{domain}: {jumlah} pesan")


# Nama file
file_nama = "data-short.txt"

# Membaca log email dan menghitung histogram domain
domain_histogram = baca_domain_email(file_nama)

# Menampilkan hasil histogram domain
tampilkan_histogram_domain(domain_histogram)
