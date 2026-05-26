async function enviarPergunta() {
  const input = document.getElementById("pergunta");
  const chatBox = document.getElementById("chatBox");

  const pergunta = input.value;

  if (!pergunta.trim()) return;

  chatBox.innerHTML += `<div class="user">${pergunta}</div>`;

  const resposta = await fetch("/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ pergunta })
  });

  const dados = await resposta.json();

  chatBox.innerHTML += `<div class="bot">${dados.resposta}</div>`;

  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function simular() {
  const valor = document.getElementById("valor").value;
  const parcelas = document.getElementById("parcelas").value;
  const juros = document.getElementById("juros").value;

  const resposta = await fetch("/simular", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ valor, parcelas, juros })
  });

  const dados = await resposta.json();

  document.getElementById("resultado").innerHTML = `
    <p>Valor final: R$ ${dados.valor_final}</p>
    <p>Valor por parcela: R$ ${dados.valor_parcela}</p>
  `;
}