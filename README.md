
# Synapsis Challenge Test

This is a challenge test from Synapsis ID.  
An AI Customer Support Agent

# Requirements
- Docker
- Docker Compose

# Specification
For this challenge, I use Macbook Pro M1 with 8GB RAM and 512GB Storage.

That's the reason I don't use GPU on Docker Compose for Ollama.

# Model
- Llama 3.2 3B

# Question List
- Bagaimana cara claim garansi ?
- Apa kelebihan serta harga dari produk smartwatch ?
- Apa kelebihan dari produk keyboard ?
- Bagaimana status dari pesanan dengan order id 003 ?
- Di mana lokasi pesanan saya dengan tracking number TN123456 ?
- Bagaimana status pesanan saya saat ini dengan tracking number TN123456?

# Tool List
- customer_order_checking
- claim_guarantee
- info_product


# Database Design
```
CREATE TABLE conversation (
  id INTEGER PRIMARY KEY,
  user_prompt TEXT NOT NULL,
  system_answer TEXT NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  order_id TEXT NOT NULL UNIQUE,
  tracking_number TEXT,
  customer_location TEXT,
  product_current_location TEXT,
  product_name TEXT NOT NULL,
  order_status TEXT NOT NULL,
  estimated_time_arrival DATE
);
```

# Library & Frameworks
```
fastapi==0.115.9
langchain==0.3.25
langchain-openai==0.3.18
python-dotenv==1.1.0
rich==14.0.0
uvicorn==0.34.2
```

# Installation
Clone the project

```bash
  git clone https://github.com/kylzer/synapsis-challenge.git
```

Go to the project directory

```bash
  cd synapsis-challenge
```

Up Docker Container

```bash
  docker-compose -f docker-compose.yml up -d --build
```

Logging Container  
Chat Logs
```
  docker logs synapsis-chat-1
```
Ollama Logs
```
  docker logs synapsis-ollama-1
```

# Usage
I use Postman to test the the API.  
For the first time, it tooks a while to download the model first, you can look at `ollama logs`.

To do asking, hit with POST Method to this endpoint `http://127.0.0.1:3001/chat`
```
{
  "question": "Apa kelebihan serta harga dari smartwatch ?"
}
```

To get conversation history, you can hit with GET Method to fetch from database to this endpoint `http://127.0.0.1:3001/history`

For alternative, you can use cURL  
Chat
```
curl -X POST "http://127.0.0.1:3001/chat" \
  -H "Content-Type: application/json" \
  -d '{"question":"bagaimana cara claim garansi?"}'
```  
Conversation History  
```
curl -X GET "http://127.0.0.1:3001/history" \
  -H "Content-Type: application/json" 
```

# Example 1
Payload  
```
{
  "question": "apa kelebihan dari produk keyboard ?"
}
```
Output
```
{
    "answer": "Berikut adalah jawaban Anda:\n\nKeyboard adalah salah satu produk yang kami tawarkan di Toko Elektronik kami. Kelebihan dari produk keyboard adalah:\n\n1. **Kenyamanan Typing**: Keyboard memungkinkan Anda untuk mengetik dengan lebih cepat dan akurat, sehingga dapat meningkatkan produktivitas Anda.\n2. **Kualitas Memori**: Keyboard memiliki kualitas memori yang baik, sehingga dapat menyimpan data dengan aman dan stabil.\n3. **Durable**: Keyboard terbuat dari bahan yang kuat dan tahan lama, sehingga dapat bertahan dalam jangka panjang.\n4. **Versiabel**: Keyboard tersedia dalam berbagai jenis dan ukuran, sehingga Anda dapat memilih yang sesuai dengan kebutuhan Anda.\n\nJika Anda memiliki pertanyaan lain tentang keyboard atau ingin mengetahui lebih lanjut tentang produk kami, silakan hubungi kami lagi!"
}
```
# Example 2
Payload  
```
{
  "question": "bagaimana status pesanan saya saat ini dengan tracking number TN123456?"
}
```
Output
```
{
    "answer": "Selamat datang di Toko Elektronik kami!\n\nUntuk mengetahui status pesanan Anda, silakan cek informasi berikut:\n\n- Nomor Pesanan: TN123456\n- Status Pesanan: Telah Dikirim\n- Lokasi saat ini: Jakarta\n- Waktu Tiba yang Diprediksi: 2025-08-25\n\nJika Anda memiliki pertanyaan lain atau memerlukan bantuan tambahan, jangan ragu untuk bertanya!"
}
```

# Example 3
Payload  
```
{
  "question": "bagaimana cara claim garansi ?"
}
```
Output
```
{
    "answer": "Selamat datang di Toko Elektronik kami!\n\nUntuk mengetahui status pesanan Anda, silakan cek informasi berikut:\n\n- Nomor Pesanan: TN123456\n- Status Pesanan: Telah Dikirim\n- Lokasi saat ini: Jakarta\n- Waktu Tiba yang Diprediksi: 2025-08-25\n\nJika Anda memiliki pertanyaan lain atau memerlukan bantuan tambahan, jangan ragu untuk bertanya!"
}
```
# Get Conversation History
Run cURL
```
curl -X GET "http://127.0.0.1:3001/history" \
  -H "Content-Type: application/json" 
```
or with Postman  
Result
```
{
    "records": [
        {
            "user_prompt": "bagaimana cara claim garansi ?",
            "system_answer": "Selamat datang di Toko Elektronik kami!\n\nUntuk melakukan klaim garansi, silakan ikuti instruksi berikut:\n\n1. Siapkan bukti pembelian (invoice) dan nomor seri produk.\n2. Laporkan kendala ke CS dan jelaskan gejala masalah (sertakan foto/video jika perlu).\n3. Tim kami verifikasi dalam 1-2 hari kerja; bila diminta, kirim produk ke alamat servis resmi.\n4. Proses perbaikan/penukaran 7-14 hari kerja setelah barang diterima pusat servis.\n\nJika Anda memiliki pertanyaan atau memerlukan bantuan lebih lanjut, jangan ragu untuk menghubungi kami melalui [nomor telepon] atau [email]. Kami siap membantu!"
        },
        {
            "user_prompt": "bagaimana status pesanan saya saat ini dengan tracking number TN123456?",
            "system_answer": "Selamat datang di Toko Elektronik kami!\n\nUntuk mengetahui status pesanan Anda, silakan cek informasi berikut:\n\n- Nomor Pesanan: TN123456\n- Status Pesanan: Telah Dikirim\n- Lokasi saat ini: Jakarta\n- Waktu Tiba yang Diprediksi: 2025-08-25\n\nJika Anda memiliki pertanyaan lain atau memerlukan bantuan tambahan, jangan ragu untuk bertanya!"
        },
        {
            "user_prompt": "apa kelebihan dari produk keyboard",
            "system_answer": "Berikut adalah jawaban Anda:\n\nKeyboard adalah salah satu produk yang kami tawarkan di Toko Elektronik kami. Kelebihan dari produk keyboard adalah:\n\n1. **Kenyamanan Typing**: Keyboard memungkinkan Anda untuk mengetik dengan lebih cepat dan akurat, sehingga dapat meningkatkan produktivitas Anda.\n2. **Kualitas Memori**: Keyboard memiliki kualitas memori yang baik, sehingga dapat menyimpan data dengan aman dan stabil.\n3. **Durable**: Keyboard terbuat dari bahan yang kuat dan tahan lama, sehingga dapat bertahan dalam jangka panjang.\n4. **Versiabel**: Keyboard tersedia dalam berbagai jenis dan ukuran, sehingga Anda dapat memilih yang sesuai dengan kebutuhan Anda.\n\nJika Anda memiliki pertanyaan lain tentang keyboard atau ingin mengetahui lebih lanjut tentang produk kami, silakan hubungi kami lagi!"
        },
        {
            "user_prompt": "bagaimana status pesanan saya saat ini dengan tracking number TN123456?",
            "system_answer": "Pertanyaan Anda telah ditanggapi. Menurut informasi yang kami miliki, status pesanan Anda sekarang (satu-satunya pesanan yang ada di database) adalah \"Telah Dikirim\" dan lokasinya masih berada di Jakarta."
        },
        {
            "user_prompt": "di mana lokasi pesanan saya saat ini dengan tracking number TN123456?",
            "system_answer": "Lokasi pesanan Anda saat ini adalah Jakarta."
        }
    ]
}
```
