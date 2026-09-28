import matplotlib.pyplot as plt

protocolos = ['RIPv2', 'OSPFv2', 'eBGP']
cores = ['#2ca02c', '#1f77b4', '#d62728']

# 1. Gráfico: Tamanho da Tabela de Roteamento (Prefixos)
plt.figure(figsize=(6, 4))
valores_tabela = [5, 5, 5]
barras = plt.bar(protocolos, valores_tabela, color=cores, width=0.45)
plt.title('Tamanho da Tabela de Roteamento (R1)', fontsize=11, fontweight='bold')
plt.ylabel('Quantidade de Prefixos', fontsize=10)
plt.ylim(0, 7)
for b in barras:
    plt.text(b.get_x() + b.get_width()/2, b.get_height() + 0.15, f'{int(b.get_height())} prefixos', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('grafico_1_tabela.png', dpi=300)
plt.close()

# 2. Gráfico: Quantidade de Pacotes de Roteamento Enviados
plt.figure(figsize=(6, 4))
valores_pacotes = [2, 6, 4]
barras = plt.bar(protocolos, valores_pacotes, color=cores, width=0.45)
plt.title('Qtd. de Pacotes de Roteamento Capturados', fontsize=11, fontweight='bold')
plt.ylabel('Pacotes de Controle', fontsize=10)
plt.ylim(0, 8)
for b in barras:
    plt.text(b.get_x() + b.get_width()/2, b.get_height() + 0.15, f'{int(b.get_height())} pkts', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('grafico_2_pacotes.png', dpi=300)
plt.close()

# 3. Gráfico: Taxa de Transmissão Utilizada (Bytes/s)
plt.figure(figsize=(6, 4))
valores_taxa = [6.93, 9.60, 1.69]
barras = plt.bar(protocolos, valores_taxa, color=cores, width=0.45)
plt.title('Taxa de Transmissão Utilizada (Overhead)', fontsize=11, fontweight='bold')
plt.ylabel('Taxa de Controle (Bytes/s)', fontsize=10)
plt.ylim(0, 12)
for b in barras:
    plt.text(b.get_x() + b.get_width()/2, b.get_height() + 0.2, f'{b.get_height():.2f} B/s', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('grafico_3_taxa_transmissao.png', dpi=300)
plt.close()

# 4. Gráfico: Delay Médio Fim-a-Fim (RTT)
plt.figure(figsize=(6, 4))
valores_delay = [0.070, 0.086, 0.082]
barras = plt.bar(protocolos, valores_delay, color=cores, width=0.45)
plt.title('Delay Médio Fim-a-Fim (RTT)', fontsize=11, fontweight='bold')
plt.ylabel('Latência Média (ms)', fontsize=10)
plt.ylim(0, 0.11)
for b in barras:
    plt.text(b.get_x() + b.get_width()/2, b.get_height() + 0.002, f'{b.get_height():.3f} ms', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('grafico_4_delay.png', dpi=300)
plt.close()

print("Os 4 gráficos foram gerados com sucesso!")
