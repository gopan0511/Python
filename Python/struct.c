
// Inside a structure , a structure variable is not allowed.

struct xxx
{
	int data;
	struct xxx *ad;
};

main()
{
	struct xxx *x = malloc(sizeof(struct xxx));
	struct xxx *y = malloc(sizeof(struct xxx));

	x->data = 10;
	x->ad = 0;

	y->data = 20;
	y->ad = 0;

	printf("%d %x\n",x->data,x->ad);
	printf("%d %x\n",y->data,y->ad);

	x->ad = y;
	printf("%d %x\n",y->data,y->ad);
	printf("%d %x\n",x->ad->data,x->ad->ad);
}