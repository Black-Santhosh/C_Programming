#include<stdio.h>

/*
// 1. without argument without return

void add()
{
    int a = 10, b = 5;
    int c = a+b;
    printf("%d\n",c);
}

void main()
{
    add();
}
*/

/*
// without argument with return

int add()
{
    int a = 10, b = 5;
    int c = a+b;
    return c;
}

void main()
{
    int d = add();
    printf("%d\n",d);
}
    */


    /*
// with argument with return

int add(int a, int b)
{
    int c = a+b;
    return c;
}

void main()
{
    int d = add(10,5);
    printf("%d\n",d);
}    
*/


// with argument without return

void add(int a, int b)
{
    int c = a+b;
    printf("%d\n",c);
}

void main()
{
    add(10,5);
}  