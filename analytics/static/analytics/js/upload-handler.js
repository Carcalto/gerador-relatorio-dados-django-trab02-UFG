// Atualiza o nome do arquivo selecionado
document.getElementById('file').addEventListener('change', function() {
    const fileName = this.files[0]?.name || 'Nenhum arquivo selecionado';
    document.getElementById('fileName').textContent = fileName;
});

// Gerencia o upload e a barra de progresso
document.getElementById('uploadForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    const progressWrapper = document.getElementById('progressWrapper');
    const progressBar = document.querySelector('.progress-bar');
    const progressText = document.querySelector('.progress-text');
    
    progressWrapper.style.display = 'block';
    let progress = 0;
    
    // Simula o progresso enquanto processa
    const interval = setInterval(() => {
        if (progress < 90) {
            progress += Math.random() * 10;
            progress = Math.min(progress, 90);
            updateProgress(progress);
        }
    }, 500);

    fetch('', {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => response.text())
    .then(html => {
        clearInterval(interval);
        progress = 100;
        updateProgress(progress);
        
        setTimeout(() => {
            document.documentElement.innerHTML = html;
        }, 500);
    })
    .catch(error => {
        clearInterval(interval);
        console.error('Erro:', error);
        progressWrapper.style.display = 'none';
        alert('Erro ao processar o arquivo. Por favor, tente novamente.');
    });
});

// Função para atualizar a barra de progresso
function updateProgress(progress) {
    const progressBar = document.querySelector('.progress-bar');
    const progressText = document.querySelector('.progress-text');
    const roundedProgress = Math.round(progress);
    
    progressBar.style.width = roundedProgress + '%';
    progressText.textContent = roundedProgress + '%';
}