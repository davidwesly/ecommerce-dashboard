\# 📊 E-Commerce Data Analysis Project



\## 📌 Project Overview



Proyek ini bertujuan untuk melakukan analisis data pada Brazilian E-Commerce Public Dataset (Olist) guna memperoleh insight strategis terkait performa bisnis marketplace.



Analisis dilakukan mulai dari data wrangling, exploratory data analysis (EDA), customer segmentation (RFM), hingga pembuatan dashboard interaktif menggunakan Streamlit.



---



\## 🎯 Business Questions



1\. Bagaimana tren pertumbuhan revenue dan jumlah order selama periode dataset?

2\. Bagaimana segmentasi pelanggan berdasarkan RFM Analysis dan segmen mana yang berkontribusi paling besar terhadap revenue?

3\. Apakah revenue terkonsentrasi pada wilayah geografis tertentu?

4\. Apakah marketplace bergantung pada kategori produk atau seller tertentu?



---



\## 📂 Dataset



Dataset terdiri dari 9 tabel utama:



\- customers

\- orders

\- order\_items

\- order\_payments

\- order\_reviews

\- products

\- sellers

\- product\_category\_name\_translation

\- geolocation



Total transaksi yang dianalisis: 96.478 delivered orders  

Total revenue: 15.489.665  



---



\## 🔎 Analysis Process



\### 1️⃣ Data Understanding

\- Audit struktur data

\- Identifikasi missing value

\- Identifikasi duplicate

\- Validasi relasi antar tabel



\### 2️⃣ Data Wrangling

\- Konversi kolom datetime

\- Filter hanya transaksi delivered

\- Merge seluruh tabel menjadi master dataset

\- Feature engineering (revenue, month\_year)



\### 3️⃣ Revenue Analysis

\- Total Revenue: 15.49M

\- Total Orders: 96.478

\- Unique Customers: 93.358

\- Average Order Value (AOV): 160.55



Revenue menunjukkan pertumbuhan signifikan pada 2017 dan stabil pada 2018.



\### 4️⃣ RFM Customer Segmentation

Customer dikelompokkan menjadi:



\- Champions

\- Loyal Customers

\- Big Spenders

\- Potential

\- At Risk



Loyal Customers dan Big Spenders menyumbang lebih dari 60% total revenue.



Pareto analysis menunjukkan 48.74% customer menyumbang 80% revenue.



\### 5️⃣ Geospatial Analysis

Revenue terkonsentrasi di wilayah Southeast Brazil.



São Paulo menyumbang sekitar 37% total revenue.



\### 6️⃣ Product Category Analysis

Kategori dengan revenue tertinggi:

\- Health \& Beauty

\- Watches \& Gifts

\- Bed, Bath \& Table



Revenue cukup terdiversifikasi tanpa dominasi ekstrem satu kategori.



\### 7️⃣ Seller Analysis

18.52% seller menyumbang 80% revenue, menunjukkan adanya konsentrasi performa pada seller tertentu.



---



\## 📊 Dashboard Features



Dashboard Streamlit menyediakan:



\- KPI (Revenue, Orders, Customers, AOV)

\- Monthly Revenue Trend

\- Monthly Order Trend

\- Revenue by State

\- Top Product Categories

\- RFM Segment Distribution

\- Filter interaktif berdasarkan tanggal dan state



---



\## 🚀 How to Run Dashboard



1\. Masuk ke folder `dashboard`

2\. Pastikan file `main\_data.csv` tersedia

3\. Install dependencies:



```bash

pip install -r requirements.txt

```



4\. Jalankan Streamlit:



```bash

streamlit run dashboard.py

```



---



\## 🏆 Key Insights



\- Marketplace mengalami pertumbuhan signifikan pada 2017 dan stabil pada 2018.

\- Repeat rate relatif rendah (~3%), menunjukkan peluang besar untuk strategi retention.

\- Revenue customer relatif merata (48% customer menyumbang 80% revenue).

\- Revenue seller cukup terkonsentrasi (18% seller menyumbang 80% revenue).

\- São Paulo merupakan kontributor terbesar revenue.

\- Struktur kategori produk cukup terdiversifikasi.



---



\## 📌 Strategic Recommendations



1\. Fokus pada peningkatan customer retention.

2\. Optimalkan loyalty program untuk segmen Loyal \& Champions.

3\. Kembangkan seller mid-tier untuk mengurangi konsentrasi.

4\. Ekspansi pasar di luar wilayah Southeast Brazil.

5\. Optimalkan kategori high-performing untuk cross-selling strategy.



---



\## 👨‍💻 Author



Data Analysis Project - E-Commerce Business Intelligence

