#include <stdio.h>
#include <math.h>

/* INFORMATICA 1 - 1R3 - Ing. Electrónica - UTN FRC
 * Alumno: Philippeaux Enrique Walter - Legajo: 86153
 * Trabajo Práctico Nº3: Aplicación de la privacidad a la criptografía (3.48)
 */

int main(void)
{
    char inputChar[4];
    int input[4];
    int output[4];
    printf("Ingrese el numero encriptado de %d digito\nSu numero: ", 4);
    scanf("%c%c%c%c", &inputChar[0], &inputChar[1], &inputChar[2], &inputChar[3]);

    //Convertir caracteres en numeros:
    for (int i = 0; i < 4; i++)
        input[i] = inputChar[i] - '0';
    
    //Operacion 1: intercambie el primer dígito con el tercero, y el segundo dígito con el cuarto.
    output[0] = input[2];
    output[1] = input[3];
    output[2] = input[0];
    output[3] = input[1];

    //Operacion 2: Reemplace cada dígito con el resultado de sumar 7 al dígito y obtener el resto después de dividir el nuevo valor por 10.
    int numero;
    for (int i = 0; i < 4; i++)
    {
        numero = (output[i] - 7);
        if (numero < 0)
            numero = 10 + numero;
        output[i] = numero;
    }

    //Operacion 3: imprima el entero encriptado. 
    printf("Numero desencriptado: %d%d%d%d", output[0], output[1], output[2], output[3]);
    return 1;
}

