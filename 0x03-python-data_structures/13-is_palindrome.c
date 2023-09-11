#include "lists.h"

/**
 * reverse - reverse sec. half of the list
 * @head: head of the sec. half
 *
 * Return: nothing to return
 */
void reverse(listint_t **head)
{
	listint_t *pst;
	listint_t *prsnt;
	listint_t *ftr;

	pst = NULL;
	prsnt = *head;


	while (prsnt != NULL)
	{
	ftr = prsnt->next;
		prsnt->next = pst;
		pst = prsnt;
		prsnt = ftr;
	}

	*head = pst;
}

/**
 * compare_list - each int of the list to be compare
 * @list1: list of the first half
 * @list2: list of the sec. half
 *
 * Return: 1 when equals, 0 when not
 */
int compare_list(listint_t *list1, listint_t *list2)
{
	listint_t *dol1;
	listint_t *dol2;

	dol1 = list1;
	dol2 = list2;

	while (dol1 != NULL && dol2 != NULL)
	{
		if (dol1->n == dol2->n)
		{
			dol1 = dol1->next;
			dol2 = dol2->next;
		}
		else
		{
			return (0);
		}
	}

	if (dol1 == NULL && dol2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks for singly linked list
 * @head: pointer to head of list
 *
 * Return: 0 if it is not a palindrome,
 * 	1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *sec_half, *middle;
	int is_pal;

	slow = fast = prev_slow = *head;
	middle = NULL;
	is_pal = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		sec_half = slow;
		prev_slow->next = NULL;
		reverse(&sec_half);
		is_pal = compare_list(*head, sec_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = sec_half;
		}
		else
		{
			prev_slow->next = sec_half;
		}
	}

	return (is_pal);
}
