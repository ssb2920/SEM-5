#include<stdio.h>
#include<string.h>
void xor(char S1[],char S2[], int m, int n, int r) // Generates the Sender side code
{
char temp[30],qt[100],rem[30],S3[30];
int i, j;
strcpy(S3,S2);
for(i=0;i<n;i++)
temp[i]=S1[i];
for(i=0;i<m;i++)
{ //main loop to carry out xor for each bit
qt[i]=temp[0];
if(qt[i]=='0')
for(j=0;j<n;j++)
S2[j]='0';
else
for(j=0;j<n;j++)
S2[j]=S3[j];
for(j=0;j<n;j++)
{
if(temp[j]==S2[j])
rem[j]='0';
else
rem[j]='1';
}
for(j=0;j<n;j++){
rem[j]=rem[j+1];
}
rem[n-1]=S1[i+n];
strcpy(temp,rem);
}
strcpy(rem,temp);
printf("\nQuotient is "); // prints the Quotient of the operation
for (i=0;i<m;i++)
printf("%c",qt[i]);
printf("\nCRC is "); // prints the Remainder of the operation
for (i=0;i<n-1;i++)
printf("%c",rem[i]);
printf("\nFinal data is: "); // Final data is the concatenation of S1 and the remainder
for (i=0;i<m;i++)
printf("%c",S1[i]);
for (i=0;i<n-1;i++)
printf("%c",rem[i]);

printf("\n");
}
void check(char S1[],char S2[], int m, int n, int r) // Check for error in receiver side's code
{ // Same Logic as xor() but with less bits in string S1
char temp[30],qt[100],rem[30],S3[30],res[30];
int i, j, temp2;
temp2 = 0;
for(i = 0; i < n-1; i++)
{
res[i] = '0';
}
strcpy(S3,S2);
for(i=0;i<n;i++)
temp[i]=S1[i];
for(i=0;i+n<m+1;i++)
{
qt[i]=temp[0];
if(qt[i]=='0')
for(j=0;j<n;j++)
S2[j]='0';
else
for(j=0;j<n;j++)
S2[j]=S3[j];
for(j=0;j<n;j++)
{
if(temp[j]==S2[j])
rem[j]='0';
else
rem[j]='1';
}
for(j=0;j<n;j++){
rem[j]=rem[j+1];
}
rem[n-1]=S1[i+n];
}
strcpy(rem,temp);
for(i = 0; i < n-1; i++) // IF Remainder is zero
{
if(rem[i] == '0')
temp2 = 0;
else
{ temp2 = 1;
break;
}
}
if(temp2 == 0)
printf("N0 Error in the receiver side \n");
else
printf("There is error on the receiver side",i);

}
void main()
{
int i,j, m, n, r, bit,m2,r2;
char S1[100],S2[30],S3[50],S4[50];
printf("Enter data to be sent: \n"); // Input String of S1
gets(S1);
printf("Enter generator: \n"); // Divisor String of S2
gets(S2);
strcpy(S4,S2);
m=strlen(S1);
n=strlen(S2);
r=n-1;
for(i=m;i<m+r;i++)
S1[i]='0';
xor(S1,S2,m,n,r); // Function call to generate sender side code
printf("Enter the received code \n");
gets(S3);
m2 = strlen(S3);
check(S3,S4,m2,n,r); // Function call to check receiver side code
}