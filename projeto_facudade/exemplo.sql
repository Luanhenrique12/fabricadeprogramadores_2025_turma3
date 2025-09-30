    UPDATE usuario  set nome  = 'Luan' WHERE id  = 1 ;

    UPDATE usuario SET(nome, email, senha_hash,) = ('Laun', 'luan.henrique@gmail.com', '1234')
    WHERE id = 1; 

SELECT(rua) FROM enderecos;
    DELETE FROM  enderecos;
    DELETE FROM usuario;
    DELETE FROM notas;

SELECT currval('endereco_id_seq');
SELECT nextval('endereco_id_seq');