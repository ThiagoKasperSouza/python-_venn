"""

Método 1: Usando Lógica de Diagrama de Venn (De dentro para fora)

Para preencher ou calcular a quantidade de elementos de cada região exata de 3 conjuntos:
1. Intersecção Tripla: Comece definindo os elementos que pertencem aos três conjuntos ao mesmo tempo.
2. Intersecções Duplas Exclusivas
3. Conjuntos Exclusivos (Somente um deles):
"""
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
C = {5, 6, 8, 9}

# 1. Interseção dos três (centro)
tripla = A & B & C  # {5}

# 2. Interseções duplas puras (excluindo quem está no terceiro conjunto)
ab_apenas = (A & B) - C  # {4}
ac_apenas = (A & C) - B  # set() (vazio, pois o 5 está nos três)
bc_apenas = (B & C) - A  # {6}

# 3. Conjuntos exclusivos (pertencem apenas a um conjunto)
somente_a = A - B - C  # {1, 2, 3}
somente_b = B - A - C  # {7}
somente_c = C - A - B  # {8, 9}

print("Somente A:", somente_a)
print("Somente B:", somente_b)
print("Somente C:", somente_c)
print("A e B (sem C):", ab_apenas)
print("A e C (sem B):", ac_apenas)
print("B e C (sem A):", bc_apenas)
print("A, B e C:", tripla)

plt.figure(figsize=(6, 6))
venn3([A, B, C], set_labels=('A', 'B', 'C'))

plt.title("Cardinalidade Venn com Sets Reais")
# Salva a imagem no disco em vez de tentar abrir uma janela
plt.savefig("diagrama_venn.png", dpi=300, bbox_inches='tight')

plt.close()

plt.figure(figsize=(6, 6))
subsets_counts = (
    len(somente_a),
    len(somente_b),
    len(ab_apenas),
    len(somente_c),
    len(ac_apenas),
    len(bc_apenas),
    len(tripla)
)

v = venn3(subsets=subsets_counts, set_labels=('A', 'B', 'C'))

# 3. Função auxiliar para formatar os sets como strings legíveis (ex: "{1, 2, 3}" ou vázio "")
def format_set(s):
    if not s:
        return ""
    # Transforma o set em string ordenada para ficar bonito (ex: "{1, 2, 3}")
    return str(set(s)).replace("set()", "")

# 4. Substituindo os textos padrão pelos elementos reais
# Mapeando os IDs do venn3 para os nossos sets calculados
regioes = {
    '100': somente_a,
    '010': somente_b,
    '001': somente_c,
    '110': ab_apenas,
    '101': ac_apenas,
    '011': bc_apenas,
    '111': tripla
}

for id_regiao, conjunto in regioes.items():
    label = v.get_label_by_id(id_regiao)
    if label:
        # Define o texto com os elementos reais
        label.set_text(format_set(conjunto))




plt.title("Diagrama de Venn com Elementos Reais")

# Salva a imagem gerada
plt.savefig("diagrama_venn_elementos.png", dpi=300, bbox_inches='tight')
plt.close()

print("Diagrama com rótulos personalizados gerado com sucesso!")