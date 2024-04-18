#include<stdio.h>
#define MAX 1002


bool adj[MAX][MAX] = { false };
int parent[MAX];
bool count[MAX];

int find(int x) {
	if (parent[x] == x) return x;
	return parent[x] = find(parent[x]);
}

void unionParent(int a, int b) {
	a = find(a);
	b = find(b);
	if (a < b) {
		parent[b] = a;
	}
	else {
		parent[a] = b;
	}
}

int main() {
	int n, m;
	int c = 0;
	scanf("%d %d", &n, &m);
	for (int i = 1; i <= n; i++) {
		parent[i] = i;
	}

	for (int i = 1; i <= m; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		adj[a][b] = true;
		adj[b][a] = true;
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (adj[i][j]) {
				unionParent(i, j);
			}
		}
	}
	
	for(int i = 1; i <= n; i++){
		if (!count[parent[i]]) {
			count[parent[i]] = true;
			c++;
		}
	}
	printf("%d", c);
}