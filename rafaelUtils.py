# ========== 0. FUNCOES ==========
def formatar_cnpj(cnpj):
    '''
    Formatação de cnpj, 
    funciona quando o cnpj está em formato numérico
    '''
    if pd.isna(cnpj):
        return None
    s = str(int(float(cnpj))).zfill(14)
    return f"{s[0:2]}.{s[2:5]}.{s[5:8]}/{s[8:12]}-{s[12:14]}"
