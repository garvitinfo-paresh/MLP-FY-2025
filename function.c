// //WAWR
// #include<stdio.h>
// void pattern(int y) //Function Defination
// {
//     int i,j,sp=10;
//     for ( i = 1; i < y; i++)
//     {
//         for ( j = 1; j < sp; j++)
//             printf(" ");
//         for ( j = 1; j < i*2; j++)
//         {
//             printf("*");
//         }
//         sp--;
//         printf("\n");
//     }    
// } 
// int main()
// {
//     pattern(11);
//     pattern(8);
//     pattern(6);
    
//     return 0;
// }



// //WAWR
// #include<stdio.h>
// int doSum(int x,int y) //Function Defination
// {
//     return x+y;
// } 
// int main()
// {
//     int sum,x,y;
//     // int doSum(int,int ); //Function Declaration  

//     printf("Enter value of x : ");
//     scanf("%d",&x); 
//     printf("Enter value of y : ");
//     scanf("%d",&y); 
    
//     sum=doSum(x,y);

//     printf("\n x + y : %d",sum);
//     return 0;
// }



// //NAWR
// #include<stdio.h>
// int main()
// {
//     int sum;
//     int doSum(); //Function Declaration  
//     sum=doSum();

//     // printf("\n %d + %d : %d",n,m,n+m);
//     printf("\n x + y : %d",sum);
//     return 0;
// }
// int doSum() //Function Defination
// {
//     int x,y;

//     printf("Enter value of x : ");
//     scanf("%d",&x); 
//     printf("Enter value of y : ");
//     scanf("%d",&y); 

//     return x+y;
    
// } 


// //WANR
// #include<stdio.h>
// int main()
// {
//     int x,y;
//     void doSum(int,int); //Function Declaration
  
//     printf("Enter value of x : ");
//     scanf("%d",&x); 
//     printf("Enter value of y : ");
//     scanf("%d",&y); 
  
//     doSum(x,y);
//     return 0;
// }
// void doSum(int n,int m) //Function Defination
// {
//     printf("\n %d + %d : %d",n,m,n+m);
// } 


//NANR
// #include<stdio.h>
// int main()
// {
//     void doSum(); //Function Declaration
//     doSum();
//     doSum();
//     return 0;
// }
// void doSum() //Function Defination
// {
//     int x,y;
//     printf("\n Enter value of x : ");
//     scanf("%d",&x); 
//     printf("\n Enter value of y : ");
//     scanf("%d",&y); 
  
//     printf("\n %d + %d : %d",x,y,x+y);
// } 