# coding: utf-8

class Loja:
  
  def __init__(self, nome_loja, logradouro, numero, complemento, bairro, 
               municipio, estado, cep, telefone, observacao, cnpj,
               inscricao_estadual):
    self.nome_loja = nome_loja
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual

  def validar_campos_obrigatorios(self):
    if (self.nome_loja == "" or self.nome_loja == None):
        raise Exception("O campo nome da loja é obrigatório")
    if (self.logradouro == "" or self.logradouro == None):
        raise Exception("O campo logradouro do endereço é obrigatório")
    if (self.numero == 0):
        self.numero = "s/n"
    if (self.municipio == "" or self.municipio == None):
        raise Exception("O campo município do endereço é obrigatório")
    if (self.estado == "" or self.estado == None):
        raise Exception("O campo estado do endereço é obrigatório")
    if (self.cnpj == "" or self.cnpj == None):
        raise Exception("O campo CNPJ da loja é obrigatório")
    if (self.inscricao_estadual == "" or self.inscricao_estadual == None):
        raise Exception("O campo inscrição estadual da loja é obrigatório")

  def dados_loja(self):
    # Implemente aqui
    _COMPLEMENTO = ""
    if (self.complemento != "" and self.complemento != None):
        _COMPLEMENTO = " " + self.complemento


    _BAIRRO = ""
    if (self.bairro != "" and self.bairro != None) :
        _BAIRRO = self.bairro + " - "


    _CEP = ""
    _TELEFONE = ""

    if (self.cep != "" and self.cep != None) :
        _CEP = "CEP:" + self.cep
        if (self.telefone != "" and self.telefone != None):
            _TELEFONE = " Tel " + self.telefone
    else :
        _CEP = ""
        if (self.telefone != "" and self.telefone != None):
            _TELEFONE = "Tel " + self.telefone

    _OBSERVACAO = ""

    if(self.observacao != "" and self.observacao != None):
        _OBSERVACAO = self.observacao


    _NUMERO = ""
    if (self.numero != 0):
        _NUMERO = self.numero


    if (self.numero == 0 or self.numero == None or self.numero == ""):
        _NUMERO = "s/n"



    show = f'''{self.nome_loja}
{self.logradouro}, {_NUMERO}{_COMPLEMENTO}
{_BAIRRO}{self.municipio} - {self.estado}
{_CEP}{_TELEFONE}
{_OBSERVACAO}
CNPJ: {self.cnpj}
IE: {self.inscricao_estadual}'''
    return show
