from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def resposta_ia(pergunta):
    pergunta = pergunta.lower()

    if "pix" in pergunta:
        return "Pix é uma forma de pagamento instantâneo criada pelo Banco Central. Ele permite transferências rápidas, geralmente em poucos segundos."

    elif "juros" in pergunta:
        return "Juros são valores cobrados sobre um dinheiro emprestado ou parcelado. Quanto maior o prazo ou a taxa, maior pode ser o valor final."

    elif "cartão" in pergunta or "credito" in pergunta:
        return "O cartão de crédito permite comprar agora e pagar depois. É importante acompanhar a fatura para evitar juros altos."

    elif "organizar" in pergunta or "contas" in pergunta:
        return "Uma boa forma de organizar as contas é separar gastos fixos, variáveis e criar uma reserva para imprevistos."

    else:
        return "Posso te ajudar com dúvidas sobre finanças, Pix, cartão, juros, organização financeira e simulações simples."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    dados = request.get_json()
    pergunta = dados.get("pergunta", "")
    resposta = resposta_ia(pergunta)
    return jsonify({"resposta": resposta})

@app.route("/simular", methods=["POST"])
def simular():
    dados = request.get_json()

    valor = float(dados.get("valor", 0))
    parcelas = int(dados.get("parcelas", 1))
    juros = float(dados.get("juros", 0))

    valor_final = valor + (valor * juros / 100)
    valor_parcela = valor_final / parcelas

    return jsonify({
        "valor_final": round(valor_final, 2),
        "valor_parcela": round(valor_parcela, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)