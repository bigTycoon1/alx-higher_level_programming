#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - to inserts a new node
 * @head: head list.
 * @number: index number of the list of new node added
 *
 * Return: address of the new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *h;
	listint_t *top_h;

	h = *head;
	node = malloc(sizeof(listint_t));

	if (node == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		top_h = h;
		h = h->next;
	}

	node->n = number;

	if (*head == NULL)
	{
		node->next = NULL;
		*head = node;
	}
	else
	{
		node->next = h;
		if (h == *head)
			*head = node;
		else
			top_h->next = node;
	}

	return (node);
}
