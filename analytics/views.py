import markdown
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.conf import settings
import os
from .services import process_csv
from django.http import HttpResponse

def home(request):
    analysis_result = None
    if request.method == 'POST' and request.FILES['file']:
        # Verifica se é uma requisição AJAX
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        # Salva o arquivo enviado pelo usuário
        file = request.FILES['file']
        file_path = default_storage.save(file.name, file)
        
        # Obtém o caminho absoluto do arquivo
        absolute_file_path = os.path.join(settings.MEDIA_ROOT, file_path)
        print(f"Caminho absoluto do arquivo: {absolute_file_path}")
        
        try:
            # Processa o CSV e obtém a análise
            analysis_result = process_csv(absolute_file_path)
            
            # Converte o Markdown em HTML
            analysis_result_html = markdown.markdown(analysis_result)
            
            # Apaga o arquivo CSV após o processamento
            if os.path.exists(absolute_file_path):
                os.remove(absolute_file_path)
                print(f"Arquivo CSV removido: {absolute_file_path}")
            
            context = {'analysis_result': analysis_result_html}
            
            # Se for AJAX, renderiza apenas o conteúdo
            if is_ajax:
                return render(request, 'analytics/base.html', context)
            return render(request, 'analytics/base.html', context)
            
        except Exception as e:
            print(f"Erro durante o processamento: {str(e)}")
            # Garante que o arquivo seja removido mesmo em caso de erro
            if os.path.exists(absolute_file_path):
                os.remove(absolute_file_path)
                print(f"Arquivo CSV removido após erro: {absolute_file_path}")
            
            context = {'error': str(e)}
            if is_ajax:
                return render(request, 'analytics/base.html', context)
            return render(request, 'analytics/base.html', context)
    
    # Renderiza a página inicial
    return render(request, 'analytics/base.html', {'analysis_result': None})