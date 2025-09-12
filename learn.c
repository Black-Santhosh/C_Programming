#include<stdio.h>

void hello()
{
    printf("Hello, Santhosh\n");
}

void bye()
{
    printf("Bye, Santhosh\n");
}

void main()
{
    void (*funcptr)();
    funcptr = hello;
    funcptr();

    funcptr = bye;
    funcptr();
}
