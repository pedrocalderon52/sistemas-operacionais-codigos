#include <stdio.h>
#include <stdlib.h>
#ifdef _WIN32
    #include <windows.h>
#else 
    #include <unistd.h>
    #include <sys/stat.h>
#endif

int main(){
    #ifdef _WIN32
        if (CreateDirectory("diretorio1_win", NULL)){
            printf("Diretorio criado com sucesso! (Windows)\n");
        } else {
            printf("Erro ao criar diretório! \n");
        }
    #else 
        if (mkdir("diretorio1_linx", 0777) == 0){ /* O 0777 simboliza as permissões RWX (read, write, execute), na ordem 1 - dono, 2 - grupo, 3 - outros. Isso é na base octal, então o 777 significa: permissões RWX para dono, grupo e outros */
            printf("Diretório criado com sucesso! (Linux)\n")
        } else {
            printf("Erro ao criar diretório! \n");
        }
    #endif

    return 0;
}