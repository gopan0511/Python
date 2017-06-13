#include "stdio.h"
#include "fcntl.h"
#include "unistd.h"


main()
{
	int *k;
	char path[] = "a.txt";
	char mode[] = "r";
	char data[100];

	memset(data,'\0',sizeof(data));

	k = syscall(5,path,O_RDONLY);
	if(k == 0)
	{
		printf("open failed\n");
	}
	else
	{
		printf("open okay\n");
	}

	syscall(3,k,data,100);
	printf("%s\n",data);
	syscall(6,k);
}