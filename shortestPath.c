#include <stdio.h>

int Row = 6, Col = 8, cnt;
int map[10][10];
int x[100], y[100], l[100];

void enqueue(int _x, int _y, int _l)
{
	x[cnt] = _x;
	y[cnt] = _y;
	l[cnt] = _l;
	cnt++;
}

void BFS(int _x, int _y)
{
	int pos = 0;

	enqueue(_x, _y, 1);
	
	while (pos < cnt && (x[pos] != Row - 1 || y[pos] != Col - 1))
	{
        int xx = x[pos];
        int yy = y[pos];
		map[x[pos]][y[pos]] = 0;
		
		if (x[pos] > 0 && map[x[pos] - 1][y[pos]] == 1)
			enqueue(x[pos]-1, y[pos], l[pos] + 1);
		
		if (x[pos] < Row - 1 && map[x[pos] + 1][y[pos]] == 1)
			enqueue(x[pos]+1, y[pos], l[pos] + 1);
		
		if (y[pos] > 0 && map[x[pos]][y[pos] - 1] == 1)
			enqueue(x[pos], y[pos]-1, l[pos] + 1);
		
		if (y[pos] < Col - 1 && map[x[pos]][y[pos] + 1] == 1)
			enqueue(x[pos], y[pos]+1, l[pos] + 1);6 8
		pos++;
	}

	if (pos < cnt)
		printf("%d\n", l[pos]);
}

int main()
{
	int i, j;

	scanf("%d %d",&Row, &Col);
	
	for (i = 0; i < Row; i++)
		for (j = 0; j < Col; j++)
			scanf("%d", &map[i][j]);
	BFS(0, 0);

	return 0;
}