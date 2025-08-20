PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
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
  order_current_location TEXT,
  product_name TEXT NOT NULL,
  order_status TEXT NOT NULL,
  estimated_time_arrival DATE
);
INSERT INTO orders VALUES(1,'001','TN123456','Surabaya','Jakarta','TWS','Telah Dikirim','2025-08-25');
INSERT INTO orders VALUES(2,'002','TN654321','Bogor','Depok','Charger GaN 65W','Sedang Transit','2025-08-23');
INSERT INTO orders VALUES(3,'003','TN278410','Cibubur','Lebak Bulus','Keyboard','Selesai','2025-08-15');
INSERT INTO orders VALUES(4,'004','TN111856','Sidoarjo','Semarang','Smartwatch','Paket Telah Diambil Kurir','2025-08-21');
INSERT INTO orders VALUES(5,'005','TN320955','Banten','Tangerang','Mouse Wireless','Dibatalkan','2025-08-19');
COMMIT;
