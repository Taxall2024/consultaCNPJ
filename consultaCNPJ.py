import requests
import json
import streamlit as st
import pandas as pd
import base64


st.set_page_config(layout='wide')
background_image ="Untitleddesign.jpg"
st.markdown(
     f"""
     <iframe src="data:image/jpg;base64,{base64.b64encode(open(background_image, 'rb').read()).decode(

    )}" style="width:3000px;height:9000px;position: absolute;top:-3vh;right:-350px;opacity: 0.5;background-size: cover;background-position: center;"></iframe>
     """,
     unsafe_allow_html=True )

def consultaCNPJ(cnpj:str)->pd.DataFrame:
    url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'

    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}

    response = requests.request("GET", url, params=querystring)

    if response.status_code == 200:
        data = response.json()
        main_data = {
            'CNPJ': data.get('cnpj'),
            'Abertura': data.get('abertura'),
            'Situação': data.get('situacao'),
            'Tipo': data.get('tipo'),
            'Nome': data.get('nome'),
            'Fantasia': data.get('fantasia'),
            'Porte': data.get('porte'),
            'Natureza Jurídica': data.get('natureza_juridica'),
            'Logradouro': data.get('logradouro'),
            'Número': data.get('numero'),
            'Complemento': data.get('complemento'),
            'Município': data.get('municipio'),
            'Bairro': data.get('bairro'),
            'UF': data.get('uf'),
            'CEP': data.get('cep'),
            'Telefone': data.get('telefone'),
            'Email': data.get('email'),
            'Capital Social': data.get('capital_social'),
            'Optante Simples': data.get('simples', {}).get('optante'),
            'Data Situação Simples': data.get('simples', {}).get('data_opcao'),
            'Optante Simei': data.get('simei', {}).get('optante'),
            'Data Situação Especial': data.get('data_situacao_especial')
        }

       
        atividade_principal = pd.DataFrame(data.get('atividade_principal', []))
    
        atividades_secundarias = pd.DataFrame(data.get('atividades_secundarias', []))
        
        qsa = pd.DataFrame(data.get('qsa', []))

        df_main = pd.DataFrame([main_data])

        return df_main, atividade_principal, atividades_secundarias, qsa
    else:
        print(f"Erro na consulta: {response.status_code}")
        return None, None, None, None

def gerandoVisuizacao(cnpj):

    df_main, df_atividade_principal, df_atividades_secundarias, df_qsa = consultaCNPJ(cnpj)

    st.header("Dados principais:")
    st.dataframe(df_main,use_container_width=True)

    st.header("\nAtividade principal:")
    st.dataframe(df_atividade_principal,use_container_width=True)

    st.header("\nAtividades secundárias:")
    st.dataframe(df_atividades_secundarias,use_container_width=True)

    st.header("\nQuadro societário (QSA):")
    st.dataframe(df_qsa,use_container_width=True)



if __name__=='__main__':

    col1,col2,col3 = st.columns(3)
    
    with col1:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        cnpj= st.text_input('Digite o CNPJ',key=f'cnpj1')
        gerandoVisuizacao(cnpj)

    with col2:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        cnpj= st.text_input('Digite o CNPJ',key=f'cnpj2')
        gerandoVisuizacao(cnpj)
    with col3:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        cnpj= st.text_input('Digite o CNPJ',key=f'cnpj3')
        gerandoVisuizacao(cnpj)




