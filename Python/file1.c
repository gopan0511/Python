#include <stdio.h>
#include <string.h>

main()
{
	FILE *k;
	char path[] = "a.txt";
	char mode[] = "r";
	char data[100];

	memset(data,'\0',sizeof(data));

	k = fopen(path, mode);

	if(k == 0)
	{
		printf("fopen failed\n");
	}
	else
	{
		printf("fopen okay\n");
	}

	fread(data, 1,100,k);

	printf("%s\n",data);

	fclose(k);
}