import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pyautogui
import time


# Função para o teste PBM

def testa_pbm():
    log_evento("Iniciando Teste PBM")

    def acesso_ao_front_balcao():
        pyautogui.moveTo(x=641, y=446)
        pyautogui.click()
        pyautogui.write('', interval=0.1)
        pyautogui.press('enter')
        time.sleep(0.7)

    def pesquisa_medicamento():
        pyautogui.write('', interval=0.1)
        time.sleep(0.9)
        pyautogui.press('enter')
        time.sleep(0.9)
        time.sleep(1.0)

    def insere_medicamento():
        pyautogui.click()
        time.sleep(1.0)
        pyautogui.moveTo(x=1249, y=581)
        pyautogui.click()
        time.sleep(1.0)
        pyautogui.press('enter')
        time.sleep(1.0)
        time.sleep(1.0)
        pyautogui.press('enter')
        time.sleep(1.0)
        time.sleep(1.0)
        pyautogui.keyDown('alt')
        pyautogui.press('c')
        pyautogui.keyUp('alt')
        time.sleep(1.0)
        pyautogui.press('F4')

    acesso_ao_front_balcao()
    pesquisa_medicamento()
    insere_medicamento()

    log_evento("Finalizando Teste PBM")


# Função para o teste Farmácia Popular
def execute_correcao_erro():
    log_evento("Iniciando Teste Farmácia Popular")

    def logar_farmacia_popular():
        pyautogui.moveTo(x=278, y=148)
        pyautogui.click()
        pyautogui.moveTo(x=655, y=441)
        pyautogui.click()
        pyautogui.write('')
        time.sleep(0.9)
        pyautogui.press('enter')

    def pesquisar_sku_acessar_login():
        pyautogui.write('')
        pyautogui.press('enter')
        pyautogui.moveTo(x=582, y=591)
        pyautogui.click()
        pyautogui.moveTo(x=609, y=397)
        pyautogui.click()
        pyautogui.write('')
        pyautogui.press('tab')
        pyautogui.write('')
        pyautogui.press('enter')

    def preencher_dados_receita():
        pyautogui.moveTo(x=1217, y=360)
        pyautogui.click()
        pyautogui.moveTo(x=729, y=294)
        pyautogui.click()
        pyautogui.press('F1')
        pyautogui.moveTo(x=671, y=427)
        pyautogui.click()
        pyautogui.press('enter')
        pyautogui.press('enter')

    def preencher_dados_prescritor():
        pyautogui.press('F2')
        pyautogui.moveTo(x=424, y=610)
        pyautogui.click()
        pyautogui.moveTo(x=451, y=267)
        pyautogui.click()
        pyautogui.scroll(-200)
        pyautogui.moveTo(x=383, y=557)
        pyautogui.click()
        pyautogui.moveTo(x=535, y=603)
        pyautogui.click()
        pyautogui.write('', interval=0.1)
        pyautogui.press('enter')

    def preencher_dados_paciente():
        pyautogui.scroll(-1200)
        pyautogui.moveTo(x=865, y=393)
        pyautogui.click()
        pyautogui.press('F3')
        pyautogui.click()
        pyautogui.scroll(-1200)
        pyautogui.click()
        pyautogui.press('enter')

    def preencher_dados_produto():
        pyautogui.press('F4')
        pyautogui.click()
        pyautogui.scroll(-200)
        pyautogui.scroll(-200)
        pyautogui.moveTo(x=488, y=522)
        pyautogui.click()
        pyautogui.write('c')
        pyautogui.click()
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('F9')

    logar_farmacia_popular()
    pesquisar_sku_acessar_login()
    preencher_dados_receita()
    preencher_dados_prescritor()
    preencher_dados_paciente()
    preencher_dados_produto()

    log_evento("Finalizando Teste Farmácia Popular")


# Função para o acesso ao servidor
def inicia_servico():
    log_evento("Iniciando Acesso ao Servidor")

    pyautogui.PAUSE = 1.0
    pyautogui.hotkey('win', 'r')
    time.sleep(0.8)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(1.0)
    time.sleep(0.7)
    time.sleep(0.7)
    pyautogui.press('tab')
    pyautogui.keyDown('shift')
    pyautogui.write('')
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    pyautogui.write('***')
    pyautogui.keyUp('shift')
    pyautogui.write('')
    pyautogui.press('enter')

    log_evento("Finalizando Acesso ao Servidor")
    
    
    
def inicia_app():
    log_evento("Iniciando processo para travar a tela")
    
    pyautogui.PAUSE = 1.0
    pyautogui.alert("PROCESSANDO")
    while True:
        pyautogui.click()
        time.sleep(3)
        
    log_evento("Finaliza processo de travamento de tela")


# Função para abrir a janela de popup e executar o processo
def executar_processo(funcao_teste):
    # Minimize a janela principal
    root.iconify()

    # Cria uma nova janela popup
    popup = tk.Toplevel()
    popup.title("Executando Processo")
    popup.geometry("300x150")

    # Label na popup informando que o processo está sendo executado
    label = tk.Label(popup, text="Executando processo...", font=("Helvetica", 14))
    label.pack(pady=40)

    # Executa o processo após 1 segundo e fecha o popup
    popup.after(1000, lambda: [funcao_teste(), fechar_popup(popup)])


def fechar_popup(popup):
    popup.destroy()  # Fecha a janela popup
    root.deiconify()  # Restaura a janela principal


# Função para logar eventos na caixa de texto
def log_evento(mensagem):
    log_text.config(state=tk.NORMAL)  # Habilita a edição
    log_text.insert(tk.END, f"{mensagem}\n")  # Adiciona a mensagem ao log
    log_text.config(state=tk.DISABLED)  # Desabilita a edição para impedir o usuário de alterar


# Criando a interface gráfica
root = tk.Tk()
root.title("TESTE PYTHON DPSP")
root.geometry("800x600")

# Estilo para os botões
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)

# Emojis de engrenagem
gear_emoji = "\u2699"

# Frame para os botões na lateral esquerda
frame = tk.Frame(root, bg='#2b2b2b', width=200)
frame.pack(side='left', fill='y')

# Título no cabeçalho
header = tk.Label(root, text="AUTOMAÇÃO BALCÃO 2.0", bg='#0e6efd', fg='white', font=("Helvetica", 16))
header.pack(side='top', fill='x')

# Adicionando uma imagem na área branca
image_path = "Capturar.PNG"  # Nome do arquivo de imagem (que está na mesma pasta)
img = Image.open(image_path)  # Carrega a imagem usando o caminho especificado
img = img.resize((600, 400), Image.Resampling.LANCZOS)  # Redimensiona a imagem
photo = ImageTk.PhotoImage(img)

# Exibe a imagem abaixo do cabeçalho
image_label = tk.Label(root, image=photo)
image_label.pack(side='top', pady=20)  # Adiciona a imagem com espaçamento vertical

# Função para criar botões estilizados com emoji
def criar_botao(text, command):
    button_text = f"{gear_emoji} {text}"
    button = ttk.Button(frame, text=button_text, command=command, style="TButton")
    button.pack(pady=20, padx=20, anchor='w', fill='x')  # Para o botão ocupar a largura do frame
    return button


# Adicionando área de log de eventos
log_frame = tk.Frame(root, bg='white')
log_frame.pack(side='bottom', fill='x', pady=10)

log_label = tk.Label(log_frame, text="Log de Eventos:", font=("Helvetica", 12))
log_label.pack(anchor='w', padx=10)

log_text = tk.Text(log_frame, height=6, state=tk.DISABLED)
log_text.pack(fill='x', padx=10, pady=5)


# Botões para cada automação com emoji ⚙️ e função para executar o processo correspondente
btn_teste_pbm = criar_botao("Teste PBM", command=lambda: executar_processo(testa_pbm))
btn_teste_farmacia_popular = criar_botao("Teste Farmácia Popular", command=lambda: executar_processo(execute_correcao_erro))
btn_acesso_server = criar_botao("Acesso ao Servidor", command=lambda: executar_processo(inicia_servico))
btn_inicia_app = criar_botao("Manter tela ligada", command=lambda: executar_processo(inicia_app))

# Rodapé com informações do desenvolvedor
footer = tk.Label(root, text="Desenvolvido por Caio Pixu", bg='#2b2b2b', fg='white', font=("Helvetica", 10))
footer.pack(side='bottom', fill='x')

# Rodando a interface gráfica
root.mainloop()
