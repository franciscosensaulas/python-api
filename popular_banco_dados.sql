DROP DATABASE IF EXISTS SteamFake;
CREATE DATABASE SteamFake;
USE SteamFake;

INSERT INTO api_categoria (nome) VALUES ('Ação');
INSERT INTO api_categoria (nome) VALUES ('Aventura');
INSERT INTO api_categoria (nome) VALUES ('RPG');
INSERT INTO api_categoria (nome) VALUES ('Estratégia');
INSERT INTO api_categoria (nome) VALUES ('Simulação');
INSERT INTO api_categoria (nome) VALUES ('Esporte');
INSERT INTO api_categoria (nome) VALUES ('Tiro em Primeira Pessoa');
INSERT INTO api_categoria (nome) VALUES ('Plataforma');
INSERT INTO api_categoria (nome) VALUES ('Horror');
INSERT INTO api_categoria (nome) VALUES ('Multiplayer Online');

INSERT INTO api_jogo (nome, preco, desenvolvedora, data_lancamento, classificacao_metacritic, tags, plataforma, descricao, imagem, categoria_id, disponivel_venda) VALUES 
('The Last of Us Part II', 199.90, 'Naughty Dog', '2020-06-19', 93, '["Ação", "Aventura", "Multiplayer Online"]', '["PlayStation 4"]', 'Uma emocionante jornada de sobrevivência e redenção em um mundo pós-apocalíptico.', 'jogos/the last of us 2.avif', 2, TRUE);

INSERT INTO api_jogo (nome, preco, desenvolvedora, data_lancamento, classificacao_metacritic, tags, plataforma, descricao, imagem, categoria_id, disponivel_venda) VALUES 
('Spider-Man: Miles Morales', 149.90, 'Insomniac Games', '2020-11-12', 85, '["Ação", "Aventura"]', '["PlayStation 4", "PlayStation 5"]', 'Viva as aventuras de Miles Morales como o novo Homem-Aranha em Nova York.', 'jogos/spider-man.jfif', 2, TRUE);

INSERT INTO api_jogo (nome, preco, desenvolvedora, data_lancamento, classificacao_metacritic, tags, plataforma, descricao, imagem, categoria_id, disponivel_venda) VALUES 
('The Witcher 3: Wild Hunt', 299.90, 'CD Projekt Red', '2015-05-19', 93, '["RPG", "Aventura"]', '["PC", "PlayStation 4", "Xbox One", "Nintendo Switch"]', 'Um RPG épico em um mundo aberto cheio de monstros e escolhas morais complexas.', 'jogos/The Witcher 3.jfif', 3, TRUE);

INSERT INTO api_jogo (nome, preco, desenvolvedora, data_lancamento, classificacao_metacritic, tags, plataforma, descricao, imagem, categoria_id, disponivel_venda) VALUES 
('Final Fantasy VII Remake', 249.90, 'Square Enix', '2020-04-10', 87, '["RPG", "Ação"]', '["PlayStation 4"]', 'Reviva a história clássica com gráficos modernos e jogabilidade renovada.', 'jogos/Final Fantasy VII.jfif', 3, TRUE);

INSERT INTO api_jogo (nome, preco, desenvolvedora, data_lancamento, classificacao_metacritic, tags, plataforma, descricao, imagem, categoria_id, disponivel_venda) VALUES 
('Assassin\'s Creed Valhalla', 199.90, 'Ubisoft', '2020-11-10', 84, '["Ação", "Aventura", "RPG"]', '["PC", "PlayStation 4", "Xbox One", "PlayStation 5", "Xbox Series X"]', 'Entre no papel de um viking e explore a Inglaterra durante a Era dos Viking.', 'jogos/Assassins Creed Valhalla.webp', 2, TRUE);

INSERT INTO api_jogo (nome, preco, desenvolvedora, data_lancamento, classificacao_metacritic, tags, plataforma, descricao, imagem, categoria_id, disponivel_venda) VALUES 
('Fortnite', 0.00, 'Epic Games', '2017-07-25', 88, '["Multiplayer Online", "Ação"]', '["PC", "PlayStation 4", "Xbox One", "Nintendo Switch", "Mobile"]', 'O famoso battle royale onde você pode construir e lutar para ser o último em pé.', 'jogos/Fortnite.jfif', 10, TRUE);

INSERT INTO api_jogo (nome, preco, desenvolvedora, data_lancamento, classificacao_metacritic, tags, plataforma, descricao, imagem, categoria_id, disponivel_venda) VALUES 
('Half-Life: Alyx', 199.90, 'Valve', '2020-03-23', 93, '["Ação", "Horror"]', '["PC (VR)"]', 'Um jogo de realidade virtual que leva a franquia Half-Life a novos patamares.', 'jogos/Half-Life.jpg', 9, TRUE);

INSERT INTO api_jogo (nome, preco, desenvolvedora, data_lancamento, classificacao_metacritic, tags, plataforma, descricao, imagem, categoria_id, disponivel_venda) VALUES 
('Elden Ring', 249.90, 'FromSoftware', '2022-02-25', 95, '["RPG", "Ação"]', '["PC", "PlayStation 4", "Xbox One", "PlayStation 5", "Xbox Series X"]', 'Uma vasta aventura de RPG em um mundo aberto criado por Hidetaka Miyazaki e George R. R. Martin.', 'jogos/Elden Ring.jpg', 3, TRUE);

INSERT INTO api_jogo (nome, preco, desenvolvedora, data_lancamento, classificacao_metacritic, tags, plataforma, descricao, imagem, categoria_id, disponivel_venda) VALUES 
('Destiny 2', 0.00, 'Bungie', '2017-09-06', 84, '["Tiro em Primeira Pessoa", "Multiplayer Online"]', '["PC", "PlayStation 4", "Xbox One"]', 'Um jogo de tiro em primeira pessoa com elementos de RPG e um mundo em constante evolução.', 'jogos/Destiny 2.jfif', 7, TRUE);

INSERT INTO api_jogo (nome, preco, desenvolvedora, data_lancamento, classificacao_metacritic, tags, plataforma, descricao, imagem, categoria_id, disponivel_venda) VALUES 
('GTA V', 199.90, 'Rockstar Games', '2013-09-17', 97, '["Ação", "Aventura"]', '["PC", "PlayStation 4", "Xbox One", "PlayStation 5"]', 'Um mundo aberto recheado de atividades e missões em Los Santos.', 'jogos/GTA V.webp', 2, TRUE);

INSERT INTO api_jogo (nome, preco, desenvolvedora, data_lancamento, classificacao_metacritic, tags, plataforma, descricao, imagem, categoria_id, disponivel_venda) VALUES 
('Overcooked! 2', 79.90, 'Ghost Town Games', '2018-08-07', 80, '["Simulação", "Multiplayer Online"]', '["PC", "PlayStation 4", "Xbox One", "Nintendo Switch"]', 'Um jogo de culinária cooperativa onde você e seus amigos devem preparar pratos em cozinha caóticas.', 'jogos/Overcooked.avif', 5, TRUE);

INSERT INTO api_jogo (nome, preco, desenvolvedora, data_lancamento, classificacao_metacritic, tags, plataforma, descricao, imagem, categoria_id, disponivel_venda) VALUES 
('FIFA 23', 299.90, 'EA Sports', '2022-09-30', 82, '["Esporte"]', '["PC", "PlayStation 5", "Xbox Series X"]', 'O jogo de futebol que traz as ligas e equipes do mundo todo para suas mãos.', 'jogos/FIFA 23.avif', 6, TRUE);


