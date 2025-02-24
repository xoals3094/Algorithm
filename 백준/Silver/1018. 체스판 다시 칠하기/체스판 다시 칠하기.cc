#include<stdio.h>
#define MAX 50

char buffer[MAX][MAX + 1];

int minPainting(int i, int j) {
	//true = B , false = W
	bool painting[8][8];
	int x, y, k, z;
	for (y = i - 8, k = 0; y < i; y++, k++) {
		for (x = j - 8, z = 0; x < j; x++, z++) {
			painting[k][z] = buffer[y][x] == 'B' ? true : false;
		}
	}

	int count1 = 0;
	for (int y = 0; y < 8; y++) {
		for (int x = 0; x < 8; x++) {
			if (y - 1 >= 0 && painting[y - 1][x] == painting[y][x]) { //상
				painting[y - 1][x] = !painting[y][x];
				count1++;
			}
			if (y + 1 < 8 && painting[y + 1][x] == painting[y][x]) { //하
				painting[y + 1][x] = !painting[y][x];
				count1++;
			}
			if (x - 1 >= 0 && painting[y][x - 1] == painting[y][x]) { //좌
				painting[y][x - 1] = !painting[y][x];
				count1++;
			}
			if (x + 1 < 8 && painting[y][x + 1] == painting[y][x]) { //우;
				painting[y][x + 1] = !painting[y][x];
				count1++;
			}
		}
	}

	for (y = i - 8, k = 0; y < i; y++, k++) {
		for (x = j - 8, z = 0; x < j; x++, z++) {
			painting[k][z] = buffer[y][x] == 'B' ? true : false;
		}
	}
	painting[0][0] = !painting[0][0];
	int count2 = 0;
	for (int y = 0; y < 8; y++) {
		for (int x = 0; x < 8; x++) {
			if (y - 1 >= 0 && painting[y - 1][x] == painting[y][x]) { //상
				painting[y - 1][x] = !painting[y][x];
				count2++;
			}
			if (y + 1 < 8 && painting[y + 1][x] == painting[y][x]) { //하
				painting[y + 1][x] = !painting[y][x];
				count2++;
			}
			if (x - 1 >= 0 && painting[y][x - 1] == painting[y][x]) { //좌
				painting[y][x - 1] = !painting[y][x];
				count2++;
			}
			if (x + 1 < 8 && painting[y][x + 1] == painting[y][x]) { //우;
				painting[y][x + 1] = !painting[y][x];
				count2++;
			}
		}
	}
	count2++;
	return count1 < count2 ? count1 : count2;
}

int main() {
	int n, m, min = 32, returnPainting = 0;
	
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		scanf("%s", buffer[i]);
	}
	for (int i = 8; i <= n; i++) {
		for (int j = 8; j <= m; j++) {
			returnPainting = minPainting(i, j);
			min = min < returnPainting ? min : returnPainting;
		}
	}
	printf("%d", min);

}