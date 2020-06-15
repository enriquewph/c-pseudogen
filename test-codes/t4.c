#include <stdio.h>

/* INFORMATICA 1 - 1R3 - Ing. Electrónica - UTN FRC
 * Alumno: Philippeaux Enrique Walter - Legajo: 86153
 * 
 * Trabajo Práctico Nº3: Aplicación de la privacidad a la criptografía (3.48)
 * 
 * Consigna:
 * El crecimiento explosivo de las comunicaciones por Internet y el almacenamiento de datos
 * en las computadoras conectadas a Internet ha aumentado considerablemente las
 * preocupaciones sobre la privacidad. El campo de la criptografía se refiere a la codificación
 * de datos para dificultar (y, con suerte, con los esquemas más avanzados, imposibilitar) la
 * lectura para los usuarios no autorizados. En este Trabajo, Ud. investigará un esquema
 * simple para cifrar y descifrar datos. Una compañía que desea enviar datos a través de
 * Internet le ha pedido que escriba un programa que los encriptará para que se transmitan de
 * manera más segura. Todos los datos se transmiten como enteros de cuatro dígitos. Su
 * aplicación debe leer un número entero de cuatro dígitos ingresado por el usuario y
 * encriptarlo de la siguiente manera: 
 * 
 * 1. Reemplace cada dígito con el resultado de sumar 7 al
 *    dígito y obtener el resto después de dividir el nuevo valor por 10. 
 * 2. Luego intercambie el primer dígito con el tercero, y el segundo dígito con el cuarto. 
 * 3. Luego imprima el entero encriptado. 
 * 
 * Escriba una aplicación por separado que ingrese un entero cifrado de cuatro
 * dígitos y lo descifra (invirtiendo el esquema de cifrado) para formar el número original.
 * Como lectura opcional: Investigue la "criptografía de clave pública" en general y el
 * esquema de clave pública específico de PGP (Pretty Good Privacy). También es posible
 * investigar el esquema RSA, que se utiliza ampliamente en aplicaciones industriales.
 */

int main(void)
{
    char inputChar[4];
    int input[4];
    int output[4];
    printf("Ingrese el numero de %d digitos a ser encriptado.\nSu numero: ", 4);
    scanf("%c%c%c%c", &inputChar[0], &inputChar[1], &inputChar[2], &inputChar[3]);

    //Convertir caracteres en numeros:
    for (int i = 0; i < 4; i++)
        input[i] = inputChar[i] - '0';
    
    //Operacion 1: Reemplace cada dígito con el resultado de sumar 7 al dígito y obtener el resto después de dividir el nuevo valor por 10.
    for (int i = 0; i < 4; i++)
        input[i] = (input[i] + 7) % 10;

    //Operacion 2: intercambie el primer dígito con el tercero, y el segundo dígito con el cuarto.
    output[0] = input[2];
    output[1] = input[3];
    output[2] = input[0];
    output[3] = input[1];

    //Operacion 3: imprima el entero encriptado. 
    printf("Numero encriptado: %d%d%d%d", output[0], output[1], output[2], output[3]);
    return 1;
}
