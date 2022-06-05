from youtube_dl import YoutubeDL
from tkinter import Tk,messagebox,StringVar,OptionMenu
from tkinter.ttk import Label,Entry,Button,Style

class Tampil(Tk):
   def __init__(self):
      super().__init__()

      #deklarasi window
      self.title('YouTube Simple Downloader')
      self.geometry('600x312')
      self.configure(bg='white')
      self.resizable(width=False, height=False)
      # self.iconbitmap('ytdownloader.ico')

      #deklarasi style
      Style().configure('TLabel', foreground='black', background='white', font=('Microsoft PhagsPa',12))
      Style().configure('TButton', foreground='black', background='white', font=('Microsoft PhagsPa',12))

      #deklarasi objek
      self.labelURL = Label(self, text='Masukkan URL : ', style='TLabel')
      self.entryURL = Entry(self)
      self.buttonCheck = Button(self, text='Check', style='TButton', command=self.Check)
      self.labelSpasi1 = Label(self, text=' ', style='TLabel')
      self.labelVideo = Label(self, text='Status : Menunggu Check ...', style='TLabel')
      self.labelSpasi2 = Label(self, text=' ', style='TLabel')

      self.labelKualitas = Label(self, text='Kualitas\t: ', style='TLabel')
      self.Kualitas = StringVar(self)
      self.Kualitas.set("   Pilih\t") # default value
      self.dropdownKualitas = OptionMenu(self, self.Kualitas, '  Tinggi\t', '  Rendah\t')

      self.labelFormat = Label(self, text='Format\t: ', style='TLabel')
      self.Format = StringVar(self)
      self.Format.set("   Pilih\t") # default value
      self.dropdownFormat = OptionMenu(self, self.Format, '  mp3\t', '  mp4\t')

      self.labelDrive = Label(self, text='Save to\t➤Drive\t:', style='TLabel')
      self.entryDrive = Entry(self)
      self.labelFolder = Label(self, text='\t➤Folder\t:', style='TLabel')
      self.entryFolder = Entry(self)
      self.labelNama = Label(self, text='\t➤Nama\t:', style='TLabel')
      self.entryNama = Entry(self)
      self.buttonDownload = Button(self, text='Download', style='TButton', command=self.Download)
      self.labelSpasi4 = Label(self, text=' ', style='TLabel')
      self.labelProsesDownload = Label(self, text='Status : Menunggu Download ...', style='TLabel')
      self.buttonInfo = Button(self, text=' INFO', style='TButton', command=self.Info, width=6)
      self.buttonReset = Button(self, text='RESET', style='TButton', command=self.Reset, width=6)
      
      #deklarasi grid
      self.labelURL.grid(row=0, column=0, padx=250, sticky='w', columnspan=2)
      self.entryURL.grid(row=1, column=0, padx=8, sticky='w', ipadx=173, ipady=4, columnspan=2)
      self.buttonCheck.grid(row=1, column=0, padx=485, sticky='w', columnspan=2)
      self.labelSpasi1.grid(row=2, column=0, padx=8)
      self.labelVideo.grid(row=3, column=0, padx=220, sticky='w', columnspan=2)
      self.labelSpasi2.grid(row=4, column=0, padx=8)
      self.labelKualitas.grid(row=5, column=0, padx=8, sticky='w')
      self.dropdownKualitas.grid(row=5, column=0, sticky='w', padx=100)
      self.labelFormat.grid(row=6, column=0, padx=8, sticky='w')
      self.dropdownFormat.grid(row=6, column=0, sticky='w', padx=100)
      self.labelDrive.grid(row=5, column=0, padx=300, sticky='w')
      self.entryDrive.grid(row=5, column=0, padx=467, sticky='w')
      self.labelFolder.grid(row=6, column=0, padx=300, sticky='w')
      self.entryFolder.grid(row=6, column=0, padx=467, sticky='w')
      self.labelNama.grid(row=7, column=0, padx=300, sticky='w')
      self.entryNama.grid(row=7, column=0, padx=467, sticky='w')
      self.buttonDownload.grid(row=8, column=0, padx=250, sticky='w', columnspan=2)
      self.labelSpasi4.grid(row=9, column=0, padx=8)
      self.labelProsesDownload.grid(row=10, column=0, padx=200, sticky='w', columnspan=2)
      self.buttonInfo.grid(row=10, column=0, padx=8, sticky='w')
      self.buttonReset.grid(row=10, column=0, padx=530, sticky='w')

      #auto deklarasi
      self.entryDrive.insert('end', 'C')
      self.entryFolder.insert('end', 'Musik')

   def Check(self):
      if self.entryURL.get() != "" :
         url = self.entryURL.get()
         ydl_opts = {
            'format': 'worstaudio',
            'noplaylist': True,
         }
         with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url)
            video_title = info_dict.get('title', None)
         print(video_title)
         self.labelVideo.destroy()
         self.labelVideo = Label(self, text=f'Judul : {video_title}', style='TLabel')
         self.labelVideo.grid(row=3, column=0, padx=8, sticky='w', columnspan=2)
      else :
         messagebox.showerror('Kesalahan', 'Masukkan URL Video terlebih dahulu')

   def Download(self):
      if self.entryURL.get() != "" :
         if self.Kualitas.get() != "   Pilih\t" and self.Format.get() != "   Pilih\t" and self.entryDrive.get() != "" and self.entryFolder.get() != "" and self.entryNama.get() != "" :
            drive = self.entryDrive.get()
            folder = self.entryFolder.get()
            name = self.entryNama.get()
            url = self.entryURL.get()

            formats = ''
            if self.Format.get() == '  mp3\t' :
               formats = 'mp3'
            elif self.Format.get() == '  mp4\t' :
               formats = 'mp4'

            kualitas = ''
            if formats == 'mp3' :
               if self.Kualitas.get() == '  Tinggi\t' :
                  kualitas = 'bestaudio/best'
               elif self.Kualitas.get() == '  Rendah\t' :
                  kualitas = 'worstaudio/worst'
            elif formats == 'mp4' :
               if self.Kualitas.get() == '  Tinggi\t' :
                  kualitas = 'best'
               elif self.Kualitas.get() == '  Rendah\t' :
                  kualitas = 'worst'

            print(kualitas)

            ydl_opts = {
            'format': f'{kualitas}',
            'outtmpl': f'{drive}:\\{folder}\\{name}'+f'.{formats}',
            'noplaylist': True,
            'extract-audio': True,
            'audioformat': f'{formats}'
            }

            with YoutubeDL(ydl_opts) as ydl:
               self.labelProsesDownload.destroy()
               self.labelProsesDownload = Label(self, text='Status : Sedang di Download ...', style='TLabel')
               self.labelProsesDownload.grid(row=10, column=0, padx=190, sticky='w', columnspan=2)
               ydl.extract_info(url, download=True)
               messagebox.showinfo('Selesai', f'Download Selesai\n\nHasil Download disimpan di {drive}:\{folder}\{name}.{formats}')
               self.labelProsesDownload.destroy()
               self.labelProsesDownload = Label(self, text='Status : Selesai di Download', style='TLabel')
               self.labelProsesDownload.grid(row=10, column=0, padx=200, sticky='w', columnspan=2)
         else :
            messagebox.showerror('Kesalahan', 'Lengkapi pengaturan Kualitas, Format, dan penyimpanan pada Drive dan Folder serta Nama penyimpanan')
      else :
         messagebox.showerror('Kesalahan', 'Masukkan URL Video terlebih dahulu')
   
   def Info(self):
      messagebox.showinfo('Informasi', 'Terimakasih telah mengunduh YouTube Simple Downloader\nAplikasi ini dibuat berbasis Python\n\nCara penggunaan :\n    1. Masukkan URL Video\n    2. Tekan Check untuk validasi Video\n    3. Atur kualitas dan format download\n    4. Atur Drive dan Folder untuk letak penyimpanan\n    5. Atur Nama untuk nama file saat  penyimpanan\n    6. Tekan Download lalu tunggu hingga selesai\n\nTips :\nGunakan RESET untuk mereset seluruh form\n\nDeveloped by Naufal Fawwazi\nContact naufalfawwazi@outlook.com for more information')

   def Reset(self):
      self.entryURL.delete(0, 'end')
      self.labelVideo.destroy()
      self.labelVideo = Label(self, text='Status : Menunggu Check ...', style='TLabel')
      self.labelVideo.grid(row=3, column=0, padx=220, sticky='w', columnspan=2)
      self.Kualitas.set("   Pilih\t")
      self.Format.set("   Pilih\t")
      self.entryDrive.delete(0, 'end')
      self.entryDrive.insert('end', 'C')
      self.entryFolder.delete(0, 'end')
      self.entryFolder.insert('end', 'Musik')
      self.entryNama.delete(0, 'end')
      self.labelProsesDownload.destroy()
      self.labelProsesDownload = Label(self, text='Status : Menunggu Download ...', style='TLabel')
      self.labelProsesDownload.grid(row=10, column=0, padx=200, sticky='w', columnspan=2)

if __name__ == "__main__":
   app = Tampil()
   app.mainloop()