#include "lists.h"

/**
 * print_dlistint - print elements of a doubly linked list
 * @h: pointer to a doubly linked list
 * Description: the function takes a doubly linked list and
 *		prints all its elements
 * Return: Returns the number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t node_count = 0;
	const dlistint_t *current = h;

	while (current != NULL)
	{
		printf("%d\n", current->n);
		current = current->next;
		node_count++;
	}
	return (node_count);
}
