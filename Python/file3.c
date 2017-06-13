#include "fcntl.h"

main()
{
	int k; // file descriptor
	char data[100];

	k = open("lit.txt",O_WRONLY|O_CREAT);

	printf("Enter the data : \n");
	gets(&data);

	write(k,data,strlen(data));

	close(k);
}