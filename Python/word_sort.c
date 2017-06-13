main()
{
	int i,j,k;
	char s[] = "i am lit india";
	char word[10][10];
	int x;
	int temp[10];

	memset(word,'\0',sizeof(word));

	j = 0;
	k = 0;
	for(i = 0; i < sizeof(s);i++)//for controlling the string array
	{
		if(s[i] != ' ')
		{
			word[j][k] = s[i];
			k++;
		}
		else if (s[i] == ' ')
		{
			j++;
			k = 0;
		}

	}
	for(i = 0; i < 10;i++)
	{
		printf("%s\n",word[i]);
	}

	j = 0;
	while(j<5)
	{
		k = j+1;
		while(k<5)
		{
			x = 0;
			if(word[j][x] > word[k][x])
			{
				strcpy(temp,word[j]);
				strcpy(word[j],word[k]);
				strcpy(word[k],temp);
			
			}
			
			
			k++;
		}
		j++;
	}

	for(i = 0; i < 10;i++)
	{
		printf("%s\n",word[i]);
	}
}




















