/////////////////////////////////////////////////////////////////
// AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
// DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
// TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
// DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
// DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
// OU PLÁGIO.
// DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
// DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
// SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
// DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
// DIVULGADOS NA PÁGINA DA DISCIPLINA.
// ENTENDO QUE EPS SEM ESTE CABEÇALHO NÃO SERÃO CORRIGIDOS E,
// AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.
// Nome : Renzo Real Machado Filho
// NUSP : 154.869.07
// Turma: BCC 2024
// Prof.: Roberto Hirata Jr.
// Referências: 
// - O algoritmo Insertion Sort Otimizado foi baseado em
// https://www.geeksforgeeks.org/insertion-sort/

#include <stdio.h>

void countingC(int *V, int n){

    int max = V[0];
    int contador = 0;

    for (int i=0; i<n-1; i++){

        if (max < V[i+1])
            max = V[i+1];
    }

    int assistant[max+1];

    for (int j=0; j<max+1; j++){

        assistant[j] = 0;
    }

    for (int k=0; k<n; k++){

        assistant[V[k]] = assistant[V[k]] + 1;
    }

    for (int m=0; m<max+1; m++){

        for (int n=0; n<assistant[m]; n++){

            V[contador] = m;
            contador++;
        }
    }
}

void selectionC(int *V, int n){

    int swap;

    for (int i=0; i<n; i++){

        for (int j=i+1; j<n; j++){

                if (V[i] > V[j]){

                    swap = V[i];
                    V[i] = V[j];
                    V[j] = swap;
                }
        }
    }
}

void bubbleC(int *V, int n){

    int houveTroca = 0;
    int swap;

    for (int i=1; i<n; i++){

        for (int j=0; j<n-i; j++){

            if (V[j] > V[j+1]){

                swap = V[j+1];
                V[j+1] = V[j];
                V[j] = swap;

                houveTroca = 1;
            }

        if(houveTroca == 0)
            break;
        }
    }
}

void insertion_optC(int *V, int n){

    int key;
    int j;

    for (int i=1; i<n; i++){
        key = V[i];
        j = i - 1;


        while ((j>=0) && (V[j]>key)){
            V[j + 1] = V[j];
            j = j - 1;
        }

        V[j + 1] = key;
    }
}

void insertionC(int *V, int n){

    int swap;

    for (int i=1; i<n; i++){

        if (V[i] < V[i-1]){

            swap = V[i];
            V[i] = V[i-1];
            V[i-1] = swap;

            for (int j=1; j<i; j++){

                if (V[i-j] < V[i-j-1]){

                        swap = V[i-j];
                        V[i-j] = V[i-j-1];
                        V[i-j-1] = swap;
                } else {
                        break;
                }
            }
        }
    }
}
