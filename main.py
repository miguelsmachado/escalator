import streamlit as st
from datetime import datetime, date, timedelta
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    # BACKEND

    st.set_option('deprecation.showPyplotGlobalUse', False)

    medico_de_dia = pd.read_csv("medico.csv", sep=";")
    pd.to_datetime(medico_de_dia.ultimo_sv_preta, format='%Y-%m-%d')
    pd.to_datetime(medico_de_dia.ultimo_sv_vermelha, format='%Y-%m-%d')
    pd.to_datetime(medico_de_dia.ultimo_sv_roxa, format='%Y-%m-%d')

    enfermeiro_de_dia = pd.read_csv("enfermeiro.csv", sep=";")
    pd.to_datetime(enfermeiro_de_dia.ultimo_sv, format='%Y-%m-%d')

    supervisor_de_dia = pd.read_csv("supervisor.csv", sep=";")
    pd.to_datetime(supervisor_de_dia.ultimo_sv, format='%Y-%m-%d')

    medico_sv_preta = pd.read_csv("medico_sv_preta.csv", sep=";")
    pd.to_datetime(medico_sv_preta.data, format='%Y-%m-%d')
    medico_sv_vermelha = pd.read_csv("medico_sv_vermelha.csv", sep=";")
    pd.to_datetime(medico_sv_vermelha.data, format='%Y-%m-%d')
    medico_sv_roxa = pd.read_csv("medico_sv_roxa.csv", sep=";")
    pd.to_datetime(medico_sv_roxa.data, format='%Y-%m-%d')

    enfermeiro_sv = pd.read_csv("enfermeiro_sv.csv", sep=";")
    pd.to_datetime(enfermeiro_sv.data, format='%Y-%m-%d')

    supervisor_sv = pd.read_csv("supervisor_sv.csv", sep=";")
    pd.to_datetime(supervisor_sv.data, format='%Y-%m-%d')

    class Pessoa:
        def __init__(self, posto, nome, ultimo_sv_preta, ultimo_sv_vermelha, ultimo_sv_roxa):
            self.posto = posto
            self.nome = nome
            self.ultimo_sv_preta = ultimo_sv_preta
            self.ultimo_sv_vermelha = ultimo_sv_vermelha
            self.ultimo_sv_roxa = ultimo_sv_roxa
            self.folga_preta = 0
            self.folga_vermelha = 0
            self.folga_roxa = 0
            self.pronto = 1
            if posto == 'Cel':
                self.antiguidade = 0
            elif posto == 'TC':
                self.antiguidade = 1
            elif posto == 'Maj':
                self.antiguidade = 2
            elif posto == 'Cap':
                self.antiguidade = 3
            elif posto == '1ºTen':
                self.antiguidade = 4
            elif posto == '2ºTen':
                self.antiguidade = 5
            elif posto == 'Asp':
                self.antiguidade = 6
            elif posto == 'ST':
                self.antiguidade = 7
            elif posto == '1ºSgt':
                self.antiguidade = 8
            elif posto == '2ºSgt':
                self.antiguidade = 9
            elif posto == '3ºSgt':
                self.antiguidade = 10
            elif posto == 'Cb':
                self.antiguidade = 11
            elif posto == 'Sd':
                self.antiguidade = 12

        def atualizar(self):
            self.folga_preta = date.today().toordinal() - self.ultimo_sv_preat.toordinal()
            self.folga_vermelha = date.today().toordinal() - self.ultimo_sv_vermelha.toordinal()
            self.folga_roxa = date.today().toordinal() - self.ultimo_sv_roxa.toordinal()

    def atualizar_folgas(df):
        for i in range(df.shape[0]):
            df.folga_preta.iloc[i] = date.today().toordinal() - df.ultimo_sv_preta.iloc[i].toordinal()
            df.folga_vermelha.iloc[i] = date.today().toordinal() - df.ultimo_sv_vermelha.iloc[i].toordinal()
            df.folga_roxa.iloc[i] = date.today().toordinal() - df.ultimo_sv_roxa.iloc[i].toordinal()

    # lendo df
    medico_de_dia = pd.read_csv("medico.csv", sep=";")
    pd.to_datetime(medico_de_dia.ultimo_sv_preta, format='%Y-%m-%d')
    pd.to_datetime(medico_de_dia.ultimo_sv_vermelha, format='%Y-%m-%d')
    pd.to_datetime(medico_de_dia.ultimo_sv_roxa, format='%Y-%m-%d')

    enfermeiro_de_dia = pd.read_csv("enfermeiro.csv", sep=";")
    # pd.to_datetime(enfermeiro_de_dia.ultimo_sv_preta, format='%Y-%m-%d')
    # pd.to_datetime(enfermeiro_de_dia.ultimo_sv_vermelha, format='%Y-%m-%d')
    # pd.to_datetime(enfermeiro_de_dia.ultimo_sv_roxa, format='%Y-%m-%d')

    supervisor_de_dia = pd.read_csv("supervisor.csv", sep=";")
    # pd.to_datetime(supervisor_de_dia.ultimo_sv_preta, format='%Y-%m-%d')
    # pd.to_datetime(supervisor_de_dia.ultimo_sv_vermelha, format='%Y-%m-%d')
    # pd.to_datetime(supervisor_de_dia.ultimo_sv_roxa, format='%Y-%m-%d')

    # exportando df
    # medico_de_dia.to_csv("medico.csv", sep=";", index=False)
    # supervisor_de_dia.to_csv("supervisor.csv", sep=";", index=False)
    # enfermeiro_de_dia.to_csv("enfermeiro.csv", sep=";", index=False)

    # ---------------------------------------------------------------------------------------------------------------#

    # ---------------------------------------------------------------------------------------------------------------#
    st.title("Escala de serviço do Posto Médico da Guarnição de Goiânia")
    st.markdown("Desenvolvido por *Miguel S. Machado*")
    st.markdown("")
    st.markdown("___")

    # Incluíndo militar no sistema
    st.header("**Incluindo Militar:**")
    st.markdown("")

    escala = st.selectbox("Selecione qual escala o militar será incluído: ", ['Médico de dia', 'Enfermeiro de dia',
                                                                              'Supervisor de dia'])

    posto = st.selectbox("Selecione o posto: ", ['Cel', 'TC', 'Maj', 'Cap', '1ºTen', '2ºTen', 'Asp', 'ST', '1ºSgt',
                                                 '2ºSgt', '3ºSgt', 'Cb', 'Sd'])
    nome = st.text_input('Digite o nome:')
    if not st.checkbox('Militar recém chegado'):
        ultimo_sv_preta = st.date_input('Informe a data do último serviço na escala preta:', datetime.today())
        ultimo_sv_vermelha = st.date_input('Informe a data do último serviço na escala vermalha:', datetime.today())
        ultimo_sv_roxa = st.date_input('Informe a data do último serviço na escala roxa:', datetime.today())
    else:
        ultimo_sv_preta = datetime.strptime("1/1/2000", "%d/%m/%Y").date()
        ultimo_sv_vermelha = datetime.strptime("1/1/2000", "%d/%m/%Y").date()
        ultimo_sv_roxa = datetime.strptime("1/1/2000", "%d/%m/%Y").date()

    if st.button('Incluir'):
        # Recebendo os dados dos campos
        militar = Pessoa(str(posto), str(nome), ultimo_sv_preta, ultimo_sv_vermelha, ultimo_sv_roxa)
        # Atualizando a folga do militar
        militar.folga_preta = date.today().toordinal() - militar.ultimo_sv_preta.toordinal()
        militar.folga_vermelha = date.today().toordinal() - militar.ultimo_sv_vermelha.toordinal()
        militar.folga_roxa = date.today().toordinal() - militar.ultimo_sv_roxa.toordinal()
        # Ajustando tudo em um df
        mil_df = pd.DataFrame([militar.posto, militar.nome, militar.ultimo_sv_preta, militar.folga_preta,
                               militar.ultimo_sv_vermelha, militar.folga_vermelha, militar.ultimo_sv_roxa,
                               militar.folga_roxa, militar.pronto, militar.antiguidade]).transpose()
        mil_df.columns = ['posto', 'nome', 'ultimo_sv_preta', 'folga_preta', 'ultimo_sv_vermelha', 'folga_vermelha',
                          'ultimo_sv_roxa', 'folga_roxa', 'pronto', 'antiguidade']

        # Incluindo no df geral
        if escala == 'Médico de dia':
            medico_de_dia = pd.concat([medico_de_dia, mil_df])
            # Exportando o documento e relendo-o
            medico_de_dia.to_csv("medico.csv", sep=";", index=False)
            medico_de_dia = pd.read_csv("medico.csv", sep=";")
            pd.to_datetime(medico_de_dia.ultimo_sv_preta, format='%Y-%m-%d')
            pd.to_datetime(medico_de_dia.ultimo_sv_vermelha, format='%Y-%m-%d')
            pd.to_datetime(medico_de_dia.ultimo_sv_roxa, format='%Y-%m-%d')
        elif escala == 'Enfermeiro de dia':
            enfermeiro_de_dia = pd.concat([enfermeiro_de_dia, mil_df])
            # Exportando o documento e relendo-o
            enfermeiro_de_dia.to_csv("enfermeiro.csv", sep=";", index=False)
            enfermeiro_de_dia = pd.read_csv("enfermeiro.csv", sep=";")
            pd.to_datetime(enfermeiro_de_dia.ultimo_sv, format='%Y-%m-%d')
        elif escala == 'Supervisor de dia':
            supervisor_de_dia = pd.concat([supervisor_de_dia, mil_df])
            # Exportando o documento e relendo-o
            supervisor_de_dia.to_csv("supervisor.csv", sep=";", index=False)
            supervisor_de_dia = pd.read_csv("supervisor.csv", sep=";")
            pd.to_datetime(supervisor_de_dia.ultimo_sv, format='%Y-%m-%d')

    # ---------------------------------------------------------------------------------------------------------------#
    # Atualizando folgas
    # if st.button('Atualizar folgas'):
    #     # Lendo os dataframe e já com ajustando as datas para datetime
    #     medico_de_dia = pd.read_csv("medico.csv", sep=";")
    #     enfermeiro_de_dia = pd.read_csv("enfermeiro.csv", sep=";")
    #     supervisor_de_dia = pd.read_csv("supervisor.csv", sep=";")
    #
    #     medico_de_dia.ultimo_sv = pd.to_datetime(medico_de_dia.ultimo_sv, format='%Y-%m-%d')
    #     enfermeiro_de_dia.ultimo_sv = pd.to_datetime(enfermeiro_de_dia.ultimo_sv, format='%Y-%m-%d')
    #     supervisor_de_dia.ultimo_sv = pd.to_datetime(supervisor_de_dia.ultimo_sv, format='%Y-%m-%d')
    #     # atualizando todas as folgas
    #     atualizar_folgas(medico_de_dia)
    #     atualizar_folgas(enfermeiro_de_dia)
    #     atualizar_folgas(supervisor_de_dia)
    #     # Exportando dataframes pronto
    #     medico_de_dia.to_csv("medico.csv", sep=";", index=False)
    #     supervisor_de_dia.to_csv("supervisor.csv", sep=";", index=False)
    #     enfermeiro_de_dia.to_csv("enfermeiro.csv", sep=";", index=False)
    #
    # st.markdown("___")
    # ---------------------------------------------------------------------------------------------------------------#

    # Alterando Pronto/nPronto
    st.header("**Alterando situção do militar:**")
    st.markdown("")

    escala_p_np = st.selectbox("Selecione a escala do militar: ", ['Médico de dia', 'Enfermeiro de dia',
                                                                              'Supervisor de dia'], key='01')

    if escala_p_np == 'Médico de dia':
        nome_p_np = st.selectbox("Selecione o nome do militar: ", medico_de_dia.nome.to_list(), key='02')
    elif escala_p_np == 'Enfermeiro de dia':
        nome_p_np = st.selectbox("Selecione o nome do militar: ", enfermeiro_de_dia.nome.to_list(), key='03')
    elif escala_p_np == 'Supervisor de dia':
        nome_p_np = st.selectbox("Selecione o nome do militar: ", supervisor_de_dia.nome.to_list(), key='04')

    pergunta_p_np = st.radio("O militar está pronto para o serviço? ", ("Sim", "Não"))

    if st.button('Alterar Situação'):
        if pergunta_p_np == 'Sim':
            if escala_p_np == 'Médico de dia':
                medico_de_dia.loc[medico_de_dia.nome == nome_p_np, "pronto"] = 1
                medico_de_dia.to_csv("medico.csv", sep=";", index=False)
            elif escala_p_np == 'Enfermeiro de dia':
                enfermeiro_de_dia.loc[enfermeiro_de_dia.nome == nome_p_np, "pronto"] = 1
                medico_de_dia.to_csv("enfermeiro.csv", sep=";", index=False)
            elif escala_p_np == 'Supervisor de dia':
                supervisor_de_dia.loc[supervisor_de_dia.nome == nome_p_np, "pronto"] = 1
                supervisor_de_dia.to_csv("supervisor.csv", sep=";", index=False)
        elif pergunta_p_np == 'Não':
            if escala_p_np == 'Médico de dia':
                medico_de_dia.loc[medico_de_dia.nome == nome_p_np, "pronto"] = 0
                medico_de_dia.to_csv("medico.csv", sep=";", index=False)
            elif escala_p_np == 'Enfermeiro de dia':
                enfermeiro_de_dia.loc[enfermeiro_de_dia.nome == nome_p_np, "pronto"] = 0
                medico_de_dia.to_csv("enfermeiro.csv", sep=";", index=False)
            elif escala_p_np == 'Supervisor de dia':
                supervisor_de_dia.loc[supervisor_de_dia.nome == nome_p_np, "pronto"] = 0
                supervisor_de_dia.to_csv("supervisor.csv", sep=";", index=False)

    # ---------------------------------------------------------------------------------------------------------------#

    # Exibindo Previsões
    st.header("**Exibindo Previsões:**")
    st.markdown("")

    escala_previsoes = st.selectbox("Selecione a escala desejada: ", ['Médico de dia', 'Enfermeiro de dia',
                                                                   'Supervisor de dia'], key='05')

    tipo_previsoes = st.selectbox("Selecione o tipo de escala: ", ['Preta', 'Vermelha',
                                                                              'Roxa'], key='11')

    nr_previsoes = st.slider('Escolha o número de previsões:', min_value=1, max_value=31, value=1)

    # ---------------------------------------------------------------------------------------------------------------#
    # Atualizando folgas
    if st.button('Atualizar folgas'):
        # Lendo os dataframe e já com ajustando as datas para datetime
        medico_de_dia = pd.read_csv("medico.csv", sep=";")
        enfermeiro_de_dia = pd.read_csv("enfermeiro.csv", sep=";")
        supervisor_de_dia = pd.read_csv("supervisor.csv", sep=";")

        medico_de_dia.ultimo_sv_preta = pd.to_datetime(medico_de_dia.ultimo_sv_preta, format='%Y-%m-%d')
        medico_de_dia.ultimo_sv_vermelha = pd.to_datetime(medico_de_dia.ultimo_sv_vermelha, format='%Y-%m-%d')
        medico_de_dia.ultimo_sv_roxa = pd.to_datetime(medico_de_dia.ultimo_sv_roxa, format='%Y-%m-%d')

        enfermeiro_de_dia.ultimo_sv = pd.to_datetime(enfermeiro_de_dia.ultimo_sv, format='%Y-%m-%d')
        supervisor_de_dia.ultimo_sv = pd.to_datetime(supervisor_de_dia.ultimo_sv, format='%Y-%m-%d')
        # atualizando todas as folgas
        atualizar_folgas(medico_de_dia)
        atualizar_folgas(enfermeiro_de_dia)
        atualizar_folgas(supervisor_de_dia)
        # Exportando dataframes pronto
        medico_de_dia.to_csv("medico.csv", sep=";", index=False)
        supervisor_de_dia.to_csv("supervisor.csv", sep=";", index=False)
        enfermeiro_de_dia.to_csv("enfermeiro.csv", sep=";", index=False)
    # ---------------------------------------------------------------------------------------------------------------#

    if st.button('Gerar Previsões'):
        medico_de_dia = pd.read_csv("medico.csv", sep=";")
        pd.to_datetime(medico_de_dia.ultimo_sv_preta, format='%Y-%m-%d')
        pd.to_datetime(medico_de_dia.ultimo_sv_vermelha, format='%Y-%m-%d')
        pd.to_datetime(medico_de_dia.ultimo_sv_roxa, format='%Y-%m-%d')

        enfermeiro_de_dia = pd.read_csv("enfermeiro.csv", sep=";")
        pd.to_datetime(enfermeiro_de_dia.ultimo_sv, format='%Y-%m-%d')

        supervisor_de_dia = pd.read_csv("supervisor.csv", sep=";")
        pd.to_datetime(supervisor_de_dia.ultimo_sv, format='%Y-%m-%d')

        if escala_previsoes == 'Médico de dia':
            if nr_previsoes > medico_de_dia.shape[0]:
                if tipo_previsoes == 'Preta':
                    st.table(medico_de_dia[medico_de_dia.pronto == 1].sort_values(by="folga_preta",
                                                                                  ascending=False)[['posto', 'nome',
                                                                                                'ultimo_sv_preta',
                                                                                                'folga_preta']])
                elif tipo_previsoes == 'Vermelha':
                    st.table(medico_de_dia[medico_de_dia.pronto == 1].sort_values(by="folga_vermelha",
                                                                                  ascending=False)[['posto', 'nome',
                                                                                                    'ultimo_sv_vermelha',
                                                                                                    'folga_vermelha']])
                elif tipo_previsoes == 'Roxa':
                    st.table(medico_de_dia[medico_de_dia.pronto == 1].sort_values(by="folga_roxa",
                                                                                  ascending=False)[['posto', 'nome',
                                                                                                    'ultimo_sv_roxa',
                                                                                                    'folga_roxa']])
            else:
                if tipo_previsoes == 'Preta':
                    st.table(medico_de_dia[medico_de_dia.pronto == 1].sort_values(by="folga_preta",
                                                                                  ascending=False)[['posto', 'nome',
                                                                                                    'ultimo_sv_preta',
                                                                                                    'folga_preta']].head(nr_previsoes))
                elif tipo_previsoes == 'Vermelha':
                    st.table(medico_de_dia[medico_de_dia.pronto == 1].sort_values(by="folga_vermelha",
                                                                                  ascending=False)[['posto', 'nome',
                                                                                                    'ultimo_sv_vermelha',
                                                                                                    'folga_vermelha']].head(nr_previsoes))
                elif tipo_previsoes == 'Roxa':
                    st.table(medico_de_dia[medico_de_dia.pronto == 1].sort_values(by="folga_roxa",
                                                                                  ascending=False)[['posto', 'nome',
                                                                                                    'ultimo_sv_roxa',
                                                                                                    'folga_roxa']].head(nr_previsoes))
        if escala_previsoes == 'Enfermeiro de dia':
            if nr_previsoes > enfermeiro_de_dia.shape[0]:
                st.table(enfermeiro_de_dia[enfermeiro_de_dia.pronto == 1].sort_values(by="folga",
                                                                                      ascending=False)[['posto', 'nome',
                                                                                                      'ultimo_sv',
                                                                                                      'folga']])
            else:
                st.table(enfermeiro_de_dia[enfermeiro_de_dia.pronto == 1].sort_values(by="folga",
                                                                                      ascending=False)[['posto',
                                                                                                        'nome',
                                                                                                        'ultimo_sv',
                                                                                                        'folga']].head(nr_previsoes))
        if escala_previsoes == 'Supervisor de dia':
            if nr_previsoes > supervisor_de_dia.shape[0]:
                st.table(supervisor_de_dia[supervisor_de_dia.pronto == 1].sort_values(by="folga",
                                                                              ascending=False)[['posto', 'nome',
                                                                                                'ultimo_sv', 'folga']])
            else:
                st.table(supervisor_de_dia[supervisor_de_dia.pronto == 1].sort_values(by="folga",
                                                                              ascending=False)[['posto',
                                                                                                'nome',
                                                                                                'ultimo_sv',
                                                                                                'folga']].head(nr_previsoes))
    # ---------------------------------------------------------------------------------------------------------------#

    # Escalando Militar
    st.header("**Escalando Militar:**")
    st.markdown("")

    escala_escalar = st.selectbox("Selecione a escala do militar: ", ['Médico de dia', 'Enfermeiro de dia',
                                                                              'Supervisor de dia'], key='21')

    if escala_escalar == 'Médico de dia':
        nome_p_np = st.selectbox("Selecione o nome do militar: ", medico_de_dia[medico_de_dia.pronto == 1].nome.to_list(), key='11')
    elif escala_escalar == 'Enfermeiro de dia':
        nome_p_np = st.selectbox("Selecione o nome do militar: ", enfermeiro_de_dia[enfermeiro_de_dia.pronto == 1].nome.to_list(), key='12')
    elif escala_escalar == 'Supervisor de dia':
        nome_p_np = st.selectbox("Selecione o nome do militar: ", supervisor_de_dia[enfermeiro_de_dia.pronto == 1].nome.to_list(), key='13')

    data_escala = st.date_input('Selecione uma data para escalar o militar:', datetime.today())

    check_roxa = st.checkbox("Escala Roxa?")

    if st.button("Verificar disponibilidade"):

        data_escala_ordinal = data_escala.toordinal()
        sv_preta = datetime.strptime(medico_de_dia.loc[medico_de_dia.nome == nome_p_np, "ultimo_sv_preta"].tolist()[0], '%Y-%m-%d')
        sv_vermelha = datetime.strptime(medico_de_dia.loc[medico_de_dia.nome == nome_p_np, "ultimo_sv_vermelha"].tolist()[0], '%Y-%m-%d')
        sv_roxa = datetime.strptime(medico_de_dia.loc[medico_de_dia.nome == nome_p_np, "ultimo_sv_roxa"].tolist()[0], '%Y-%m-%d')
        check1 = abs(data_escala_ordinal - sv_preta.toordinal()) <= 2
        check2 = abs(data_escala_ordinal - sv_vermelha.toordinal()) <= 2
        check3 = abs(data_escala_ordinal - sv_roxa.toordinal()) <= 2

        if check1 or check2 or check3:
            st.markdown("### **O tempo de descanso do militar NÃO esta sendo respeitado**")
            if check1:
                st.write("Problema na escala preta")
            elif check2:
                st.write("Problema na escala vermelha")
            elif check2:
                st.write("Problema na escala roxa")
        else:
            st.write("Militar em condições de tirar o serviço")


    if st.button('Escalar'):
        if not check_roxa:
            if escala_escalar == 'Médico de dia':
                if data_escala.weekday() < 5:
                    medico_de_dia.loc[medico_de_dia.nome == nome_p_np, "ultimo_sv_preta"] = data_escala
                    medico_de_dia.to_csv("medico.csv", sep=";", index=False)

                    # Incluindo no banco de dados geral
                    escalado_df = medico_de_dia[medico_de_dia.nome == nome_p_np][['ultimo_sv_preta', 'posto', 'nome']]
                    escalado_df.columns = ['data', 'posto', 'nome']
                    medico_sv_preta = pd.concat([medico_sv_preta, escalado_df])

                    # Exportando o documento e relendo-o
                    medico_sv_preta.to_csv("medico_sv_preta.csv", sep=";", index=False)
                    medico_sv_preta = pd.read_csv("medico_sv_preta.csv", sep=";")
                    pd.to_datetime(medico_sv_preta.data, format='%Y-%m-%d')
                else:
                    medico_de_dia.loc[medico_de_dia.nome == nome_p_np, "ultimo_sv_vermelha"] = data_escala
                    medico_de_dia.to_csv("medico.csv", sep=";", index=False)

                    # Incluindo no banco de dados geral
                    escalado_df = medico_de_dia[medico_de_dia.nome == nome_p_np][['ultimo_sv_vermelha', 'posto', 'nome']]
                    escalado_df.columns = ['data', 'posto', 'nome']
                    medico_sv_vermelha = pd.concat([medico_sv_vermelha, escalado_df])

                    # Exportando o documento e relendo-o
                    medico_sv_vermelha.to_csv("medico_sv_vermelha.csv", sep=";", index=False)
                    medico_sv_vermelha = pd.read_csv("medico_sv_vermelha.csv", sep=";")
                    pd.to_datetime(medico_sv_vermelha.data, format='%Y-%m-%d')

            elif escala_escalar == 'Enfermeiro de dia':
                enfermeiro_de_dia.loc[enfermeiro_de_dia.nome == nome_p_np, "ultimo_sv"] = date.fromordinal(date.today().toordinal() + 1)
                enfermeiro_de_dia.to_csv("enfermeiro.csv", sep=";", index=False)

                # Incluindo no banco de dados geral
                escalado_df = enfermeiro_de_dia[enfermeiro_de_dia.nome == nome_p_np][['ultimo_sv', 'posto', 'nome']]
                escalado_df.columns = ['data', 'posto', 'nome']
                enfermeiro_sv = pd.concat([enfermeiro_sv, escalado_df])

                # Exportando o documento e relendo-o
                enfermeiro_sv.to_csv("enfermeiro_sv.csv", sep=";", index=False)
                enfermeiro_sv = pd.read_csv("enfermeiro_sv.csv", sep=";")
                pd.to_datetime(enfermeiro_sv.data, format='%Y-%m-%d')

            elif escala_escalar == 'Supervisor de dia':
                supervisor_de_dia.loc[supervisor_de_dia.nome == nome_p_np, "ultimo_sv"] = date.fromordinal(date.today().toordinal() + 1)
                supervisor_de_dia.to_csv("supervisor.csv", sep=";", index=False)

                # Incluindo no banco de dados geral
                escalado_df = supervisor_de_dia[supervisor_de_dia.nome == nome_p_np][['ultimo_sv', 'posto', 'nome']]
                escalado_df.columns = ['data', 'posto', 'nome']
                supervisor_sv = pd.concat([supervisor_sv, escalado_df])

                # Exportando o documento e relendo-o
                supervisor_sv.to_csv("supervisor_sv.csv", sep=";", index=False)
                supervisor_sv = pd.read_csv("supervisor_sv.csv", sep=";")
                pd.to_datetime(supervisor_sv.data, format='%Y-%m-%d')

        else:
            if escala_escalar == 'Médico de dia':
                medico_de_dia.loc[medico_de_dia.nome == nome_p_np, "ultimo_sv_roxa"] = data_escala
                medico_de_dia.to_csv("medico.csv", sep=";", index=False)

                # Incluindo no banco de dados geral
                escalado_df = medico_de_dia[medico_de_dia.nome == nome_p_np][['ultimo_sv_roxa', 'posto', 'nome']]
                escalado_df.columns = ['data', 'posto', 'nome']
                medico_sv_roxa = pd.concat([medico_sv_roxa, escalado_df])

                # Exportando o documento e relendo-o
                medico_sv_roxa.to_csv("medico_sv_roxa.csv", sep=";", index=False)
                medico_sv_roxa = pd.read_csv("medico_sv_roxa.csv", sep=";")
                pd.to_datetime(medico_sv_roxa.data, format='%Y-%m-%d')

            elif escala_escalar == 'Enfermeiro de dia':
                enfermeiro_de_dia.loc[enfermeiro_de_dia.nome == nome_p_np, "ultimo_sv"] = date.fromordinal(date.today().toordinal() + 1)
                enfermeiro_de_dia.to_csv("enfermeiro.csv", sep=";", index=False)

                # Incluindo no banco de dados geral
                escalado_df = enfermeiro_de_dia[enfermeiro_de_dia.nome == nome_p_np][['ultimo_sv', 'posto', 'nome']]
                escalado_df.columns = ['data', 'posto', 'nome']
                enfermeiro_sv = pd.concat([enfermeiro_sv, escalado_df])

                # Exportando o documento e relendo-o
                enfermeiro_sv.to_csv("enfermeiro_sv.csv", sep=";", index=False)
                enfermeiro_sv = pd.read_csv("enfermeiro_sv.csv", sep=";")
                pd.to_datetime(enfermeiro_sv.data, format='%Y-%m-%d')

            elif escala_escalar == 'Supervisor de dia':
                supervisor_de_dia.loc[supervisor_de_dia.nome == nome_p_np, "ultimo_sv"] = date.fromordinal(date.today().toordinal() + 1)
                supervisor_de_dia.to_csv("supervisor.csv", sep=";", index=False)

                # Incluindo no banco de dados geral
                escalado_df = supervisor_de_dia[supervisor_de_dia.nome == nome_p_np][['ultimo_sv', 'posto', 'nome']]
                escalado_df.columns = ['data', 'posto', 'nome']
                supervisor_sv = pd.concat([supervisor_sv, escalado_df])

                # Exportando o documento e relendo-o
                supervisor_sv.to_csv("supervisor_sv.csv", sep=";", index=False)
                supervisor_sv = pd.read_csv("supervisor_sv.csv", sep=";")
                pd.to_datetime(supervisor_sv.data, format='%Y-%m-%d')

        st.subheader(f"{nome_p_np} foi escalado(a) para o serviço de {data_escala} com sucesso!")
    # ---------------------------------------------------------------------------------------------------------------#

    # Relatórios
    st.header("**Relatórios:**")
    st.markdown("")

    st.subheader("**Militares em cada escala:**")

    escala_rel1 = st.selectbox("Selecione a escala do militar: ", ['Médico de dia', 'Enfermeiro de dia',
                                                                              'Supervisor de dia'], key='31')


    pergunta_rel1 = st.radio("", ("Todos", "Prontos", "Não Prontos"))

    if st.button('Visualizar'):
        if escala_rel1 == 'Médico de dia':
            if pergunta_rel1 == 'Prontos':
                st.table(medico_de_dia[medico_de_dia.pronto == 1][['posto', 'nome']])
            elif pergunta_rel1 == 'Não Prontos':
                st.table(medico_de_dia[medico_de_dia.pronto == 0][['posto', 'nome']])
            elif pergunta_rel1 == 'Todos':
                st.table(medico_de_dia[['posto', 'nome']])
        elif escala_rel1 == 'Enfermeiro de dia':
            if pergunta_rel1 == 'Prontos':
                st.table(enfermeiro_de_dia[enfermeiro_de_dia.pronto == 1][['posto', 'nome', 'ultimo_sv', 'folga']])
            elif pergunta_rel1 == 'Não Prontos':
                st.table(enfermeiro_de_dia[enfermeiro_de_dia.pronto == 0][['posto', 'nome', 'ultimo_sv', 'folga']])
            elif pergunta_rel1 == 'Todos':
                st.table(enfermeiro_de_dia[['posto', 'nome', 'ultimo_sv', 'folga']])
        elif escala_rel1 == 'Supervisor de dia':
            if pergunta_rel1 == 'Prontos':
                st.table(supervisor_de_dia[supervisor_de_dia.pronto == 1][['posto', 'nome', 'ultimo_sv', 'folga']])
            elif pergunta_rel1 == 'Não Prontos':
                st.table(supervisor_de_dia[supervisor_de_dia.pronto == 0][['posto', 'nome', 'ultimo_sv', 'folga']])
            elif pergunta_rel1 == 'Todos':
                st.table(supervisor_de_dia[['posto', 'nome', 'ultimo_sv', 'folga']])

    st.subheader("**Serviços por militar:**")

    escala_rel2 = st.selectbox("Selecione a escala do militar: ", ['Médico de dia', 'Enfermeiro de dia',
                                                                              'Supervisor de dia'], key='33')

    tipo_rel2 = st.selectbox("Selecione o tipo de escala: ", ['Preta', 'Vermelha',
                                                                   'Roxa'], key='41')

    if escala_rel2 == 'Médico de dia':
        if tipo_rel2 == 'Preta':
            medico_sv = pd.read_csv("medico_sv_preta.csv", sep=";")
            pd.to_datetime(medico_sv.data, format='%Y-%m-%d')

            grafico_medicos = medico_sv.groupby('nome')['nome'].count().sort_values(ascending=False)
            st.dataframe(grafico_medicos)

            if st.button("Gerar Gráfico"):
                plt.figure(figsize=(16, 8))
                sns.set_style("whitegrid")
                plt.xticks(rotation=45)

                sns.barplot(x=grafico_medicos.index,
                            y=grafico_medicos.values,
                            palette=sns.color_palette("BuGn_r", n_colors=len(grafico_medicos.index))).set_title(
                    "Médico de Dia - Escala Preta")
                st.pyplot()

        elif tipo_rel2 == 'Vermelha':
            medico_sv = pd.read_csv("medico_sv_vermelha.csv", sep=";")
            pd.to_datetime(medico_sv.data, format='%Y-%m-%d')

            grafico_medicos = medico_sv.groupby('nome')['nome'].count().sort_values(ascending=False)
            st.dataframe(grafico_medicos)

            if st.button("Gerar Gráfico"):
                plt.figure(figsize=(16, 8))
                sns.set_style("whitegrid")
                plt.xticks(rotation=45)

                sns.barplot(x=grafico_medicos.index,
                            y=grafico_medicos.values,
                            palette=sns.color_palette("BuGn_r", n_colors=len(grafico_medicos.index))).set_title(
                    "Médico de Dia - Escala Vermelha")
                st.pyplot()

        elif tipo_rel2 == 'Roxa':
            medico_sv = pd.read_csv("medico_sv_roxa.csv", sep=";")
            pd.to_datetime(medico_sv.data, format='%Y-%m-%d')

            grafico_medicos = medico_sv.groupby('nome')['nome'].count().sort_values(ascending=False)
            st.dataframe(grafico_medicos)

            if st.button("Gerar Gráfico"):
                plt.figure(figsize=(16, 8))
                sns.set_style("whitegrid")
                plt.xticks(rotation=45)

                sns.barplot(x=grafico_medicos.index,
                            y=grafico_medicos.values,
                            palette=sns.color_palette("BuGn_r", n_colors=len(grafico_medicos.index))).set_title(
                    "Médico de Dia - Escala Roxa")
                st.pyplot()

    elif escala_rel2 == 'Enfermeiro de dia':
        enfermeiro_sv = pd.read_csv("enfermeiro_sv.csv", sep=";")
        pd.to_datetime(enfermeiro_sv.data, format='%Y-%m-%d')

        grafico_enfermeiro = enfermeiro_sv.groupby('nome')['nome'].count().sort_values(ascending=False)
        st.dataframe(grafico_enfermeiro)

        if st.button("Gerar Gráfico"):
            plt.figure(figsize=(16, 8))
            sns.set_style("whitegrid")
            plt.xticks(rotation=45)

            sns.barplot(x=grafico_enfermeiro.index,
                        y=grafico_enfermeiro.values,
                        palette=sns.color_palette("BuGn_r", n_colors=len(grafico_enfermeiro.index))).set_title(
                "Enfermeiro de Dia")
            st.pyplot()
    elif escala_rel2 == 'Supervisor de dia':
        supervisor_sv = pd.read_csv("supervisor_sv.csv", sep=";")
        pd.to_datetime(supervisor_sv.data, format='%Y-%m-%d')

        grafico_supervisor = supervisor_sv.groupby('nome')['nome'].count().sort_values(ascending=False)
        st.dataframe(grafico_supervisor)

        if st.button("Gerar Gráfico"):
            plt.figure(figsize=(16, 8))
            sns.set_style("whitegrid")
            plt.xticks(rotation=45)

            sns.barplot(x=grafico_supervisor.index,
                        y=grafico_supervisor.values,
                        palette=sns.color_palette("BuGn_r", n_colors=len(grafico_supervisor.index))).set_title(
                "Supervisor de Dia")
            st.pyplot()


    st.subheader("**Exibindo todos os serviços:**")

    escala_rel3 = st.selectbox("Selecione a escala do militar: ", ['Médico de dia', 'Enfermeiro de dia',
                                                                              'Supervisor de dia'], key='43')

    tipo_rel3 = st.selectbox("Selecione o tipo de escala: ", ['Preta', 'Vermelha',
                                                              'Roxa'], key='61')

    if escala_rel3 == 'Médico de dia':
        if tipo_rel3 == 'Preta':
            st.table(medico_sv_preta.set_index("data").sort_index(ascending=False)[['posto', 'nome']])
        if tipo_rel3 == 'Vermelha':
            st.table(medico_sv_vermelha.set_index("data").sort_index(ascending=False)[['posto', 'nome']])
        if tipo_rel3 == 'Roxa':
            st.table(medico_sv_roxa.set_index("data").sort_index(ascending=False)[['posto', 'nome']])
    elif escala_rel3 == 'Enfermeiro de dia':
        st.table(enfermeiro_sv.set_index("data").sort_index(ascending=False)[['posto', 'nome']])
    elif escala_rel3 == 'Supervisor de dia':
        st.table(supervisor_sv.set_index("data").sort_index(ascending=False)[['posto', 'nome']])


if __name__ == '__main__':
    main()
