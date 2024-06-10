function getData() {
    const now = new Date();
    const datas = {
        dia: 'numeric',
        mes: 'long',
        ano: 'numeric',
    };
    return now.toLocaleDateString('en-US', datas);
}

function getTempo() {
    const now = new Date();
    const tempos = {
        hora: '2-digit',
        minutos: '2-digit',
        segundos: '2-digit',
    };
    return now.toLocaleTimeString('en-US', tempos);
}

function updateDataTempo() {
    const dataString = getData();
    const tempoString = getTempo();
    document.getElementById('data').textContent = dataString;
    document.getElementById('tempo').textContent = tempoString;
}

updateDataTempo();

setInterval(updateDataTempo, 1000);

window.onload = function() {
    updateDataTempo();
};


document.addEventListener('DOMContentLoaded', (event) => {
    const toggleButton = document.getElementById('toggle-mode');
    const body = document.body;

    // Verificar se há um modo salvo no localStorage
    const savedMode = localStorage.getItem('theme');
    if (savedMode) {
        body.classList.add(savedMode);
    } else {
        body.classList.add('light-mode'); // Padrão é o modo claro
    }

    toggleButton.addEventListener('click', () => {
        if (body.classList.contains('light-mode')) {
            body.classList.remove('light-mode');
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark-mode');
        } else {
            body.classList.remove('dark-mode');
            body.classList.add('light-mode');
            localStorage.setItem('theme', 'light-mode');
        }
    });
});