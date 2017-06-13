struct xxx
{
	int data;
	struct xxx *ad;
};

main()
{
	struct xxx *p = malloc(sizeof(struct xxx));
	int data;
	int ch;
	struct xxx *base = p;
	printf("Enter the data : \n");
	scanf("%d",&data);

	p->data = data;

	while(1)
	{
		printf("1 for add a node\n");
		printf("0 for exit\n");

		printf("Enter the choice : \n");
		scanf("%d",&ch);

		if(ch == 1)
		{
			struct xxx *q =  malloc(sizeof(struct xxx));
			printf("Enter data :\n");
			scanf("%d",&data);

			q->data = data;
			
			p->ad = q;
			p = q;

		}
		else
			if(ch == 0)
			{
				p->ad = 0;
				break;
			}
		else
		{
			printf('Invalid choice\n');
		}


	}

	p = base;
	while(p != 0)
	{
		printf("%d\n",p->data );
		p = p->ad;
	}
	//printf("%d\n",p->data);

}