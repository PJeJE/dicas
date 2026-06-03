---
title: "Chave de acesso"
date: 2022-11-23T17:50:08-03:00
weight: 1
---

No modelo de documento, utilize as variáveis:

`#{processoTrfHome.tabelaHashDocumentosComId}`

`#{processoTrfHome.tabelaHashDocumentos}`

Ao minutar o documento, será incluída uma tabela com a lista de documentos do processo e suas respectivas chaves de acesso.

Com as chaves, o usuário pode conferir o conteúdo de cada um dos documentos na página de consulta. Selecione o tribunal abaixo para abrir o endereço correspondente:

<div style="margin:1em 0;">
  <select id="pje-consulta-select" onchange="document.getElementById('pje-consulta-link').setAttribute('href', this.value); var l=document.getElementById('pje-consulta-link'); if(this.value){l.style.display='inline-block'; l.textContent='Abrir consulta de documentos »';} else {l.style.display='none';}">
    <option value="">— Selecione o tribunal —</option>
    <optgroup label="TSE">
      <option value="https://pje.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TSE</option>
    </optgroup>
    <optgroup label="1º grau (Zonas Eleitorais)">
      <option value="https://pje1g-ac.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Acre (AC)</option>
      <option value="https://pje1g-al.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Alagoas (AL)</option>
      <option value="https://pje1g-ap.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Amapá (AP)</option>
      <option value="https://pje1g-am.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Amazonas (AM)</option>
      <option value="https://pje1g-ba.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Bahia (BA)</option>
      <option value="https://pje1g-ce.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Ceará (CE)</option>
      <option value="https://pje1g-df.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Distrito Federal (DF)</option>
      <option value="https://pje1g-es.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Espírito Santo (ES)</option>
      <option value="https://pje1g-go.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Goiás (GO)</option>
      <option value="https://pje1g-ma.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Maranhão (MA)</option>
      <option value="https://pje1g-mt.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Mato Grosso (MT)</option>
      <option value="https://pje1g-ms.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Mato Grosso do Sul (MS)</option>
      <option value="https://pje1g-mg.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Minas Gerais (MG)</option>
      <option value="https://pje1g-pa.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Pará (PA)</option>
      <option value="https://pje1g-pb.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Paraíba (PB)</option>
      <option value="https://pje1g-pr.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Paraná (PR)</option>
      <option value="https://pje1g-pe.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Pernambuco (PE)</option>
      <option value="https://pje1g-pi.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Piauí (PI)</option>
      <option value="https://pje1g-rj.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Rio de Janeiro (RJ)</option>
      <option value="https://pje1g-rn.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Rio Grande do Norte (RN)</option>
      <option value="https://pje1g-rs.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Rio Grande do Sul (RS)</option>
      <option value="https://pje1g-ro.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Rondônia (RO)</option>
      <option value="https://pje1g-rr.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Roraima (RR)</option>
      <option value="https://pje1g-sc.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Santa Catarina (SC)</option>
      <option value="https://pje1g-sp.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">São Paulo (SP)</option>
      <option value="https://pje1g-se.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Sergipe (SE)</option>
      <option value="https://pje1g-to.tse.jus.br/pje/Processo/ConsultaDocumento/listView.seam">Tocantins (TO)</option>
    </optgroup>
    <optgroup label="2º grau (TREs)">
      <option value="https://pje.tre-ac.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-AC</option>
      <option value="https://pje.tre-al.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-AL</option>
      <option value="https://pje.tre-ap.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-AP</option>
      <option value="https://pje.tre-am.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-AM</option>
      <option value="https://pje.tre-ba.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-BA</option>
      <option value="https://pje.tre-ce.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-CE</option>
      <option value="https://pje.tre-df.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-DF</option>
      <option value="https://pje.tre-es.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-ES</option>
      <option value="https://pje.tre-go.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-GO</option>
      <option value="https://pje.tre-ma.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-MA</option>
      <option value="https://pje.tre-mt.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-MT</option>
      <option value="https://pje.tre-ms.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-MS</option>
      <option value="https://pje.tre-mg.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-MG</option>
      <option value="https://pje.tre-pa.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-PA</option>
      <option value="https://pje.tre-pb.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-PB</option>
      <option value="https://pje.tre-pr.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-PR</option>
      <option value="https://pje.tre-pe.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-PE</option>
      <option value="https://pje.tre-pi.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-PI</option>
      <option value="https://pje.tre-rj.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-RJ</option>
      <option value="https://pje.tre-rn.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-RN</option>
      <option value="https://pje.tre-rs.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-RS</option>
      <option value="https://pje.tre-ro.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-RO</option>
      <option value="https://pje.tre-rr.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-RR</option>
      <option value="https://pje.tre-sc.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-SC</option>
      <option value="https://pje.tre-sp.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-SP</option>
      <option value="https://pje.tre-se.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-SE</option>
      <option value="https://pje.tre-to.jus.br/pje/Processo/ConsultaDocumento/listView.seam">TRE-TO</option>
    </optgroup>
  </select>
  <a id="pje-consulta-link" href="#" target="_blank" rel="noopener" style="display:none; margin-left:0.75em;">Abrir consulta de documentos »</a>
</div>
