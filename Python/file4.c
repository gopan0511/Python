#include "fcntl.h"
#include "stdio.h"
main()
{
	char f_name[20];
	int k; //File descriptor
	char line[20];
	char cmd[20] = "python ";

	printf("Enter the python file name : \n");
	scanf("%s",&f_name);

	k = open(f_name,O_CREAT|O_WRONLY);

	while(1)
	{
		gets(&line);
		if(strcmp(line,"Exit") == 0 || strcmp(line,"exit") == 0)
		{
			close(k);
			break;
		}
		
		write(k,line,strlen(line));
		write(k,"\n",strlen("\n"));
	}

	strcat(cmd,f_name);
	printf("\n");
	system(cmd);
	printf("\n");
}