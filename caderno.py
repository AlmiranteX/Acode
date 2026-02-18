from customtkinter import *
import ast #para transforma str em dicionario

janela=CTk()

# Variaveis de configuracoes
cor_fundo_geral = "#272D3B"
cor_fundo_variado = "#252B38"
cor_sobras = "#2A3140"
cor_borda = "#4B4E54"
cor_fundo_escuro = "#0F1522"
cor_texto = "#D7DBE3"
cor_texto2 = "silver"


# Variaveis de dados
ponto_prova_var = StringVar(value="100")
qtd_atividade = StringVar(value="5")

questionario = None

# Texto de prompt:_________________________________________________________________________________________
prompt1 = f"Analise os PDFs enviados e gere uma atividade em formato de dicionário com {qtd_atividade} questões."
prompt2 = "Cada questões deve ter 5 alternativas, sendo uma correta e quatro incorretas."
prompt3 = "O resultado deve estar no seguinte formato:"
prompt4 = {
    "p1": "{",
    "p2": '"Questao_1": {',
    "p3": '"pergunta" : ' '"Texto pergunta",',
    "p4": '"resposta" : ["Resposta A", "Resposta B", "Resposta C", "Resposta D"],',
    "p5": '"Reposta_Correta" : "Reposta correta",',

    "p6": "}",
    "p7": '"Questao_2": {',
    "p8": '"pergunta" : ' '"Texto pergunta",',
    "p9": '"resposta" : ["Resposta A", "Resposta B", "Resposta C", "Resposta D"],',
    "p10": '"Reposta_Correta" : "Reposta correta",',
    "p11": '}',
    "p12": '}'
}

#__________________________________________________________________________________________________________





def config_janela():
    janela.geometry("1024x700")
    #janela.overrideredirect(True)
    janela.title("Caderno de Atividades")
    janela.config(background="white")
    janela.resizable(False, False)

config_janela()

home=CTkFrame(janela, width=1024, height=700,fg_color=cor_fundo_geral, bg_color=cor_fundo_geral)
home.place(relx=0.5, rely=0.5, anchor=CENTER)

def pagina_principal():

    #Nome da atividade
    atividade_name=CTkLabel(home, text="Nome da atividade:", text_color=cor_texto, font=("arial", 18, "italic"), bg_color="#272D3B")
    atividade_name.place(relx=0.07, rely=0.07)

    name_ativade=CTkEntry(home, width=150, height=25, border_width=1, fg_color=cor_fundo_escuro, bg_color="#272D3B", placeholder_text="Nome da atividade", text_color=cor_texto, border_color=cor_borda)
    name_ativade.place(relx=0.23, rely=0.074)

    #Quantidade de atividades
    quantidade_atividade=CTkLabel(home, text="N° de Questões:", text_color=cor_texto, font=("arial", 18, "italic"))
    quantidade_atividade.place(relx=0.42, rely=0.07)

    quantidade_atv=CTkComboBox(home, values=["5", "10", "15", "20", "25", "30"], state="readonly",\
        width=60, height=25, corner_radius=10,\
        fg_color=cor_fundo_escuro, text_color=cor_texto, border_color=cor_borda, border_width=0.2, \
        button_hover_color=cor_sobras, dropdown_hover_color="red", button_color=cor_fundo_escuro, dropdown_fg_color=cor_fundo_variado, dropdown_text_color=cor_texto,\
        bg_color=cor_fundo_geral, variable=qtd_atividade
            )
    quantidade_atv.place(relx=0.555, rely=0.074)


    #Valor ponto da prova
    pont_prova = CTkLabel(home, text="Ponto da Prova:", text_color=cor_texto, font=("arial", 18, "italic"), bg_color="#272D3B", )
    pont_prova.place(relx=0.71, rely=0.07)

    pont_pv = CTkEntry(home, width=80, height=24, placeholder_text="Pontuação", textvariable=ponto_prova_var, text_color=cor_texto, bg_color="#272D3B", fg_color=cor_fundo_escuro, border_color=cor_borda)
    pont_pv.place(relx=0.84, rely=0.074)

    #  @--VISUAL--/ Frame de fundo gerar prompt 01
    fundo_prompt=CTkFrame(home, width=900, height=450, border_width=1, bg_color=cor_fundo_geral, fg_color=cor_fundo_escuro, corner_radius=10,\
        border_color=cor_borda)
    fundo_prompt.place(relx=0.5, rely=0.45, anchor=CENTER)

    #Label texte gerar prompt para chatgpt
    gerar_label = CTkLabel(fundo_prompt, text="Gerar Prompt para ChatGpt:", text_color=cor_texto)
    gerar_label.place(relx=0.03, rely=0.02)

    #  @--VISUAL--/ Linha decorativa frame
    linha_frame =CTkFrame(fundo_prompt, width=850, height=1, fg_color=cor_borda, border_color=cor_borda, border_width=2)
    linha_frame.place(relx=0.03, rely=0.08)

    #  @--VISUAL--/ Frame de fundo
    fundo_frame=CTkFrame(fundo_prompt, width=400, height=350, border_width=1 ,corner_radius=10,\
        fg_color=cor_fundo_geral, border_color=cor_borda)
    fundo_frame.place(relx=0.25, rely=0.50, anchor=CENTER)

    #texto informativo do prompt dentro do elemento frame de fundo
    def Texto_prompt():
        #Atualizar quantidade de atividades
        prompt1 = f"Analise os PDFs enviados e gere uma atividade em formato de dicionário com {quantidade_atv.get()} questões."
        prompt_info1=CTkLabel(fundo_frame, text=prompt1, font=("arial", 9), \
            text_color=cor_texto2, bg_color=cor_fundo_geral)

        prompt_info2=CTkLabel(fundo_frame, text=prompt2, font=("arial", 9), \
            text_color=cor_texto2,  bg_color=cor_fundo_geral)

        prompt_info3=CTkLabel(fundo_frame, text=prompt3, font=("arial", 9), \
            text_color=cor_texto2,  bg_color=cor_fundo_geral)

        prompt_info1.place(relx=0.02, rely=0.03)
        prompt_info2.place(relx=0.02, rely=0.1)
        prompt_info3.place(relx=0.02, rely=0.17)

        # @--VISUAL--/ elemento Frame info do dicionario 
        caixa_frame_dic=CTkFrame(fundo_frame, width=380, height=240, \
        border_width=1, corner_radius=10, \
        fg_color=cor_fundo_geral, border_color=cor_borda       
        )
        caixa_frame_dic.place(relx=0.5, rely=0.6, anchor=CENTER)

        #Testo dento do elemento visual caixa_frame_dic____________________________________________________________________________
        dic_texto1=CTkLabel(caixa_frame_dic, text=prompt4["p1"], font=("arial", 9), text_color=cor_texto2, bg_color=cor_fundo_geral)
        dic_texto1.place(relx=0.02, rely=0.01)

        dic_texto2=CTkLabel(caixa_frame_dic, text=prompt4["p2"], font=("arial", 9), text_color=cor_texto2, bg_color=cor_fundo_geral)
        dic_texto2.place(relx=0.05, rely=0.07)

        dic_texto3=CTkLabel(caixa_frame_dic, text=prompt4["p3"], font=("arial", 9), text_color=cor_texto2, bg_color=cor_fundo_geral)
        dic_texto3.place(relx=0.1, rely=0.15)

        dic_texto4=CTkLabel(caixa_frame_dic, text=prompt4["p4"], font=("arial", 9), text_color=cor_texto2, bg_color=cor_fundo_geral)
        dic_texto4.place(relx=0.1, rely=0.23)

        dic_texto5=CTkLabel(caixa_frame_dic, text=prompt4["p5"], font=("arial", 9), text_color=cor_texto2, bg_color=cor_fundo_geral)
        dic_texto5.place(relx=0.1, rely=0.31)

        dic_texto6=CTkLabel(caixa_frame_dic, text=prompt4["p6"], font=("arial", 9), text_color=cor_texto2, bg_color=cor_fundo_geral)
        dic_texto6.place(relx=0.1, rely=0.39)

        dic_texto7=CTkLabel(caixa_frame_dic, text=prompt4["p7"], font=("arial", 9), text_color=cor_texto2, bg_color=cor_fundo_geral)
        dic_texto7.place(relx=0.05, rely=0.47)

        dic_texto8=CTkLabel(caixa_frame_dic, text=prompt4["p8"], font=("arial", 9), text_color=cor_texto2, bg_color=cor_fundo_geral)
        dic_texto8.place(relx=0.1, rely=0.55)

        dic_texto9=CTkLabel(caixa_frame_dic, text=prompt4["p9"], font=("arial", 9), text_color=cor_texto2, bg_color=cor_fundo_geral)
        dic_texto9.place(relx=0.1, rely=0.63)

        dic_texto10=CTkLabel(caixa_frame_dic, text=prompt4["p10"], font=("arial", 9), text_color=cor_texto2, bg_color=cor_fundo_geral)
        dic_texto10.place(relx=0.1, rely=0.71)

        dic_texto12=CTkLabel(caixa_frame_dic, text=prompt4["p11"], font=("arial", 9), text_color=cor_texto2, bg_color=cor_fundo_geral)
        dic_texto12.place(relx=0.1, rely=0.79)

        dic_texto13=CTkLabel(caixa_frame_dic, text=prompt4["p12"], font=("arial", 9), text_color=cor_texto2, bg_color=cor_fundo_geral)
        dic_texto13.place(relx=0.02, rely=0.87)
        #___________________________________________________________________________________________________________________________
    Texto_prompt()

    #  Area de colagem do dicionario
    colar_dic=CTkTextbox(fundo_prompt, width=400, height=350, border_width=1 ,corner_radius=10,\
        fg_color=cor_fundo_geral, border_color=cor_borda)
    colar_dic.place(relx=0.75, rely=0.50, anchor=CENTER)


    #  @--VISUAL--/ linha separadora Frame de fundo
    linha_vertical=CTkFrame(fundo_prompt, width=1, height=300, border_width=1, border_color=cor_borda, fg_color=cor_borda)
    linha_vertical.place(relx=0.5, rely=0.5, anchor=CENTER)

    #Colar dicionario de atividade na area textbox
    def colar_dicionario():
        #limpar a area Textbox
        colar_dic.delete("0.0", "end")

        #Colar Dicionario na area e passa para variavel
        colar_dic.insert("0.0", janela.clipboard_get())

    #Botao colar Prompt
    But_colar=CTkButton(fundo_prompt, text="Colar Diciónario", text_color=cor_texto, font=("arial", 20, "bold"), \
                        bg_color=cor_fundo_escuro, fg_color="#1A7640", border_color=cor_borda, border_width=1,\
                        height=10, \
                        border_spacing=1, hover_color="orange", command=colar_dicionario)
    But_colar.place(relx=0.65, rely=0.90)

    #Funcao para copiar prompt
    def copiar_prompt():
        #Chama def texto_promp() para atualisa dados na tela
        Texto_prompt()


        #Atualizar valor de atividades
        prompt1 = f"Analise os PDFs enviados e gere uma atividade em formato de dicionário com {quantidade_atv.get()} questões."
        adcional = "me der isso como dicionario, para min colar em um elemento CTkTextbox e torna em dicionario no programa py"
        prompt_pronto = (prompt1+prompt2+prompt3) + '\n{\n    "Questao 1" : {\n          "pergunta" : "Testo pergunta",\n          "resposta" : ["resposta A", "resposta B", "resposta C", "resposta D"],\n          "correta": "resposta correta"\n            }\n}\n ' + adcional

        #1 Limpar area de transferencia
        janela.clipboard_clear()

        #2 Adcionar texto a area de tranferencia
        janela.clipboard_append(prompt_pronto)

    #Botao copiar Prompt
    But_prompt=CTkButton(fundo_prompt, text="Copiar Prompt", text_color=cor_texto, font=("arial", 20, "bold"), \
                        bg_color=cor_fundo_escuro, fg_color="#474AEF", border_color=cor_borda, border_width=1,\
                        height=10, \
                        border_spacing=1, hover_color="red", command=copiar_prompt
                        )
    But_prompt.place(relx=0.15, rely=0.90)


    def cheque_condicoes():

        texto = colar_dic.get("0.0", "end").strip() # pega o texto do CTkTextbox
        questionario = ast.literal_eval(texto)  # converte str -> dict

        print(type(questionario))


    #Butao para gerar atividade
    But_iniciar=CTkButton(home, text="Iniciar Atividade", text_color=cor_fundo_escuro, width=50, height=50, fg_color="yellow", bg_color=cor_fundo_geral, \
            border_color=cor_fundo_escuro, border_width=1, corner_radius=10, font=("arial", 20, "bold"), command=cheque_condicoes)
    But_iniciar.place(relx=0.5, rely=0.85, anchor=CENTER) 



pagina_principal()


janela.mainloop()