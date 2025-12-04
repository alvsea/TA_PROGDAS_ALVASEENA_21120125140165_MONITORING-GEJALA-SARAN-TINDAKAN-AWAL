import tkinter as tk 
from tkinter import messagebox, scrolledtext
from datetime import datetime

# ==================== MODUL 1: USER LOGIN STATE ====================
# Variable global untuk user yang sedang login
current_user = None


# ==================== MODUL 4: FUNCTION UNTUK AUTENTIKASI ====================

def login_user(username, password):
    
    # MODUL 2: Pengkondisian

    global current_user

    # MODUL 2: Validasi input
    if not username or not password:
        return False, "Username dan password wajib diisi!"

    current_user = username
    return True, f"Login berhasil! Selamat datang, {username}"


# ==================== MODUL 4: FUNCTION & METHOD ====================
# Function untuk analisis gejala berdasarkan scoring

def hitung_score_gejala(suhu, durasi, demam, batuk, sesak, mual, pusing):
    """
    MODUL 1: Tipe Data (float, int, boolean)
    MODUL 2: Pengkondisian (if-elif)

    Menghitung score berdasarkan input gejala
    Return: integer (score)
    """
    score = 0

    # Modul 2: Pengkondisian bertingkat untuk suhu
    if suhu >= 39:
        score += 4
    elif suhu >= 38:
        score += 3
    elif suhu >= 37.5:
        score += 2
    elif suhu >= 37:
        score += 1

    # Pengkondisian untuk durasi
    if durasi >= 5:
        score += 3
    elif durasi >= 3:
        score += 2
    elif durasi >= 1:
        score += 1

    # Modul 2: Pengkondisian sederhana (boolean)
    if demam:
        score += 1
    if batuk:
        score += 1
    if mual:
        score += 1
    if pusing:
        score += 1
    if sesak:
        score += 4  # Sesak napas prioritas tinggi

    return score


def tentukan_severity(score):
    
    # MODUL 2: Pengkondisian

    if score <= 3:
        return "RINGAN"  
    elif 4 <= score <= 7:
        return "SEDANG"   
    else:
        return "BERAT" 


def buat_saran(severity):
    
    # MODUL 2: Pengkondisian
    # MODUL 1: Tipe Data String
    
    saran_dict = {
        "RINGAN": """
🏠 TINDAKAN MANDIRI:
• Istirahat cukup di rumah
• Minum air putih minimal 8 gelas/hari
• Konsumsi makanan bergizi
• Monitor suhu tubuh secara rutin
• Gunakan obat penurun panas jika perlu

⚠️ PERINGATAN:
Jika gejala memburuk dalam 2-3 hari, segera konsultasi dokter.
        """,

        "SEDANG": """
🏥 KONSULTASI MEDIS:
• Hubungi dokter dalam 24-48 jam
• Persiapkan riwayat gejala detail
• Jangan tunda jika ada perburukan
• Gunakan masker jika batuk
• Catat perkembangan gejala
• Hindari kontak dengan orang rentan

⚠️ PERINGATAN:
Segera ke fasilitas kesehatan jika:
- Sesak napas bertambah
- Demam tidak turun > 3 hari
- Kesadaran menurun
        """,

        "BERAT": """
🚨 TINDAKAN DARURAT:
• SEGERA ke IGD/Rumah Sakit
• Jangan tunda penanganan
• Informasikan riwayat penyakit
        """
    }

    return saran_dict.get(severity, "Saran tidak tersedia")


# ==================== MODUL 1: ARRAY/LIST ====================
# List untuk menyimpan riwayat pemeriksaan
riwayat_pemeriksaan = []


def tambah_riwayat(data_nama):
    """
    MODUL 1: Array/List - append data
    MODUL 1: Dictionary untuk struktur data

    Menambahkan data ke riwayat pemeriksaan
    """
    # Modul 1: Dictionary (tipe data terstruktur)
    riwayat = {
        "waktu": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "nama": data_nama["nama"],
        "suhu": data_nama["suhu"],
        "severity": data_nama["severity"],
        "score": data_nama["score"],
        "gejala": data_nama["gejala_list"]
    }

    # Modul 1: List operation - append
    riwayat_pemeriksaan.append(riwayat)

# MODUL 5 OOP (OBJECT ORIENTED PROGRAMMING)
# ==================== GUI CLASS: LOGIN ====================

class LoginRegisterFrame(tk.Frame):
    """
    MODUL 4: Class untuk Login
    MODUL 8: GUI Frame
    """

    def __init__(self, parent, on_login_success):
        """
        Constructor untuk frame login
        """
        super().__init__(parent, bg="#f0f4f8")
        self.on_login_success = on_login_success
        self.show_password = False

        self.buat_ui()

    def buat_ui(self):
        """
        Membuat tampilan login
        """
        # Container utama
        main_container = tk.Frame(self, bg="#f0f4f8")
        main_container.pack(expand=True, fill="both", padx=50, pady=50)

        # Frame untuk card login
        card = tk.Frame(main_container, bg="white", relief="solid", bd=1)
        card.place(relx=0.5, rely=0.5, anchor="center", width=450, height=500)

        # Header
        tk.Label(
            card,
            text="SISTEM MONITORING GEJALA",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            fg="#3b82f6"
        ).pack(pady=(30, 5))

        tk.Label(
            card,
            text="Silakan login untuk melanjutkan",
            font=("Segoe UI", 10),
            bg="white",
            fg="#6b7280"
        ).pack(pady=(0, 20))

        # Frame untuk form
        form_frame = tk.Frame(card, bg="white")
        form_frame.pack(padx=40, fill="x")

        # Username
        tk.Label(
            form_frame,
            text="Username:",
            font=("Segoe UI", 10),
            bg="white",
            fg="#1e293b",
        ).pack(anchor="w", pady=(0, 10))

        self.entry_username = tk.Entry(
            form_frame,
            font=("Segoe UI", 11),
            relief="solid",
            bd=1,
        )
        self.entry_username.pack(fill="x", ipady=5, pady=(0, 15))

        # Password
        tk.Label(
            form_frame,
            text="Password:",
            font=("Segoe UI", 10),
            bg="white",
            fg="#1e293b"
        ).pack(anchor="w", pady=(0, 5))

        # Frame untuk password + show/hide button
        pass_frame = tk.Frame(form_frame, bg="white")
        pass_frame.pack(fill="x", pady=(0, 20))

        self.entry_password = tk.Entry(
            pass_frame,
            font=("Segoe UI", 11),
            relief="solid",
            bd=1,
            show="●"
        )
        self.entry_password.pack(side="left", fill="x", expand=True, ipady=5)

        self.btn_show_pass = tk.Button(
            pass_frame,
            text="👁",
            font=("Segoe UI", 10),
            command=self.toggle_password,
            relief="flat",
            bg="white",
            cursor="hand2",
            width=3
        )
        self.btn_show_pass.pack(side="left", padx=(5, 0))

        # Tombol Login
        tk.Button(
            form_frame,
            text="LOGIN",
            command=self.handle_login,
            font=("Segoe UI", 11, "bold"),
            bg="#3b82f6",
            fg="white",
            activebackground="#2563eb",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            pady=10
        ).pack(fill="x", pady=(0, 10))

        # Info text 
        tk.Label(
            card,
            text="Masukkan username dan password untuk login",  
            font=("Segoe UI", 8),
            bg="white",
            fg="#9ca3af",
            justify="center"
        ).pack(pady=(20, 0))
        
        tk.Label(
            card,
            text="Password harus 4 digit angka",  
            font=("Segoe UI", 8),
            bg="white",
            fg="#9ca3af",
            justify="center"
        ).pack(pady=(20, 0))

        # Bind Enter key untuk login
        self.entry_password.bind('<Return>', lambda e: self.handle_login())

    def toggle_password(self):
        """
        Toggle show/hide password
        """
        self.show_password = not self.show_password
        if self.show_password:
            self.entry_password.config(show="")
            self.btn_show_pass.config(text="🙈")
        else:
            self.entry_password.config(show="●")
            self.btn_show_pass.config(text="👁")

    def handle_login(self):
        """
        MODUL 4: Method untuk handle login
        """
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()
        
        # Validasi username hanya huruf
        if not username.isalpha():
            messagebox.showerror("Error", "Username hanya boleh berisi huruf (A-Z), tidak boleh angka!")
            return
        
        # Validasi password 4 digit angka
        if not password.isdigit() or len(password) != 4:
            messagebox.showerror("Error", "Password harus 4 digit angka!")
            return

        # MODUL 4: Panggil function login
        success, message = login_user(username, password)

        # MODUL 2: Pengkondisian hasil login
        if success:
            messagebox.showinfo("Login Berhasil", message)
            self.on_login_success()  # Callback ke main app
        else:
            messagebox.showerror("Login Gagal", message)


# ==================== GUI CLASS ====================
class AplikasiMonitoringGejala:
    """
    MODUL 4: Method dalam Class
    MODUL 8: GUI Programming dengan Tkinter
    """

    def __init__(self, parent):
        """
        MODUL 4: Constructor method
        MODUL 1: Variable initialization
        """
        # Gunakan parent frame, bukan root window
        self.root = parent

        # MODUL 1: Variable untuk styling
        self.bg_color = "#f0f4f8"
        self.primary_color = "#3b82f6"
        self.text_color = "#1e293b"

        # Configure parent background
        self.root.configure(bg=self.bg_color)

        # MODUL 4: Memanggil method
        self.buat_header()
        self.buat_form_input()
        self.buat_tombol_aksi()
        self.buat_area_hasil()


    def buat_header(self):
        """
        MODUL 8: Label widget
        """
        frame_header = tk.Frame(self.root, bg=self.primary_color, height=120)
        frame_header.pack(fill="x")
        frame_header.pack_propagate(False)

        # Frame untuk konten header
        header_content = tk.Frame(frame_header, bg=self.primary_color)
        header_content.pack(fill="both", expand=True)

        # Tombol Logout di pojok kanan atas
        logout_frame = tk.Frame(header_content, bg=self.primary_color)
        logout_frame.pack(side="right", anchor="ne", padx=20, pady=10)

        tk.Button(
            logout_frame,
            text="LOGOUT",
            command=self.handle_logout,
            font=("Segoe UI", 9, "bold"),
            bg="#dc2626",
            fg="white",
            activebackground="#b91c1c",
            activeforeground="white",
            relief="flat",
            padx=15,
            pady=5,
            cursor="hand2"
        ).pack()

        # Info user di pojok kiri atas
        user_frame = tk.Frame(header_content, bg=self.primary_color)
        user_frame.pack(side="left", anchor="nw", padx=20, pady=10)

        tk.Label(
            user_frame,
            text=f"👤 User: {current_user}",
            font=("Segoe UI", 9, "bold"),
            bg=self.primary_color,
            fg="white"
        ).pack()

        # Info shortcut di pojok kanan bawah
        shortcut_frame = tk.Frame(header_content, bg=self.primary_color)
        shortcut_frame.pack(side="bottom", anchor="se", padx=20, pady=5)

        tk.Label(
            shortcut_frame,
            text="F11: Fullscreen | ESC: Exit Fullscreen",
            font=("Segoe UI", 8),
            bg=self.primary_color,
            fg="#e0e7ff"
        ).pack()

        # Judul di tengah
        title_frame = tk.Frame(header_content, bg=self.primary_color)
        title_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            title_frame,
            text="🏥 SISTEM MONITORING GEJALA KESEHATAN",
            font=("Segoe UI", 20, "bold"),
            bg=self.primary_color,
            fg="white"
        ).pack()

        tk.Label(
            title_frame,
            text="Deteksi Dini • Analisis Cepat • Saran Akurat",
            font=("Segoe UI", 10),
            bg=self.primary_color,
            fg="#e0e7ff"
        ).pack(pady=(5, 0))

    def buat_form_input(self):
        """
        MODUL 8: Frame, Label, Entry, Checkbutton widgets
        """
        # Container utama - FIXED, tidak responsive
        container = tk.Frame(self.root, bg=self.bg_color)
        container.pack(padx=20, pady=15, fill="x")  # fill="x" saja, bukan "both"

        # Frame kiri: Input data - FIXED SIZE
        frame_kiri = tk.LabelFrame(
            container,
            text="📝 Data & Gejala",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg=self.text_color,
            padx=15,
            pady=15,
            width=500,
            height=350
        )
        frame_kiri.pack(side="left", padx=(0, 10))
        frame_kiri.pack_propagate(False)  # PENTING: Prevent auto-resize

        # MODUL 8: Entry widgets untuk input
        # 1. Nama 
        tk.Label(
            frame_kiri,
            text="Nama:",
            font=("Segoe UI", 10),
            bg="white",
            fg=self.text_color
        ).grid(row=0, column=0, sticky="w", pady=8, padx=5)

        self.entry_nama = tk.Entry(
            frame_kiri,
            font=("Segoe UI", 10),
            width=20,  
            relief="solid",
            bd=1
        )
        self.entry_nama.grid(row=0, column=1, pady=8, padx=5)

        # 2. Suhu Tubuh
        tk.Label(
            frame_kiri,
            text="Suhu Tubuh (°C):",
            font=("Segoe UI", 10),
            bg="white",
            fg=self.text_color
        ).grid(row=1, column=0, sticky="w", pady=8, padx=5)

        self.entry_suhu = tk.Entry(
            frame_kiri,
            font=("Segoe UI", 10),
            width=20,  # Fixed width
            relief="solid",
            bd=1
        )
        self.entry_suhu.grid(row=1, column=1, sticky="w", pady=8, padx=5)

        # 3. Durasi Gejala
        tk.Label(
            frame_kiri,
            text="Durasi Gejala (hari):",
            font=("Segoe UI", 10),
            bg="white",
            fg=self.text_color
        ).grid(row=2, column=0, sticky="w", pady=8, padx=5)

        self.entry_durasi = tk.Entry(
            frame_kiri,
            font=("Segoe UI", 10),
            width=20,  # Fixed width
            relief="solid",
            bd=1
        )
        self.entry_durasi.grid(row=2, column=1, sticky="w", pady=8, padx=5)

        # MODUL 8: Checkbutton untuk gejala
        # MODUL 1: IntVar untuk boolean state
        tk.Label(
            frame_kiri,
            text="Pilih Gejala yang Dialami:",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg=self.text_color
        ).grid(row=3, column=0, columnspan=2, sticky="w", pady=(15, 5), padx=5)

        frame_checkbox = tk.Frame(frame_kiri, bg="white")
        frame_checkbox.grid(row=4, column=0, columnspan=2, sticky="w", pady=5, padx=5)

        # MODUL 1: Variable boolean
        self.var_demam = tk.IntVar()
        self.var_batuk = tk.IntVar()
        self.var_sesak = tk.IntVar()
        self.var_mual = tk.IntVar()
        self.var_pusing = tk.IntVar()

        # MODUL 3: Perulangan untuk membuat checkbox
        gejala_list = [
            ("🤒 Demam", self.var_demam),
            ("😷 Batuk", self.var_batuk),
            ("🫁 Sesak Napas", self.var_sesak),
            ("🤢 Mual", self.var_mual),
            ("😵 Pusing", self.var_pusing)
        ]

        for i, (text, var) in enumerate(gejala_list):
            tk.Checkbutton(
                frame_checkbox,
                text=text,
                variable=var,
                font=("Segoe UI", 10),
                bg="white",
                fg=self.text_color,
                activebackground="white"
            ).grid(row=i//2, column=i % 2, sticky="w", padx=10, pady=5)

    def buat_tombol_aksi(self):
        """
        MODUL 8: Button widget dengan command
        """
        frame_tombol = tk.Frame(self.root, bg=self.bg_color)
        frame_tombol.pack(pady=10)

        # Tombol Analisis
        tk.Button(
            frame_tombol,
            text="🔍 ANALISIS GEJALA",
            command=self.proses_analisis,  # MODUL 4: method call
            font=("Segoe UI", 11, "bold"),
            bg=self.primary_color,
            fg="white",
            activebackground="#2563eb",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(side="left", padx=5)

        # Tombol Reset
        tk.Button(
            frame_tombol,
            text="🔄 RESET",
            command=self.reset_form,
            font=("Segoe UI", 10),
            bg="#6b7280",
            fg="white",
            activebackground="#4b5563",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(side="left", padx=5)

        # Tombol Hapus Riwayat
        tk.Button(
            frame_tombol,
            text="🗑️ HAPUS RIWAYAT",
            command=self.hapus_riwayat,
            font=("Segoe UI", 10),
            bg="#dc2626",
            fg="white",
            activebackground="#b91c1c",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(side="left", padx=5)

        # Separator
        tk.Frame(frame_tombol, width=30, bg=self.bg_color).pack(side="left")

        # Tombol Buka Form Hasil Analisis
        tk.Button(
            frame_tombol,
            text="📊 LIHAT HASIL ANALISIS",
            command=self.buka_form_hasil_analisis,
            font=("Segoe UI", 10),
            bg="#10b981",
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(side="left", padx=5)

        # Tombol Buka Form Riwayat
        tk.Button(
            frame_tombol,
            text="📋 LIHAT RIWAYAT",
            command=self.buka_form_riwayat,
            font=("Segoe UI", 10),
            bg="#f59e0b",   
            fg="white",
            activebackground="#d97706",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(side="left", padx=5)

    def buat_area_hasil(self):
        """
        MODUL 8: Text widget untuk output
        """
        self.frame_hasil = tk.LabelFrame(
            self.root,
            text="📊 Hasil Analisis",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg=self.text_color,
            padx=15,
            pady=15
        )
        self.frame_hasil.pack(padx=20, pady=(0, 10), fill="both", expand=True)

        self.text_hasil = scrolledtext.ScrolledText(
            self.frame_hasil,
            height=8,
            font=("Consolas", 10),
            bg="#f9fafb",
            fg=self.text_color,
            relief="flat",
            wrap="word"
        )
        self.text_hasil.pack(fill="both", expand=True)

    def proses_analisis(self):
        """
        MODUL 4: Method utama untuk memproses data
        MODUL 2: Pengkondisian validasi
        MODUL 1: Konversi tipe data
        """
        # MODUL 1: Ambil data dari Entry (string)
        nama = self.entry_nama.get().strip()
        suhu_str = self.entry_suhu.get().strip()
        durasi_str = self.entry_durasi.get().strip()
        
        # Validasi nama hanya huruf
        if not nama.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Nama hanya boleh berisi huruf (A-Z), tidak boleh angka!")
            return

        # MODUL 2: Validasi input
        if not nama:
            messagebox.showwarning("Peringatan", "Nama wajib diisi!")
            return

        # MODUL 1: Konversi tipe data string ke float/int
        try:
            suhu = float(suhu_str.replace(",", "."))
            durasi = int(durasi_str)
        except ValueError:
            messagebox.showerror(
                "Error Input",
                "Suhu harus berupa angka (contoh: 37.5)\n"
                "Durasi harus berupa angka bulat (contoh: 3)"
            )
            return

        # MODUL 2: Validasi range nilai
        if suhu < 35 or suhu > 45:
            messagebox.showwarning(
                "Peringatan",
                "Suhu tidak wajar! Mohon periksa kembali."
            )
            return

        if durasi < 0:
            messagebox.showwarning(
                "Peringatan",
                "Durasi tidak boleh negatif!"
            )
            return

        # MODUL 1: Ambil nilai boolean dari IntVar
        demam = bool(self.var_demam.get())
        batuk = bool(self.var_batuk.get())
        sesak = bool(self.var_sesak.get())
        mual = bool(self.var_mual.get())
        pusing = bool(self.var_pusing.get())

        # MODUL 4: Panggil function
        score = hitung_score_gejala(suhu, durasi, demam, batuk, sesak, mual, pusing)
        severity = tentukan_severity(score)   # ← Diperbaiki: hanya 1 nilai
        saran = buat_saran(severity)

        # MODUL 1: List untuk menyimpan gejala terpilih
        gejala_aktif = []
        if demam:
            gejala_aktif.append("Demam")
        if batuk:
            gejala_aktif.append("Batuk")
        if sesak:
            gejala_aktif.append("Sesak Napas")
        if mual:
            gejala_aktif.append("Mual")
        if pusing:
            gejala_aktif.append("Pusing")

        # MODUL 1: String formatting
        gejala_text = ", ".join(gejala_aktif) if gejala_aktif else "Tidak ada gejala spesifik"

        # Tampilkan hasil
        self.text_hasil.delete("1.0", tk.END)
        hasil_text = f"""
{'='*70}
                    HASIL ANALISIS GEJALA
{'='*70}

IDENTITAS       :
  Nama          : {nama}
  Waktu Periksa : {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

DATA VITAL      :
  Suhu Tubuh    : {suhu}°C
  Durasi Gejala : {durasi} hari
  Gejala        : {gejala_text}

KATEGORI ANALISIS :  
  Kategori        : {severity}

{'='*70}
{saran}
{'='*70}
        """

        self.text_hasil.insert("1.0", hasil_text)

        # MODUL 1: Dictionary untuk struktur data
        # MODUL 4: Panggil function untuk simpan riwayat
        data_nama = {
            "nama": nama,
            "suhu": suhu,
            "severity": severity,
            "score": score,
            "gejala_list": gejala_aktif
        }
        tambah_riwayat(data_nama)

 

        # Notifikasi
        messagebox.showinfo(
            "Analisis Selesai",
            f"Nama: {nama}\n"
            f"Kategori: {severity}\n"
            f"Hasil lengkap tersedia di area hasil analisis."
        )

    

    def reset_form(self):
        """
        MODUL 4: Method untuk reset form
        """
        self.entry_nama.delete(0, tk.END)
        self.entry_suhu.delete(0, tk.END)
        self.entry_durasi.delete(0, tk.END)

        self.var_demam.set(0)
        self.var_batuk.set(0)
        self.var_sesak.set(0)
        self.var_mual.set(0)
        self.var_pusing.set(0)

        self.text_hasil.delete("1.0", tk.END)
        self.text_hasil.insert(
            "1.0",
            "Form telah direset.\nSilakan masukkan data baru."
        )

    def hapus_riwayat(self):
        """
        MODUL 2: Pengkondisian
        MODUL 1: List operation (clear)
        """
        # MODUL 2: Konfirmasi dengan pengkondisian
        if messagebox.askyesno(
            "Konfirmasi",
            "Yakin ingin menghapus semua riwayat?"
        ):
            # MODUL 1: List clear
            riwayat_pemeriksaan.clear()
            messagebox.showinfo(
                "Berhasil",
                "Semua riwayat telah dihapus."
            )

    def buka_form_hasil_analisis(self):
        """
        MODUL 4: Method untuk membuka window form hasil analisis
        MODUL 8: Toplevel window
        """
        # Buat window baru
        window_hasil = tk.Toplevel(self.root)
        window_hasil.title("📊 Hasil Analisis Terakhir")
        window_hasil.geometry("900x600")
        window_hasil.configure(bg="white")

        # Header
        header = tk.Frame(window_hasil, bg=self.primary_color, height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="📊 HASIL ANALISIS GEJALA",
            font=("Segoe UI", 18, "bold"),
            bg=self.primary_color,
            fg="white"
        ).pack(pady=20)

        # Container untuk content
        content_frame = tk.Frame(window_hasil, bg="white", padx=20, pady=20)
        content_frame.pack(fill="both", expand=True)

        # Text area untuk hasil
        text_hasil_popup = scrolledtext.ScrolledText(
            content_frame,
            font=("Consolas", 11),
            bg="#f9fafb",
            fg=self.text_color,
            relief="solid",
            bd=1,
            wrap="word"
        )
        text_hasil_popup.pack(fill="both", expand=True)

        # MODUL 2: Cek apakah ada hasil analisis
        current_text = self.text_hasil.get("1.0", tk.END).strip()
        if current_text and current_text != "Form telah direset.\nSilakan masukkan data baru.":
            text_hasil_popup.insert("1.0", current_text)
        else:
            text_hasil_popup.insert(
                "1.0",
                "="*70 + "\n" +
                "              BELUM ADA HASIL ANALISIS\n" +
                "="*70 + "\n\n" +
                "Silakan lakukan analisis gejala terlebih dahulu\n" +
                "dengan mengisi form dan klik tombol 'ANALISIS GEJALA'.\n\n" +
                "Hasil analisis akan ditampilkan di sini setelah\n" +
                "proses analisis selesai."
            )

        # Readonly
        text_hasil_popup.config(state="disabled")

        # Footer dengan tombol
        footer = tk.Frame(window_hasil, bg="white", pady=10)
        footer.pack(fill="x")

        # Tombol Close
        tk.Button(
            footer,
            text="✖ TUTUP",
            font=("Segoe UI", 10),
            bg="#6b7280",
            fg="white",
            activebackground="#4b5563",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            command=window_hasil.destroy
        ).pack(side="right", padx=10)

    def buka_form_riwayat(self):
        """
        MODUL 4: Method untuk membuka window form riwayat pemeriksaan
        MODUL 8: Toplevel window
        """
        # Buat window baru
        window_riwayat = tk.Toplevel(self.root)
        window_riwayat.title("📋 Riwayat Pemeriksaan")
        window_riwayat.geometry("1000x600")
        window_riwayat.configure(bg="white")

        # Header
        header = tk.Frame(window_riwayat, bg="#f59e0b", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="📋 RIWAYAT PEMERIKSAAN",
            font=("Segoe UI", 18, "bold"),
            bg="#f59e0b",
            fg="white"
        ).pack(pady=20)

        # Container untuk content
        content_frame = tk.Frame(window_riwayat, bg="white", padx=20, pady=20)
        content_frame.pack(fill="both", expand=True)

        # Info jumlah riwayat
        info_frame = tk.Frame(content_frame, bg="white")
        info_frame.pack(fill="x", pady=(0, 10))

        jumlah_riwayat = len(riwayat_pemeriksaan)
        tk.Label(
            info_frame,
            text=f"Total Pemeriksaan: {jumlah_riwayat} data",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg=self.text_color
        ).pack(side="left")

        # Text area untuk riwayat
        text_riwayat_popup = scrolledtext.ScrolledText(
            content_frame,
            font=("Consolas", 10),
            bg="#f9fafb",
            fg=self.text_color,
            relief="solid",
            bd=1,
            wrap="word"
        )
        text_riwayat_popup.pack(fill="both", expand=True)

        # MODUL 2: Cek apakah ada riwayat
        if not riwayat_pemeriksaan:
            text_riwayat_popup.insert(
                "1.0",
                "="*80 + "\n" +
                "                 BELUM ADA RIWAYAT PEMERIKSAAN\n" +
                "="*80 + "\n\n" +
                "Belum ada data pemeriksaan yang tersimpan.\n\n" +
                "Riwayat akan otomatis tersimpan setiap kali Anda melakukan\n" +
                "analisis gejala pada form utama.\n\n" +
                "Data yang tersimpan meliputi:\n" +
                "• Waktu pemeriksaan\n" +
                "• Nama\n" +
                "• Suhu tubuh\n" +
                "• Kategori keparahan\n" +
                "• Score gejala\n" +
                "• Daftar gejala yang dialami\n"
            )
        else:
            # MODUL 3: Perulangan untuk menampilkan semua riwayat
            text_riwayat_popup.insert("1.0", f"{'='*80}\n")
            text_riwayat_popup.insert("end", "RIWAYAT PEMERIKSAAN LENGKAP\n")
            text_riwayat_popup.insert("end", f"{'='*80}\n\n")

            for i, data in enumerate(riwayat_pemeriksaan, start=1):
                # MODUL 1: Akses dictionary
                gejala_str = ", ".join(data["gejala"]) if data["gejala"] else "Tidak ada gejala spesifik"

                riwayat_text = f"""
{i}. [{data['waktu']}] {data['nama']}
   Kategori  : {data['severity']} 
   Suhu      : {data['suhu']}°C
   Gejala    : {gejala_str}
{'-'*80}
"""
                text_riwayat_popup.insert("end", riwayat_text)

        # Readonly
        text_riwayat_popup.config(state="disabled")

        # Footer dengan tombol
        footer = tk.Frame(window_riwayat, bg="white", pady=10)
        footer.pack(fill="x")

        # Tombol Hapus Semua
        tk.Button(
            footer,
            text="🗑️ HAPUS SEMUA",
            font=("Segoe UI", 10),
            bg="#dc2626",
            fg="white",
            activebackground="#b91c1c",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            command=lambda: self.hapus_riwayat_dari_popup(window_riwayat)
        ).pack(side="left", padx=10)

        # Tombol Hapus Satu
        tk.Button(
            footer,
            text="❌ HAPUS SATU",
            font=("Segoe UI", 10),
            bg="#ef4444",
            fg="white",
            activebackground="#dc2626",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            command=lambda: self.hapus_satu_riwayat(window_riwayat)
        ).pack(side="left", padx=10)

        
        # Tombol Refresh
        tk.Button(
            footer,
            text="🔄 REFRESH",
            font=("Segoe UI", 10),
            bg="#3b82f6",
            fg="white",
            activebackground="#2563eb",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            command=lambda: [window_riwayat.destroy(), self.buka_form_riwayat()]
        ).pack(side="left", padx=10)

        # Tombol Close
        tk.Button(
            footer,
            text="✖ TUTUP",
            font=("Segoe UI", 10),
            bg="#6b7280",
            fg="white",
            activebackground="#4b5563",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            command=window_riwayat.destroy
        ).pack(side="right", padx=10)

    def hapus_riwayat_dari_popup(self, window):
        """
        MODUL 4: Method untuk hapus riwayat dari popup window
        """
        if messagebox.askyesno(
            "Konfirmasi",
            "Yakin ingin menghapus semua riwayat?"
        ):
            riwayat_pemeriksaan.clear()
            window.destroy()
            messagebox.showinfo(
                "Berhasil",
                "Semua riwayat telah dihapus.\nWindow akan ditutup."
            )
            
    def hapus_satu_riwayat(self, window):
        """
        Hapus satu entri riwayat berdasarkan nomor urut.
        """
        if not riwayat_pemeriksaan:
            messagebox.showwarning("Kosong", "Tidak ada riwayat yang bisa dihapus.")
            return

        # Popup input nomor
        input_window = tk.Toplevel(window)
        input_window.title("Hapus Satu Riwayat")
        input_window.geometry("350x160")
        input_window.configure(bg="white")

        tk.Label(
            input_window,
            text="Masukkan nomor riwayat yang ingin dihapus:",
            font=("Segoe UI", 10),
            bg="white"
        ).pack(pady=10)

        entry_nomor = tk.Entry(input_window, font=("Segoe UI", 11), relief="solid", bd=1)
        entry_nomor.pack(pady=5)

        def konfirmasi_hapus():
            try:
                idx = int(entry_nomor.get()) - 1
                if idx < 0 or idx >= len(riwayat_pemeriksaan):
                    raise ValueError

                if messagebox.askyesno(
                    "Konfirmasi",
                    f"Yakin ingin menghapus riwayat nomor {idx+1}?"
                ):
                    del riwayat_pemeriksaan[idx]
                    messagebox.showinfo("Berhasil", f"Riwayat nomor {idx+1} telah dihapus.")
                    input_window.destroy()
                    window.destroy()
                    self.buka_form_riwayat()

            except ValueError:
                messagebox.showerror("Error", "Nomor tidak valid!")

        tk.Button(
            input_window,
            text="HAPUS",
            font=("Segoe UI", 10, "bold"),
            bg="#dc2626",
            fg="white",
            relief="flat",
            padx=15,
            pady=5,
            command=konfirmasi_hapus
        ).pack(pady=10)

    def handle_logout(self):
        """
        MODUL 4: Method untuk logout
        """
        global current_user

        # MODUL 2: Konfirmasi logout
        if messagebox.askyesno(
            "Konfirmasi Logout",
            f"Yakin ingin logout, {current_user}?"
        ):
            current_user = None

            # Akses root window dari parent
            root_window = self.root.winfo_toplevel()
            root_window.destroy()  # Tutup window aplikasi

            # Buat window login baru
            new_root = tk.Tk()
            MainApp(new_root)
            new_root.mainloop()


# ==================== MAIN APP CLASS ====================

class MainApp:
    """
    MODUL 4: Main Application Class
    Class untuk mengatur tampilan login dan aplikasi utama
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Monitoring Gejala Kesehatan")

        # FULLSCREEN & RESPONSIVE
        self.root.state('zoomed')
        self.root.minsize(800, 600)
        self.root.resizable(True, True)

        # Bind ESC key
        self.root.bind('<Escape>', lambda e: self.toggle_fullscreen())
        self.root.bind('<F11>', lambda e: self.toggle_fullscreen())

        self.is_fullscreen = True
        self.root.configure(bg="#f0f4f8")

        # Container utama
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        # MODUL 2: Pengkondisian - cek apakah user sudah login
        if current_user is None:
            self.show_login_frame()
        else:
            self.show_main_app()

    def toggle_fullscreen(self):
        """Toggle fullscreen"""
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes('-fullscreen', self.is_fullscreen)

    def show_login_frame(self):
        """
        Tampilkan frame login
        """
        # Hapus semua widget di container
        for widget in self.container.winfo_children():
            widget.destroy()

        # Tampilkan login frame
        login_frame = LoginRegisterFrame(
            self.container,
            on_login_success=self.show_main_app
        )
        login_frame.pack(fill="both", expand=True)

    def show_main_app(self):
        """
        Tampilkan aplikasi utama setelah login
        """
        # Hapus semua widget di container
        for widget in self.container.winfo_children():
            widget.destroy()

        # Buat frame baru untuk aplikasi utama
        app_frame = tk.Frame(self.container)
        app_frame.pack(fill="both", expand=True)

        # Inisialisasi aplikasi utama di dalam frame
        AplikasiMonitoringGejala(app_frame)


# ==================== MAIN PROGRAM ====================
if __name__ == "__main__":
    """
    MODUL 4: Main program
    MODUL 8: Tkinter mainloop
    """
    root = tk.Tk()
    app = MainApp(root)  # Gunakan MainApp untuk handle login
    root.mainloop()