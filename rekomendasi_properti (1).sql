-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 27, 2025 at 07:33 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rekomendasi_properti`
--

-- --------------------------------------------------------

--
-- Table structure for table `cities`
--

CREATE TABLE `cities` (
  `id` int NOT NULL,
  `nama_kota` varchar(100) DEFAULT NULL,
  `latitude` decimal(10,7) DEFAULT NULL,
  `longitude` decimal(10,7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cities`
--

INSERT INTO `cities` (`id`, `nama_kota`, `latitude`, `longitude`) VALUES
(1, 'Jakarta Selatan', -6.2607183, 106.7816163),
(2, 'Jakarta Timur', -6.2297287, 106.9004472),
(3, 'Depok', -6.3965210, 106.8187560),
(4, 'Bekasi', -6.2415820, 106.9942340);

-- --------------------------------------------------------

--
-- Table structure for table `clients`
--

CREATE TABLE `clients` (
  `id` int NOT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `lokasi_preferensi` varchar(100) DEFAULT NULL,
  `lat_preferensi` decimal(10,7) DEFAULT NULL,
  `lon_preferensi` decimal(10,7) DEFAULT NULL,
  `harga_min` int DEFAULT NULL,
  `harga_max` int DEFAULT NULL,
  `tipe_preferensi` varchar(50) DEFAULT NULL,
  `luas_min` int DEFAULT NULL,
  `kamar_min` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `preferensi_klien`
--

CREATE TABLE `preferensi_klien` (
  `id` int NOT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `user_text` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `preferensi_klien`
--

INSERT INTO `preferensi_klien` (`id`, `nama`, `user_text`, `created_at`) VALUES
(58, 'Nana', NULL, '2025-07-17 14:26:07'),
(59, 'Nana', NULL, '2025-07-17 14:48:42'),
(60, 'Nana', NULL, '2025-07-17 14:50:18'),
(61, 'Nana', NULL, '2025-07-17 14:50:26'),
(62, 'Nana', NULL, '2025-07-17 14:51:57'),
(63, 'Nana', NULL, '2025-07-17 14:54:00'),
(64, 'Nana', NULL, '2025-07-17 14:56:57'),
(65, 'Nana', NULL, '2025-07-17 14:58:07'),
(66, 'Nana', NULL, '2025-07-17 14:59:17'),
(67, 'Nana', NULL, '2025-07-17 14:59:58'),
(68, 'Nana', NULL, '2025-07-17 15:03:16'),
(69, 'Pak Andi', NULL, '2025-07-17 15:09:23'),
(70, 'Nana', NULL, '2025-07-17 15:14:16'),
(71, 'Nana', NULL, '2025-07-17 15:15:42'),
(72, 'Nana', NULL, '2025-07-17 15:17:03'),
(73, 'Nana', NULL, '2025-07-17 15:20:57'),
(74, 'Nana', NULL, '2025-07-17 15:24:21'),
(75, 'Nana', NULL, '2025-07-17 15:25:12'),
(76, 'Nana', NULL, '2025-07-17 15:26:13'),
(77, 'Nana', NULL, '2025-07-17 15:26:27'),
(78, 'Nana', NULL, '2025-07-17 15:26:42'),
(79, 'Nana', NULL, '2025-07-17 15:27:08'),
(80, 'Nana', NULL, '2025-07-17 15:31:29'),
(81, 'Nana', NULL, '2025-07-17 15:32:10'),
(82, 'Nana', NULL, '2025-07-17 15:34:24'),
(83, 'Nana', NULL, '2025-07-17 15:35:25'),
(84, 'Nana', NULL, '2025-07-17 15:37:12'),
(85, 'Nana', NULL, '2025-07-17 15:37:38'),
(86, 'Nana', NULL, '2025-07-17 15:38:29'),
(87, 'Nana', NULL, '2025-07-17 15:42:07'),
(88, 'Nana', NULL, '2025-07-17 15:53:49'),
(89, 'Budi Santoso', NULL, '2025-07-17 16:07:56'),
(90, 'Budi Santoso', NULL, '2025-07-17 16:12:23'),
(91, 'Budi Santoso', NULL, '2025-07-17 16:15:51'),
(92, 'Batik', NULL, '2025-07-17 16:16:43'),
(93, 'Nana', NULL, '2025-07-17 16:19:56'),
(94, 'Budi', NULL, '2025-07-17 16:29:04'),
(95, 'Batik', NULL, '2025-07-17 16:31:52'),
(96, 'Batik', NULL, '2025-07-17 16:32:23'),
(97, 'Batik', NULL, '2025-07-17 16:32:49'),
(98, 'Kualitas', NULL, '2025-07-17 16:33:04'),
(99, 'Nana', NULL, '2025-07-17 16:35:16'),
(100, 'Nana', NULL, '2025-07-17 16:36:30'),
(101, 'Nana', NULL, '2025-07-17 16:37:27'),
(102, 'Nana', NULL, '2025-07-17 16:38:00'),
(103, 'Nana', NULL, '2025-07-17 16:40:35'),
(104, 'Nana', NULL, '2025-07-17 16:42:07'),
(105, 'Nana', NULL, '2025-07-17 16:42:57'),
(106, 'Nana', NULL, '2025-07-17 16:43:16'),
(107, 'Nana', NULL, '2025-07-17 16:44:16'),
(108, 'Nana', NULL, '2025-07-17 16:46:27'),
(109, 'Nana', NULL, '2025-07-17 16:49:34'),
(110, 'Nana', NULL, '2025-07-17 16:51:56'),
(111, 'Nana', NULL, '2025-07-17 16:53:56'),
(112, 'Nana', NULL, '2025-07-17 16:54:12'),
(113, 'Nana', NULL, '2025-07-17 16:54:57'),
(114, 'Nana', NULL, '2025-07-17 16:55:37'),
(115, 'Nana', NULL, '2025-07-17 16:56:29'),
(116, 'Nana', NULL, '2025-07-17 16:57:00'),
(117, 'Nana', NULL, '2025-07-17 16:58:25'),
(118, 'bekasi', NULL, '2025-07-17 16:58:46'),
(119, 'nana', NULL, '2025-07-18 06:47:25'),
(120, 'nana', NULL, '2025-07-18 07:02:46'),
(121, 'nana', NULL, '2025-07-18 07:03:14'),
(122, 'Nana', NULL, '2025-07-18 07:06:02'),
(123, 'nana', NULL, '2025-07-18 07:11:37'),
(124, 'Nana', 'saya ingin rumah 800 minimalis', '2025-07-18 12:43:54'),
(125, 'nana', 'saya ingin mobil', '2025-07-24 05:02:31'),
(126, 'Nana', 'saya ingin pesawat', '2025-07-24 05:03:04');

-- --------------------------------------------------------

--
-- Table structure for table `properties`
--

CREATE TABLE `properties` (
  `id` int NOT NULL,
  `nama_properti` varchar(150) DEFAULT NULL,
  `lokasi` varchar(100) DEFAULT NULL,
  `latitude` decimal(10,7) DEFAULT NULL,
  `longitude` decimal(10,7) DEFAULT NULL,
  `harga` bigint DEFAULT NULL,
  `luas_tanah` int DEFAULT NULL,
  `luas_bangunan` int DEFAULT NULL,
  `jumlah_kamar` int DEFAULT NULL,
  `deskripsi` text,
  `image_url` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `tipe_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `properties`
--

INSERT INTO `properties` (`id`, `nama_properti`, `lokasi`, `latitude`, `longitude`, `harga`, `luas_tanah`, `luas_bangunan`, `jumlah_kamar`, `deskripsi`, `image_url`, `created_at`, `tipe_id`) VALUES
(12, 'Rumah Taman Indah', 'Jakarta Timur', -6.2297287, 106.9004472, 950000000, 150, 100, 3, 'Rumah minimalis dengan taman depan, carport, dan dekat sekolah.', NULL, '2025-07-17 08:04:53', 1),
(13, 'Villa Asri Cakung', 'Jakarta Timur', -6.2401280, 106.9103120, 1250000000, 200, 140, 4, 'Hunian nyaman dua lantai di Cakung, tersedia kolam kecil dan gazebo.', NULL, '2025-07-17 08:04:53', 1),
(14, 'Green Residence Pondok Kopi', 'Jakarta Timur', -6.2228880, 106.9212340, 800000000, 120, 90, 3, 'Dekat taman kota dan halte busway, lingkungan ramah anak.', NULL, '2025-07-17 08:04:53', 1),
(15, 'Cluster Bambu Apus', 'Jakarta Timur', -6.2839210, 106.8862040, 1100000000, 160, 120, 4, 'Rumah hook dengan sirkulasi udara baik, keamanan 24 jam.', NULL, '2025-07-17 08:04:53', 1),
(16, 'Griya Harmoni', 'Jakarta Timur', -6.2530110, 106.9056120, 750000000, 100, 70, 2, 'Cocok untuk keluarga muda, dekat minimarket dan masjid.', NULL, '2025-07-17 08:04:53', 1),
(17, 'Permata Ciracas', 'Jakarta Timur', -6.3132220, 106.8701130, 900000000, 130, 95, 3, 'Dua lantai, tersedia balkon dan halaman belakang luas.', NULL, '2025-07-17 08:04:53', 1),
(18, 'Rumah Melati Residence', 'Jakarta Timur', -6.2718270, 106.8973000, 1050000000, 140, 110, 4, 'Fasilitas dekat: RS, SPBU, dan sekolah unggulan.', NULL, '2025-07-17 08:04:53', 1),
(19, 'Citra Garden East', 'Jakarta Timur', -6.2673910, 106.9158120, 870000000, 125, 85, 3, 'Rumah modern dengan akses langsung ke jalan utama.', NULL, '2025-07-17 08:04:53', 1),
(20, 'Kenanga Premier Estate', 'Jakarta Timur', -6.2265550, 106.8903120, 980000000, 135, 100, 3, 'Desain elegan, sudah renovasi full, air PAM dan sumur.', NULL, '2025-07-17 08:04:53', 1),
(21, 'Rumah Syariah Halim', 'Jakarta Timur', -6.2641280, 106.9047200, 790000000, 110, 75, 2, 'Tanpa riba, lokasi strategis dekat tol dan bandara.', NULL, '2025-07-17 08:04:53', 1),
(22, 'Tanah Kavling Pondok Kopi', 'Jakarta Timur', -6.2228880, 106.9212340, 500000000, 200, 0, 0, 'Lahan siap bangun, bebas banjir, akses jalan 2 mobil, dekat masjid dan minimarket.', NULL, '2025-07-17 08:05:17', 2),
(23, 'Lahan Strategis Cakung', 'Jakarta Timur', -6.2457280, 106.9123450, 650000000, 250, 0, 0, 'Cocok untuk ruko atau rumah tinggal, 100 meter dari jalan raya besar.', NULL, '2025-07-17 08:05:17', 2),
(24, 'Tanah Investasi Pulogebang', 'Jakarta Timur', -6.2600000, 106.9330000, 780000000, 300, 0, 0, 'Zona kuning, cocok untuk kos-kosan, dekat kampus dan halte BRT.', NULL, '2025-07-17 08:05:17', 2),
(25, 'Lahan Kosong Matraman', 'Jakarta Timur', -6.2056110, 106.8612230, 1200000000, 180, 0, 0, 'Tanah padat penduduk, dekat pasar dan sekolah, cocok untuk cluster.', NULL, '2025-07-17 08:05:17', 2),
(26, 'Kavling Siap Bangun Kampung Melayu', 'Jakarta Timur', -6.2158120, 106.8732210, 450000000, 160, 0, 0, 'Sudah SHM, akses mudah ke terminal Kampung Melayu dan RS Hermina.', NULL, '2025-07-17 08:05:17', 2),
(27, 'Tanah Komersial Jatinegara', 'Jakarta Timur', -6.2227810, 106.8755000, 1750000000, 500, 0, 0, 'Sangat strategis, cocok untuk gudang atau toko, 50 meter dari jalan utama.', NULL, '2025-07-17 08:05:17', 2),
(28, 'Lahan Cluster Rawamangun', 'Jakarta Timur', -6.1972340, 106.8869000, 980000000, 275, 0, 0, 'Cocok untuk developer, lokasi tenang, jalan beton, SHM lengkap.', NULL, '2025-07-17 08:05:17', 2),
(29, 'Tanah Kebon Pala', 'Jakarta Timur', -6.2461280, 106.8912110, 620000000, 220, 0, 0, 'Tanah datar, sudah berpagar keliling, akses 2 arah, dekat SPBU.', NULL, '2025-07-17 08:05:17', 2),
(30, 'Lahan Kosong Halim', 'Jakarta Timur', -6.2642100, 106.9052340, 820000000, 280, 0, 0, 'Hanya 5 menit dari Tol Halim, cocok untuk rumah atau kantor kecil.', NULL, '2025-07-17 08:05:17', 2),
(31, 'Kavling Mungil Ciracas', 'Jakarta Timur', -6.3158000, 106.8650000, 390000000, 130, 0, 0, 'Harga terjangkau, SHM, cocok untuk rumah minimalis atau investasi.', NULL, '2025-07-17 08:05:17', 2),
(32, 'Apartemen Bassura City Tower Dahlia', 'Jakarta Timur', -6.2212340, 106.8912120, 450000000, 0, 24, 1, 'Unit fully furnished dengan kolam renang, gym, foodcourt, dan akses ke tol.', NULL, '2025-07-17 08:05:41', 3),
(33, 'Apartemen Green Pramuka City', 'Jakarta Timur', -6.1907280, 106.8932100, 530000000, 0, 33, 2, 'Dekat TransJakarta, fasilitas mall, swimming pool, dan keamanan 24 jam.', NULL, '2025-07-17 08:05:41', 3),
(34, 'Apartemen Signature Park Grande', 'Jakarta Timur', -6.2412330, 106.8698120, 600000000, 0, 36, 2, 'Unit strategis di MT Haryono, akses stasiun, kolam & sky garden.', NULL, '2025-07-17 08:05:41', 3),
(35, 'Apartemen Tifolia Pulo Mas', 'Jakarta Timur', -6.1902100, 106.9023450, 520000000, 0, 29, 1, 'Dekat kampus dan halte busway, dilengkapi AC dan kitchen set.', NULL, '2025-07-17 08:05:41', 3),
(36, 'Apartemen Sentra Timur Residence', 'Jakarta Timur', -6.2266000, 106.9398120, 410000000, 0, 21, 1, 'Akses langsung ke terminal Sentra Timur, harga terjangkau, bebas macet.', NULL, '2025-07-17 08:05:41', 3),
(37, 'Apartemen Bassura City Tower Cattleya', 'Jakarta Timur', -6.2221000, 106.8909800, 490000000, 0, 25, 1, 'Full furnished, ada ATM center, foodcourt, dan mini waterpark.', NULL, '2025-07-17 08:05:41', 3),
(38, 'Apartemen Green Palace Kalibata', 'Jakarta Timur', -6.2501200, 106.8519020, 560000000, 0, 32, 2, 'Tersedia cafe, gym, kolam renang, dan basement parking.', NULL, '2025-07-17 08:05:41', 3),
(39, 'Apartemen MT Haryono Square', 'Jakarta Timur', -6.2359000, 106.8667000, 580000000, 0, 35, 2, 'Dekat flyover Cawang, cocok untuk karyawan, fully furnished.', NULL, '2025-07-17 08:05:41', 3),
(40, 'Apartemen Puri Park View Tower F', 'Jakarta Timur', -6.2099880, 106.8661230, 500000000, 0, 28, 1, 'Terdekat ke halte busway, tersedia kids playground & minimarket.', NULL, '2025-07-17 08:05:41', 3),
(41, 'Apartemen Jakarta River View', 'Jakarta Timur', -6.2231000, 106.8869000, 615000000, 0, 40, 2, 'View kota Jakarta, tersedia sky gym, jogging track dan cafe rooftop.', NULL, '2025-07-17 08:05:41', 3),
(42, 'Gudang Industri Pulogadung A1', 'Jakarta Timur', -6.2221280, 106.9008120, 3500000000, 800, 600, 2, 'Gudang besar di Kawasan Industri Pulogadung, akses truk kontainer, dekat tol.', NULL, '2025-07-17 08:06:57', 4),
(43, 'Gudang Pergudangan Cakung Timur', 'Jakarta Timur', -6.2438210, 106.9234110, 2950000000, 700, 550, 2, 'Tersedia kantor 2 lantai, loading dock, dan parkir luas.', NULL, '2025-07-17 08:06:57', 4),
(44, 'Gudang Jatinegara Barat', 'Jakarta Timur', -6.2182120, 106.8701230, 3200000000, 600, 500, 1, 'Gudang beton, jalan depan muat truk, cocok untuk logistik.', NULL, '2025-07-17 08:06:57', 4),
(45, 'Gudang Produksi Kampung Melayu', 'Jakarta Timur', -6.2142210, 106.8738720, 2750000000, 550, 450, 1, 'Gudang pabrik kecil dengan fasilitas listrik 22000 VA dan air PAM.', NULL, '2025-07-17 08:06:57', 4),
(46, 'Gudang Simpang Halim', 'Jakarta Timur', -6.2633210, 106.9021140, 3650000000, 850, 700, 3, 'Dekat tol JORR dan bandara Halim, cocok untuk distribusi.', NULL, '2025-07-17 08:06:57', 4),
(47, 'Gudang Pusat Otomotif Cililitan', 'Jakarta Timur', -6.2503180, 106.8654220, 3100000000, 620, 520, 2, 'Zona komersial, bisa untuk bengkel besar, showroom, atau servis center.', NULL, '2025-07-17 08:06:57', 4),
(48, 'Gudang Logistik Ciracas', 'Jakarta Timur', -6.3103210, 106.8708000, 2800000000, 700, 580, 2, 'Bangunan tinggi, ventilasi udara baik, lantai kuat angkut forklift.', NULL, '2025-07-17 08:06:57', 4),
(49, 'Gudang Kecil Kramat Jati', 'Jakarta Timur', -6.2677100, 106.8677120, 1950000000, 400, 350, 1, 'Cocok untuk warehouse usaha UMKM, 2 akses pintu masuk.', NULL, '2025-07-17 08:06:57', 4),
(50, 'Gudang Kayu Putih', 'Jakarta Timur', -6.1878210, 106.8842000, 2550000000, 500, 400, 1, 'Fasilitas lengkap: toilet, kantor admin, dan keamanan CCTV.', NULL, '2025-07-17 08:06:57', 4),
(51, 'Gudang Sentra Niaga Rawamangun', 'Jakarta Timur', -6.1971210, 106.8991880, 3400000000, 780, 600, 2, 'Di area niaga, sangat cocok untuk usaha skala menengah ke atas.', NULL, '2025-07-17 08:06:57', 4),
(52, 'Citra gran - cibubur', 'Jakarta Timur', -6.2297287, 106.9004472, 2500000000, 250, 300, 4, 'Citra Gran', 'hijau.png', '2025-07-17 08:12:34', 1),
(53, 'Raffles Hills', 'Jakarta Timur', -6.2297287, 106.9004472, 6000000000, 350, 200, 4, 'Dijual siap huni', NULL, '2025-07-17 09:00:40', 1);

-- --------------------------------------------------------

--
-- Table structure for table `property_types`
--

CREATE TABLE `property_types` (
  `id` int NOT NULL,
  `nama` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_types`
--

INSERT INTO `property_types` (`id`, `nama`) VALUES
(1, 'Rumah'),
(2, 'Tanah'),
(3, 'Apartemen'),
(4, 'Gudang');

-- --------------------------------------------------------

--
-- Table structure for table `recommendations`
--

CREATE TABLE `recommendations` (
  `id` int NOT NULL,
  `client_id` int DEFAULT NULL,
  `property_id` int DEFAULT NULL,
  `similarity_score` float DEFAULT NULL,
  `recommended_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cities`
--
ALTER TABLE `cities`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `preferensi_klien`
--
ALTER TABLE `preferensi_klien`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `properties`
--
ALTER TABLE `properties`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tipe` (`tipe_id`);

--
-- Indexes for table `property_types`
--
ALTER TABLE `property_types`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recommendations`
--
ALTER TABLE `recommendations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `client_id` (`client_id`),
  ADD KEY `property_id` (`property_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cities`
--
ALTER TABLE `cities`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `clients`
--
ALTER TABLE `clients`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `preferensi_klien`
--
ALTER TABLE `preferensi_klien`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=127;

--
-- AUTO_INCREMENT for table `properties`
--
ALTER TABLE `properties`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `property_types`
--
ALTER TABLE `property_types`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `recommendations`
--
ALTER TABLE `recommendations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `properties`
--
ALTER TABLE `properties`
  ADD CONSTRAINT `fk_tipe` FOREIGN KEY (`tipe_id`) REFERENCES `property_types` (`id`);

--
-- Constraints for table `recommendations`
--
ALTER TABLE `recommendations`
  ADD CONSTRAINT `recommendations_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `recommendations_ibfk_2` FOREIGN KEY (`property_id`) REFERENCES `properties` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
