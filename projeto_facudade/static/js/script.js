document.getElementById('cadastroForm')?.addEventListener('submit', async function (e) {
    e.preventDefault();

    const usuario = document.getElementById('usuario').value;
    const nota = parseFloat(document.getElementById('nota').value);
    const curso = document.getElementById('curso').value;
    const senha = document.getElementById('senha').value;
    const titulo = document.getElementById('titulo').value;
    const email = document.getElementById('email').value;

    const data = { usuario, nota, curso, senha, titulo, email };

    try {
        const response = await fetch("/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok && result.success) {
            window.location.href = result.redirect || "/login";
        } else {
            document.getElementById("mensagem").textContent = result.error || "Erro ao cadastrar.";
            document.getElementById("mensagem").classList.add("error");
        }
    } catch (error) {
        document.getElementById("mensagem").textContent = "Erro na conexão com o servidor.";
        document.getElementById("mensagem").classList.add("error");
    }
});


document.getElementById('loginForm')?.addEventListener('submit', async function (e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;

    try {
        const response = await fetch("/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, senha })
        });

        const result = await response.json();

        if (result.success) {
            window.location.href = result.redirect || "/home";
        } else {
            document.getElementById("mensagem").textContent = result.error || "Falha no login.";
            document.getElementById("mensagem").classList.add("error");
        }
    } catch (err) {
        document.getElementById("mensagem").textContent = "Erro na conexão.";
        document.getElementById("mensagem").classList.add("error");
    }
});


async function carregarUsuarios() {
    const container = document.getElementById("usuarios-container");
    if (!container) return;

    container.innerHTML = "<p>Carregando...</p>";

    try {
        const response = await fetch("/api/users");
        const data = await response.json();

        if (data.success) {
            mostrarUsuarios(data.data);
        } else {
            container.innerHTML = "<p>Erro ao carregar dados.</p>";
        }
    } catch (err) {
        container.innerHTML = `<p>Erro: ${err.message}</p>`;
    }
}

function mostrarUsuarios(usuarios) {
    const container = document.getElementById("usuarios-container");

    if (!usuarios.length) {
        container.innerHTML = "<p>Nenhum usuário encontrado.</p>";
        return;
    }

    let html = `
        <table border="1" cellpadding="8">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Usuário</th>
                    <th>Email</th>
                    <th>Data de Criação</th>
                    <th>Notas</th>
                </tr>
            </thead>
            <tbody>
    `;

    usuarios.forEach(u => {
        const notasHtml = u.notas.map(n => 
            `<p><strong>${n.titulo}</strong>: ${n.conteudo} 
            <br><small>(${n.criado_em})</small></p>`
        ).join("");

        html += `
            <tr>
                <td>${u.id}</td>
                <td>${u.usuario}</td>
                <td>${u.email}</td>
                <td>${u.criado_em}</td>
                <td>${notasHtml || "Nenhuma nota"}</td>
            </tr>
        `;
    });

    html += `</tbody></table>`;
    container.innerHTML = html;
}

document.addEventListener("DOMContentLoaded", carregarUsuarios);