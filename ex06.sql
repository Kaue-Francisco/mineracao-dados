CREATE DATABASE IF NOT EXISTS ecommerce_vendas;
USE ecommerce_vendas;

-- 1. Tabela de Categorias (Dimensão)
CREATE TABLE Categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome_categoria VARCHAR(50) NOT NULL
);

-- 2. Tabela de Produtos (Dimensão)
CREATE TABLE Produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    id_categoria INT,
    CONSTRAINT fk_categoria FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria)
);

-- 3. Tabela de Vendas (Fato)
CREATE TABLE Vendas (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,
    id_produto INT,
    quantidade INT NOT NULL,
    data_venda DATE NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,
    CONSTRAINT fk_produto_venda FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);

-- Populando Categorias (15 registros)
INSERT INTO Categorias (nome_categoria) VALUES 
('Smartphones'), ('Notebooks'), ('Acessórios'), ('Monitores'), ('Teclados'),
('Mouses'), ('Headsets'), ('Smartwatches'), ('Tablets'), ('Impressoras'),
('Câmeras'), ('Armazenamento'), ('Placas de Vídeo'), ('Processadores'), ('Roteadores');

-- Populando Produtos (15 registros)
INSERT INTO Produtos (nome_produto, preco, id_categoria) VALUES 
('iPhone 15 Pro', 8500.00, 1),
('MacBook Air M2', 11000.00, 2),
('Carregador USB-C 20W', 199.00, 3),
('Monitor LG 27" 4K', 2500.00, 4),
('Teclado Mecânico RGB', 450.00, 5),
('Mouse Gamer Sem Fio', 320.00, 6),
('Headset HyperX Cloud II', 580.00, 7),
('Apple Watch Series 9', 3800.00, 8),
('Galaxy Tab S9', 4200.00, 9),
('Impressora HP LaserJet', 1500.00, 10),
('Câmera Sony Alpha a7', 12000.00, 11),
('SSD NVMe 1TB', 600.00, 12),
('RTX 4070 Ti', 5500.00, 13),
('Ryzen 7 7800X3D', 2800.00, 14),
('Roteador Wi-Fi 6 Mesh', 890.00, 15);

-- Populando Vendas (30 registros com datas variadas de 2024)
INSERT INTO Vendas (id_produto, quantidade, data_venda, valor_total) VALUES 
(1, 1, '2024-01-10', 8500.00), (3, 5, '2024-01-12', 995.00), (5, 2, '2024-01-15', 900.00),
(2, 1, '2024-01-18', 11000.00), (12, 3, '2024-01-20', 1800.00), (7, 1, '2024-01-25', 580.00),
(14, 1, '2024-02-05', 2800.00), (1, 2, '2024-02-08', 17000.00), (6, 4, '2024-02-10', 1280.00),
(8, 1, '2024-02-14', 3800.00), (4, 2, '2024-02-20', 5000.00), (15, 1, '2024-02-25', 890.00),
(13, 1, '2024-03-02', 5500.00), (11, 1, '2024-03-05', 12000.00), (9, 2, '2024-03-10', 8400.00),
(10, 1, '2024-03-12', 1500.00), (3, 10, '2024-03-15', 1990.00), (5, 1, '2024-03-18', 450.00),
(12, 5, '2024-03-22', 3000.00), (2, 1, '2024-03-25', 11000.00), (1, 1, '2024-04-01', 8500.00),
(7, 2, '2024-04-05', 1160.00), (6, 2, '2024-04-08', 640.00), (14, 1, '2024-04-12', 2800.00),
(8, 1, '2024-04-15', 3800.00), (4, 1, '2024-04-20', 2500.00), (15, 2, '2024-04-25', 1780.00),
(13, 2, '2024-05-01', 11000.00), (3, 3, '2024-05-05', 597.00), (9, 1, '2024-05-10', 4200.00);
