
// Data da revelação do presente
const dataRevelacao = new Date("2026-11-19T00:00:00-03:00").getTime();

// Atualiza a contagem regressiva
function atualizarContagem() {

    const agora = new Date().getTime();

    const diferenca = dataRevelacao - agora;

    // Quando chegar a data
    if (diferenca <= 0) {
        window.location.href = "/verificar";
        return;
    }

    // Calcula os dias, horas, minutos e segundos
    const dias = Math.floor(diferenca / (1000 * 60 * 60 * 24));

    const horas = Math.floor(
        (diferenca % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
    );

    const minutos = Math.floor(
        (diferenca % (1000 * 60 * 60)) / (1000 * 60)
    );

    const segundos = Math.floor(
        (diferenca % (1000 * 60)) / 1000
    );

    // Exibe os valores na página
    document.getElementById("dias").innerText = String(dias).padStart(2, "0");

    document.getElementById("horas").innerText = String(horas).padStart(2, "0");

    document.getElementById("minutos").innerText = String(minutos).padStart(2, "0");

    document.getElementById("segundos").innerText = String(segundos).padStart(2, "0");
}

// Executa imediatamente
atualizarContagem();

// Atualiza a cada segundo
setInterval(atualizarContagem, 1000);
