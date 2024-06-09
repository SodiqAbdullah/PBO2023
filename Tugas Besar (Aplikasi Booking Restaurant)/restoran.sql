-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 19, 2024 at 04:08 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `freedb_restoran`
--

-- --------------------------------------------------------

--
-- Table structure for table `detail_orderan`
--

CREATE TABLE `detail_orderan` (
  `id` int(11) NOT NULL,
  `kode` varchar(10) NOT NULL,
  `no_meja` varchar(10) NOT NULL,
  `kode_order` varchar(10) NOT NULL,
  `qty` int(11) NOT NULL,
  `harga` int(11) NOT NULL,
  `subtotal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `detail_orderan`
--

INSERT INTO `detail_orderan` (`id`, `kode`, `no_meja`, `kode_order`, `qty`, `harga`, `subtotal`) VALUES
(25, '>[5Pd', '1', '1001', 1, 13000, 13000),
(26, 'xxVL\"', '1', '2003', 1, 2000, 2000),
(27, '/^jz|', '1', '2001', 1, 3000, 3000);

-- --------------------------------------------------------

--
-- Table structure for table `orderan`
--

CREATE TABLE `orderan` (
  `id` int(11) NOT NULL,
  `kode_order` varchar(10) NOT NULL,
  `nama_orderan` varchar(255) NOT NULL,
  `harga` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orderan`
--

INSERT INTO `orderan` (`id`, `kode_order`, `nama_orderan`, `harga`) VALUES
(1, '1002', 'Ketoprak', 10000),
(3, '1001', 'Nasi Goreng', 13000),
(4, '1003', 'Nasi Lengko', 6000),
(5, '1004', 'Mie Ayam', 10000),
(6, '2001', 'Kopi Hitam', 3000),
(7, '2002', 'Jus Alpukat', 12000),
(8, '2003', 'Es Teh', 2000);

-- --------------------------------------------------------

--
-- Table structure for table `penyewa`
--

CREATE TABLE `penyewa` (
  `id` int(11) NOT NULL,
  `no_meja` varchar(10) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `jumlah_orang` int(11) NOT NULL,
  `tanggal` date NOT NULL,
  `jam` time NOT NULL,
  `total_bayar` int(11) NOT NULL,
  `lunas` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `penyewa`
--

INSERT INTO `penyewa` (`id`, `no_meja`, `nama`, `jumlah_orang`, `tanggal`, `jam`, `total_bayar`, `lunas`) VALUES
(22, '1', 'sodiq abdullah', 4, '2024-03-30', '09:00:00', 18000, 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `level` enum('admin','customer') NOT NULL DEFAULT 'customer'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `nama`, `password`, `level`) VALUES
(4, 'sodiq@umc.ac.id', 'Sodiq Abdullah', '$2y$10$2vl40E6j9RS7dhhl2Jo6Y..afee1P6gaaXGq28B1DTfT7CNiT85zW', 'admin'),
(12, 'jhon@gmail.com', 'jhon doe', '$2b$12$n4Bx3FsYg2ccPY7w2Aoxv.3fVFDhdfAsnP7NlN1ZFhRD9N4FCfqm2', 'customer');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `detail_orderan`
--
ALTER TABLE `detail_orderan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kode` (`kode`);

--
-- Indexes for table `orderan`
--
ALTER TABLE `orderan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kode_order` (`kode_order`);

--
-- Indexes for table `penyewa`
--
ALTER TABLE `penyewa`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `no_meja` (`no_meja`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `detail_orderan`
--
ALTER TABLE `detail_orderan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `orderan`
--
ALTER TABLE `orderan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `penyewa`
--
ALTER TABLE `penyewa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
