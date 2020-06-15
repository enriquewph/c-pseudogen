#include <stdio.h>

int main(void)
{
    int codigo_empleado, var, var2;
    float salario_gerente, salario_por_hora_trabajadores, salario_por_articulo_destajo, salario, salario_acumulado = 0, var3;
    printf("Programa para el calculo de pago semanal.\n");
    printf("Por favor, ingrese el salario fijo para los gerentes: ");
    scanf("%f", &salario_gerente);
    printf("Por favor, ingrese el salario por hora para trabajadores regulares: ");
    scanf("%f", &salario_por_hora_trabajadores);
    printf("Por favor, ingrese el monto por articulo vendido para trabajadores a destajo: ");
    scanf("%f", &salario_por_articulo_destajo);

    printf("\n");
    printf("\n");

    printf("------------------------\n");
    printf("Gerente:              1 \n");
    printf("Trabajador por hora:  2 \n");
    printf("Comisionista:         3 \n");
    printf("Trabajador a destajo: 4 \n");
    printf("------------------------\n");
    printf("Tenga presente la tabla para ingresar los codigos, ingrese cualquier otro numero para salir.\n");

    do
    {
        printf("Introduzca codigo de empleado:"); /* indicador para la entrada */
        scanf("%d", &codigo_empleado);

        switch (codigo_empleado)
        {
        case 1: //Gerente
            salario_acumulado += salario_gerente;
            printf("El salario del empleado es de: $%.2f\n\n", salario_gerente);
            break;
        case 2: //Trabajador por hora
            printf("Horas trabajadas: "); /* indicador para la entrada */
            scanf("%d", &var);
            var2 = var - 40; //almacenar horas extra trabajadas en var
            if (var2 < 0)
                var2 = 0; //No hay horas extra...
            var = var - var2; //almacenar horas de pago fijo.

            //Computar salario
            salario = ((float)var * salario_por_hora_trabajadores) + ((float)var2 * 1.5 * salario_por_hora_trabajadores);
            
            salario_acumulado += salario;
            printf("El salario del empleado es de: $%.2f\n\n", salario);
            break;
        case 3: //Comisionista
            salario = 250;
            printf("Ventas brutas en pesos: "); /* indicador para la entrada */
            scanf("%f", &var3); //var 3 es de tipo float.
            salario += var3 * 0.057; //Comision del 5,7%
            salario_acumulado += salario;
            printf("El salario del empleado es de: $%.2f\n\n", salario);
            break;
        case 4: //Trabajador a destajo
            printf("Articulosvendidos: "); /* indicador para la entrada */
            scanf("%d", &var);
            salario = (float)(salario_por_articulo_destajo * var);
            salario_acumulado += salario;
            printf("El salario del empleado es de: $%.2f\n\n", salario);
            break;
        default: //No hacer nada.
            codigo_empleado = -1;
            break;
        }
    } while (codigo_empleado > 0);

    printf("El monto total en salarios de esta semana es de $%.2f\n", salario_acumulado);
    return 0;
}
