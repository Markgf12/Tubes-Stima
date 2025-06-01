# Algoritma Greeddy yang Diimplementasikan
Kode ini mengimplementasikan bot untuk game pengumpulan berlian menggunakan algoritma greedy yang berfokus pada efficiency. Bot memiliki sistem prioritas berlapis: pertama menghindari musuh dalam radius bahaya, kemudian mengembalikan berlian ke base jika sudah mengumpulkan 4 atau lebih, lalu mencari dan mengumpulkan berlian dengan sistem scoring yang mempertimbangkan jarak dan nilai berlian. Bot juga memiliki mekanisme eksplorasi cerdas yang mengarah ke pusat papan permainan daripada bergerak acak. Keseluruhan strategi dirancang untuk memaksimalkan efficiency pengumpulan berlian sambil meminimalkan risiko dari musuh.

# Requirement program dan instalasi tertentu dan Command dalam meng-compile atau build program

Cara Menjalankan Game Engine
a. Requirement yang harus di-install 
- Node.js (Node.js — Run JavaScript Everywhere) 
- Docker desktop (https://www.docker.com/products/docker-desktop/ )
- Yarn (npm install --global yarn)

b. Instalasi dan konfigurasi awal
- Download source code (.zip) pada https://github.com/haziqam/tubes1-IF2211-game-engine/releases/tag/v1.1.0 
- Extract zip tersebut, lalu masuk ke folder hasil extractnya dan buka terminal 
- Masuk ke root directory dari project (sesuaikan dengan nama rilis terbaru) 
  (cd tubes1-IF2110-game-engine-1.1.0)

Install dependencies menggunakan Yarn 
- [yarn]

Setup default environment variable dengan menjalankan script berikut Untuk Windows
- [./scripts/copy-env.bat]

Setup local database (buka aplikasi docker desktop terlebih dahulu, lalu jalankan command berikut di terminal)
- [docker compose up -d database] 

Lalu jalankan script berikut. Untuk Windows 
.[/scripts/setup-db-prisma.bat] 

C. Build 
[npm run build]

D. Run
[npm run start]
 
Kunjungi frontend melalui http://localhost:8082/



Cara Menjalankan Bot
a. Requirement yang harus di-install 
- Python (https://www.python.org/downloads/ ) dan konfigurasi awal 

b. Download source code (.zip) pada https://github.com/haziqam/tubes1-IF2211-bot-starter-pack/releases/tag/v1.0.1
- Extract zip tersebut, lalu masuk ke folder hasil extractnya dan buka terminal 
- Masuk ke root directory dari project (sesuaikan dengan nama rilis terbaru) 
- cd tubes1-IF2110-bot-starter-pack-1.0.1 

c. Install dependencies menggunakan pip 
- [pip install -r requirements.txt]

d. Run
Untuk menjalankan satu bot (pada contoh ini, kita menjalankan satu bot dengan logic yang terdapat pada file game/logic/random.py) 

python main.py --logic Random --email=your_email@example.com --name=your_name --password=your_password --team et

Untuk menjalankan beberapa bot sekaligus (pada contoh ini, kita menjalankan 4 bot dengan logic yang sama, yaitu game/logic/random.py)
Untuk windows 
- [./run-bots.bat] 

## Authors

| Nama                        | NIM      |
|-----------------------------|----------|
| Memory Simanjuntak          | 123140095 |
| Arsa Salsabila             | 123140108 |
| Grace Exauditha Nababan     | 123140115 |
