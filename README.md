# Bot Pengumpul Berlian - Algoritma Greedy

## Deskripsi Algoritma

Kode ini mengimplementasikan bot untuk game pengumpulan berlian menggunakan algoritma greedy yang berfokus pada efficiency. Bot memiliki sistem prioritas berlapis: pertama menghindari musuh dalam radius bahaya, kemudian mengembalikan berlian ke base jika sudah mengumpulkan 4 atau lebih, lalu mencari dan mengumpulkan berlian dengan sistem scoring yang mempertimbangkan jarak dan nilai berlian. Bot juga memiliki mekanisme eksplorasi cerdas yang mengarah ke pusat papan permainan daripada bergerak acak. Keseluruhan strategi dirancang untuk memaksimalkan efficiency pengumpulan berlian sambil meminimalkan risiko dari musuh.

## Requirements, Instalasi dan Command

### Game Engine

#### A. Requirements
- **Node.js** - [Download di sini](https://nodejs.org/)
- **Docker Desktop** - [Download di sini](https://www.docker.com/products/docker-desktop/)
- **Yarn** - Install dengan command: `npm install --global yarn`

#### B. Instalasi dan Konfigurasi
1. **Download source code** dari [releases page](https://github.com/haziqam/tubes1-IF2211-game-engine/releases/tag/v1.1.0)
2. **Extract** file zip dan masuk ke folder hasil extract
3. **Masuk ke root directory** project:
   ```bash
   cd tubes1-IF2110-game-engine-1.1.0
   ```
4. **Install dependencies**:
   ```bash
   yarn
   ```
5. **Setup environment variables** (Windows):
   ```bash
   ./scripts/copy-env.bat
   ```
6. **Setup database** (pastikan Docker Desktop sudah berjalan):
   ```bash
   docker compose up -d database
   ```
7. **Setup database schema** (Windows):
   ```bash
   ./scripts/setup-db-prisma.bat
   ```

#### C. Build
```bash
npm run build
```

#### D. Run
```bash
npm run start
```

Akses frontend melalui: **http://localhost:8082/**

### Bot

#### A. Requirements
- **Python** - [Download di sini](https://www.python.org/downloads/)

#### B. Instalasi dan Konfigurasi
1. **Download source code** dari [releases page](https://github.com/haziqam/tubes1-IF2211-bot-starter-pack/releases/tag/v1.0.1)
2. **Extract** file zip dan masuk ke folder hasil extract
3. **Masuk ke root directory** project:
   ```bash
   cd tubes1-IF2110-bot-starter-pack-1.0.1
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

#### C. Menjalankan Bot

**Menjalankan satu bot:**
```bash
python main.py --logic Random --email=your_email@example.com --name=your_name --password=your_password --team et
```

**Menjalankan beberapa bot sekaligus (Windows):**
```bash
./run-bots.bat
```

# Video Penjelasan
https://bit.ly/VideoPenjelasan-Visualisasi

## Authors

| Nama                        | NIM       |
|-----------------------------|-----------|
| Memory Simanjuntak          | 123140095 |
| Arsa Salsabila             | 123140108 |
| Grace Exauditha Nababan     | 123140115 |
