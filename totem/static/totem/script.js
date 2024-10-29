const btnProsseguir = document.getElementById('btn-prosseguir');
const popup = document.getElementById('popup');
const tempoRestanteSpan = document.getElementById('tempo-restante');
const telaSuspensa = document.getElementById('telaSuspensa');
const telaMenu = document.getElementById('telaMenu');
// Variáveis para controlar a inatividade
let contadorInatividade;
let tempoInatividade = 5;  // Tempo máximo de inatividade
let tempoAviso = 2;        // Tempo para exibir o aviso
let tempoRestante = tempoInatividade;

// Função para iniciar a contagem de inatividade
function iniciarContadorInatividade() {
  contadorInatividade = setInterval(() => {
    tempoRestante--;

    // Exibe o tempo restante no console a cada segundo
    console.log(`Tempo restante para inatividade: ${tempoRestante} segundos`);

    // Mostra o popup quando restarem 10 segundos
    if (tempoRestante === tempoAviso) {
      popup.style.display = 'block';
      tempoRestanteSpan.textContent = tempoRestante;
    }

    // Atualiza o tempo restante no popup
    if (tempoRestante <= tempoAviso) {
      tempoRestanteSpan.textContent = tempoRestante;
    }

    // Volta para a tela de welcome quando o tempo acaba
    if (tempoRestante <= 0) {
      resetarInatividade();
    }
  }, 1000);
}

// Função para resetar a inatividade
function resetarInatividade() {
  clearInterval(contadorInatividade);
  tempoRestante = tempoInatividade;
  popup.style.display = 'none';
  telaSuspensa.style.display = 'block';
  telaMenu.style.display = 'none';
}

// Função para detectar qualquer interação do usuário
function resetarContador() {
  clearInterval(contadorInatividade); // Parar o contador atual
  tempoRestante = tempoInatividade;   // Resetar o tempo restante
  popup.style.display = 'none';       // Ocultar o popup, se visível
  iniciarContadorInatividade();       // Reiniciar o contador
}

// Mudar para a tela de compras e iniciar o contador de inatividade
btnProsseguir.addEventListener('click', () => {
  iniciarContadorInatividade();
});

// Reseta o contador ao detectar cliques ou teclas pressionadas na tela de compras
telaMenu.addEventListener('mousemove', resetarContador);
telaMenu.addEventListener('click', resetarContador);
telaMenu.addEventListener('keydown', resetarContador);

$('input').on('change', function() {
  $('body').toggleClass('blue');
});

