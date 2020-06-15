#include <stdio.h>

int main()
{
    int fila, col, a, incognitas;
    float mat[20][20], num, res[10];


    //ingreso de datos
    printf("\nIngrese el orden de la matriz: ");
    scanf("%d", &incognitas);
    printf("\nIngrese los elementos a continuacion:\n");
    for (fila = 1; fila <= incognitas; fila++)
    {
        for (col = 1; col <= (incognitas + 1); col++)
        {
            printf(" - %d,%d:", fila, col);
            scanf("%f", &mat[fila][col]);
        }
    }
    
    //Calculo
    for (col = 1; col <= incognitas; col++) //Ciclar por columnas
    {
        for (fila = 1; fila <= incognitas; fila++) //Ciclar por filas
        {
            if (fila != col) //Solo interactuar fuera de la diagonal principal de la matriz.
            {
                num = mat[fila][col] / mat[col][col]; //Obtener escalar para la posterior eliminacion del elemento.

                //mat[fila][col] es el elemento fuera de la diagonal principal, que va a ser eliminado
                //mat[col][col] es el elemento de la diagonal principal para esta fila
                for (int i = 1; i <= incognitas + 1; i++)
                    mat[fila][i] = mat[fila][i] - num * mat[col][i];
                    /*Eliminar el resto de los elementos de la columna.*/
            }
        }
    }

    printf("El resultado de la ecuacion es:\n");
    for (fila = 1; fila <= incognitas; fila++)
    {
        res[fila] = mat[fila][incognitas + 1] / mat[fila][fila]; 
        //armar matriz resultante, dividiendo los elementos en la 
        //ultima columna, por los de su diagonal principal
        printf("X%d = %f\n", fila, res[fila]);
    }
    return 0;
}