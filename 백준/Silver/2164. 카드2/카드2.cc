#include<stdio.h>
#include<stdlib.h>
#define MAX 500001
typedef struct Queue {
	int front, rear;
	int *data;
}Queue;

void enqueue(Queue* queue, int v) {
	if (queue->rear == MAX)
		queue->rear = 0;
	queue->data[queue->rear++] = v;
}

int dequeue(Queue* queue) {
	if (queue->front == MAX)
		queue->front = 0;
	return queue->data[queue->front++];
}

int main() {
	Queue queue;
	int n;
	queue.data = (int*)malloc(sizeof(int) * MAX);
	queue.front = 0;
	queue.rear = 0;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		enqueue(&queue, i);
	}
	while ((queue.front - queue.rear < 0 ? -(queue.front - queue.rear) : queue.front - queue.rear) != 1) {
		dequeue(&queue);
		enqueue(&queue, dequeue(&queue));
	}
	printf("%d", dequeue(&queue));
	free(queue.data);
}
