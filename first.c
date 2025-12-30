// 
// 

#include<stdio.h>
int main()
{
    // int a=10,b=100,c=1000;
    // if(a>b && a>c)
    // {
    //     printf("a is greater.");
    // }
    // else if(b>c)
    // {
    //     printf("b is greater.");
    // }
    // else
    // {
    //     printf("c is greater.");
    // }

    // unary operator
    //                  ++                              --
    //              inc by  1                        dec by 1
    // a=10         a=a+1                            a=a-1
    //              a=11                             a=9  
    //  pre inc                post inc |   pre dec             post dec
    //  ++a                         a++ |       --a             a--
    // 


    // int a=97;
    // printf("\n1. : %d",--a);        //    
    // printf("\n2. : %d",--a);        //
    // printf("\n3. : %d",a++);        //    
    // printf("\n4. : %d",--a);        //
    // printf("\n5. : %d",a++);        //
    // printf("\n6. : %d",a--);        //
    // printf("\n7. : %d",--a);        //
    // printf("\n8. : %d",a++);        //
    // printf("\n9. : %d",a--);        //
    // printf("\nX. : %d",a);          //




    // printf("\n %d %d %d ", a++,++a,a);  
    // // 97   99     99


    // for(exp1;exp2;exp3)
    // {
    //     // iterative statemets
    // }
    // exp1 : init         start     i=1        enter in loop only once     
    // exp2 : condition    stop      i<=10      befor enter     
    // exp2 : inc/dec      step      i++        befor exit     

    // int i;
    // for(i=1;i<=10;i++)
    // {
    //     printf("\t%d",i);
    // }
    // char i;
    // for(i='z';i>='a';i+=2)
    // {
    //     printf("\t%c",i);
    // }

    // int i,j;
    // for(i=1,j=10;i<=10;i++,j--)
    // {
    //         printf("\n%d - %d" ,i,j);
    // }

    // int i,j;
    // for(i=1;i<=5;i++) //row
    // {       
    //     for(j=1;j<=5;j++) // col
    //     {
    //         printf(" *");
    //     }
    //     printf("\n");
    // }


// i,j
// i  i<=5      j   j<=5                        j++     i++
// 1  1<=5  T   1   1<=5    T       print       2
             // X   2<=5    T       print       3   
             // X   3<=5    T       print       4
             // X   4<=5    T       print       5
             // X   5<=5    T       print       6
             // X   6<=5    F      ------X              2

// 2  2<=5  T   1   1<=5    T       print       2
             // X   2<=5    T       print       3   
             // X   3<=5    T       print       4
             // X   4<=5    T       print       5
             // X   5<=5    T       print       6
             // X   6<=5    F      ------X              3

// 3  2<=5  T   1   1<=5    T       print       2
             // X   2<=5    T       print       3   
             // X   3<=5    T       print       4
             // X   4<=5    T       print       5
             // X   5<=5    T       print       6
             // X   6<=5    F      ------X              4

// 4  2<=5  T   1   1<=5    T       print       2
             // X   2<=5    T       print       3   
             // X   3<=5    T       print       4
             // X   4<=5    T       print       5
             // X   5<=5    T       print       6
             // X   6<=5    F      ------X              5

// 5  2<=5  T   1   1<=5    T       print       2
             // X   2<=5    T       print       3   
             // X   3<=5    T       print       4
             // X   4<=5    T       print       5
             // X   5<=5    T       print       6
             // X   6<=5    F      ------X              6

// 6  6<=5  F  ------X




// * * * * *



// * * * * *
// * * * * *
// * * * * *
// * * * * *
// * * * * *



    // int i,j;
    // for(i=5;i>=1;i--) //row
    // {       
    //     for(j=1;j<=i;j++) // col
    //     {
    //         printf(" *");
    //     }
    //     printf("\n");
    // }

// *
// * * 
// * * * 
// * * * * 
// * * * * *


// 11  12  13  14  15

// 21  22  23  24  25

// 31  32  33  34  35

    // int i,j;
    // for(i=1;i<=5;i++) //row
    // {       
    //     for(j=5;j>=i;j--) // col
    //     {
    //         printf(" *");
    //     }
    //     printf("\n");
    // }
    
    // int i,j,k,sp=10;
    // for(i=1;i<=5;i++) //row
    // {       
    //     for(k=1;k<=sp;k++) // col    
    //     {
    //         printf(" ");
    //     }
    //     for(j=1;j<i*2;j++) // col
    //     {
    //         printf("*");
    //     }
    //     sp--;
    //     printf("\n");
    // }
    
//           *
//          **
//         ***
//        ****
//       *****

//           _*
//          _*_*
//         _*_*_*
//        _*_*_*_*
//       _*_*_*_*_*
    
    // int i,j;
    // for(i=1;i<=5;i++) //row
    // {       
    //     for(j=1;j<i*2;j++) // col
    //     {
    //         printf("*");
    //     }
    //     printf("\n");
    // }


//     int i,j,k,sp=10;
//   for(i=1;i<=4;i++) //row
//     {       
//         for(k=1;k<=sp;k++) // col    
//         {
//             printf(" ");
//         }
//         for(j=1;j<i*2;j++) // col
//         {
//             printf("*");
//         }
//         sp--;
//         printf("\n");
//     }
//     // sp++;
//     for(i=5;i>=1;i--) //row
//     {       
//         for(k=1;k<=sp;k++) // col    
//         {
//             printf(" ");
//         }
//         for(j=1;j<i*2;j++) // col
//         {
//             printf("*");
//         }
//         sp++;
//         printf("\n");
//     }

//       *********
//        *******
//         *****
//          ***
//           *

    // for(int i=0;i<=10;i++)
    // {
    //     printf("\t%d",i);
    // }
    // ------------------------
    // i=1;
    // while(i<=10)
    // {
    //     printf("\t%d",i);
    //     i++;
    // }
    // --------
    // i=1;
    // do
    // {
    //     printf("\t%d",i);
    //     i++;
    // }while(i<=10);


    
    // Array - collection of data which has a same D.T.

    // int a=10;  

    // printf("\n a : %d",sizeof(a));
    // printf("\n %d",sizeof(char));
    // printf("\n %d",sizeof(float));
    // printf("\n %d",sizeof());
    // printf("\n a : %d",a);
    // printf("\n a : %u",&a);
    // int arr[10]={11,22,33,44,55}; //dec
    // printf("\n %d",sizeof(arr));
    // printf("\n arr : %u",&arr);
    // for (int i = 0; i <10; i++)
    // {
    //     printf("\n%d -  %u",arr[i],&arr[i]);
    // }
    
    // int arr1[10]={11,22,33}; //dec

    // int arr1[5];
    // int i;
    // for (int i = 0; i < 5; i++)
    // {
    //     printf("\n Enter arr1[ %d ] : ",i+1);
    //     scanf("%d",&arr1[i]);
    // }
    // for (int i = 0; i < 5; i++)
    // {
    //     printf("\n arr1[ %d ] : %d",i+1,arr1[i]);
    // }
    
    //30-12-2025

    // int a1=10;
    // int *a2;
    // a2=&a1;
    // printf("\n Address of a1 : %u",&a1);
    // printf("\n Value of a1 :  %d",a1);

    // printf("\n\n Address of a2 : %u",&a2);
    // printf("\n Value of a2 address of a1:  %u",a2);
    // printf("\n Value of a1 using a2:  %d",*a2);

    // int arr1[5] ={11,22,33,44,55};
    // int i,*ptr;
    // ptr=arr1;

    // printf("\nsizeof(arr1) : %d",sizeof(arr1));
    // printf("\nsizeof(ptr) : %d",sizeof(ptr));

    // printf("\n %u",&arr1);
    // printf("\n %u",ptr);
  
    // for (int i = 0; i < 5; i++)
    // {
    //     printf("\n Enter arr1[ %d ] : ",i+1);
    //     scanf("%d",&arr1[i]);
    // }
    // for (int i = 0; i < 5; i++)
    // {
    //     printf("\n %d -  %d",arr1[i],*(ptr+i));
    // }    

    // int arr[5][5];
    // int i,j;    
    // for ( i = 0; i < 3; i++)
    // {
    //     for ( j = 0; j < 3; j++)
    //     {
    //         printf("%u",&a[i][j])
    //     }
    // }
    
/*
1   2   3
4   5   6   
7   8   9



*/



    
    return 0;
}