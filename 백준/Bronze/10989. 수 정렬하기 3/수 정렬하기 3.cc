#include<stdio.h>
#define MAX 10000

int arr[MAX] = { 0 };

int main() {
	int n, v, max = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &v);
		max = max > v ? max : v;
		arr[v - 1]++;
	}
	for (int i = 0; i < max; i++) {
		for (int j = 0; j < arr[i]; j++) {
			printf("%d\n", i + 1);

		}
	}
}