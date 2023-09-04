#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function to check singly-linked list has a cycle.
 * @list: singly-linked list.
 *
 * Return: 0 - if there is no cycle
 *         1 - if there is a cycle
 */
int check_cycle(listint_t* list)
{
	listint_t *tort, *hare;


	if (list == NULL)
	{
		return (0);
	}

	tort = list;
	hare = list;

	while (hare != NULL && hare->next != NULL)
	{
		tort = tort->next;
		hare = hare->next->next;

	if (tort == hare)
	{
		return (1);
	}
    }

	return (0);
}
