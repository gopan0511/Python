#include "pthread.h"
#include "sys/types.h"

struct xxx
{
	char name[20];
	int ctime;
};

bbsr(struct xxx*p)
{
	int i;
	for(i = 0;i < p->ctime;i++)
	{
		printf("I am %s\n",p->name);
		sleep(1);
	}
}

main()
{
	struct xxx a = {
			.name = "thread_1",
			.ctime = 5
			};
	struct xxx b = {
			.name = "thread_2",
			.ctime = 10
			};
	struct xxx c = {
			.name = "thread_3",
			.ctime = 15
			};

	pthread_t t1,t2,t3;
	
	pthread_create(&t1,0,bbsr,&a);
	
	pthread_create(&t2,0,bbsr,&b);
	pthread_create(&t3,0,bbsr,&c);

	while(1)
	{
		printf("I am MAIN Thread!!\n");
		sleep(1);
	}
}
