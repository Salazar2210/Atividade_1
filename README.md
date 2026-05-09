Trabalho de Algoritmos de Programação, Projetos e Computação
Atividade Avaliativa 1

Curso: Engenharia de Software 
Disciplina: Algoritmos de Programação, Projetos e Computação
Trabalho: Atividade avaliativa 1; SEUC-4 Sistema de Escoamento de Unidades de Carga
Alunos: 
1.	Luis Gustavo Fortunato Filho               RA: 
2.	Matheus Augusto Papa Batista           RA: 26006951 
3.	Murilo Passini Tafarelo                            RA: 26004479
4.	Rafael Salazar Ahumada Comitre     RA: 26000336 
Data: 09/05/2026
 








Problema da Refinaria Delta-9
Contextualização do problema
A Refinaria Delta-9 opera com um Duto Principal de Escoamento (DPE), responsável por manter toda a operação da refinaria em funcionamento. Durante cada turno de trabalho, são realizadas diversas leituras de pressão hidrodinâmica no duto, medidas em UPC (Unidade de Pressão Constrita).
Recentemente, uma tempestade geomagnética danificou os chips de memória estática do servidor central da refinaria. Como consequência direta, o sistema perdeu a capacidade de armazenar dados (não é capaz de ter um histórico do que houve), ele consegue capturar o valor de pressão em tempo real, mas é incapaz de guardar registros anteriores. Diante disso, a Delta-9 passou a operar sem memória de armazenamento, com o controle de pressão sendo realizado manualmente por operadores sobrecarregados.
A ausência de um sistema automatizado representa um risco operacional grave. Se a pressão no duto ultrapassar o limite crítico sem detecção imediata, o duto pode romper. Por outro lado, caso a pressão caia abaixo do limite mínimo, o fluído pode cristalizar e entupir o sistema, comprometendo a produção inteira. Um perigo adicional é o chamado “Efeito de Fadiga de Material”: embora um único pico de pressão crítica seja suportável, dois picos consecutivos na Zona Vermelha provocam vibração harmônica suficiente para destruir as juntas de expansão do duto.
Solução proposta
Diante desse cenário, a equipe foi contratada para desenvolver o SEUC-4: um sistema leve em linguagem Python, projetado para rodar diretamente nos buffers dos sensores, sem depender de memória de armazenamento persistente. O sistema funciona como uma sentinela de fluxo, ele lê cada dado de pressão em tempo real, aplica os cálculos necessários, classifica o estado do duto, detecta situações críticas e, ao final, exibe as métricas do turno de operação. Tudo isso sem precisar guardar um histórico completo dos valores.



Desenvolvimento do Projeto
Estrutura Geral do Sistema O SEUC-4 
O sistema foi implementado em Python puro, sem o uso de bibliotecas externas além das nativas da linguagem. A escolha foi intencional, como o sistema precisa rodar em ambientes com recursos limitados, qualquer dependência externa poderia inviabilizar sua execução.
O programa foi organizado em funções bem definidas, cada uma responsável por uma etapa específica do processamento. Essa separação por funções facilita a leitura do código e simplifica a manutenção futura. 
 Estrutura do código
O sistema foi desenvolvido organizado em dois arquivos:
•	main.py – responsável pela interface com o usuário, pelo fluxo principal de execução e pela exibição dos resultados.
•	funcoes.py – contém todas as funções auxiliares utilizadas no processamento das leituras de pressão.

Funcionamento do Sistema
Ao iniciar, o sistema exibe um painel de informações com as zonas de pressão e os parâmetros de operação, facilitando a compreensão do operador sobre os limites do duto. Em seguida, solicita o número total de leituras previstas para o turno.
Para cada leitura inserida, o sistema executa os seguintes passos:
1.	Ajuste Térmico: leituras acima de 150 UPC recebem um acréscimo de 8% (expansão térmica); leituras iguais ou abaixo de 150 UPC sofrem uma redução de 4% (contração). 
Esse ajuste simula o comportamento físico do fluído dentro do duto sob diferentes condições de temperatura. 
2.	Classificação de Estabilidade: após o ajuste, a pressão é classificada em uma das três zonas: 
a.	Zona Verde (Estável): entre 120 e 180 UPC — operação normal.
b.	Zona Amarela (Oscilação): abaixo de 250 UPC — atenção recomendada.
c.	Zona Vermelha (Crítica): acima de 250 UPC — risco imediato.
d.	Abaixo de 120 UPC: fluído cristalizado — interrupção imediata.
3.	Protocolo de Travamento: Caso haja duas leituras consecutivas classificadas na Zona Vermelha, o sistema interrompe imediatamente o escoamento, seguindo o protocolo de segurança contra o "Efeito de Fadiga de Material". 
4.	Variação de Pressão: a partir da segunda leitura, o sistema informa ao operador se a pressão subiu ou abaixou em relação à leitura anterior, fornecendo uma noção de tendência do comportamento do duto em tempo real.

Métricas Finais
	Ao encerrar, seja por conclusão de todas as leituras ou por travamento de emergência, o sistema exibe um resumo completo com:
•	Média das pressões ajustadas de todo o turno. 
•	Menor e maior pressão registrada durante o processo. 
•	Porcentagem de leituras que ficaram na Zona Verde. 
•	Caso tenha havido travamento: o percentual de leituras realizadas em relação ao total previsto.
•	Estabilidade da operação: Mostra a estabilidade da operação, baseado na porcentagem de leituras na Zona Verde
•	Chance de travamento no próximo turno, estimada com base no percentual de leituras efetivamente realizadas, quanto menor esse percentual, maior o risco de um travamento acontecer no turno seguinte

Funcionalidades Extras Implementadas 
A equipe implementou funcionalidades adicionais com o objetivo de tornar o SEUC-4 mais robusto e útil para os operadores da Delta-9:
•	Avaliação de Estabilidade da Operação: esta função analisa o percentual de leituras que permaneceram na Zona Verde e retorna um diagnóstico qualitativo da saúde do duto. Isso permite que a equipe de manutenção tome decisões preventivas, mesmo que nenhum travamento tenha ocorrido durante o turno.
•	Estimativa de Risco para o Próximo Turno: se um turno foi encerrado por travamento antes de completar todas as leituras previstas, o percentual realizado revela a fragilidade do duto. Essa função usa esse dado para estimar a probabilidade de um novo travamento no turno seguinte, auxiliando no planejamento operacional.
•	Descrição e Variação de Pressão em Tempo Real: O sistema calcula e exibe automaticamente se a pressão subiu ou caiu em relação à leitura anterior, informando o valor exato da variação em UPC. Isso permite ao operador acompanhar a tendência do duto em tempo real, sem precisar comparar valores manualmente. 
Bibliotecas Utilizadas
O projeto utilizou apenas a biblioteca os, nativa do Python, exclusivamente para limpar tela, melhorando a experiência visual do operador no terminal e deixando a usabilidade do sistema mais fácil. Nenhuma biblioteca externa foi necessária, mantendo o sistema leve e compatível com ambientes com recursos limitados, como os buffers de sensores da refinaria.
Dificuldades Encontradas e Soluções Adotadas 
A principal dificuldade do time foi implementar o Protocolo de Travamento sem o uso de listas ou estruturas de armazenamento, respeitando a restrição de que o sistema opera sem memória. A solução encontrada foi utilizar apenas duas variáveis: “contador_vermelho”, que incrementa a cada leitura na Zona Vermelha consecutiva e é zerado ao sair dela, e “pressao_anterior”, que guarda somente o valor imediatamente anterior para calcular a variação. Dessa forma, o sistema "sente" o perigo sem precisar olhar para o histórico completo. 
Ambiente de Execução
O sistema deve ser executado no Visual Studio Code (VSCode) com o interpretador Python 3 configurado. Ambos os arquivos (main.py e funcoes.py) devem estar na mesma pasta para que a importação do módulo “funcoes” funcione corretamente, assim garantido a funcionabilidade do sistema.
Referências bibliográficas
Lucia Filomena De Almeida Guimarães - Notas de Aula – Algoritmos de Programação, Projetos e Computação. Canvas – PUC-Campinas, 2026.
