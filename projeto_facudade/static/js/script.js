document.getElementById('cadastroForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const usuario = document.getElementById('usuario').value;
    const nota = parseFloat(document.getElementById('nota').value);
    const curso = document.getElementById('curso').value;
    const senha = parseFloat(document.getElementById('senha').value);
    const titulo = document.getElementById('titulo').value;
    const email = document.getElementById('email').value;
    


    const data = {
        usuario,
        nota,
        curso,
        senha,
        titulo, 
        email
    };

    try {
        const response = await fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById("mensagem").textContent = "Cadastro realizado com sucesso!";
            document.getElementById("cadastroForm").reset();
        } else {
            document.getElementById("mensagem").textContent = result.error || "Erro ao cadastrar.";
        }
    } catch (error) {
        document.getElementById("mensagem").textContent = "Erro na conexão com o servidor.";
    }
});